from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.sno} - {self.title}'


@app.route('/')
def show():
    todo = Todo(title="first todo", desc="Start Investing")
    db.session.add(todo)
    db.session.commit()
    all_todo = Todo.query.all()
    # print(all_todo)
    return render_template('index.html', all_todo=all_todo)


@app.route('/show')
def products():
    all_todo = Todo.query.all()
    print(all_todo)
    return 'This is products page.'


if __name__ == '__main__':
    app.run(debug=True)
