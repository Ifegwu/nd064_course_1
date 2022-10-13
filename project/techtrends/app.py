import sqlite3
import os
import sys
from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort
import logging

# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    connection.close()
    app.logger.info(f"{post} succesfully fetch")
    return post

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
IS_DEV = app.env == 'development'  # FLASK_ENV env. variable

# Define the main route of the web application 
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    app.logger.info("posts succefully fetch")
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
        app.logger.info("404 page return")
        return render_template('404.html'), 404
    else:
        app.logger.info("posts request successful")
        return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
    app.logger.info("about request successful")
    return render_template('about.html')

# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()

            return redirect(url_for('index'))
    app.logger.info("title and content successful created")
    return render_template('create.html')

@app.route('/healthz')
def healthCheck():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info("status request successful")
    return response

@app.route("/metrics")
def metrics():
    connection = get_db_connection()
    posts = connection.execute('SELECT Count(*) FROM posts').fetchall()
    if posts is None:
        raise ValueError("No post found")
    post_count = posts[0][0]
    response = app.response_class(
        response=json.dumps({"db_connection_count": 1, "post_count": post_count}),
        status=200,
        mimetype='application/json'
    )
    connection.close()
    app.logger.info("post request metrics successful")
    return response

# start the application on port 3111
if __name__ == "__main__":
    # setting environment variable
    assert os.path.exists('.env')  # for other environment variables...
    os.environ['FLASK_ENV'] = 'development'  # HARD CODE since default is production
    

    # format output
    log_format = '%(asctime)s %(levelname)s %(message)s' 
    format_output = logging.Formatter(log_format)
    
    # set logger to handle STDOUT and STDERR 
    stdout_handler = logging.StreamHandler(sys.stdout) # stdout handler
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(format_output) # return stdout_handler
    stderr_handler =  logging.StreamHandler(sys.stderr) # stderr handler 
    stdout_handler.setLevel(logging.DEBUG)
    stderr_handler.setFormatter(format_output) # return stderr_handler
    handlers = [stderr_handler, stdout_handler]

    logging.basicConfig(datefmt='%Y-%m-%d %H:%M:%S', handlers=handlers)
    # logging.basicConfig(format=format_output, level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S', handlers=handlers)
    
    app.run(host='0.0.0.0', port='3111', debug=True)
