from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.OverallView.as_view()),
    path('animals',views.AnimalsOvearallView.as_view(),name='animals'),
    path('cages',views.CagesOvearallView.as_view(),name='cages'),
    path('animals/<int:pk>',views.AnimalsDetailedView.as_view()),
    path('employees',views.EmployeesView.as_view(),name="employees"),
    path('employees/<int:id>',views.EmployeesDetailedView.as_view()),
    path('cages/<int:id>',views.CagesDetailedView.as_view()),
    path('positions',views.PositionsView.as_view(),name='positions'),
    path('positions/<int:id>',views.PositionsDetailedView.as_view())
]