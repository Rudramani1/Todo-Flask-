from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# SQLite database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'  # Use the right path here
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Todo class to define the table structure
class Todo(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date= db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}>'

# Create the tables in the database
with app.app_context():
    db.create_all()

# Route to the homepage
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        titles = request.form['title']
        descs = request.form['desc']
        todo = Todo(title=titles , desc = descs)
        db.session.add(todo)
        db.session.commit()
    todos = Todo.query.all()  # Get all todos from the database
    return render_template('hello.html', todos=todos)


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == "POST":
        titles = request.form['title']
        descs = request.form['desc']
        
        # Fetch the Todo entry with the given Sno
        todos = Todo.query.filter_by(Sno=sno).first()
        
        # Update its properties
        if todos:
            todos.title = titles
            todos.desc = descs
            db.session.add(todos)  # Corrected typo here
            db.session.commit()
        
        return redirect('/')  # Assuming the homepage route shows all todos

    # If GET request, fetch the Todo entry to prepopulate the form
    todos = Todo.query.filter_by(Sno=sno).first()
    return render_template('update.html', todos=todos)


@app.route('/delete/<int:sno>')
def delete(sno):
    todos = Todo.query.filter_by(Sno=sno).first() 
    db.session.delete(todos)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
