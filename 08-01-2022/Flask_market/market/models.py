from market import db

class user(db.Model):
      id = db.Column(db.Integer(), primary_key=True)
      name=db.Column(db.String(length=100),nullable=False,unique=True)
      email= db.Column(db.String(length=100), nullable=False,unique=True)
      password = db.Column(db.String(length=100), nullable=False)
      budget=db.Column(db.Integer,default=10000)
      items=db.relationship('item',backref='owned_user',lazy=True)

      def __repr__(self):
          return f"User_name: {self.name}"

class item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=10), nullable=False, unique=True)
    price = db.Column(db.Integer(), default=100)
    barcode = db.Column(db.Integer(), nullable=True)
    owner=db.Column(db.Integer(),db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Item: {self.name}"