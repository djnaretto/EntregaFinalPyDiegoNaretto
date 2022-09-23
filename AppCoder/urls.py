from django.urls import path

#cosas para el login
from django.contrib.auth.views import LogoutView


from AppCoder import views




urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('add_form/', views.post, name="Add_Post"),
    path('searchPost', views.buscar, name="Search_Post"),
    path('searchResults', views.buscar, name="Search_Results"),
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name="Logout"),
    path('edit_Profile/', views.editProfile, name="Edit_Profile"),
 

]


