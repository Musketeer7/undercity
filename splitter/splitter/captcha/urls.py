from django.urls import path
from . import views

urlpatterns = [
	path('', views.CaptchaView.as_view({'get': 'list'})),
	# path('<int:user_id>/', views.UserViewSet.detail, name='detail'),
	path('captchas/<int:pk>/', views.CaptchaView, name='captchas-detail'),
	path('check/', views.CheckView, name='check-captchas')
]
