from django.urls import path
from TODO import views


urlpatterns = [
    path('',views.crud,name="index"),
    
    path('insert',views.insertData,name="insertData"),
    path('update/<id>',views.updateData,name = "updateData"),
    path('delete/<id>',views.deleteData,name = "deleteData")
    
]