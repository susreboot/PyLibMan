from django.urls import path
from .views import pdf_view
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('staff/',views.staff,name='staff'),
    path('stafflogin/',views.stafflogin,name='stafflogin'),
    path('staffsignup/',views.staffsignup,name='staffsignup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addbook/',views.addbook,name='addbook'),
    path('SignupBackend/',views.SignupBackend,name='SignupBackend'),
    path('LoginBackend/',views.LoginBackend,name='LoginBackend'),
    path('AddBookSubmission/',views.AddBookSubmission,name='AddBookSubmission'),
    path('deletebook/<int:id>',views.deletebook,name='deletebook'),
    path('bookissue/',views.bookissue,name='bookissue'),
    path('returnbook/',views.returnbook,name='returnbook'),
    path('HandleLogout/',views.HandleLogout,name='HandleLogout'),
    path('issuebooksubmission/',views.issuebooksubmission,name='issuebooksubmission'),
    path('returnbooksubmission/',views.returnbooksubmission,name='returnbooksubmission'),
    path('Search/',views.Search,name='Search'),
    path('Searchstudent/',views.Searchstudent,name='Searchstudent'),
    path('editbookdetails/<int:id>',views.editbookdetails,name='editbookdetails'),
    path('<int:id>/updatedetails/',views.updatedetails,name='updatedetails'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('addstudentsubmission/',views.addstudentsubmission,name='addstudentsubmission'),
    path('viewissuedbook/',views.viewissuedbook,name='viewissuedbook'),
    path('viewstudents/',views.viewstudents,name='viewstudents'),
    path('deletestudent/<int:id>/', views.delete_student, name='deletestudent'),
    path('pdf/', pdf_view, name='pdf_view'),
] 
