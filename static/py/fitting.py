import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error
import decimal
import os

def NB (stress, speed):
	float_speed = []
	for value in speed:
		float_value = float(value)
		float_speed.append(float_value)
		
	def stageii (x, A, n):
		return A * x ** n

	poptii, pcovii = curve_fit(stageii, stress, float_speed, maxfev = 100000)
	A = poptii[0]
	n = poptii[1]

	R2 = r2_score(float_speed, stageii(stress, A, n))
	RMSE = np.sqrt(mean_squared_error(float_speed, stageii(stress, A, n)))
		
	x_range = np.linspace(min(stress), max(stress), 100)
	y_range = stageii(x_range, A, n)

	image_path = "C:/Users/18261979136/Desktop/myweb/static/images/NB_curve.jpg"
	if os.path.exists(image_path):
		os.remove(image_path)

	# 绘制原始数据点和拟合曲线
	plt.scatter(stress, float_speed, label='Original Data')
	plt.plot(x_range, y_range, label='Fitted Curve')

	# 添加图例和标签
	plt.xlabel('Stress')
	plt.ylabel('Speed')
	plt.title('NB_curve')
	plt.legend()

	plt.savefig(image_path)
	plt.close()

	return A, n, R2, RMSE