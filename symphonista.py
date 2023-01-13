import typing as t

import simpy

from variables import TABLEWARE_DISPOSAL_TIME
from print_colors import PrintColors


def hungry_symphonista(env: simpy.Environment, name: str, start_time: int,
                       consummation_duration: int, table_spots: simpy.Resource, dishwasher: simpy.Resource,
                       waiting_times: list) -> t.Generator:
    yield env.timeout(start_time)
    print(f"{PrintColors.OKBLUE}MINUTE {env.now} - {name} is entering the kitchen and approaching served meals.")

    print(f"{PrintColors.WARNING}MINUTE {env.now} - {name} is taking the plate and the cutlery, going to the table...")
    start_waiting_for_free_spot = env.now
    with table_spots.request() as table_spot:
        yield table_spot
        free_spot_waiting_time = env.now - start_waiting_for_free_spot
        print(
            f"{PrintColors.OKBLUE}MINUTE {env.now} - {name} has just found a free place at the table and has stared "
            f"eating.")

        yield env.timeout(consummation_duration)

        print(
            f"{PrintColors.WARNING}MINUTE {env.now} - {name}: Yummy! That was tasty! Putting the plate and the "
            f"cutlery into "
            f"the dishwasher...")

    start_waiting_for_dishwasher = env.now
    with dishwasher.request() as dishwasher:
        yield dishwasher
        dishwasher_waiting_time = env.now - start_waiting_for_dishwasher
        yield env.timeout(TABLEWARE_DISPOSAL_TIME)

    print(f"{PrintColors.OKGREEN}MINUTE {env.now} - {name} has completed sorting the plates and the cutlery. "
          f"Has been waiting {free_spot_waiting_time} minutes to eat and {dishwasher_waiting_time} to sort the dishes! "
          f"Back to work! (or table tennis)")
    waiting_times.append(free_spot_waiting_time + dishwasher_waiting_time)
