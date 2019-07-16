from django.urls import path
from . import views

urlpatterns = [
	path('', views.FileUploadView.as_view({'get': 'list'})),
	# path('<int:user_id>/', views.UserViewSet.detail, name='detail'),
	path('users/<int:pk>/',	views.UserViewSet,	name='user-detail')
]
