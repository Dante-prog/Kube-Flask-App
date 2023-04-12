from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:nd3Ruzsq4xa.RfHMQhkJmNUV@flask-app-post-db.cdjokhunziur.us-east-1.rds.amazonaws.com:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    logging.basicConfig(level=logging.DEBUG)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app, db

app, db = create_app()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

@app.before_request
def log_request_info():
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    app.logger.info('Request received from %s for %s', ip_address, request.path)

#This is the home route.
@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['POST'])
def create():
    title = request.form['title']
    content = request.form['content']
    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:post_id>', methods=['POST'])
def edit(post_id):
    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/healthcheck')
def healthcheck():
    return '', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)