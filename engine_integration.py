from engine.engine import Engine
from gasoline.gasoline import GasPortion, Gasoline
from gas_pedal.gas_pedal import Pedal
from gas_pump.gas_pump import GasPump


class Benzine(Gasoline):
    pass

benzine95 = Benzine(octane=95)
benzine98 = Benzine(octane=98)

gas_tank = GasPortion(
    gasoline=benzine95,
    volume_liters=20,
)
gas_tank += GasPortion(
    gasoline=benzine98,
    volume_liters=20,
)

engine = Engine(gasoline=benzine98)

gas_pump = GasPump(
    connected_engine=engine,
    connected_gas_tank=gas_tank,
    max_flow_lps=0.2,
)

pedal = Pedal(
    connected_gas_pump=gas_pump,
)


# pedal -> voltage to gas_pump -> (gets gas from gas_portion -> sends gas to engine) -> engine rotates
# pedal.press() -> gas_pump.apply() -> engine.supply() -> returns rpms