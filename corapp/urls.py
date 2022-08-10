from corapp import views
from django.urls import path

urlpatterns=[
    path("",views.Index,name="Index"),
    path("Admin_Home",views.Admin_Home,name="Admin_Home"),
    path('Login_SignUp_Page',views.Login_SignUp_Page,name="Login_SignUp_Page"),
    path("CoursePage",views.CoursePage,name="CoursePage"),
    path("AddCourse",views.AddCourse,name="AddCourse"),
    path("Staff_SignUp",views.Staff_SignUp,name="Staff_SignUp"),
    path("Staff_Login",views.Staff_Login,name="Staff_Login"),
    path("Staff_Logout",views.Staff_Login,name="Staff_LogOut"),
    path("Add_Student",views.Add_Student,name="Add_Student"),
    path("Student_Page",views.Student_Page,name="Student_Page"),
    path("Student_Details",views.Student_Details,name="Student_Details"),
    path('Course_Details',views.Course_Details,name='Course_Details'),
    path('Staff_Details',views.Staff_Details,name='Staff_Details'),
    path('Delete_Staff/<int:id>',views.Delete_Staff,name="Delete_Staff"),
    path('Profile',views.Profile,name='Profile'),
    path("Edit_Page",views.Edit_Page,name='Edit_Page'),
    path('Edit_Profile',views.Edit_Profile,name="Edit_Profile"),
    ]

