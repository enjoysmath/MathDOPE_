from .models import QuiverArrow, QuiverObject
from sopot.settings import MAX_NOTATION_LENGTH

class Arrow(QuiverArrow):
    
class Functor(Arrow):    
    @staticmethod
    def create_functor(namespace:Namespace, domain:Category, codomain:Category):
    StringProperty(max_length=MAX_NOTATION_LENGTH)
    
    category = RelationshipTo('Category') 

class Object(QuiverArrow):
    pass