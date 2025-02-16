from django.shortcuts import render,redirect
import mysql.connector as sql

fn=''
ln=''
mo = ''
em = ''
pwd = ''

# Create your views here.
def signaction(request):
    global fn, ln, mo, em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="Ayush@2004", database='fithub')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "FirstName":
                fn = value
            if key == "LastName":
                ln = value
            if key == "MobileNumber":
                mo = value
            if key == "Email":
                em = value
            if key == "Password":
                pwd = value

        # Insert data into the database (update to match new table structure)
        c = "INSERT INTO users (Firstname, Lastname, Mobilenumber, Email, Password) VALUES ('{}', '{}', '{}', '{}', '{}')".format(fn, ln, mo, em, pwd)
        cursor.execute(c)
        m.commit()
        
     # Redirect to the login page after successful signup
        return redirect('/login/')

         

    return render(request, 'signup_page.html')


