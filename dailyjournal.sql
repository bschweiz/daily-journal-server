
CREATE TABLE `Entry` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `concept`    TEXT NOT NULL,
    `date`    TEXT NOT NULL,
    `entry`    TEXT NOT NULL,
    `mood_id` INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);

CREATE TABLE `Mood` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`mood_name`	TEXT NOT NULL
);

INSERT INTO `Entry` VALUES (null, "Test Concept 1", "2021-1-05", "test entry bluh bluh yuddu yuddu", 1);
INSERT INTO `Entry` VALUES (null, "Test Concept 2", "2021-1-06", "test entry bloh bloh yoddo yoddo", 2);
INSERT INTO `Entry` VALUES (null, "Test Concept 3", "2021-1-07", "test entry blah blah yadda yadda", 3);
INSERT INTO `Entry` VALUES (null, "Test Concept 4", "2021-1-08", "test entry blah blah yadda yadda", 4);

INSERT INTO `Mood` VALUES (null, "tired");
INSERT INTO `Mood` VALUES (null, "restless");
INSERT INTO `Mood` VALUES (null, "motivated");
INSERT INTO `Mood` VALUES (null, "stressed");
INSERT INTO `Mood` VALUES (null, "calm");
INSERT INTO `Mood` VALUES (null, "drowsy");

SELECT
            e.id,
            e.concept,
            e.date,
            e.entry text,
            e.mood_id
        FROM Entry e
        WHERE text like '%oh%'; 