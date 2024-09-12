from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.movie_add,name='movie_add'),
    path('show/',views.show_movie,name='show_movie'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('detail/<int:id>/',views.detail,name='detail'),
    path('register/',views.register_view,name='register_view'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Correct logout path
    # path('logoutv/', views.logoutv, name='_logout'),  # Correct logout path
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Correct login path
]
