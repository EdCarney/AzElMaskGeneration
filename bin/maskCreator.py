# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 09:39:48 2019

@author: Edward Carney
"""

import math
import matplotlib.pyplot as plt

class MaskHandler():
    """
    A class to handle creation of azimuth-elevation files for STK. Intended
    to be used for the BridgeSat program to generate azimuth-files for partial
    roof opening/closure.
    """
    def __init__(self, pivotAz, shutterEl_r, shutterEl_l):

        # define mask file fidelity (assumed 360 for now)
        self._fidelity = 360

        # define pivot azimuth in degrees CW from North (e.g. 0 => pivot aligns
        # with NS line, 90 => pivot aligns with EW line)
        self.pivotAz = pivotAz

        # define left and right shutter elevation
        self.shutterEl_r = shutterEl_r
        self.shutterEl_l = shutterEl_l

        # define azimuth and elevation lists; will use 1-deg fidelity; need to
        # have both 0 and 360 points (total of fidelity + 1 points)
        self.az = list(range(self._fidelity + 1))
        self.el = [0] * (self._fidelity + 1)

        # define azimuths for start, final, and max elevation of left and right 
        # shutter
        self._shutterStartAz_r = int(math.floor(self.pivotAz))
        self._shutterMaxElAz_r = int(math.floor(self.pivotAz + (self._fidelity / 4)))
        self._shutterFinalAz_r = int(math.floor(self.pivotAz + (self._fidelity / 2)))

        self._shutterStartAz_l = int(math.floor(self.pivotAz + (self._fidelity / 2)))
        self._shutterMaxElAz_l = int(math.floor(self.pivotAz + (3 * self._fidelity / 4)))
        self._shutterFinalAz_l = int(math.floor(self.pivotAz + self._fidelity))

        # generate mask values
        self._generateMask()

    def _setElevation(self, startAz, finalAz, maxEl):
        """
        Sets elevation values for a defined range of azimuth. Will do a sinusoidal progression
        from zero to the max elevation and back to zero.
        """

        # define the elevation function based on the max elevation to be used
        if maxEl == 90.0:
            elFunc = lambda az: 90.0
        elif maxEl > 90.0:
            elFunc = lambda az: 180.0 - abs(math.sin(math.pi / 180.0 * (az - self.pivotAz)) * (180.0 - maxEl))
        else:
            elFunc = lambda az: abs(math.sin(math.pi / 180.0 * (az - self.pivotAz)) * maxEl)

        # iterate through all azimuth values and set elevation
        for az in range(startAz, finalAz):
            self.el[az % self._fidelity] = elFunc(az)

    def _generateMask(self):
        """
        Sets object mask list based on left and right shutter settings.
        """

        # set elevation for the left and right shutters
        self._setElevation(self._shutterStartAz_r, self._shutterFinalAz_r, self.shutterEl_r)
        self._setElevation(self._shutterStartAz_l, self._shutterFinalAz_l, self.shutterEl_l)

        # make sure the first and last values are the same
        self.el[-1] = self.el[0]

    def plotData(self):
        """
        Plots the elevation vs azimuth for easy visualization.
        """
        plt.plot(self.az[:-1], self.el[:-1])
        plt.xlabel("Azimuth (deg)")
        plt.ylabel("Elevation (deg)")
        plt.title("Elevation vs. Azimuth")

        print("INFO: Plotting data. Close out window to continue.")

        plt.show()

    def printToFile(self, fileName):
        """
        Prints azimuth-elevation data to a provided file in STK *.aem file format.
        """

        with open(fileName, 'w') as outFile:
            # write out default file header data
            outFile.write("stk.v.11.2.1\nBEGIN AzElMask\nNumberOfPoints {0}\nBEGIN AzElMaskData\n\n".format(int(self._fidelity + 1)))

            # write out actual data
            for i in range(self._fidelity + 1):
                outFile.write("{0} {1}\n".format(self.az[i], self.el[i]))

            outFile.write("\nEND AzElMaskData\nEND AzElMask")