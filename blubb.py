#!./py/bin/python

# vim: sw=4 ai sts=4 et :

import bottle
from bottle import template, response, request, HTTPError
from bottle.ext import sqlite
from hashids import Hashids
import pygments.lexers
from pygments import highlight
from pygments.formatters import HtmlFormatter
from datetime import datetime


app = bottle.Bottle()
app.config.load_config('blubb.ini')
app.install(bottle.ext.sqlite.Plugin(dbfile='blubb.db'))
print(app.config)
hashids = Hashids(
    salt=app.config.get('blubb.hashid_salt'),
    min_length=app.config.get('blubb.hashid_min_length')
)

def get_url():
    return app.config.get('blubb.myurl', request.url)

@app.get("/")
def show_index():
    return bottle.template("index", url=get_url())

@app.get("/<hashed>")
def show_blubb(hashed, db):
    id = hashids.decrypt(hashed)
    if len(id) == 0:
        return HTTPError(404, "Page not found")

    row = db.execute("select * from blubb where docid = ?", (id[0],)).fetchone()
    if not row:
        return HTTPError(404, "Page not found")

    syntax = request.query_string
    if not syntax:
        response.content_type = "text/plain; charset=UTF-8"
        return row[0]

    try:
        lexer = pygments.lexers.get_lexer_by_name(syntax)
    except:
        lexer = pygments.lexers.TextLexer()

    response.content_type = 'text/html; charset=UTF-8'
    return highlight(
        row[0],
        lexer,
        HtmlFormatter(
            full=True,
            style='borland',
            lineanchors='n',
            linenos='inline',
            encoding='utf-8'
        )
    )

@app.post('/')
def get_blubb(db):
    response.content_type = "text/plain; charset=UTF-8"
    blubb = request.forms.get('blubb')
    cur = db.cursor()
    cur.execute("insert into blubb values(?,?)", (blubb,datetime.now().isoformat()));
    id = cur.lastrowid
    hashed = hashids.encrypt(id)
    return get_url() + hashed + "\n"

#root_app = bottle.Bottle()
#root_app.mount('/blubb', app)
#root_app.run(server='cherrypy', host='0.0.0.0', port='7280')

app.run(host='0.0.0.0', port=8280)
