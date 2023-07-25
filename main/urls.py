from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.OverallView.as_view(),name="main"),
    path('animals',views.AnimalsOvearallView.as_view(),name='animals'),
    path('cages',views.CagesOvearallView.as_view(),name='cages'),
    path('animals/<int:pk>',views.AnimalsDetailedView.as_view()),
    path('employees',views.EmployeesView.as_view(),name="employees"),
    path('employees/<int:id>',views.EmployeesDetailedView.as_view()),
    path('cages/<int:id>',views.CagesDetailedView.as_view()),
    path('positions',views.PositionsView.as_view(),name='positions'),
    path('positions/<int:id>',views.PositionsDetailedView.as_view()),
    path('register',views.RegisterUser.as_view(),name='register'),
    path('login',views.LoginUser.as_view(),name='login'),
    path('logout',views.LogoutUser.as_view())
]