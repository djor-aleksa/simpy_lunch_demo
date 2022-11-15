from variables import TABLE_CAPACITY, NUMBER_OF_DISHWASHERS
from parameters_calculator import ParametersGenerator
from symphonista import hungry_symphonista
import random
import simpy

served_dishes_number = 0
dish_request = None

symphonistas_in_hub = [
    'Tami', 'Ana', 'Sale', 'Andja', 'Nevena', 'Nikola S', 'Tasa', 'Nemanja', 'Igor', 'Veljko', 'Miksa', 'Tade',
    'P.Jovanovic', 'Dusan', 'Mihajlo', 'Milos S', 'Magi', 'Dzudi', 'Rancic', 'Marija', 'Alec', 'Adi', 'Pedja Z.',
    'Mance', 'Magz', 'Meda', 'Dana', 'Bencun', 'Joka', 'Milos']


def main():
    env = simpy.RealtimeEnvironment(initial_time=0, factor=0.3)

    table_spots = simpy.Resource(env, capacity=TABLE_CAPACITY)
    dishwasher = simpy.Resource(env, capacity=NUMBER_OF_DISHWASHERS)
    random.shuffle(symphonistas_in_hub)
    waiting_times = []

    for idx, name in enumerate(symphonistas_in_hub):
        env.process(hungry_symphonista(env, name, idx + random.choice(range(4)),
                                       ParametersGenerator.generate_meal_consummation_time(),
                                       table_spots, dishwasher, waiting_times))

    env.run()

    print('-' * 18 + ' SIMULATION END ' + '-' * 17)
    print('-' * 20 + ' VARIABLES ' + '-' * 20)
    print(f'Available table spots in total: {TABLE_CAPACITY}')
    print(f'Number of dishwashers in function is: {NUMBER_OF_DISHWASHERS}')
    print(f'Number of people today in the hub: {len(symphonistas_in_hub)}')
    print('-' * 20 + ' RESULTS ' + '-' * 20)
    print(f'Total waiting time is {sum(waiting_times)} minutes')
    print(f'Average waiting time is {round(sum(waiting_times) / len(waiting_times), 1)} minutes')


if __name__ == "__main__":
    main()
