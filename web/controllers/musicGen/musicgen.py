from . import route_musicGen
from flask import render_template

@route_musicGen.route('/musicgen',methods=["Get","POST"])
def musicgen():
    return render_template('musicGen/musicgen.html')

@route_musicGen.route('/compose',methods=["Get","POST"])
def compose():
    return render_template('musicGen/compose.html')

@route_musicGen.route('/musicplay')
def musicplay():
    return render_template('musicGen/musicplay.html')

@route_musicGen.route('/music')
def music():
    return render_template('musicGen/music.html')