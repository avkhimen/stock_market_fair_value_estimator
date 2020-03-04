import argparse

def get_input_args():
    """Returns input arguments for main file execution"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--market', '-m', type = str, default = 'NYSE', 
                        help = 'Market to query stock symbols')
    return parser.parse_args()