from forms import forms
import datetime
import json
from flask import (jsonify, render_template,request, url_for, flash, redirect)
from app import app
 
 
@app.route('/')
def home():
    return "Flask says 'Hello world!'"

@app.route('/phonebook')
def index():
    return app.send_static_file('phonebook.html')

@app.route('/api/data')
def data():
    # define some data
    d = {
        "Alice": "(708) 727-2377",
        "Bob": "(305) 734-0429"
    }
 
    app.logger.debug(str(len(d)) + " entries in phonebook")
 
    return jsonify(d)  # convert your data to JSON and return

@app.route('/lab02')
def resume():
    return app.send_static_file('lab02_resume.html')


@app.route('/lab03')
def lab03_home():
    return render_template('lab03/index.html',utc_dt=datetime.datetime.utcnow())

@app.route('/lab03/about/')
def lab03_about():
    raw_json = read_file('data/messages.json')
    messages = json.loads(raw_json)
    return render_template('lab03/comments.html', comments=messages)

@app.route('/lab03/comments/')
def lab03_comments():
    raw_json = read_file('data/messages.json')
    messages = json.loads(raw_json)
    return render_template('lab03/comments.html', comments=messages) 

@app.route('/lab04')
def leb04_bootstrap():
    return app.send_static_file('lab04_bootstrap.html')

def read_file(filename, mode="rt"):
    with open(filename, mode, encoding='utf-8') as fin:
        return fin.read()
 
 
def write_file(filename, contents, mode="wt"):
    with open(filename, mode, encoding="utf-8") as fout:
        fout.write(contents)

@app.route('/lab03/create/', methods=('GET', 'POST'))
def lab03_create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
 
        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            raw_json = read_file('data/messages.json')
            messages = json.loads(raw_json)
            messages.append({'title': title, 'content': content})
            write_file('data/messages.json', json.dumps(messages, indent=4))
            return redirect(url_for('lab03_comments'))
 
    return render_template('lab03/create.html')


@app.route('/lab06/', methods=('GET', 'POST'))
def lab06_index():
    form = forms.CourseForm()
    if form.validate_on_submit():
        raw_json = read_file('data/course_list.json')
        course_list = json.loads(raw_json)
        course_list.append({'title': form.title.data,
                            'description': form.description.data,
                            'price': form.price.data,
                            'available': form.available.data,
                            'level': form.level.data
                            })
        write_file('data/course_list.json', json.dumps(course_list, indent=4))
        return redirect(url_for('lab06_courses'))
    return render_template('lab06/index.html', form=form)

@app.route('/lab06/courses/')
def lab06_courses():
    raw_json = read_file('data/course_list.json')
    course_list = json.loads(raw_json)
    return render_template('lab06/courses.html', course_list=course_list)

@app.route('/lab07')
def lab07_form_validation():
    return app.send_static_file('lab07_form_validation.html')

@app.route('/lab07b')
def lab07b():
    return app.send_static_file('lab07b.html')

@app.route('/lab08c')
def lab08c():
    return app.send_static_file('lab08c.html')

    
@app.route('/lab08d')
def lab08d():
    return app.send_static_file('lab08d.html')

@app.route('/lab08e')
def lab08e():
    return app.send_static_file('lab08e.html')