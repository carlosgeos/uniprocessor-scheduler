import argparse
from generator import generate_tasks
from feasibility_interval import getFeasibilityInterval
from simulation import simulate_edf,simulate_llf


def no_arguments(args):
    """Wrapper to print usage information if user does not input any
    subcommands

    """
    argparser.print_help()


argparser = argparse.ArgumentParser(description='EDF and LLF scheduler')
argparser.set_defaults(func=no_arguments) # function to call if no args
subparsers = argparser.add_subparsers(help='sub-command help')

gen_parser = subparsers.add_parser('gen')
interval_parser = subparsers.add_parser('edf_interval')
edf_parser = subparsers.add_parser('edf')
llf_parser = subparsers.add_parser('llf')

gen_parser.add_argument('tasks', default=6, type=int,
                        help='Number of tasks to generate')
gen_parser.add_argument('load_factor', default=70, type=str,
                        help='Utilization factor of the system')
gen_parser.add_argument('output_file', default='tasks.txt', type=str,
                        help='Path where output file should be written')
gen_parser.set_defaults(func=generate_tasks) # dispatcher

interval_parser.add_argument("input_file", default="./data/system.txt", type=str,
                            help="Path where input file is")
interval_parser.set_defaults(func=getFeasibilityInterval)

edf_parser.add_argument("input_file", default="./data/system.txt", type=str,
                            help="Path where input file is")
edf_parser.add_argument('start', default=0, type=int,
                        help='start time')
edf_parser.add_argument('stop', default=20, type=int,
                        help='stop time')
edf_parser.set_defaults(func=simulate_edf)

llf_parser.add_argument("input_file", default="./data/system.txt", type=str,
                            help="Path where input file is")
llf_parser.add_argument('start', default=0, type=int,
                        help='start time')
llf_parser.add_argument('stop', default=20, type=int,
                        help='stop time')
llf_parser.set_defaults(func=simulate_llf)
interval_parser.set_defaults(func=getFeasibilityInterval)

# TODO, add command line options for the rest of the sub_commands
