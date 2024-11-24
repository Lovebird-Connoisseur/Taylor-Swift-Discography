import openpyxl
import sys
import sqlite3

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


# def parseSong(cursor, title, url, releaseDate, lyrics, pageViews):
# def parsePerson(cursor, name):
# def parseJob(cursor, title):
# def parseCategory(cursor, title):
# def parseTag(cursor, name):
# def parseIsCategorizedAs(cursor, title, url, category):
# def parseIsFeaturedIn(cursor, songTitle, songUrl, albumTitle, albumUrl, track):
# def parseIsTaggedAs(cursor, title, url, tag):
# def parseWorked(cursor, title, url, person, job):

def main():
    wb = openpyxl.load_workbook(sys.argv[1])
    sheet = wb[sys.argv[2]]
    dbCon = sqlite3.connect(sys.argv[3])
    cur = dbCon.cursor()
    with open(sys.argv[4], 'r') as file:
        command = file.read()

    generateTables(cur, command)
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

        # parseSong(cur, song_title, song_url, song_release_date, song_lyrics, song_page_views)
        parseCategory(cur, category)

        if hasAlbum(album_track_number):
            parseAlbum(cur, album_title, album_url)
            #parseIsFeaturedIn(cur, song_title, song_url, album_title, album_url, album_track_number)

        # for tag in song_tags:
        #     parseTag(cur, tag)

        # for person in song_artists:
        #     parsePerson(cur, name)

        # for person in song_writers:
        #     parsePerson(cur, name)

        # for person in song_producers:
        #     parsePerson(cur, name)

        # parseJob(cur, "Artist")
        # parseJob(cur, "Writer")
        # parseJob(cur, "Producer")

        # for tag in song_tags:
        #     parseTag(cur, tag)
        dbCon.commit()
    cur.close()

if __name__ == "__main__":
    main()


# TODO: verificar se o pessoal/album/som/categorie/tag já se encontra na BD
