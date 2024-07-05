from . import views
from django.urls import path

urlpatterns = [
    path('', views.plans, name='plans'),

    #add plan
    path('createplan/', views.createplan, name='createplan'),
    
    #edite
    path('update/<int:id>/',views.update_plan, name='update_plan'),
    
    #delete
    path('delete/<int:id>/' ,views.delete_plan, name='delete_plan'),
    

]
