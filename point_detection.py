from pantomkins import pt
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

class points():

    def __init__(self, data_icg, fs):
        self.data_icg = data_icg
        self.fs = fs

    def C_point_detection(self):
        pan = pt(self.data_icg, self.fs)
        data_pt = pan.fit()
        peaks = find_peaks(data_pt, distance=150)[0]
        values = data_pt[np.array(peaks)]
        maksimum = np.sort(values)[-2:]
        thr = 0.6 * np.mean(maksimum)
        peaks_thr = np.where(values > thr)
        peaks_thr2 = peaks[peaks_thr]

        plt.plot(np.arange(len(data_pt)), data_pt*1000)
        # plt.plot(np.arange(len(self.data_icg)), self.data_icg)
        plt.scatter(peaks_thr2, data_pt[peaks_thr2])
        plt.axhline(thr)
        plt.show()

        return peaks_thr2-6

