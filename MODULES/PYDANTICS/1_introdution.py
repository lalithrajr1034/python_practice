# we use pydantic for data validation  
from pydantic import BaseModel
# from typing import List , dict  "# this will inbuilt for a 3.9+" no need to import

class student(BaseModel):
    name: str
    age : int
    cource: list[str]
    acd:dict[str,str]
      
    
def lalit(pydantics):
    print(pydantics.acd.values())



m = student(**{'name':'laithrajr',
               'age':34, 
               'cource':['data science','ai'], 
               'acd':{'name':'suraj'}
               }) 
lalit(m)

