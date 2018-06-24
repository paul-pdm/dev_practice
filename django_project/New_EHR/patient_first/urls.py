from django.conf.urls import url, include
from patient_first import views

app_name = 'patient_first'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/', views.about, name='about'),
    url(r'^add_patient/$', views.add_patient, name="add_patient"),
    url(r'^patient/(?P<patient_name_slug>[\w\-]+)/$',
        views.show_patient, name='show_patient'),
    url(r'^patient/(?P<patient_name_slug>[\w\-]+)/add_encounter/$',
        views.add_encounter, name='add_encounter'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
]