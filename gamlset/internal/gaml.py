from __future__ import annotations
from typing import Type, ClassVar

class GamlObj:
    owner:ClassVar[GamlSet]
    name:ClassVar[str]
    
    @classmethod
    def _set_owner(cls, owner:GamlSet):
        cls.owner = owner

class _GamlSet_Namespace(dict):
    """Gamlobj를 받으면 type을 새로 생성"""
    def __init__(self, owner_name:str):
        # owner를 가져올 수 없음(prepare 단계라 생성 X)
        self.owner_name = owner_name 
        self.gamlobj_dict:dict[str, Type[GamlObj]] = {}

    def __make_type(self, name:str, base:Type[GamlObj]):
        type_name = f"{self.owner_name}__{name}"
        new_cls = type(
            type_name, # type 이름
            (base, ),  # base
            {}         # dict
        )
        new_cls.name = name
        return new_cls

    def __setitem__(self, key:str, value:any):
        is_class = isinstance(value, type)
            
        if is_class and issubclass(value, GamlObj):
            value = self.__make_type(key, value)
            self.gamlobj_dict[key] = value

        super().__setitem__(key, value)

class GamlSet_Meta(type):
    """GamlSet의 Meta"""
    # description
    """
    # GamlObj_Meta.__set_name__을 사용하지 않은 이유
    # -> name = Type은 __set_name__이 아님
    # GamlSet.__get_attr__를 사용하지 않은 이유
    # -> classvar는 객체 생성 전 namespace에 미리 담겨, __get_attr__를 사용하지 않음
    """


    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TypeHint : 할당은 __new__에서
        cls.gamlobj_dict:dict[str, Type[GamlObj]] 

    @classmethod
    def __prepare__(mcls, name, bases):

        return _GamlSet_Namespace(name)
    
    def __new__(mcls, name, bases, namespace: _GamlSet_Namespace, **kw):
        cls = super().__new__(mcls, name, bases, dict(namespace))
        cls.gamlobj_dict = namespace.gamlobj_dict
        
        # gamlobj의 owner설정
        for _, value in cls.gamlobj_dict.items():
            value._set_owner(cls)

        return cls

class GamlSet(metaclass=GamlSet_Meta):
    pass

