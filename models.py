def create_classes(db):
    class Ecom(db.Model):
        __tablename__ = 'ecommerce'

        id = db.Column(db.Integer, primary_key=True)
        date = db.Column(db.String(64))
        year = db.Column(db.Float)
        month = db.Column(db.String(64))
        online_food_turnover = db.Column(db.Float)
        online_nonfood_turnover = db.Column(db.Float)
        online_total_turnover = db.Column(db.Float)
        total_revenue_turnover = db.Column(db.Float)

        def __repr__(self):
            return '<Ecom %r>' % (self.date)
    return Ecom