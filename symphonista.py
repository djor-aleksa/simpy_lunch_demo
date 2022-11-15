from variables import TABLEWARE_DISPOSAL_TIME
import typing
import simpy


def hungry_symphonista(env: simpy.Environment, name: str, start_time: int,
                       consummation_duration: int, table_spots: simpy.Resource, dishwasher: simpy.Resource,
                       waiting_times: list) -> typing.Generator:
    yield env.timeout(start_time)
    print(f"MIN {env.now} - {name} is entering the kitchen, approaching served meals...")

    print(f"MIN {env.now} - {name} is taking the plate and the cutlery, going to the table...")
    start_waiting_to_eat_timestamp = env.now
    with table_spots.request() as table_spot:
        yield table_spot
        to_eat_waiting_time = env.now - start_waiting_to_eat_timestamp
        print(f"MIN {env.now} - {name} has just found a free place at the table and has stared eating...")
        yield env.timeout(consummation_duration)
        print(f"MIN {env.now} - {name}: Yummy! That was tasty! Putting the plate and the cutlery into "
              f"the dishwasher")

    start_waiting_for_dishwasher = env.now
    with dishwasher.request() as dishwasher:
        yield dishwasher
        dishwasher_waiting_time = env.now - start_waiting_for_dishwasher
        yield env.timeout(TABLEWARE_DISPOSAL_TIME)

    print(f"MIN {env.now} - {name} has completed sorting the plates and the cutlery. "
          f"Has been waiting {to_eat_waiting_time} minutes to eat and {dishwasher_waiting_time} to sort the dishes! "
          f"Back to work! (or table tennis)")
    waiting_times.append(to_eat_waiting_time + dishwasher_waiting_time)
