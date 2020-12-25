from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=40))
    unit = db.Column(db.String(length=40))
    provider_id = db.Column(db.Integer, db.ForeignKey('providers.id'))

    def __repr__(self):
        return f"{self.name}, {self.unit}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()


class Department(db.Model):
    __tablename__ = 'departaments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=40))
    chief = db.Column(db.String(length=40))

    def __repr__(self):
        return f"{self.name}, {self.chief}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()


class Provider(db.Model):
    __tablename__ = 'providers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=40))

    orders = db.relationship('Order', backref='provider')

    def __repr__(self):
        return f"{self.name}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()


