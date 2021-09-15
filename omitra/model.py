from omitra import db


class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    assignment = db.Column(db.Text, nullable=False)
    assignment_type = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer,nullable=True)
class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment.id'), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    review = db.Column(db.String(120), nullable=False)

