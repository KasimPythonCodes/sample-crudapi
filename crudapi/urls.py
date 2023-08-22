
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.StudentRegistration.as_view(),),
    path('<int:id>/',views.Studentupdate.as_view(),),
    path('search/',views.StudentRegistrationsearch.as_view(),),

]
