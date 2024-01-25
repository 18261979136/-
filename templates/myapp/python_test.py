
from scipy.optimize import curve_fit


print('hallo')
stress_amp = [79135, 95565, 106983, 2098530, 5373760]
Nf2 = [750, 700, 650, 600, 540]

def func_b(x, sigmaf, b):
	return sigmaf * x ** b
popte, pcove = curve_fit(func_b, Nf2, stress_amp, maxfev=100000)
sigmaf = popte[0]
b = popte[1]

with open('C:/Users/18261979136/Desktop/myweb/scripts/fitting_result.txt', 'w') as f:
	f.write('sigmaf:{}\n'.format(sigmaf))
	f.write('b:{}\n'.format(b))
