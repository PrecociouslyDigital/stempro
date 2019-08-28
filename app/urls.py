from django.urls import path
from app import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('recommend', views.Recommend.as_view(), name='recommend'),
    path('subscribe_result', views.thanks_subscribe_view, name='subscribe_result'),
    path('involved', views.InvolvedActiveView.as_view(), name='involved'),
    path('course', views.CourseView.as_view(), name='course'),
    path('tutor', views.TutorActiveView.as_view(), name='tutor'),
    path('program', views.ProgramView.as_view(), name='program'),
    path('confirm', views.RegisterView.as_view(), name='confirm'),    
]
