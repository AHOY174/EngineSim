from engine.engine import Engine
from gasoline.gasoline import GasPortion, Gasoline
from gas_pump.gas_pump import GasPump
from gas_pedal.gas_pedal import Pedal


class TestEverythingTogether:
    def test_everything_ok(self) -> None:
        """
        Here is the scenario:
        1. Create a Benzine type of Gasoline
        2. Create two gas portions of 95 and 98 for a gas tank
        3. Create an engine that is supposed to work with Benzine 98
        4. Create a gas pump asnd connect to the gas tank and the engine to it
        5. Create a pedal a connect to the pump
        6. Press the pedal and see that the rotations are increased
        :return:
        """

        # STEP 1. Create a Benzine type of Gasoline
        class Benzine(Gasoline):
            pass

        # STEP 2. Create two gas portions of 95 and 98 for a gas tank
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
        # so, we should get 40 liters of (95+98)/2 == 96.5?
        assert gas_tank.volume_liters == 40
        assert gas_tank.gasoline.octane == 96.5

        # STEP 3. Create an Engine that is supposed to work with Benzine 98
        engine = Engine(
            gasoline=benzine98,
        )

        # STEP 4. Create a gas pump and connect the gas tank and the engine to it
        gas_pump = GasPump(
            connected_engine=engine,
            connected_gas_tank=gas_tank,
            max_flow_lps=0.2,
        )

        # STEP 5. Create a pedal and connect to the pump
        pedal = Pedal(
            connected_gas_pump=gas_pump,
        )

        # STEP 6. Press a pedal and see that the gas level has decreased
        gas_portion = pedal.press(
            how_hard=0.8,
            seconds=5,
        )

        # STEP 7. Apply gas to engine and see the rotations count
        rotations = gas_pump.apply_gas(gas_portion=gas_portion, seconds=5)
        