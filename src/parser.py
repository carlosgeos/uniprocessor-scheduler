import csv
from classes import Task

def parse_system(input_file):
    """Given a properly formatted input file, it returns a list of tasks."""
    reader = csv.DictReader(open(input_file),
                            fieldnames=['offset', 'period', 'wcet'],
                            delimiter=';')
    return [Task(row['offset'], row['wcet'], row['period'], i) for i, row in enumerate(reader)]
