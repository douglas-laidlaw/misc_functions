import numpy
# import myFont
from calcCn2R0 import *
from bin_profile import bin_profile
from matplotlib import pyplot#; pyplot.ion()


def esoTurbProfile(layerHeight):
    r0_Median = 0.1

    alpha_Median = 1.052

    """ HIGH-RES """

    height = numpy.array([30, 90, 150, 200, 245, 300, 390, 600, 1130, 1880, 2630, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 10500, 11500, 
                        12500, 13500, 14500, 15500, 16500, 17500, 18500, 19500, 20500, 21500, 22500, 23500, 24500, 25500, 26500])
    windSpeed = numpy.array([ 5.5, 5.5, 5.1, 5.5, 5.6, 5.7, 5.8, 6, 6.5, 7, 7.5, 8.5, 9.5, 11.5, 17.5, 23, 26, 29, 32, 27, 22, 14.5, 9.5, 
                        6.3, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10 ]) * alpha_Median
    r0Percent = numpy. array([ 24.2, 12, 9.68, 5.9, 4.73, 4.73, 4.73, 4.73, 3.99, 3.24, 1.62, 2.6, 1.56, 1.04, 1, 1.2, 0.4, 1.4, 1.3, 0.7, 
                        1.6, 2.59, 1.9, 0.99, 0.62, 0.4, 0.25, 0.22, 0.19, 0.14, 0.11, 0.06, 0.09, 0.05, 0.04 ])

    cn2 = (r0Percent/100.) * calcCn2(r0_Median, 500e-9)
    r0 = calcR0(cn2, 500e-9)

    """ LOW-RES """

    heightStep = numpy.arange(0, 26500 + 10, 1)
    cn2Step = numpy.zeros(heightStep.shape[0])

    for i  in range(height.shape[0]):
        cn2Step[numpy.where(heightStep==height[i])] = cn2[i]

    ys, bin_size, num_binPoints, xc, yc = bin_profile(heightStep, cn2Step, layerHeight)

    """ FOR SOAPY """
    r0p = ys / ys.sum()
    r0i = calcR0(ys.sum(), 500e-9)

    print(r0i)


    return ys, height, cn2, r0





def esoTurbProfile_flat(layerHeight):
    r0_Median = 0.1
    alpha_Median = 1.052
    """ HIGH-RES """

    height = numpy.array([30, 90, 150, 200, 245, 300, 390, 600, 1130, 1880, 2630, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 10500, 11500, 
                        12500, 13500, 14500, 15500, 16500, 17500, 18500, 19500, 20500, 21500, 22500, 23500, 24500, 25500, 26500])

    r0Percent = numpy. array([ 24.2, 12, 9.68, 5.9, 4.73, 4.73, 4.73, 4.73, 3.99, 3.24, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 
                        0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 
                        0.8828, 0.8828, 0.8828, 0.8828, 0.8828 ])
    cn2 = (r0Percent/100.) * calcCn2(r0_Median, 500e-9)
    r0 = calcR0(cn2, 500e-9)

    """ LOW-RES """
    heightStep = numpy.arange(0, 26500 + 10, 1)
    cn2Step = numpy.zeros(heightStep.shape[0])
    for i  in range(height.shape[0]):
        cn2Step[numpy.where(heightStep==height[i])] = cn2[i]

    ys, xl, yl = binProfile(heightStep, cn2Step, layerHeight, 1)

    """ FOR SOAPY """


    r0p = ys / ys.sum()
    r0i = calcR0(ys.sum(), 500e-9)


    return ys, height, cn2, r0



def esoTurbProfile_flat_weak(layerHeight):
    r0_Median = 0.1
    alpha_Median = 1.052
    """ HIGH-RES """

    height = numpy.array([30, 90, 150, 200, 245, 300, 390, 600, 1130, 1880, 2630, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 10500, 11500, 
                        12500, 13500, 14500, 15500, 16500, 17500, 18500, 19500, 20500, 21500, 22500, 23500, 24500, 25500, 26500])

    r0Percent = numpy. array([ 24.2, 12, 9.68, 5.9, 4.73, 4.73, 4.73, 4.73, 3.99, 3.24, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 
                        0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 0.8828, 
                        0.8828, 0.8828, 0.8828, 0.8828, 0.8828 ])

    print(r0Percent.sum())

    perc_reduc = 10.
    r0Percent[10:] /= perc_reduc
    # r0Percent[:10] += numpy.sum(r0Percent[10:]/perc_reduc)/r0Percent[:10].shape[0]

    print(r0Percent.sum())

    # r0_correction = calcCn2(r0_Median, 500e-9) - 

    cn2 = (r0Percent/100.) * calcCn2(r0_Median, 500e-9)
    r0 = calcR0(cn2, 500e-9)

    """ LOW-RES """
    heightStep = numpy.arange(0, 26500 + 10, 1)
    cn2Step = numpy.zeros(heightStep.shape[0])
    for i  in range(height.shape[0]):
        cn2Step[numpy.where(heightStep==height[i])] = cn2[i]

    ys, xl, yl = bin_profile(heightStep, cn2Step, layerHeight, 1)

    """ FOR SOAPY """


    r0p = ys / ys.sum()
    r0i = calcR0(ys.sum(), 500e-9)


    return ys, height, cn2, r0


if __name__ == '__main__':
    layer_alt = numpy.linspace(0,24000,7)
    ys, height, cn2, r0 = esoTurbProfile(layer_alt)



