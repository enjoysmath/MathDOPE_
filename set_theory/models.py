from neomodel import *
#from django_neomodel import DjangoNode
#from django.db import models
from dope.settings import MAX_ATOMIC_LATEX_LENGTH   #, DEFAULT_CATEGORY_NAME
#from django.core.exceptions import ObjectDoesNotExist
#from neomodel import db
#from dope.python_tools import deep_get
#from dope.variable import Variable
#from dope.keyword import Keyword
#from database.neo4j_tools import neo4j_escape_regex_str 


class Node(StructuredNode):
   uid = UniqueIdProperty()
   atomic_latex = StringProperty(max_length=MAX_ATOMIC_LATEX_LENGTH)
   inhabits = RelationshipTo('Node', 'IS_ELEMENT_OF', cardinality=ZeroOrMore)   
   
   @property
   def latex(self):
      return self.atomic_latex
      
class Class(Node):
   pass

class Set(Class):
   pass

class BinaryOpExpr(Node):
   left = RelationshipTo('Node', 'HAS_LEFT_ARG', cardinality=One)
   right = RelationshipTo('Node', 'HAS_RIGHT_ARG', cardinality=One)   
   operator = RelationshipTo('Node', 'HAS_OPERATOR', cardinality=One)
   
   @property
   def latex(self):
      return self.left.get().latex + self.operator.get().latex + self.right.get().latex
   
   