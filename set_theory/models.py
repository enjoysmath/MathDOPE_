from theory.models import *

class Class(Node):
   def __mul__(self, right:Node) -> BinaryOpExpr:
      return self.binary_op_expr(right, op=r'\times ')
   
   def __le__(self, right:Node) -> BinaryOpExpr:
      return self.binary_op_expr(right, op=r'\subset ')
            
def load_default_theory():
   load_transitivity_of_subclassing_axiom()
   
def load_transitivity_of_subclassing_axiom():
   A, B, C = symbols(Class, 'A', 'B', 'C')   
   axiom = theorem([A <= B, B <= C], [A <= C], english='Subclass-of is a transitive relation.')
   return axiom
   
   #B = get_unique(Class, atomic_latex='B')
   #A_sub_B = Assertion().save()
   #A_sub_B.expr.connect(A < B)
   #B_sub_C = Assertion().save().expr.connect(B < C)
   #A_sub_C = Assertion().save().expr.connect(A < C)
   #axiom.premises.connect(A_sub_B, B_sub_C)
   #axiom.conclusions.connect(A_sub_C)
   #english = get_unique(English, string=)
   #english.data.connect(axiom)
   
   #print(axiom.latex())
   
   
      
      