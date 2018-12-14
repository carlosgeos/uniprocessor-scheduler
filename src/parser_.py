import csv
from classes import Task


def parse_system(input_file):
    """Given a properly formatted input file, it returns a list of tasks."""
    reader = csv.DictReader(open(input_file),
                            fieldnames=['offset', 'wcet', 'period'],
                            delimiter=';')
    return [Task(int(row['offset']), int(row['wcet']), int(row['period']), i) for i, row in enumerate(reader)]


def save_system(tasks, output_file):
    """Saves the list of tasks to an output file."""
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['offset', 'wcet', 'period'], delimiter='; ')
        for task in tasks:
            writer.writerow({
                "offset": task.offset,
                "wcet": task.wcet,
                "period": task.period
            })
