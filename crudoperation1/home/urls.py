from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('registration/',views.registration),
    path('login/',views.login),
    path('table/',views.table),
    path('update/<int:uid>/',views.update_views),
    path('update/',views.Update_form_data),
    path('delete/<int:pk>/',views.delete_user,name="delete"),
]
