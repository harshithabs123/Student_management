import imp
from django.shortcuts import render, redirect
from . models import Student

# Create your views here.



def index(request):
    return login_request(request)

def student_login(reqeust):
    Students = Student.objects.all()
    return render(reqeust, "students/admin/student_dashboard.html", {"students" : Students})

def login_request(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, password)
        # user = authenticate(email=email, password=password)
        # print(user)
        if Student.objects.filter(email=email, password=password).exists():
            return redirect('/students/user/dashboard')
    return render(request, "students/login.html")



def signup(request):
    message = {"email" : None, "password" : None}
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        contact_number = request.POST["contact"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password == confirm_password:
            if Student.objects.filter(email=email).exists():
                message["email"] = "User already registered with this email id"
            else:
                student = Student(name=name, email=email, contact_number=contact_number, password=password)
                student.save()
                return redirect('/students/login')
        else:
            message["password"] ="Password Not Matched"
    return render(request, 'students/signup.html', {"message" : message })



def logout_request(request):
	return redirect("/students/login")


def add_student(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        contact_number = request.POST["contact"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password == confirm_password:
            if Student.objects.filter(email=email).exists():
                print("User already registered with this email id")
            else:
                student = Student(name=name, email=email, contact_number=contact_number, password=password)
                student.save()
    return redirect('/students/user/dashboard')