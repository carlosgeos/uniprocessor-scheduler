import csv


def parse_system(input_file):
    """Given a properly formatted input file, it returns an array of
    dictionnaries (one for each task) with keys 'offset', 'period' and
    'wcet'

    """
    reader = csv.DictReader(open(input_file),
                            fieldnames=['offset', 'period', 'wcet'],
                            delimiter=';')
    return list(reader)
