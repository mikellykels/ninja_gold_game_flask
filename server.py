from flask import Flask, render_template, request, redirect, session
import random, math
from datetime import datetime
app = Flask(__name__)
app.secret_key = '3333'


@app.route('/')
def index():
    if not session.get('gold'):
        session['gold'] = 0
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if (request.form['building'] == 'farm'):
        session['building'] = random.randrange(9, 21)
        date_time = datetime.now()
        activity = {'activity': "Earned {} from the farm {}".format(session['building'], date_time), 'class': 'win'}
        print session['building'], activity
    elif (request.form['building'] == 'cave'):
        session['building'] = random.randrange(4, 11)
        date_time = datetime.now()
        activity = {'activity': "Earned {} from the cave {}".format(session['building'], date_time), 'class': 'win'}
        print session['building']
    elif (request.form['building'] == 'house'):
        session['building'] = random.randrange(1, 5)
        date_time = datetime.now()
        activity = {'activity': "Earned {} from the house {}".format(session['building'], date_time), 'class': 'win'}
        print session['building']
    elif (request.form['building'] == 'casino'):
        session['building'] = random.randrange(-51, 51)
        date_time = datetime.now()
        if session['building'] > 0:
            activity = {'activity': "Earned {} from the casino {}".format(session['building'], date_time), 'class': 'win'}
        if session['building'] < 0:
            session['building'] = int(math.fabs(session['building']))
            activity = {'activity': "Lost {} from the casino {}".format(session['building'], date_time), 'class': 'lose'}
        print session['building']
    else:
        print "Somthing went wrong!"

    session['gold'] += session['building']
    session['activities'].append(activity)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
