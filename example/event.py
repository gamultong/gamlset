"""
EventSet
"""

from gamlset import GamlObj, GamlSet
from typing import TypeVar, Generic
from dataclasses import dataclass

PAYLOAD_TYPE = TypeVar("PAYLOAD_TYPE")

@dataclass
class Event(Generic[PAYLOAD_TYPE], GamlObj):
    paylaod:PAYLOAD_TYPE

class EventSet(GamlSet):
    EXAMPLE_EVENT_1 = Event[int]
    EXAMPLE_EVENT_2 = Event[str]

def some_func(event:EventSet.EXAMPLE_EVENT_1):
    # TypeHint
    event.paylaod

event = EventSet.EXAMPLE_EVENT_1(paylaod=1)
print(event)
event = EventSet.EXAMPLE_EVENT_2(paylaod="str")
print(event)