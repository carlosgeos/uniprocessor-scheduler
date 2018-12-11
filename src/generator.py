from classes import Task
from fractions import Fraction
from feasibility_interval import lcm
from parser_ import save_system
from random import randint

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
    n_tasks = params['tasks']
    load_factor = Fraction(params['load_factor'])
    # We receive a percentage, divide by 100
    load_factor /= 100
    # This is the fraction of time a process uses individually
    load_by_process = load_factor / n_tasks
    # load_by_process is a Fraction, so its numerator and denominator are
    # the smallest quotients we can use that divide time equally
    wcet = load_by_process.numerator
    period = load_by_process.denominator
    tasks = [Task(randint(0, period // 2), wcet, period, i) for i in range(n_tasks)]
    save_system(tasks, params["output_file"])
