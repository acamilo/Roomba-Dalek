#!/usr/bin/python
from flask import Flask, request
from flask import render_template
import os
import glob
import string
app = Flask(__name__)

clients = []


# The main page
@app.route('/')
def main_page():
    try:
        i = clients.index(request.remote_addr)
        print "Client %s is position %d in the queue" % (request.remote_addr,i)
    except ValueError:
        print "Client %s is not in the queue, Adding them." % request.remote_addr
        clients.append(request.remote_addr)
        i = clients.index(request.remote_addr)
    return render_template("main.html", position = i);

@app.route('/position')
def my_position():
    try:
        i = clients.index(request.remote_addr)
    except ValueError:
        clients.append(request.remote_addr)
        i = clients.index(request.remote_addr)
    return "{ \"position\" :%d}" % i

@app.route('/done')
def give_up_control():

    try:
        clients.remove(request.remote_addr)
        print "Client %s has given up control" % (request.remote_addr)
        return ""
    except ValueError:
        print "Client %s attempted to give up control but was not on the list"
        return ""
    


# The Driving URL. 
@app.route('/drive/<string:arc>/<string:speed>')
def drive(arc,speed):
    try:
        #Are they the head of the queue?
        if clients.index(request.remote_addr)==0:
            print '%s: Arc:%0.2f Speed:%0.2f' % (request.remote_addr,float(arc),float(speed))
            return ""
        else:
            print "Wait Your Turn!"
            return ""
    except ValueError:
        return "Error, You're not in the queue!"
    # show the post with the given id, the id is an integer

#List Sounds URL
@app.route('/sounds/')
def show_sounds():
    # show the post with the given id, the id is an integer
     sounds=[]
     for b in glob.glob("sounds/*.mp3"):
          sounds.append(os.path.splitext(os.path.basename(b))[0])
     return render_template('show_sounds.html', sounds=sounds)

#Play Sound URL
@app.route('/sounds/<string:sound>')
def play_sound(sound):
    # show the post with the given id, the id is an integer
     sanitized_sound = ''.join(c for c in sound if c in ("-_.() %s%s" % (string.ascii_letters, string.digits)))
     
     os.system("mpg321 sounds/%s.mp3 & " % sanitized_sound.replace(' ','\ '))
     
     return 'playing sound %s' % sanitized_sound



if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0')


