"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from signup.views import signaction
from login.views import loginaction, calorie_count, bmi_calculator, diet_page,workoutplan_page,own_diet,demo_work_out


from login.views import homepage  # Import the homepage view

urlpatterns = [
    path('', homepage, name='homepage'),  # Add this line to handle the root URL
    path('admin/', admin.site.urls),
    path('signup/', signaction, name='signup'),
    path('login/', loginaction, name='login'),
    path('login/caloriecount_page/', calorie_count, name='caloriecount_page'),
    path('login/bmi_page/', bmi_calculator, name='bmi_page'),
    path('login/diet_page/', diet_page, name='diet_page'),
    path('login/workoutplan_page', workoutplan_page, name='workoutplan_page'),
    path('login/own_diet/', own_diet, name='own_diet'),
    path('demo_work_out/', demo_work_out, name='demo_work_out'),
    

]

