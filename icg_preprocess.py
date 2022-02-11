import numpy as np
import pandas as pd
from locale import atof
from scipy.signal import butter, lfilter, iirnotch, filtfilt
from bwr import calc_baseline
from scipy.io import loadmat
from scipy.signal import butter, lfilter, freqz
from scipy.signal import savgol_filter as sg


class icg_preprocess():
    def __init__(self, file, lim, sampling_rate, cutoff_low, cutoff_high, order_low, order_high, radius=3):
        self.file = file
        self.lim = lim
        self.radius = radius
        self.sampling_rate = sampling_rate
        self.cutoff_low = cutoff_low
        self.cutoff_high = cutoff_high
        self.order_low = order_low
        self.order_high = order_high

    def load_data(self):
        mat = loadmat(self.file)
        icg = mat['ICG']
        return icg[:self.lim]

    def rolling_mean(self):
        data = self.load_data()
        means = np.zeros(len(data))

        for i in range(self.radius, len(data)-self.radius):
            slice = np.mean(data[(i-self.radius):(i+self.radius)])
            means[i] = slice

        for j in range(self.radius):
            means[j] = data[j]
            means[len(data)-j-1] = data[len(data)-1-j]

        return means

    def sg_filter(self, window_length=11, polyorder=4):
        data = self.rolling_mean()
        data = sg(data, window_length, polyorder, mode='nearest')
        return data

    def baseline(self):
        data = self.sg_filter()
        bl = calc_baseline(data)
        data = data - bl
        return data





