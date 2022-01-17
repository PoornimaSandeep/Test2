from market import db
from market import bcrypt

class user(db.Model):
      id = db.Column(db.Integer(), primary_key=True)
      name=db.Column(db.String(length=100),nullable=False,unique=True)
      email= db.Column(db.String(length=100), nullable=False,unique=True)
      password = db.Column(db.String(length=100), nullable=False)
      budget=db.Column(db.Integer,default=10000)
      items=db.relationship('item',backref='owned_user',lazy=True)

      @property
      def password_decrypt(self):
          return self.password

      @password_decrypt.setter
      def password_decrypt(self,password_plain_text):
          self.password=bcrypt.generate_password_hash(password_plain_text).decode('utf-8')

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