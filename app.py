from flask import Flask, url_for, render_template, Markup
from sql_query import *
from misaka import Markdown, HtmlRenderer  # For markdown
import crawl
import os

app = Flask(__name__)
DATABASE_FILE_NAME = "jobs.db"

SQL_FILE = os.path.join(os.path.abspath("."), DATABASE_FILE_NAME)

@app.route("/")
@app.route("/home")
def home():
    data = all_jobs(SQL_FILE)
    return render_template("home.html", jobs=data)


@app.route("/description/<job_id>")
def description(job_id):
    title = job_title(job_id, SQL_FILE)
    # render markdown to html
    render = HtmlRenderer()
    md = Markdown(render)
    JD = Markup(md(job_description(job_id, SQL_FILE)))
    return render_template("description.html",title=title, description=JD)


if __name__ == '__main__':
    app.run(debug=True)
