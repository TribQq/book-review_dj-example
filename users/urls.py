from . import views

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='br:index'), name='logout'),
    path('register/', views.RegisterFormView.as_view(), name='register')
]