from flask import Flask, url_for, render_template, Markup
from misaka import Markdown, HtmlRenderer  # For markdown
from sqllib.select import select_all_job, select_job
import os

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    data = select_all_job()
    return render_template("home.html", jobs=data)


@app.route("/description/<job_id>")
def description(job_id):
    # SELECT JOB FROM DATABASE
    job = select_job(job_id)
    # render descripton markdown to html
    render = HtmlRenderer()
    md = Markdown(render)
    job["description"] = Markup(md(job.get("description")))
    return render_template("description.html", job=job)


if __name__ == '__main__':
    app.run(debug=True)
