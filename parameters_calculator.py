import random

from variables import CONSUMMATION_TIME, CONSUMMATION_TIME_MARGIN_ERROR, START_TIME_MAX_DELAY


class ParametersGenerator:

    @staticmethod
    def generate_meal_consummation_duration():
        return random.choice(range(CONSUMMATION_TIME - CONSUMMATION_TIME_MARGIN_ERROR,
                                   CONSUMMATION_TIME + CONSUMMATION_TIME_MARGIN_ERROR + 1))

    @staticmethod
    def generate_start_delay_duration():
        return random.choice(range(START_TIME_MAX_DELAY))
