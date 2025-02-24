from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    due_date = db.Column(db.String(10), nullable=False)
    importance = db.Column(db.Integer, nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Task {self.title}>"
