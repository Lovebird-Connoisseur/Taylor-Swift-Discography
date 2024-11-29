CREATE TABLE Album(
title TEXT,
url TEXT,
PRIMARY KEY (url)
);

CREATE TABLE Category(
title text PRIMARY KEY
);

CREATE TABLE Song(
title TEXT,
url TEXT,
releaseDate TEXT,
lyrics TEXT,
pageViews INTEGER,
PRIMARY KEY (url)
);

CREATE TABLE Tag(
title text PRIMARY KEY
);

CREATE TABLE Person(
title text PRIMARY KEY
);

CREATE TABLE Job(
title text PRIMARY KEY
);

CREATE TABLE IsTaggedAs(
songUrl TEXT,
tagTitle TEXT,

FOREIGN KEY(songUrl) REFERENCES Song(url),
FOREIGN KEY(tagTitle) REFERENCES Tag(title),
PRIMARY KEY (songURL, tagTitle)
);

CREATE TABLE IsFeaturedIn(
songUrl TEXT,
albumUrl TEXT,
track INTEGER,

FOREIGN KEY(songUrl) REFERENCES Song(url),
FOREIGN KEY(albumUrl) REFERENCES Album(url),
PRIMARY KEY (songUrl, albumUrl)
);

CREATE TABLE IsCategorizedAs(
songUrl TEXT,
categoryName TEXT,

FOREIGN KEY(songUrl) REFERENCES Song(url),
FOREIGN KEY(categoryName) REFERENCES Category(title),
PRIMARY KEY (songUrl, categoryName)
);

CREATE TABLE Worked(
songUrl TEXT,
staffName TEXT,
jobTitle TEXT,

FOREIGN KEY(songUrl) REFERENCES Song(url),
FOREIGN KEY(staffName) REFERENCES Person(title),
FOREIGN KEY(jobTitle) REFERENCES Job(title),
PRIMARY KEY (songUrl, staffName, jobTitle)
);
