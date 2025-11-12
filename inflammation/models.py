"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np
import os
import glob

# from pathlib import Path

# import self
# from inflammation.models import *

def load_csv(filename):
    """Load a Numpy array from a CSV
    
    :param filename: Filename of CSV to load
    """
    
    return np.loadtxt(fname=filename, delimiter=',')


def load_multiple_csvs(data_dir):
# def load_multiple_csvs(data_dir: Path ):
    """
    Scans directory for csv files, and loads them into a list of lists. 
    
    - input arg: requires data_dir to be pathlib.Path; 
    """
    
    # get list of files
    data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
    
    # alternative:
    # data_file_paths = data_dir.glob('inflammation*.csv') 
        # can be used because its now Path
        # also glob and os don't need to be imported
    
    # check not empty
    if len(data_file_paths) == 0:
        raise ValueError(f"No inflammation data CSV files found in path {data_dir}")
    
    # load multiple files into array
    data = list(map(load_csv, data_file_paths))
    
    return data


def daily_mean(data):
    """Calculate the daily mean of a 2d inflammation data array."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2d inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2d inflammation data array."""
    return np.min(data, axis=0)

