from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home , name='index'),

    path("login/", views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path("logout/", views.logout_request, name='logout'),

    path('optum/', views.optum_calc , name='optum'),
    path('optum_drug_predict/', views.optum_drug_predict , name='optum-api'),


    path('calorie/', views.cal_calc , name='cal-calc'),
    path('profile/', views.profile, name='profile'),
    path('diet/', views.diet, name='diet'),
    path('update/', views.update , name='update'),
    path('chart/', views.chart , name='chart'),

    #path('about/', views.about , name='about'),
    #path('blog/', views.blog , name='blog'),
    #path('contact/', views.contact , name='contact'),
    #path('services/', views.services, name='services'),
    #path('service/<int:num>/', views.service_num, name='service'),
    #path('work/', views.work, name='work'),
    #path('work/add', views.add_work, name='add-work'),
    #path('work/list', views.work_list , name='work-list'),
    #path('work/delete/<int:pk>', views.work_delete , name='work-del'),

]



