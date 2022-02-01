import json
import os
from pathlib import Path
from typing import Any, Optional
from uuid import uuid4 
from pydantic import BaseModel


class DatabaseBaseModel(BaseModel):
    id : str
    _BASE_DIR = f'{os.getcwd()}/DB/'
    
    
    def save(self):
        _new = {}
        if not self._is_directory_there():
            Path(self._BASE_DIR).mkdir(parents=True, exist_ok=True)
            
        if not self._is_db_file_there():
            with open(self.file_name() , 'w') as f:
                json.dump({},f)
                    
        with open(self.file_name() , 'r') as f:
            old = json.load(f) 
            if not old :
                _new = {self.key : self.json()}
            else:
                old[self.key] = self.json()
                _new = old
        with open(self.file_name() , 'w') as f:
            json.dump(_new,f)

    @classmethod
    def search_one(cls, field:str , value:Any):
        try:
            with open(cls.file_name() , 'r') as f:
                for _key , _object_data in json.load(f).items():
                    if _object_data is not None:
                        _object = json.loads(_object_data)
                        if _object.get(field) == value:
                            return cls(**_object)
        except Exception as e:
            print('Error at Database : ' , e)
            return None
    
    @classmethod
    def search_all(cls, field:str , value:Any):
        try:
            res = []
            with open(cls.file_name() , 'r') as f:
                for _key , _object_data in json.load(f).items():
                    if _object_data is not None:
                        _object = json.loads(_object_data)
                        if _object.get(field) == value:
                            res.append(cls(**_object))
            return res
        except Exception as e:
            print('Error at Database : ' , e)
            return []
    
    @classmethod
    def get(cls, key):
        try:
            with open(cls.file_name() , 'r') as f:
                d = json.load(f).get(key)
                if d is not None:
                    return cls(**json.loads(d))
        except Exception as e:
            print('Error at Database : ', e)
            return None
            
    
    @classmethod
    def file_name(cls):
        return f'{cls._BASE_DIR}{cls.__name__}.json'
    
    def _is_db_file_there(self): 
        return os.path.exists(self.file_name())
    
    def _is_directory_there(self):
        return os.path.isdir(self._BASE_DIR)
        
    

    @property
    def key(self):
        if hasattr(self, 'id'):
            if self.id is not None:
                return self.id
        try:
            return hash(self)
        except TypeError :
            return str(uuid4())

