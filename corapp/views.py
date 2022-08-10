from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *


# Create your views here.

def Index(request):
    return render(request,"user/index.html")


def Admin_Home(request):
    if not request.user.is_staff:
        return redirect('Login_SignUp_Page')
    return render(request,'admin/adminhome.html')


def CoursePage(request):
    return render(request,'admin/addcourse.html')


def AddCourse(request):
    if request.method == 'POST':
        coursename=request.POST['coursename']
        coursefees=request.POST['coursefees']
        data = CourseModel(Course_Name=coursename,Course_Fees=coursefees)
        data.save()
        # messages.info(request, 'New User Added')
        return redirect('Index')

def Login_SignUp_Page(request):
    courses=CourseModel.objects.all()
    context={'course':courses}
    return render(request,'user/login&signup.html',context)


def Staff_SignUp(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        username=request.POST['username']
        address=request.POST['address']
        email=request.POST['email']
        gender=request.POST['gender']
        course=request.POST['select']
        age=request.POST['age']
        password=request.POST['password']
        confirm_password=request.POST['confirmpassword']

        # if request.FILES.get('photo') is not None:
        photo=request.FILES.get('photo')
        # else:
        #     photo="static/images/download.png"
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This Username Already Exists!')
                return redirect('Login_SignUp_Page')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This Email Already Exists!')
                return redirect('Login_SignUp_Page')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
                user.save()
                messages.success(request, 'SuccessFully Registered')
                print("Successed...")

                data=User.objects.get(id=user.id)
                cdata=CourseModel.objects.get(id=course)
                ext_user_data=StaffModel(Staff_Address=address,Staff_Gender=gender,Staff_Age=age,Staff_Photo=photo,Staff=data,Course=cdata)
                ext_user_data.save()
                messages.success(request, 'SuccessFully Registered')
                print('success..')
                return redirect('Login_SignUp_Page')

    # return render(request,'login&signup.html')
        else:
            # messages.info(request, 'Password doesnt match !')
            print("Password is not Matching.. ") 
            return redirect('Login_SignUp_Page') 
        return redirect('Teacher_Login')
    else:
        return render(request,'login&signup.html')


def Staff_Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        # request.session['uid']=user.id
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('Admin_Home')
            else:
                login(request,user)
                auth.login(request,user)
                # messages.info(request,f'welocome{username}')
                return redirect('Index')
        else: 
            return redirect('Staff_Login')
    else:
        return redirect('Admin_Home')
        # else:
        #     return redirect('Teacher_Login_SignUp_Page')

def Teacher_LogOut(request):
    # request.session['uid']=""             # session id method
    if request.user.is_authenticated:     # is authenticated method
        auth.logout(request)
    return redirect('Index')


def Student_Page(request):
    courses=CourseModel.objects.all()
    context={'courses':courses}
    return render(request,'admin/addstudent.html',context)


def Add_Student(request):
    if request.method=='POST':
        stdname=request.POST['stdname']
        stdaddress=request.POST['stdaddress']
        stdage=request.POST['stdage']
        # joindate=request.POST['joindate']
        select=request.POST['select']
        course=CourseModel.objects.get(id=select)
        data = StudentModel(Std_Name=stdname,Std_Address=stdaddress,Std_Age=stdage,Course=course)
        data.save()
        return redirect('Index')


def Student_Details(request):
    if not request.user.is_staff:
        return redirect('Login_SignUp_Page')
    student_detail = StudentModel.objects.all()
    return render(request,'admin/studentdetail.html',{'student':student_detail})


def Course_Details(request):
    if not request.user.is_staff:
        return redirect('Login_SignUp_Page')
    course=CourseModel.objects.all()
    return render(request,'admin/coursedetails.html',{'cdata':course,})



def Staff_Details(request):
    if not request.user.is_staff:
        return redirect('Login_SignUp_Page')
    teacher_detail = StaffModel.objects.all()
    return render(request,'admin/staffdetails.html',{'staff':staff_detail})

def Delete_Staff(request,id):
    if not request.user.is_staff:
        return redirect('Login_SignUp_Page')
    tchr = StaffModel.objects.get(id=id)
    tchr.delete()
    return redirect('Staff_Details')

# @login_required(login url='Sigin_signUp_page')
def Profile(request):
    users=StaffModel.objects.get(Staff=request.user)
    context={"user":users}
    return render(request,'user/profile.html',context)


def Edit_Page(request):
    teacher=StaffModel.objects.get(Staff=request.user)
    return render(request,"user/editprofile.html",{'edit':Staff})

def Edit_Profile(request):
    if request.method=='POST':
        tdata = StaffModel.objects.get(Staff=request.user)
        tdata.first_name = request.POST.get('firstname')
        tdata.last_name = request.POST.get('lastname')
        tdata.username = request.POST.get('username')
        tdata.email = request.POST.get('email')
        tdata.Staff_Address = request.POST.get('address')
        tdata.Staff_Gender = request.POST.get('gender')
        tdata.Staff_age = request.POST.get('age')
        tdata.Staff_Photo =request.POST.get('photo')
        tdata.save()
        return redirect('Profile')
    return render(request, 'user/editprofile.html')
