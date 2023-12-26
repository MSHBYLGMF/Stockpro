from django.urls import path
from .import views


urlpatterns=[
    path('edu/',views.home,name='home'),
    path('post/',views.entry,name ='entry'),
    path('list/',views.comp_list,name ='list'),
    path('update/<int:id>',views.comp_edit,name ='update'),
    path('delete/<int:id>',views.computer_delete,name ='delete'),
    path('register/',views.registration,name ='registration'),
    path('login/',views.login,name ='login')

    
]
