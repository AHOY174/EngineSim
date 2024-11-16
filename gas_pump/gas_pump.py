import dataclasses 
from dataclasses import dataclass, replace
from typing import Optional

from engine.engine import Engine
from gasoline.gasoline import GasPortion


class NegativeVoltage(ValueError):
    pass


class TooHighVoltage(ValueError):
    pass


@dataclass
class GasPump:
    connected_gas_tank: GasPortion
    connected_engine: Optional[Engine]
    max_flow_lps: float # liters per second

    def pull_gas(
        self,
        voltage: float,
        seconds: float,        
    ) -> GasPortion:
        if voltage < 0:
            raise NegativeVoltage
        if voltage > 14:
            raise TooHighVoltage
        flow_lps = self.max_flow_lps * voltage / 12
        volume = round(min(
            self.connected_gas_tank.volume_liters,
            flow_lps * seconds
        ), ndigits=2)
        self.connected_gas_tank.volume_liters -= volume
        gas_portion = replace(
            self.connected_gas_tank,
            volume_liters=volume
        )

        return gas_portion
    
    def apply_gas(
        self,
        gas_portion: GasPortion,
        seconds: float,  
    ) -> float:
        if self.connected_engine is not None:
            rotations = self.connected_engine.supply(
                gas_portion=gas_portion,
                seconds=seconds,
            )
        
        return rotations