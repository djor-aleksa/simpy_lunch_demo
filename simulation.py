import time
import random

import simpy

from variables import TABLE_CAPACITY, NUMBER_OF_DISHWASHERS, SIMULATION_INITIAL_TIME, SIMULATION_FACTOR
from parameters_calculator import ParametersGenerator
from symphonista import hungry_symphonista

symphonistas_in_hub = [
    'Tami', 'Ana', 'Sale', 'Andja', 'Nikola S', 'Tasa', 'Nemanja', 'Igor', 'Veljko', 'Miksa', 'Tade',
    'P.Jovanovic', 'Dusan', 'Mihajlo', 'Milos S', 'Magi', 'Dzudi', 'Rancic', 'Marija', 'Alec', 'Adi', 'Pedja Z.',
    'Mance', 'Magz', 'Meda', 'Dana', 'Bencun', 'Joka', 'Milos', 'Ana']


def print_simulation_info():
    print('-' * 20 + ' VARIABLES ' + '-' * 20)
    print(f'Available table spots in total: {TABLE_CAPACITY}')
    print(f'Number of dishwashers in function is: {NUMBER_OF_DISHWASHERS}')
    print(f'Number of people today in the hub: {len(symphonistas_in_hub)}')
    time.sleep(3)


def main():
    print_simulation_info()
    env = simpy.RealtimeEnvironment(initial_time=SIMULATION_INITIAL_TIME, factor=SIMULATION_FACTOR)

    table_spots = simpy.Resource(env, capacity=TABLE_CAPACITY)
    dishwasher = simpy.Resource(env, capacity=NUMBER_OF_DISHWASHERS)

    random.shuffle(symphonistas_in_hub)
    waiting_times = []

    for idx, name in enumerate(symphonistas_in_hub):
        env.process(hungry_symphonista(env, name, idx + ParametersGenerator.generate_start_delay_duration(),
                                       ParametersGenerator.generate_meal_consummation_duration(),
                                       table_spots, dishwasher, waiting_times))

    env.run()

    print('-' * 18 + ' SIMULATION END ' + '-' * 17)

    print('-' * 20 + ' RESULTS ' + '-' * 20)
    print(f'Total waiting time is {sum(waiting_times)} minutes')
    print(f'Average waiting time per person is {round(sum(waiting_times) / len(waiting_times), 1)} minutes')


if __name__ == "__main__":
    main()
