from flask import Flask, render_template, request, redirect, send_file
from indeed import get_jobs
from make_csv import save_to_file

app = Flask("Scrapper")

db = {}


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/report')
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect('/')
    return render_template("report.html", search=word, resultNumber=len(jobs), jobs=jobs)


@app.route('/export')
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")

    except:
        return redirect('/')


app.run()
