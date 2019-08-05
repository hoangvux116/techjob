from flask import Flask, url_for, render_template, Markup, request
from misaka import Markdown, HtmlRenderer  # For markdown
from sqllib.select import select_page, select_job, num_of_row, num_of_result, select_page_bytag
import os
import math
from tag import tag
from pagination import pagination_range

app = Flask(__name__)
app.jinja_env.globals.update(tags=tag)
app.jinja_env.globals.update(pagination_range=pagination_range)
PAGESIZE = 20
NUM_OF_BUTTON_PER_PAGINATION = 5


@app.route("/")
@app.route("/home")
def home():
    page = 1
    data = select_page(page, PAGESIZE)
    NUM_OF_PAGE = math.ceil(num_of_row() / PAGESIZE)
    return render_template("home.html",current_page=page, num_of_result=num_of_row(),num_of_page=NUM_OF_PAGE, num_of_button=NUM_OF_BUTTON_PER_PAGINATION, jobs=data)


@app.route("/description/<job_id>")
def description(job_id):
    # SELECT JOB FROM DATABASE
    job = select_job(job_id)
    # render descripton markdown to html
    render = HtmlRenderer()
    md = Markdown(render)
    job["description"] = Markup(md(job.get("description")))
    return render_template("description.html", job=job)


@app.route("/jobs")
def show_page_job():
    NUM_OF_PAGE = math.ceil(num_of_row() / PAGESIZE)
    if request.args.get('page'):
        page = int(request.args.get('page'))
        if page < 1 or page > NUM_OF_PAGE:
            return render_template('404.html'), 404
    else:
        page = 1
    data = select_page(page, PAGESIZE)
    return render_template("jobs.html", current_page=page,num_of_result=num_of_row(), num_of_page=NUM_OF_PAGE, num_of_button=NUM_OF_BUTTON_PER_PAGINATION, jobs=data)


@app.route("/tags/<string:tag_name>")
def show_tag_result(tag_name):
    NUM_OF_RESULT = num_of_result(tag_name)
    NUM_OF_PAGE = math.ceil(NUM_OF_RESULT / PAGESIZE)
    if request.args.get('page'):
        page = int(request.args.get('page'))
        if page < 1 or page > NUM_OF_PAGE:
            return render_template('404.html'), 404
    else:
        page = 1
    if NUM_OF_RESULT < 1:
        return render_template('404.html'), 404
    data = select_page_bytag(tag_name, page, PAGESIZE)
    return render_template("tags.html",keyword=tag_name,num_of_result=NUM_OF_RESULT, current_page=page, num_of_page=NUM_OF_PAGE, num_of_button=NUM_OF_BUTTON_PER_PAGINATION, jobs=data)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
