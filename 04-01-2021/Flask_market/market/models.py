from market import db

class user(db.Model):
      id = db.Column(db.Integer(), primary_key=True)
      name=db.Column(db.String,nullable=False)
      Phone_num=db.Column(db.String,nullable=False)
      email = db.Column(db.String, nullable=False)
      password = db.Column(db.String, nullable=False)
      budget=db.Column(db.Integer,default=10000)
      item=db.relationship('item',backref='owned_user',lazy=True)

      def __repr__(self):
          return f"USer_name: {self.name}"

class item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=10), nullable=False, unique=True)
    barcode = db.Column(db.Integer(), nullable=True)
    price = db.Column(db.Integer(), default=100)
    owner=db.Column(db.Integer(),db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Item: {self.name}"