from gamlset import GamlObj, GamlSet
"""
사용 코드 예시
"""

from dataclasses import dataclass

@dataclass
class Example1_GamlObj(GamlObj):
    feild:int
@dataclass
class Example2_GamlObj(GamlObj):
    feild:str

class Example_GamlSet(GamlSet):
    TYPE_1 = Example1_GamlObj
    TYPE_2 = Example2_GamlObj