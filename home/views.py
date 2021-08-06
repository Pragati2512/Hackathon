from django.shortcuts import render
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

#from django.contrib.staticfiles.templatetags.staticfiles import static
from .models import person , detail, food
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#from django.contrib.staticfiles import finders


#from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.model_selection import train_test_split

'''
def tryML(request):
    if request.method == 'POST':
        form = MLForm(request=request, data=request.POST)
        if form.is_valid():
            gender = form.cleaned_data.get('gender')
            age = form.cleaned_data.get('age')
            height = form.cleaned_data.get('height')

       address = 'D:\ml_data2.csv'
       people = pd.read_csv(address)
       X = people.iloc[:,[1,2,3]]
       Z = people.iloc[:,4]
       X_test = pandas.DataFrame({
                   'col1': ['Age', age],
                   'col2': ['Gender', gender],
                   'col3': ['Height', height],
        })

       knn1 = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
       knn1.fit(X, Z)
       y_pred = knn1.predict(X_test)
       print (y_pred)

       return render(request, 'ml_page.html')
    return HttpResponse("Error")
'''


def home(request):
       print ("homepage")
       address = '/home/DietCheck/dietCheck/static/Hack1.csv'
       data = pd.read_csv(address)
       X = data.iloc[:,[0,1,6,7,9]]
       Y = data.iloc[: , [2,4]]
       X_test = pd.DataFrame({
                   'Age'  : [ 35 ] ,
                   'gdr_cd': [ 0 ] ,
                   'CancerType' : [ 60 ] ,
                   'Height' : [ 12 ] ,
                   'Weight' : [ 12 ] ,
        })
       knn1 = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
       knn1.fit(X, Y)
       y_pred = knn1.predict(X_test)
       print ("Ans")
       print (y_pred)
       return render(request, 'index.html')


def profile(request):
    uss = request.user
    prsn = person.objects.get(user=uss)
    data = detail.objects.get(person=prsn)
    return render(request, 'profile.html', { "data": data, })


def diet(request):
    return render(request, 'diet.html', { "profile": diet, })


def update(request):
    return render(request, 'update.html', { "profile": diet, })


def cal_calc(request):
    if request.method == 'POST':
        #form = Form1(request=request, data=request.POST)
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        a=age.split("-")
        agey = 2020 - int(a[0])
        if gender==0:
            gen= "Male"
        else:
            gen= "Female"
        h = int(height)
        bmi = (int(weight)/(h*h))*10000
        bmia = round(bmi,2)
        address = '/home/DietCheck/dietCheck/static/Book1.csv'
        people = pd.read_csv(address)
        X = people.iloc[:,[3,4,5]]
        Z = people.iloc[:,8]
        X_test = pd.DataFrame({
                   'gdr_cd':  [ int(gender) ] ,
                   'Height' : [ int(height) ] ,
                   'Weight' : [ int(weight) ] ,
        })

        knn1 = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
        knn1.fit(X, Z)
        y_pred = knn1.predict(X_test)
        context = {'ans':y_pred, 'age':agey , 'gender':gen, 'height':height, 'weight':weight, 'bmi':bmia, }
        return render(request, 'answer.html', context )
    return render(request, 'calorie_calc.html')




def optum_calc(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        cancer = request.POST.get('cancer')
        print(age)
        print(height)
        if gender==0:
            gen= "Male"
        else:
            gen= "Female"
        address = '/home/DietCheck/dietCheck/static/Hack1.csv'
        data = pd.read_csv(address)
        X = data.iloc[:,[0,1,6,7,9]]
        Y = data.iloc[: , [2,4]]
        X_test = pd.DataFrame({
                   'Age':  [ int(age) ] ,
                   'gdr_cd':  [ int(gender) ] ,
                   'Height' : [ int(height) ] ,
                   'Weight' : [ int(weight) ] ,
                   'CancerType' : [ int(cancer) ] ,
        })
        knn1 = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
        knn1.fit(X, Y)
        y_pred = knn1.predict(X_test)
        drug = drug_name(y_pred[0][0])
        dose = y_pred[0][1]
        context = {'drug': drug , 'dose':dose, 'age':age , 'gender':gen, 'height':height, 'weight':weight,  }
        return render(request, 'answer2.html', context )
    return render(request, 'optum_calc.html')


@api_view(['POST'])
@csrf_exempt
def optum_drug_predict(request):
    if request.method == 'POST':
        print(request.POST)
        age = request.data.get('age')
        gender = request.data.get('gender')
        height = request.data.get('height')
        weight = request.data.get('weight')
        cancer = request.data.get('cancer')
        print(age)
        print(height)
        if gender==0:
            gen= "Male"
        else:
            gen= "Female"
        address = '/home/DietCheck/dietCheck/static/Hack1.csv'
        data = pd.read_csv(address)
        X = data.iloc[:,[0,1,6,7,9]]
        Y = data.iloc[: , [2,4]]
        X_test = pd.DataFrame({
                   'Age':  [ int(age) ] ,
                   'gdr_cd':  [ int(gender) ] ,
                   'Height' : [ int(height) ] ,
                   'Weight' : [ int(weight) ] ,
                   'CancerType' : [ int(cancer) ] ,
        })
        knn1 = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
        knn1.fit(X, Y)
        y_pred = knn1.predict(X_test)
        drug = drug_name(y_pred[0][0])
        dose = y_pred[0][1]
        #context = {'drug': drug , 'dose':dose, 'age':age , 'gender':gen, 'height':height, 'weight':weight,  }
        return JsonResponse({'success': True, 'drug': drug , 'dose':dose,  })
    return JsonResponse({'success': False,  'info': 'Error'})



def drug_name(argument):
    switcher = {
        0: "J3590",
        1: "J0885",
        2: "J1447",
        3: "J1950",
        4: "J1950",
        5: "J2354",
        6: "J2796",
        7: "J2820",
        8: "J2860",
        9: "J3490",
    }
    return switcher.get(argument, "Not Found")



def login_request(request):
    message = ''
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                message = "Success: You are now logged in. "
                return render(request, 'index.html',{"message": message,})
            else:
                message = "Error: Invalid username or password."
        else:
            message = "Error: Invalid employee code or password."
    form = AuthenticationForm()
    context = {"form": form,
               "message": message, }
    return render(request, "login.html", context)


def logout_request(request):
    logout(request)
    message = "Logged out successfully!"
    return render(request, 'index.html', {"message": message, })


def register(request):
    return render(request, 'register.html')


def chart(request):
    return render(request, 'chart.html')
