from gasoline.gasoline import GasPortion, Gasoline
from gas_pump.gas_pump import GasPump


class Benzine(Gasoline):
    pass


class TestGasPump:
    def test_gas_pump(self) -> None:
        gas_tank = GasPortion(
            gasoline=Benzine(
                octane=95,
            ),
            volume_liters=10,
        )
        gas_pump = GasPump(
            connected_gas_tank=gas_tank,
            connected_engine=None,
            max_flow_lps=0.2,
        )
        output_gas = gas_pump.pull_gas(
            voltage=6,
            seconds=5,
        )
        # flow speed = 0.2, we apply it for 5 seconds, so it makes 11.
        #voltage = 6 (of max 12), so we divide it by 2,
        #should be 0.5 in the end
        assert output_gas.volume_liters == 0.5
