import variables
import random


class ParametersGenerator:

    @staticmethod
    def generate_meal_consummation_time():
        return random.choice(range(variables.CONSUMMATION_TIME-variables.CONSUMMATION_TIME_MARGIN_ERROR,
                                   variables.CONSUMMATION_TIME+variables.CONSUMMATION_TIME_MARGIN_ERROR+1))
