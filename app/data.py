from __init__ import db
import datetime
from marshmallow_sqlalchemy import ModelSchema

class Board(db.Model):

    __table_name__ = 'boards'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.Float, onupdate=datetime.datetime.now())
    

    board_elements = db.relationship('Element')
    
    def __init__(self, title):
        self.title = title
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

class Element(db.Model):
    __tablename__ = 'elements'

    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id')) #Modify here
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.Float, onupdate=datetime.datetime.now())
    description = db.Column(db.String(50))

    def __init__(self, board_id, category, description):
        self.category = category
        self.board_id = board_id
        self.description = description
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        
    
    
class BoardSchema(ModelSchema):
    class Meta:
        model = Board


class ElementSchema(ModelSchema):
    class Meta:
        model = Element

board_schema = BoardSchema()
element_schema = ElementSchema()
