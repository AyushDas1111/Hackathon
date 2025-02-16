from django.shortcuts import render, redirect
import mysql.connector as sql

def loginaction(request):
    error_message = ""  # For passing error messages to the template

    if request.method == "POST":
        # Connect to the database
        m = sql.connect(host="localhost", user="root", passwd="Ayush@2004", database='fithub')
        cursor = m.cursor()

        # Extract email and password from the POST data
        d = request.POST
        em = d.get("email", "").strip()
        pwd = d.get("password", "").strip()

        # Query to get the password for the provided email
        query = "SELECT Password FROM users WHERE Email = %s"

        cursor.execute(query, (em,))
        result = cursor.fetchone()

        # Close the database connection
        cursor.close()
        m.close()

        # Check if the user exists and use plain-text comparison
        if result:
            if pwd == result[0]:  # Use plain-text comparison for now
                return render(request, "homepage_after.html")

            else:
                error_message = "Invalid password. Please try again."
        else:
            error_message = " Account doesn't exist. Sign up first!"

    return render(request, 'login_page.html', {'error_message': error_message})

from django.shortcuts import render


def calorie_count(request):

   return render(request, 'caloriecount_page.html')
def bmi_calculator(request):
  return render(request, 'bmi_page.html')
def diet_page(request):
    return render(request, 'diet_page.html')

# login/views.py
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage_before.html')  # Adjust the template name if needed

from django.shortcuts import render

def workoutplan_page(request):
    return render(request, 'workoutplan_page.html')

from django.shortcuts import render

def own_diet(request):
    return render(request, 'own_diet.html')

def demo_work_out(request):
    return render(request, 'demo_work_out.html')





