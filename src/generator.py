import random


def deviate_load(elem, coll):
    """Randomize average load for each of the tasks

    """
    pass


def load_to_wcet_period_ratio(elem):
    """Establish an approximate ratio WCET / Period that satisfies the
    load factor of the task given as input in elem.

    """
    pass


def generate_tasks(args):
    params = vars(args)
    avg_load = params['load_factor'] / params['tasks']
    print(avg_load)
