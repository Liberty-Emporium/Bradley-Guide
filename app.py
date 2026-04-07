"""
Bradley's AI Guide - Tutorial website for using OpenClaw
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getting-started')
def getting_started():
    return render_template('getting-started.html')

@app.route('/daily-activities')
def daily_activities():
    return render_template('activities.html')

@app.route('/cheat-sheet')
def cheat_sheet():
    return render_template('cheatsheet.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)