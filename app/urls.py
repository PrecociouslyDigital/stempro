from django.urls import path
from app import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('recommend', views.Recommend.as_view(), name='recommend'),
    path('subscribe_result', views.thanks_subscribe_view, name='subscribe_result'),
    path('involved', views.InvolvedActiveView.as_view(), name='involved'),
    path('course', views.CourseView.as_view(), name='course'),
    path('tutor', views.TutorActiveView.as_view(), name='tutor'),
    path('confirm', views.RegisterView.as_view(), name='confirm'),
    path('presentation/', views.SubscribeProgramView.as_view(), name='presentation'),
    path('mypage', views.MyPage.as_view(), name='mypage'),
    path('mission', views.MissionView.as_view(), name='mission'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('program', views.ProgramView.as_view(), name='program'),
    path('events', views.EventsView.as_view(), name='events'),
    path('news', views.NewsView.as_view(), name='news'),
    path('volunteer', views.VolunteerView.as_view(), name='volunteer'),
    path('donate', views.DonateView.as_view(), name='donate'),
    path('club', views.PreclubView.as_view(), name='club'),             
]
