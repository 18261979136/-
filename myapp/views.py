from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Users
from myapp.models import Creep
import subprocess
from pandas import read_excel
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import static.py.fitting as fit



def first(request):
    return render(request,"myapp/首页.html")

def math(request):
    return render(request,"myapp/math.html")

def result(request):
    return render(request,"myapp/result.html")

def tezheng(request):
    return render(request,"myapp/特征量分析.html")

def pingding(request):
    return render(request,"myapp/评定模型.html")

def shiyan(request):
    return render(request,"myapp/试验部署.html")

def suv(request):
    return render(request,"myapp/suv.html")

def forest(request):
    return render(request,"myapp/forest.html")

def get_test1(request):
	data_set = read_excel("C:/Users/18261979136/Desktop/myweb/templates/myapp/1.xlsx")
	data = data_set.values[:,:]
	test_data = []
	for line in data:
		ls = []
		for j in line:
			ls.append(j)
		test_data.append(ls)
	return render(request,"myapp/get_test1.html", {'test_data': test_data})
			
def get_test2(request):
	data_set = read_excel("C:/Users/18261979136/Desktop/myweb/templates/myapp/-0.5.xlsx")
	data = data_set.values[:,:]
	test_data = []
	for line in data:
		ls = []
		for j in line:
			ls.append(j)
		test_data.append(ls)
	return render(request,"myapp/get_test2.html", {'test_data': test_data})

def display_test_data (request):
	data_set = read_excel("C:/Users/18261979136/Desktop/myweb/templates/myapp/1.xlsx")
	data = data_set.values[:,:]
	test_data = []
	for line in data:
		ls = []
		for j in line:
			if isinstance(j, int):
				ls.append(j)
		test_data.append(ls)
	sorted_test_data = sorted(test_data, reverse = True)
	return render(request, "myapp/sorted.html",{'test_data':sorted_test_data})
	
def fitting (request):
	data_set = read_excel("C:/Users/18261979136/Desktop/myweb/templates/myapp/1.xlsx")
	data = data_set.values[:,:]
	test_data = []
	for line in data:
		ls = []
		for j in line:
			if isinstance(j, int):
				ls.append(j)
			if len(ls) == 2 and ls not in test_data:
				test_data.append(ls)
	print(test_data)
	stress_amp = [row[0] for row in test_data]
	Nf2 = [row[1] for row in test_data]
	print(stress_amp)
	print(Nf2)

	def func_b(x, sigmaf, b):
		return sigmaf * x ** b
	popte, pcove = curve_fit(func_b, Nf2, stress_amp, maxfev=100000)
	sigmaf = popte[0]
	b = popte[1]
	print(sigmaf)
	print(b)

	plt.figure('S-N')
	plt.scatter(Nf2, stress_amp, marker='o')
	x = np.linspace(min(Nf2), max(Nf2), 100)
	plt.plot(x, func_b(x, sigmaf, b))
	plt.xlabel('2Nf (cycle)')
	plt.ylabel('Stress amplitude (MPa)')
	plt.title('S-N curve')

	image_path = "C:/Users/18261979136/Desktop/myweb/static/images/S-N_curve.jpg"
	plt.savefig(image_path)
	#plt.show()
	plt.close

	result = {'sigmaf':sigmaf, 'b':b}
	return render(request, "myapp/fitting.html", {'result':result})

def mysql_test (request):
	#ob = Users()
	#ob.name = "王五"
	#ob.age = 23
	#ob.phone = '1212356'
	#ob.save()
	return render(request,"myapp/mysql.html")
	
#----------------------------用户信息表单操作------------------------------------------

#浏览用户信息
def indexUsers (request):
	#try:
		ulist = Users.objects.all()
		context = {"userslist":ulist}
		return render(request,"myapp/users/index.html",context)
	#except:
		#return HttpResponse("没有找到用户信息！")

#加载添加用户信息表
def addUsers (request):
	return render(request,"myapp/users/add.html")

#执行用户信息添加
def insertUsers (request):
	try:
		ob = Users()
		ob.name = request.POST['name']
		ob.age = request.POST['age']
		ob.phone = request.POST['phone']
		ob.save()
		context = {"info":"添加成功！"}
	except:
		context = {"info":"添加失败！"}
	return render(request,"myapp/users/info.html",context)

#执行用户信息删除
def delUsers (request,uid=0):
	try:
		ob = Users.objects.get(id = uid)
		ob.delete()
		context = {"info":"删除成功！"}
	except:
		context = {"info":"删除失败！"}
	return render(request,"myapp/users/info.html",context)

#加载用户信息修改表单
def editUsers (request,uid=0):
	try:
		ob = Users.objects.get(id = uid)
		context = {"user":ob}
		return render(request,"myapp/users/edit.html",context)
	except:
		context = {"info":"没有找到要修改的数据！"}
		return render(request,"myapp/users/info.html",context)

#执行用户信息修改
def updateUsers (request):
	try:
		uid = request.POST['id']
		ob = Users.objects.get(id = uid)
		ob.name = request.POST['name']
		ob.age = request.POST['age']
		ob.phone = request.POST['phone']
		ob.addtime = datetime.now()
		ob.save()
		context = {"info":"修改成功！"}
	except:
		context = {"info":"修改失败！"}
	return render(request,"myapp/users/info.html",context)

#--------------------------Creep表单操作---------------------------------------------

#浏览蠕变信息
def indexCreep (request):
	#try:
		ulist = Creep.objects.all()
		context = {"creeplist":ulist}
		return render(request,"myapp/creep/index.html",context)
	#except:
		#return HttpResponse("没有找到蠕变！")

#加载添加蠕变信息表
def addCreep (request):
	return render(request,"myapp/creep/add.html")

#执行蠕变信息添加
def insertCreep (request):
	try:
		ob = Creep()
		ob.temperature = request.POST['temperature']
		ob.stress = request.POST['stress']
		ob.speed = request.POST['speed']
		ob.save()
		context = {"info":"添加成功！"}
	except:
		context = {"info":"添加失败！"}
	return render(request,"myapp/creep/info.html",context)

#执行蠕变信息删除
def delCreep (request,uid=0):
	try:
		ob = Creep.objects.get(id = uid)
		ob.delete()
		context = {"info":"删除成功！"}
	except:
		context = {"info":"删除失败！"}
	return render(request,"myapp/creep/info.html",context)

#加载用户信息修改表单
def editCreep (request,uid=0):
	try:
		ob = Creep.objects.get(id = uid)
		context = {"creep":ob}
		return render(request,"myapp/creep/edit.html",context)
	except:
		context = {"info":"没有找到要修改的数据！"}
		return render(request,"myapp/creep/info.html",context)

#执行用户信息修改
def updateCreep (request):
	try:
		uid = request.POST['id']
		ob = Creep.objects.get(id = uid)
		ob.temperature = request.POST['temperature']
		ob.stress = request.POST['stress']
		ob.speed = request.POST['speed']
		ob.addtime = datetime.now()
		ob.save()
		context = {"info":"修改成功！"}
	except:
		context = {"info":"修改失败！"}
	return render(request,"myapp/creep/info.html",context)

#执行数据处理
def fitCreep(request):
	ulist = Creep.objects.all()
	stress_list = [creep.stress for creep in ulist]
	speed_list = [creep.speed for creep in ulist]
	
	A, n , R2, RMSE = fit.NB(stress_list,speed_list)
	result = {
		"A":A,
		"n":n,
		"R2":R2,
		"RMSE":RMSE
	}
	context = {
		"result":result
	}
	
	return render(request,"myapp/creep/result.html",context)
	