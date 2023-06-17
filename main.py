import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize, Bounds, LinearConstraint, NonlinearConstraint

CMAP = plt.colormaps['plasma']


def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


if __name__ == '__main__':
    data = load_data('data/time_series.csv')
    time = data['Time']
    load = data['Loadshape']
    solar = data['Solar']

    fig, ax = plt.subplots()
    ax.plot(time, load)
    ax.plot(time, solar)
    ax.bar(time, solar-load)
    fig.savefig('output/base.pdf')
