from . import route_musicGen
from flask import render_template

@route_musicGen.route('/musicgen',methods=["Get","POST"])
def musicgen():
    return render_template('musicGen/musicgen.html')