from pantomkins import pt
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

class points():

    def __init__(self, data_icg, fs):
        self.data_icg = data_icg
        self.fs = fs

    def C_point_detection(self):
        peaks = find_peaks(self.data_icg, distance=150, height=1)[0]
        return peaks

    def B_point_detection(self):
        C_points = self.C_point_detection()
        B_points = []
        for i in range(len(C_points)):
            k = C_points[i]
            minimum = False
            while(minimum == False):
                f_point = self.data_icg[k]
                n_point = self.data_icg[k-1] # next point
                nn_point = self.data_icg[k-2] # next point after next
                if(n_point < f_point and n_point < nn_point):
                    minimum = True
                    B_points.append(k-1)
                k = k-1
        return np.array(B_points)


    def X_point_detection(self):
        C_points = self.C_point_detection()
        X_points = []
        for i in range(len(C_points)):
            k = C_points[i]
            minimum = False
            while(minimum == False):
                f_point = self.data_icg[k]
                n_point = self.data_icg[k+1] # next point
                nn_point = self.data_icg[k+2] # next point after next
                if(n_point < f_point and n_point < nn_point):
                    minimum = True
                    X_points.append(k+1)
                k = k+1
        return np.array(X_points)

