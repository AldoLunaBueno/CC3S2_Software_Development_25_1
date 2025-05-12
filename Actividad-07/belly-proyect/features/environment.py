from src.belly import Belly
from unittest.mock import Mock


def before_scenario(context, scenario):
    fake_clock = Mock()
    fake_clock.return_value = 10000
    context.belly = Belly(clock_service=fake_clock)
