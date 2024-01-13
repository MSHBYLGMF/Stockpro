from django.urls import path,include
from .import views


urlpatterns=[
    path('',views.home,name='home'),
    path('list_items/',views.Stocklist,name='stocklist'),
    path('add_items/', views.add_items, name='add_items'),
    path('update_items/<int:id>/', views.update_items, name="update_items"),
    path('stock_detail/<int:id>/', views.stock_detail, name="stock_detail"),
    path('delete_items/<int:id>/', views.delete_items, name="delete_items"),
    path('issue_items/<int:id>/', views.issue_items, name="issue_items"),
    path('receive_items/<int:id>/', views.receive_items, name="receive_items"),
    path('reorder_level/<int:id>/', views.reorder_level, name="reorder_level"),
    path('accounts/', include('registration.backends.default.urls')),

]