from flask import Flask, render_template
import db

APP = Flask(__name__)

#TODO: implementar as questoes (+ habilidade para pesquisar, necessário???)
#TODO: terminar relatorio
# TODO: As questões tem de ser respondidas na hora? Ou podemos só colar na página o output que obtivemos sem fazer nenhuma query?
# TODO: O dataset n ão contém todas as músicas dos albums, por isso a página de um abum pode só ter 1 música com track number 20 :<

@APP.route('/tags/<tagName>/')
def get_tag(tagName):
    songs = db.execute('''
    Select s.Title, s.Url
    From IsTaggedAs ta
    Join Song s On s.Url = ta.SongUrl
    Where tagTitle = ?''', [tagName]).fetchall()
    return render_template('tag.html', tag=tagName, songs=songs)

@APP.route('/staff/<staffName>/')
def get_staff(staffName):
    jobs = db.execute('''
    Select s.Title, s.Url, JobTitle
    From Worked w
    Join Song s On s.Url = w.SongUrl
    Where StaffName = ?''', [staffName]).fetchall()
    return render_template('staff.html', staff=staffName, jobs=jobs)

@APP.route('/albums/<path:albumUrl>/')
def get_album(albumUrl):
    songs = db.execute('''
    Select s.Title, s.Url, fi.Track
    From Song s
    Join IsFeaturedIn fi On fi.SongUrl = s.Url
    Join Album a On a.Url = fi.AlbumUrl
    Where a.Url = ?
    Order By fi.Track ASC''', [albumUrl]).fetchall()

    title = db.execute('''
    Select Title
    From Album
    Where Url = ?''', [albumUrl]).fetchone()
    
    return render_template('album.html', songs=songs, title=title)

@APP.route('/songs/<path:songUrl>/')
def get_song(songUrl):
    songInfo = db.execute('''
    Select Title, Url, ReleaseDate, PageViews
    From Song
    Where Url = ?''', [songUrl]).fetchone()

    tags = db.execute('''
    Select tagTitle
    From IsTaggedAs ta
    Join Song s On s.Url = ta.SongUrl
    Where ta.SongUrl = ?''', [songUrl]).fetchall()
    
    return render_template('song.html', songInfo=songInfo, tags=tags)

#
# ENTRY COUNTER
#

@APP.route("/")
def main_page():
    stats = {}
    stats = db.execute('''
    Select * From
    (Select count(*) as Albums From Album)
    Join
    (Select count(*) as Songs From Song)
    Join
    (Select count(*) as Tags From Tag)
    Join
    (Select count(*) as Categories From Category)
    Join
    (Select count(*) as People From Person)
    Join
    (Select count(*) as Jobs From Job)
    Join
    (Select count(*) as nIsFeaturedIn From IsFeaturedIn)
    Join
    (Select count(*) as nIsTaggedAs From IsTaggedAs)
    Join
    (Select count(*) as nIsCategorizedAs From IsCategorizedAs)
    Join
    (Select count(*) as nWorked From Worked)
    ''').fetchone()
    return render_template('index.html', stats=stats)

#
# INDIVIDUAL TABLES
#

@APP.route('/songs/')
def list_songs():
    songs = db.execute(
      '''
      SELECT Title, Url, PageViews, ReleaseDate
      FROM Song
      ORDER BY Title
      ''').fetchall()
    return render_template('song-list.html', songs=songs)

@APP.route('/staff/')
def list_staff():
    staffs = db.execute(
      '''
      SELECT Title
      FROM Person
      ORDER BY Title
      ''').fetchall()
    return render_template('staff-list.html', staffs=staffs)

@APP.route('/albums/')
def list_albums():
    albums = db.execute(
      '''
      SELECT Title, Url
      FROM Album
      ORDER BY Title
      ''').fetchall()
    return render_template('album-list.html', albums=albums)

@APP.route('/tags/')
def list_genres():
    tags = db.execute(
      '''
      SELECT Title
      FROM Tag
      ORDER BY Title
      ''').fetchall()
    return render_template('tag-list.html', tags=tags)

#
# QUESTIONS
#

@APP.route("/question1/")
def question1():
    answer = db.execute("""SELECT DISTINCT StaffName FROM Worked WHERE SongTitle = 'Tell Me Why'""").fetchall()
    return render_template('tag-list.html', tags=tags)

@APP.route("/question2/")
def question2():
    answer = db.execute("""SELECT Title FROM Song WHERE ReleaseDate >= '2007-09-01T00:00:00' AND ReleaseDate <= '2008-10-21T00:00:00'""").fetchall()
    return render_template('tag-list.html', tags=tags)

@APP.route("/question3/")
def question3():
    answer = db.execute("""SELECT AlbumTitle FROM IsFeaturedIn WHERE SongTitle = 'The Last Time (Ft. Gary Lightbody)'""").fetchall()
    return render_template('tag-list.html', tags=tags)

@APP.route("/question4/")
def question4():
    answer = db.execute("""SELECT Lyrics FROM Song WHERE Title = 'End Game (Ft. Ed Sheeran & Future)'""").fetchall()
    return render_template('tag-list.html', tags=tags)

@APP.route("/question5/")
def question5():
    answer = db.execute("""SELECT SongTitle FROM IsCategorizedAs WHERE CategoryName = 'Non-Album Songs'""").fetchall()
    return render_template('tag-list.html', tags=tags)

@APP.route("/question6/")
def question6():
    answer = db.execute("""SELECT SongTitle FROM IsCategorizedAs WHERE CategoryName = 'Other Artist Songs'""").fetchall()
    return render_template('tag-list.html', tags=tags)

@APP.route("/question7/")
def question7():
    answer = db.execute("""SELECT Title FROM Song ORDER BY pageViews DESC LIMIT 5;""").fetchall()
    return render_template('tag-list.html', tags=tags)

@APP.route("/question8/")
def question8():
    answer = db.execute("""SELECT SongTitle
    FROM Worked
    WHERE StaffName = 'Liz Rose'
    AND JobTitle = 'Writer'

    INTERSECT

    SELECT SongTitle
    FROM Worked
    WHERE StaffName = 'Nathan Chapman'
    AND JobTitle = 'Producer'
    """).fetchall()
    return render_template('tag-list.html', tags=tags)

@APP.route("/question9/")
def question9():
    answer = db.execute("""SELECT Title FROM Song WHERE Lyrics like '%like a violin%'""").fetchall()
    return render_template('tag-list.html', tags=tags)

@APP.route("/question10/")
def question10():
    answer = db.execute("""SELECT SongTitle FROM Worked WHERE JobTitle = 'Producer' AND StaffName = 'Jack Antonoff'""").fetchall()
    return render_template('tag-list.html', tags=tags)
