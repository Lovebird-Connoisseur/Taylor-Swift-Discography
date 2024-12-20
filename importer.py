import openpyxl
import sys
import sqlite3
from datetime import datetime

def generateTables(cursor, command):
    cursor.executescript(command)

def hasAlbum(track):
    if track == 0:
        return False
    else:
        return True

def albumExists(cursor, title, url):
    res = cursor.execute("SELECT EXISTS(SELECT 1 FROM Album WHERE title = ? AND url = ?)", (title, url)).fetchone()[0]
    if res:
        return True
    return False

def parseAlbum(cursor, title, url):
    if not albumExists(cursor, title, url):
        cursor.execute("INSERT INTO Album VALUES (?, ?)", (title, url))

def categoryExists(cursor, category):
    res = cursor.execute("SELECT EXISTS(SELECT 1 FROM Category WHERE title = ?)", [category]).fetchone()[0]
    if res:
        return True
    return False

def parseCategory(cursor, category):
    if not categoryExists(cursor, category):
        cursor.execute("INSERT INTO Category VALUES (?)", [category])

def personExists(cursor, person):
    res = cursor.execute("SELECT EXISTS(SELECT 1 FROM Person WHERE title = ?)", [person]).fetchone()[0]
    if res:
        return True
    return False

def parsePerson(cursor, person):
    if not personExists(cursor, person):
        cursor.execute("INSERT INTO Person VALUES (?)", [person])

def tagExists(cursor, tag):
    res = cursor.execute("SELECT EXISTS(SELECT 1 FROM Tag WHERE title = ?)", [tag]).fetchone()[0]
    if res:
        return True
    return False

def parseTag(cursor, tag):
    if not tagExists(cursor, tag):
        cursor.execute("INSERT INTO Tag VALUES (?)", [tag])

def parseJob(cursor, title):
    cursor.execute("INSERT INTO Job VALUES (?)", [title])

def songExists(cursor, title, url):
    res = cursor.execute("SELECT EXISTS(SELECT 1 FROM Song WHERE title = ? AND url = ?)", (title, url)).fetchone()[0]
    if res:
        return True
    return False

def parseSong(cursor, title, url, releaseDate, lyrics, pageViews):
    cursor.execute("INSERT INTO Song VALUES (?, ?, ?, ?, ?)", (title, url, releaseDate, lyrics, pageViews))

def parseIsCategorizedAs(cursor, title, url, category):
    cursor.execute("INSERT INTO IsCategorizedAs VALUES (?, ?, ?)", (title, url, category))

def parseIsFeaturedIn(cursor, songTitle, songUrl, albumTitle, albumUrl, track):
    cursor.execute("INSERT INTO IsFeaturedIn VALUES (?, ?, ?, ?, ?)", (songTitle, songUrl, albumTitle, albumUrl, track))

def parseIsTaggedAs(cursor, title, url, tag):
    cursor.execute("INSERT INTO IsTaggedAs VALUES (?, ?, ?)", (title, url, tag))

def parseWorked(cursor, title, url, person, job):
    cursor.execute("INSERT INTO Worked VALUES (?, ?, ?, ?)", (title, url, person, job))

def main():
    wb = openpyxl.load_workbook(sys.argv[1])
    sheet = wb[sys.argv[2]]
    dbCon = sqlite3.connect(sys.argv[3])
    cur = dbCon.cursor()
    with open(sys.argv[4], 'r') as file:
        command = file.read()

    generateTables(cur, command)

    parseJob(cur, "Artist")
    parseJob(cur, "Writer")
    parseJob(cur, "Producer")

    for row in tuple(sheet[2:sheet.max_row]):
        album_title = row[0].value
        album_url = row[1].value
        category = row[2].value
        album_track_number = row[3].value
        song_title = row[4].value
        song_url = row[5].value
        song_artists = row[6].value
        song_release_date = row[7].value
        song_page_views = row[8].value
        song_lyrics = row[9].value
        song_writers = row[10].value
        song_producers = row[11].value
        song_tags = row[12].value

        parseCategory(cur, category)

        for tag in song_tags[2:-2].split("', '"):
            parseTag(cur, tag)

        if songExists(cur, song_title, song_url):
            print(song_title)

        if not songExists(cur, song_title, song_url):
            parseSong(cur, song_title, song_url, song_release_date.isoformat(), song_lyrics, song_page_views)
            parseIsCategorizedAs(cur, song_title, song_url, category)
            for tag in song_tags[2:-2].split("', '"):
                parseIsTaggedAs(cur, song_title, song_url, tag)


        if hasAlbum(album_track_number):
            parseAlbum(cur, album_title, album_url)
            parseIsFeaturedIn(cur, song_title, song_url, album_title, album_url, album_track_number)

        for person in song_artists[2:-2].split("', '"):
            if person == "":
                continue
            parsePerson(cur, person)
            parseWorked(cur, song_title, song_url,  person, "Artist")

        for person in song_writers[2:-2].split("', '"):
            if person == "":
                continue
            parsePerson(cur, person)
            parseWorked(cur, song_title, song_url,  person, "Writer")

        for person in song_producers[2:-2].split("', '"):
            if person == "":
                continue
            parsePerson(cur, person)
            parseWorked(cur, song_title, song_url,  person, "Producer")

        dbCon.commit()
    cur.close()

if __name__ == "__main__":
    main()
