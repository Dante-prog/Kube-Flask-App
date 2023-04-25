from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from models import db, Post

my_blueprint = Blueprint('my_blueprint', __name__)

@my_blueprint.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@my_blueprint.route('/create', methods=['POST'])
def create():
    title = request.form['title']
    content = request.form['content']
    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('my_blueprint.index'))

@my_blueprint.route('/edit/<int:post_id>', methods=['POST'])
def edit(post_id):
    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']
    db.session.commit()
    return redirect(url_for('my_blueprint.index'))

@my_blueprint.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('my_blueprint.index'))

@my_blueprint.route('/healthcheck')
def healthcheck():
    return '', 200

