from baseapp import views
from django.urls import path

urlpatterns=[
    path('',views.index,name="index"),
    path('<int:question_id>',views.show_question,name="show_problem"),
    path('<int:question_id>/add',views.add_name,name="add_name"),
    
]