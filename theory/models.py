from gqlalchemy import Memgraph, Node, Relationship, Field, Merge, Create
from typing import Optional
import os

host = '54.193.63.96'
port = 7687
username = 'fruitfulapproach@gmail.com'
# Place your Memgraph password that was created during Project creation
password= os.environ['MEMGRAPH_PASSWORD']

#def hello_world():    
db = Memgraph(host, port, username, password, encrypted=True)
    
    #results = db.execute_and_fetch(
        #'CREATE (n:FirstNode { message: "Hello Memgraph from Python!" }) RETURN n.message AS message')
    #print("Created node with message:", next(results)["message"])

#if __name__ == '__main__':
    #hello_world()

class Keyword(Node, db=db):
    string: str

class LaTeXKeyword(Keyword):
    pass

query = Create(db).node(labels="LaTeXKeyword", string=r"\\Bbb{Z}").execute()

#class Node(StructuredNode):
   #uid = UniqueIdProperty()
   #atomic_latex = StringProperty(max_length=MAX_ATOMIC_LATEX_LENGTH)
   ##inhabits = RelationshipTo('Node', 'IS_ELEMENT_OF', cardinality=ZeroOrMore)   
   
   #def latex(self) -> str:
      #return self.atomic_latex
   
   #def __str__(self):
      #return self.latex()
   
   #def binary_op_expr(self, right, op:str):
      #op = get_unique(Node, atomic_latex=op)  # TODO: need to save()?
      #expr = BinaryOpExpr().save()
      #expr.operator.connect(op)
      #expr.left.connect(self)
      #expr.right.connect(right)      
      #return expr
   
   #def english_latex(self):
      #return self.latex()
   

#class Expression(Node):
   #pass
   
      
#class BinaryOpExpr(Expression):
   #left = RelationshipTo('Node', 'HAS_LEFT_ARG', cardinality=One)
   #right = RelationshipTo('Node', 'HAS_RIGHT_ARG', cardinality=One)   
   #operator = RelationshipTo('Node', 'HAS_OPERATOR', cardinality=One)
   
   #def latex(self) -> str:
      #return self.left.get().latex() + self.operator.get().latex() + self.right.get().latex()
   

#class English(Node):
   #string = StringProperty(max_length=MAX_ENGLISH_LENGTH)
   #data = RelationshipTo('Node', 'DESCRIBES', cardinality=OneOrMore)


#class Assertion(Node):
   #expr = RelationshipTo('Expression', 'HAS_EXPRESSION', cardinality=One)
   
   #@staticmethod
   #def assertions_from_expressions(exprs:list) -> list:
      #for k in range(len(exprs)):
         #if not isinstance(exprs[k], Assertion):
            #assertion = Assertion()
            #assertion.save()
            #assertion.expr.connect(exprs[k])
            #exprs[k] = assertion
      #return exprs
   
   #def latex(self):
      #return self.expr.get().latex()
   
   #@staticmethod
   #def assertions_to_and_string(assertions) -> str:
      #string = ''      
      #for k in range(len(assertions) - 1):
         #string += f'${assertions[k].latex()}$, '      
      #string += f'and ${assertions[-1].latex()}$'      
      #return string


#class Theorem(Assertion):
   #premises = RelationshipTo('Assertion', 'HAS_PREMISE', cardinality=ZeroOrMore)
   #conclusions = RelationshipTo('Assertion', 'HAS_CONCLUSION', cardinality=OneOrMore)
   
   #def english_latex(self) -> str:
      #string = "Suppose "
      #string += Assertion.assertions_to_and_string(self.premises.all())
      #string += ".  Then "
      #string += Assertion.assertions_to_and_string(self.conclusions.all())
      #string += "."
      #return string
   

#def symbols(Model, *args):
   #symbols = []   
   #for arg in args:
      #symbol = get_unique(Model, atomic_latex=arg)
      #symbol.save()
      #symbols.append(symbol)
   #return symbols


#def theorem(premises:list, conclusions:list, english:str) -> Theorem:
   #premises = Assertion.assertions_from_expressions(premises)
   #conclusions = Assertion.assertions_from_expressions(conclusions)
   #theorem = Theorem()
   #theorem.save()
   #for premise in premises:
      #theorem.premises.connect(premise)
   #for conclusion in conclusions:
      #theorem.conclusions.connect(conclusion)
   #eng = English(string=english)
   #eng.save()
   #eng.data.connect(theorem)
   #return theorem


#def get_unique(Model, **kwargs):
   #model = Model.nodes.get_or_none(**kwargs)
   #if model is None:
      #model = Model(**kwargs)
      #model.save()
   #return model   