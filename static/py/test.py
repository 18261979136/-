
def adding (stress_list,speed_list):
	result = []
	n = len(stress_list)
	for i in range(0, n - 1):
		h = stress_list[i] + speed_list[i]
		result.append(h)
	return result
		
	