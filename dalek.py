#!/usr/bin/python
from flask import Flask, request
from flask import render_template
import os
import glob
import string
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("main.html");

@app.route('/drive/<string:arc>/<string:speed>')
def drive(arc,speed):
    # show the post with the given id, the id is an integer
     print 'Arc:%0.2f Speed:%0.2f' % (float(arc),float(speed))
     return ""

@app.route('/sounds/')
def show_sounds():
    # show the post with the given id, the id is an integer
     sounds=[]
     for b in glob.glob("sounds/*.mp3"):
          sounds.append(os.path.splitext(os.path.basename(b))[0])
     return render_template('show_sounds.html', sounds=sounds)

@app.route('/sounds/<string:sound>')
def play_sound(sound):
    # show the post with the given id, the id is an integer
     sanitized_sound = ''.join(c for c in sound if c in ("-_.() %s%s" % (string.ascii_letters, string.digits)))
     
     os.system("mpg321 sounds/%s.mp3 & " % sanitized_sound.replace(' ','\ '))
     
     return 'playing sound %s' % sanitized_sound

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0')


