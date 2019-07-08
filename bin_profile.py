import numpy
from astropy.io import fits
from matplotlib import pyplot; pyplot.ion()



def continuous_linePlot_forIntegration(xs, ys):
	"""Continuous coordinates of a scatter plot line. To be used 
	for integration. Resolution is at 1 in the x-axis. 
	Input x values do not have to be in ascending order.

	INPUT
	xs: x coordinates of scatter plot.
	ys: y coordinates of scatter plot.

	OUTPUT
	xCon: continuous x coordinates.
	yCon: continuous y coordinates."""

	sorted_index = numpy.argsort(xs)
	xs = xs[sorted_index]
	ys = ys[sorted_index]
	xPoints = numpy.round(xs).astype(int)
	yPoints = ys
	count = 0

	xCon = numpy.arange(xPoints.max())
	yCon = numpy.zeros(xCon.shape[0])

	num_binPoints_counter = numpy.zeros(xCon.shape[0])

	for i in range(xPoints.shape[0]-1):
		bin_count = 1

		deltaY = yPoints[i+1] - yPoints[i]
		deltaX = xPoints[i+1] - xPoints[i]
		yStart = yPoints[i]
		divide = deltaX
		# if divide==0:
		# 	divide=1.
		# if deltaX==0:
		# 	deltaX=1.

		if deltaX==0:
			#Gradient 
			m = deltaY
			yCon[count:count] = (yStart + m*numpy.arange(deltaX))
			#need longer integration over start/end points
			if i==0 or i==(xPoints.shape[0]-2):
				# print('hi')
				mm = yStart
				yCon[count:count] += (mm*numpy.arange(deltaX))
				num_binPoints_counter[count:count] = 1.

		else:
			#Gradient 
			m = deltaY/deltaX
			yCon[count:count+deltaX] = (yStart + m*numpy.arange(deltaX))/divide
			num_binPoints_counter[count:count+deltaX] = 1./deltaX 

			#need longer integration over start/end points
			if i==0 or i==(xPoints.shape[0]-2):
				# print('hi')
				mm = yStart/deltaX
				yCon[count:count+deltaX] += (mm*numpy.arange(deltaX))/divide
				num_binPoints_counter[count:count+deltaX] = 1./deltaX
		
		count += deltaX
		bin_count += 1

		# if i!=(xPoints.shape[0]-2):

	return xCon, yCon, num_binPoints_counter




def bin_profile(xs, ys, x_bin):
	"""Bins continuous line plot into designated bins.
	Bin width is defined by the mid-point between adjacent bins."""

	y_bin = numpy.zeros(x_bin.shape[0])
	x_bin = numpy.round(x_bin).astype('int')
	xc, yc, num_binPoints_counter = continuous_linePlot_forIntegration(xs, ys)

	bin_size = numpy.zeros(x_bin.shape[0])
	num_binPoints = numpy.zeros(x_bin.shape[0])

	for i in range(x_bin.shape[0]):


		if i == (x_bin.shape[0]-1):
			r_binStep = numpy.abs(x_bin[i] - x_bin[i-1])/2.
		if i >= 0:
			if i==(x_bin.shape[0]-1):
				r_binStep = numpy.abs(x_bin[i] - x_bin[i-1])/2.
			else:
				r_binStep = numpy.abs(x_bin[i] - x_bin[i+1])/2.

		if i==0:
			l_binStep = numpy.abs(x_bin[i] - x_bin[i+1])/2.
		else:
			l_binStep = numpy.abs(x_bin[i] - x_bin[i-1])/2.
			
		start = numpy.round(x_bin[i] - l_binStep).astype('int')
		stop = numpy.round(x_bin[i] + r_binStep).astype('int')
		if start<0:
			start = 0

		bin_size[i] = stop - start
		y_bin[i] = yc[start: stop].sum()
		num_binPoints[i] = num_binPoints_counter[start: stop].sum()#/(stop-start)
		# stopppp
		# print(i, 'Bin LHS: {}'.format(start), ';', 'Bin RHS: {}'.format(stop))
	# print(num_binPoints)
	# num_binPoints[1:] -= num_binPoints[:x_bin.shape[0]-1]
	# print(num_binPoints)

	return y_bin, bin_size, num_binPoints, xc, yc





if __name__ == '__main__':

	"""Demonstration"""
	scidar = fits.getdata('scidar_example.fits')

	scidar_x = scidar[0]
	scidar_y = scidar[1]
	# x_bin = numpy.array([0,5000,15000])
	x_bin = numpy.arange(0,25000,1000)

	y_bin, bin_size, num_binPoints, xc, yc = bin_profile(scidar_x, scidar_y, x_bin)
	pyplot.figure()
	pyplot.yscale('log')
	pyplot.ylim(1e-20, 1e-12)
	pyplot.plot(x_bin, y_bin, label='Binned Profile')
	pyplot.plot(scidar_x, scidar_y, label='Input SCIDAR Profile')
	pyplot.plot(xc,yc, label='Continuous Line Plot')
	pyplot.legend()