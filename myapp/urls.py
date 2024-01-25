from django.urls import path,include


from myapp import views


urlpatterns = [
	path('math/', views.math,name='math'),
	path('result/', views.result, name='result'),
	path('shiyan/', views.shiyan, name='shiyan'),
	path('pingding/', views.pingding, name='pingding'),
	path('tezheng/', views.tezheng, name='tezheng'),
	path('math/suv/', views.suv,name='suv'),
	path('math/forest/', views.forest,name='forest'),
	path('get_test1/', views.get_test1, name = 'get_test1'),
	path('fitting/', views.fitting, name = 'fitting'),
	path('sorted/', views.display_test_data, name = 'display_test_data'),
	path('get_test2/', views.get_test2, name = 'get_test2'),
	path('mysql/', views.mysql_test, name = 'mysql'),
	#--------------配置users信息操作路由-----------------------------------
	path('users/', views.indexUsers, name = 'indexusers'),
	path('users/add/', views.addUsers, name = 'addusers'),
	path('users/insert/', views.insertUsers, name = 'insertusers'),
	path('users/del/<int:uid>/', views.delUsers, name = 'delusers'),
	path('users/edit/<int:uid>/', views.editUsers, name = 'editusers'),
	path('users/update/', views.updateUsers, name = 'updateusers'),
	#-------------配置creep信息操作路由----------------------------------
	path('creep/', views.indexCreep, name = 'indexcreep'),
	path('creep/add/', views.addCreep, name = 'addcreep'),
	path('creep/insert/', views.insertCreep, name = 'insertcreep'),
	path('creep/del/<int:uid>/', views.delCreep, name = 'delcreep'),
	path('creep/edit/<int:uid>/', views.editCreep, name = 'editcreep'),
	path('creep/update/', views.updateCreep, name = 'updatecreep'),
	path('creep/fit/', views.fitCreep, name = 'fitcreep'),

]