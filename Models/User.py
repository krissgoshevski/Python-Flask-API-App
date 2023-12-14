#
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     email = db.Column(db.String(255), nullable=False, unique=True)
#     password = db.Column(db.String(255), nullable=False)
#     remember_token = db.Column(db.String(100), nullable=True)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
#
#     def __repr__(self):
#         return f'<User {self.name}>'