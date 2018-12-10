from classes import Task
from fractions import Fraction
from feasibility_interval import lcm
from parser_ import save_system

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
    load_factor = Fraction(params['load_factor'])
    load_factor /= 100
    print(load_factor.numerator)
    print(load_factor.denominator)
    n_tasks = params['tasks']
    period = lcm(load_factor.numerator, n_tasks) * load_factor.denominator
    wcet = lcm(load_factor.numerator, n_tasks) * load_factor.numerator // n_tasks
    tasks = [Task(0, wcet, period, i) for i in range(n_tasks)]
    save_system(tasks, params["output_file"])
