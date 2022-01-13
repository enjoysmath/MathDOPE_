from neomodel import RelationshipTo
from .category_theory import Arrow, Object
from .runnable_code import Python


class Proof(Arrow):       
    @staticmethod
    def our_create(given:Statement, goal:Statement, **kwargs):
        kwargs['domain'] = given
        kwargs['codomain'] = goal        
        ob = Proof(**kwargs).save()
        return ob  
    
    @property
    def goal(self):
        return self.codomain
    
    @property
    def given(self):
        return self.domain
    

class Statement(Object):
    pass

class OpStatement(Statement):
    @staticmethod
    def our_create(Op, *args, **kwargs):           
        for arg in args:
            assert(isinstance(arg, Statement))
            arg.namespace += '.' + Class.operator_string
        
        operation = Op(**kwargs).save()
        notation = English(operation, 
                           Python.create_code(
                           
                           ))
        return operation
    

class And(OperatorStatement):    
    English 
    operator_string = "&"
       
    @staticmethod 
    def our_create(*args, **kwargs):     
        assert(len(args) > 1)
        return OperatorStatement.our_create(And, *args, **kwargs)
        
    