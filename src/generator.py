from classes import Task
from fractions import Fraction
from feasibility_interval import lcm
from parser_ import save_system
from random import randint

def generate_tasks(args):
    """Generates a system of tasks, given its size and the desired load factor.
    Params in args:
        tasks: the number of tasks
        load_factor: the load factor of the output, in percent (can be decimal)
        output_file: the filename where to write the output
    """
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
    random_factors = [randint(1, 5) for i in range(n_tasks)]
    tasks = [Task(randint(0, period // 2), wcet * random_factors[i], period * random_factors[i], i)
            for i in range(n_tasks)]
    save_system(tasks, params["output_file"])
