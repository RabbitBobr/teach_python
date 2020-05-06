from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from .views import index, rubrics, BbCreateView, BbDetailView, BbByRubricView, BbEditView, BbDeleteView

urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    path('update/<int:pk>/', BbEditView.as_view(), name='update'),
    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),
    path('rubrics/', rubrics, name='rubrics'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('accounts/password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/', index),
    path('', index, name='index'),
]
