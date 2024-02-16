from dataclasses import dataclass, field
from typing import List
from .connectors import Connector
from . import friction


@dataclass
class OneWayFitting:
    name: str
    connectors: Connector
    #type: str
    
    def __post_init__(self) -> None:
        #self.connectors = Connector(id="1")
        self.connectors.id = "1"
        
    def calculate(self) -> None:
        c1 = self.connectors
        if c1.flowrate > 0:
            c1.area = 1
            v1 = c1.flowrate / c1.area
            c1.dzeta = 0.5
            c1.pressure_drop = friction.local_pressure_drop(c1.dzeta, v1)


@dataclass
class TwoWayFitting:
    name: str
    connectors: List[Connector] = field(init=False)
    type: str

    def __post_init__(self):
        self.connectors = [Connector(id="1"), Connector(id="2")]
    
    def calculate(self) -> None:
        c2 = self.connectors[1]
        if c2.flowrate > 0:
            c2.area = 1
            v2 = c2.flowrate / c2.area
            c2.dzeta = self.type.dzeta
            c2.pressure_drop = friction.local_pressure_drop(c2.dzeta, v2)


@dataclass
class ThreeWayFitting:
    """c1 source, c2 straight, c3 branch""" 
    name: str
    connectors: List[Connector] = field(init=False)
    #type: str

    def __post_init__(self):
        self.connectors = [Connector(id="1"), 
                           Connector(id="2"), 
                           Connector(id="3")]

    def calculate(self) -> None:
        c2 = self.connectors[1]
        c3 = self.connectors[2]

        if c2.flowrate > 0:
            c2.area = 1
            v2 = c2.flowrate / c2.area
            c2.dzeta = 0.5
            c2.pressure_drop = friction.local_pressure_drop(c2.dzeta, v2)

        if c3.flowrate > 0:
            c3.area = 1
            v3 = c3.flowrate / c3.area
            c3.dzeta = 0.5
            c3.pressure_drop = friction.local_pressure_drop(c3.dzeta, v3)