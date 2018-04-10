#Sighvatur Sveinsson

from bottle import route, run, debug, template, request, static_file, error, redirect
import pymysql
import os

conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1809003730', passwd='mypassword',db='1809003730_veflokaverkefni')
cur = conn.cursor()

@route('/<skraarnafn>')
def static_skrar(skraarnafn):
    return static_file(skraarnafn, root='./')

@error(404)
def villa(error):
    return "<h1>Villa: Þessi síða er ekki til</h1>"

@route('/')
def root():
    return template('template.tpl')

@route('/nytt')
def nytt_ToDo():
    return template('nytt.tpl')

@route('/new', method='POST')
def nytt_ToDo2():
    todo = request.forms.get('todo')
    lysing = request.forms.get('texti')
    cur.execute("INSERT INTO todo (todo, status, lysing) VALUES(%s, 1, %s)", (todo,lysing))
    conn.commit()
    return redirect('/')

@route('/breyt/<no:int>')
def nytt_ToDo(no):
    return template('breyta.tpl',no=no)

@route('/breyta/<no:int>', method='POST')
def edit_item(no):
    edit = request.forms.get('todo')
    cur.execute("UPDATE todo SET todo = %s, status = '1' WHERE id = %s", (edit, no))
    conn.commit()
    return redirect('/')

@route('/buid/<no:int>')
def buid(no):
    cur.execute("UPDATE todo SET status = %s WHERE id = %s", (0,no))
    conn.commit()
    return redirect('/')

@route('/eyda/<no:int>')
def eyda(no):
    cur.execute("DELETE FROM todo WHERE id = %s", (no))
    conn.commit()
    return redirect('/')

@route('/opna/<no:int>')
def eyda(no):
    cur.execute("UPDATE todo SET status = %s WHERE id = %s", (1,no))
    conn.commit()
    return redirect('/')

run(debug=True)