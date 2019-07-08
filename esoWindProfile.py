import numpy
import myFont
from calcCn2R0 import *
from binProfile import binProfile
from matplotlib import pyplot; pyplot.ion()


def esoWindProfile():
    r0_Median = 0.1

    alpha_Median = 1.052

    """ HIGH-RES """

    alt = numpy.array([30, 90, 150, 200, 245, 300, 390, 600, 1130, 1880, 2630, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 10500, 11500, 
                        12500, 13500, 14500, 15500, 16500, 17500, 18500, 19500, 20500, 21500, 22500, 23500, 24500, 25500, 26500])

    windSpeed = numpy.array([ 5.5, 5.5, 5.1, 5.5, 5.6, 5.7, 5.8, 6, 6.5, 7, 7.5, 8.5, 9.5, 11.5, 17.5, 23, 26, 29, 32, 27, 22, 14.5, 9.5, 
                        6.3, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10 ]) * alpha_Median

    windDirection = numpy.array([0., 2., 4., 6., 8., 10., 12., 14., 16., 18., 20., 22., 24., 26., 28., 30., 32., 34., 36., 38., 40., 42., 44., 
                        46., 48., 50., 52., 54., 56., 58., 60., 62., 64., 66., 68.])

    r0Percent = numpy. array([ 24.2, 12, 9.68, 5.9, 4.73, 4.73, 4.73, 4.73, 3.99, 3.24, 1.62, 2.6, 1.56, 1.04, 1, 1.2, 0.4, 1.4, 1.3, 0.7, 
                        1.6, 2.59, 1.9, 0.99, 0.62, 0.4, 0.25, 0.22, 0.19, 0.14, 0.11, 0.06, 0.09, 0.05, 0.04 ])


    return alt, windSpeed, windDirection

if __name__ == '__main__':
    ys, height, cn2, r0 = esoTurbProfile()



