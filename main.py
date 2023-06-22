import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.optimize import Bounds
from scipy.optimize import LinearConstraint
from scipy.optimize import NonlinearConstraint

CMAP = plt.colormaps['plasma']
DERS = np.ones(10)
DER_KW = 250*DERS
DER_KWH = 500*DERS


def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


def decarbonize(x):
    # batter = load - solar
    return x[0] - x[1]


if __name__ == '__main__':
    print(DERS, DER_KW, DER_KWH)
    data = load_data('data/time_series.csv')
    time = data['Time'].to_numpy()
    load = data['Loadshape'].to_numpy()
    solar = data['Solar'].to_numpy()

    fig, ax = plt.subplots()
    ax.plot(time, load)
    ax.plot(time, solar)
    ax.bar(time, solar-load)
    fig.savefig('output/base.pdf')

    # Starting point
    setpoints = 0*DERS

    # Optimization
    result = minimize(
    decarbonize, setpoints, method='trust-constr')

    result.x.round(3)
