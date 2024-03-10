import pandas as pd
import pyupbit as pu
import numpy as np
import os
import glob

directory_ = os.path.join(os.getcwd(), 'upbit')
paths = glob.glob(os.path.join(directory_, '*.csv'))

data_ = {}

def load():
    for path in paths:
        symbol_ = path.split('/')[-1].split('.')[0]
        data_[symbol_] = pd.read_csv(path)
    return data_

if __name__ == "__main__":
    load()