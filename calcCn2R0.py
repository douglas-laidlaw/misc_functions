import numpy

def calcR0(CN2, lam):
	r0 = (((((lam/(2*numpy.pi))**2)*(1/0.42))**-1.)*CN2)**(-3./5.)
	return r0

def calcCn2(r0, lam):
	CN2 = ((r0**(-5./3.))*((lam/(2*numpy.pi))**2)*(1/0.42))
	return CN2

if __name__=='__main__':
	lam = 0.5e-6
	r0 = 0.1
	# print calcCn2(r0, lam)
	# print calcR0(calcCn2(r0, lam), lam)
