import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from entries import get_all_entries
from entries import get_single_entry
from entries import delete_entry
# from moods import get_all_moods

class HandleRequests(BaseHTTPRequestHandler):

    # Here's a class function
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    #this is how we isolate the entrie ID NUMBER FROM THE URL aka self.path 
    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/entries/1", the resulting list will
        # have "" at index 0, "entries" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None
        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /entries
        except ValueError:
            pass  # Request had trailing slash: /entries/
        return (resource, id)  # This is a tuple

    # Here's a method on the class that overrides
    # It handles any GET request.
    def do_GET(self):
        # Set the response code to 'Ok'
        self._set_headers(200)
        response = {} #default response
        (resource, id) = self.parse_url(self.path)
        # It's if..else statements to check for various paths
        # First we check if it's entries
        if resource == "entries":
            if id is not None:
                response = f"{get_single_entry(id)}"
            else:
                response = f"{get_all_entries()}"
        # #Then we check if it"s moods
        # elif resource == "moods":
        #     if id is not None:
        #         response = f"{get_single_mood(id)}"
        #     else:
        #         response = f"{get_all_moods()}"
        # This weird code sends a response back to the client
        self.wfile.write(response.encode())

    def do_DELETE(self):
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)
        if resource == "entries":
            delete_entry(id)
        self.wfile.write("".encode())
# This function is not inside the class. It is the starting
# point of this application.
def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
