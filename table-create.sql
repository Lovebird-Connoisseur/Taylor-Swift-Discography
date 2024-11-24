CREATE TABLE Album(
title TEXT,
url TEXT,
PRIMARY KEY (title, url)
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
PRIMARY KEY (title, url)
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
songTitle TEXT,
songUrl TEXT,
tagTitle TEXT,

FOREIGN KEY(songTitle) REFERENCES Song(title),
FOREIGN KEY(songUrl) REFERENCES Song(url),
FOREIGN KEY(tagTitle) REFERENCES Tag(title),
PRIMARY KEY (songTitle, songURL, tagTitle)
);

CREATE TABLE IsFeaturedIn(
songTitle TEXT,
songUrl TEXT,
albumTitle TEXT,
albumUrl TEXT,
track INTEGER,

FOREIGN KEY(songTitle) REFERENCES Song(title),
FOREIGN KEY(songUrl) REFERENCES Song(url),
FOREIGN KEY(albumTitle) REFERENCES Album(title),
FOREIGN KEY(albumUrl) REFERENCES Album(url),
PRIMARY KEY (songTitle, songUrl, albumTitle, albumUrl)
);

CREATE TABLE IsCategorizedAs(
songTitle TEXT,
songUrl TEXT,
categoryName TEXT,

FOREIGN KEY(songTitle) REFERENCES Song(title),
FOREIGN KEY(songUrl) REFERENCES Song(url),
FOREIGN KEY(categoryName) REFERENCES Category(title),
PRIMARY KEY (songTitle, songUrl, categoryName)
);

CREATE TABLE Worked(
songTitle TEXT,
songUrl TEXT,
staffName TEXT,
jobTitle TEXT,

FOREIGN KEY(songTitle) REFERENCES Song(title),
FOREIGN KEY(songUrl) REFERENCES Song(url),
FOREIGN KEY(staffName) REFERENCES Person(title),
FOREIGN KEY(jobTitle) REFERENCES Job(title),
PRIMARY KEY (songTitle, songUrl, staffName, jobTitle)
);
