from flask import Flask, render_template
import db

APP = Flask(__name__)

#
# Pages for Individual Entries
#

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
    question = "Quêm trabalhou numa dada música?"
    query = """SELECT DISTINCT StaffName FROM Worked w JOIN Song s ON w.SongUrl = s.Url WHERE s.Title = 'Tell Me Why';"""
    answers = db.execute(query).fetchall()
    return render_template('question1.html', answers=answers, question=question, query=query)

@APP.route("/question2/")
def question2():
    question = "Em que projetos esteve a Taylor envolvida num dado periodo?"
    query = "SELECT Title, ReleaseDate FROM Song WHERE ReleaseDate >= '2007-09-01T00:00:00' AND ReleaseDate <= '2008-10-21T00:00:00' Order By ReleaseDate"
    answers = db.execute(query).fetchall()
    return render_template('question2.html', answers=answers, question=question, query=query)

@APP.route("/question3/")
def question3():
    question = "Em que albuns se encontra uma dada música?"
    query = "SELECT a.Title, fi.Track FROM IsFeaturedIn fi JOIN Album a ON a.Url = fi.AlbumUrl JOIN Song s ON s.Url = fi.SongUrl WHERE s.Title = 'The Last Time (Ft. Gary Lightbody)'"
    answers = db.execute(query).fetchall()
    return render_template('question3.html', answers=answers, question=question, query=query)

@APP.route("/question4/")
def question4():
    question = "Quais são as lyrics de uma dada música?"
    query = "SELECT Lyrics FROM Song WHERE Title = 'End Game (Ft. Ed Sheeran & Future)'"
    answers = db.execute(query).fetchall()
    return render_template('question4.html', answers=answers, question=question, query=query)

@APP.route("/question5/")
def question5():
    question = "Quantas músicas não pertencem a nenhum album?"
    query = "SELECT count(s.Url) as num FROM IsCategorizedAs ca JOIN Song s ON ca.songUrl = s.Url WHERE CategoryName = 'Non-Album Songs'"
    answers = db.execute(query).fetchall()
    return render_template('question5.html', answers=answers, question=question, query=query)

@APP.route("/question6/")
def question6():
    question = "Quais músicas foram feitas em colaboração com a Taylor Swift?"
    query = "SELECT s.Title FROM IsCategorizedAs ca JOIN Song s ON ca.songUrl = s.Url WHERE CategoryName = 'Other Artist Songs'"
    answers = db.execute(query).fetchall()
    return render_template('question6.html', answers=answers, question=question, query=query)

@APP.route("/question7/")
def question7():
    question = "Quais são as 5 músicas cujas páginas tem o maior número de visualizações?"
    query = "SELECT Title, pageViews FROM Song ORDER BY pageViews DESC LIMIT 5"
    answers = db.execute(query).fetchall()
    return render_template('question7.html', answers=answers, question=question, query=query)

@APP.route("/question8/")
def question8():
    question = "Quais músicas foram escritas por X e produzidas por Y?"
    query = """SELECT s.Title
    FROM Worked w JOIN Song s ON s.Url = w.SongUrl
    WHERE StaffName = 'Liz Rose'
    AND JobTitle = 'Writer'

    INTERSECT

    SELECT s.Title
    FROM Worked w JOIN Song s ON s.Url = w.SongUrl
    WHERE StaffName = 'Nathan Chapman'
    AND JobTitle = 'Producer'"""
    answers = db.execute(query).fetchall()
    return render_template('question8.html', answers=answers, question=question, query=query)

@APP.route("/question9/")
def question9():
    question = "Qual é o número médio de tags por música?"
    query = "SELECT ROUND(AVG(média)) as Média FROM (SELECT COUNT(ta.TagTitle) as média FROM Song s Join IsTaggedAs ta On ta.SongUrl = s.Url Join Tag t On t.Title = ta.TagTitle GROUP BY s.Url)"
    answers = db.execute(query).fetchall()
    return render_template('question9.html', answers=answers, question=question, query=query)

@APP.route("/question10/")
def question10():
    question = "Que músicas foram produzidas por uma dada pessoa?"
    query = "SELECT s.Title FROM Worked w JOIN Song s ON s.Url = w.SongUrl WHERE JobTitle = 'Producer' AND StaffName = 'Jack Antonoff'"
    answers = db.execute(query).fetchall()
    return render_template('question10.html', answers=answers, question=question, query=query)
