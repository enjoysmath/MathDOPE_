from dope.settings import (MAX_TEXT_LENGTH, MAX_NAMESPACE_LENGTH, MAX_CODE_LENGTH,
                            MAX_GLOBAL_DICT_LENGTH)
from neomodel import (StructuredNode, StructuredRel, IntegerProperty,
                      StringProperty, BooleanProperty, One, OneOrMore, 
                      ZeroOrMore, FloatProperty, UniqueIdProperty, 
                      RelationshipTo, JSONProperty)
import neomodel
import uuid
from .namespace import Namespace
import re
from .neo4j_tools import neo4j_escape_regex_str

python_identifier_regex = re.compile(r'([_A-Za-z][0-9_A-Za-z]*)')

class Code(Object):      
    code = None
    
    def run_code(self):
        raise NotImplementedError
    
    @staticmethod
    def create_code(subclass, code:str, **kwargs):
        var_query = subclass.var_subst_query(code, **kwargs)
        var_query += '\n'
        var_query += 'ORDER BY size(p.code)'
        existing_codes, meta = neomodel.db.cypher_query(var_query)
        
        for python in existing_codes:
            code = str(python.code)
            globals_dict = str(python.globals_dict)
            
            
        code = subclass(code=code, **kwargs)
        code.save()
        return code     
    
    @staticmethod
    def var_subst_query(*args, **kwargs):
        raise NotImplementedError
        
    
class Python(Code):    
    code = StringProperty(default="pass", max_length=MAX_CODE_LENGTH, required=True)
    globals_dict = StringProperty(default="dict()", max_length=MAX_GLOBAL_DICT_LENGTH, required=True)
    variable_subs = JSONProperty(
    
    )
    
    @staticmethod
    def run_code(code:str, globals_dict:str):        
        code_name = f'code_{uuid.uuid4()}'
        code_lines = str(self.code).split('\n')      # TODO: do we need to call str() here?
        for k in range(len(code_lines)):
            code_lines[k] = '    ' + code_lines[k] + '\n'
        code = ''.join(code_lines)
        exec(f'def {code_name}():\n'
             f'{code}', eval(str(self.globals_dict)))   
        ret_val = eval(code_name)()
        return ret_val        
    
    @staticmethod
    def create_code(code:str, globals_dict:str):
        return Code.create_code(Python, code, globals_dict=globals_dict)
        
    @staticmethod 
    def var_subst_query(code:str, globals_dict:str) -> str:        
        code = neo4j_escape_regex_str(code)
        code = python_identifier_regex.sub(code, python_identifier_regex.pattern)
        
        globals_dict = neo4j_escape_regex_str(globals_dict)
        globals_dict = python_identifier_regex.sub(code, python_identifier_regex.pattern)
                
        query = f"MATCH (p:Python) WHERE p.code ~= {code} AND p.globals_dict ~= {globals_dict}"        
        return query
    
    
class VariableSubstitution(Arrow):
    variable_map = RelationshipTo('Map')
    
    @staticmethod
    def create_subst(subclass, in_code:Code, out_code:Code, pattern=None):
        if pattern is None:
            pattern = '.+'
            
        in_code_str = neo4j_escape_regex_str(str(in_code.code))
        
        variable_indices = {}
        k = 0
        match = python_identifier_regex.search(in_code_str)        
        
        while match:
            var = match.group()
            variable_indices[k] = var
            start = match.end()
            match = python_identifier_regex.match(in_code_str, start=start)
            k += 1    

        variable_map = bidict()
        out_code_str = str(out_code.code)
        k = 0
        match = python_identifier_regex.search(out_code_str)
               
        while match:
            var = match.group()
            variable_indices
    
        in_code_regex = python_identifier_regex.sub(in_code_regex, pattern)
        in_code_regex = f'^{in_code_regex}$'
        
        match = python_identifier_regex.match(out_code)
        
        for 
        
        
class VariablePermutation(VariableSubstitution):
    @staticmethod 
    def create_substitution(in_code, out_code):
        return VariableSubstitution.create_subst(
            VariablePermutation, in_code, out_code, 
            pattern=python_identifier_regex.pattern)
    
    