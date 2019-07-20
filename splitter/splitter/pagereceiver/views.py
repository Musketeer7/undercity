
# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from .serializers import FileSerializer, UserSerializer, GroupSerializer, KnownSerializer, KnownRepoSerializer
from .models import File, Known, KnownRepo

from .test import test1


# class FileUploadView(viewsets.ModelViewSet):
# 	parser_class = (FileUploadParser,)

# 	queryset = File.objects.all()

# 	def post(self, request, *args, **kwargs):

# 		file_serializer = FileSerializer(data=request.data)

# 		if file_serializer.is_valid():
# 			file_serializer.save()
# 			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
# 		else:
# 			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileUploadView(viewsets.ModelViewSet):
	queryset = File.objects.all()
	serializer_class = FileSerializer

	# @detail_route(methods=['post'])
	# def upload_docs(request):
	# 	try:
	# 		file = request.data['file']
	# 	except KeyError:
	# 		raise ParseError('Request has no resource file attached')
	# 	product = Product.objects.create(image=file)
		
	def post(self, request, *args, **kwargs):
		
		file_serializer = FileSerializer(data=request.data)

		if file_serializer.is_valid():
			file_serializer.save()
			test1("inside view")
			# f = open("text.txt", "a")
			# f.write("Now the file has more content! ")
			# f.close()

			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

			


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

	def detail(request, user_id):
		return HttpResponse("You're looking at User %s." % user_id)



class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class KnownViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Known.objects.all()
	serializer_class = KnownSerializer	


class KnownRepoViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = KnownRepo.objects.all()
	serializer_class = KnownRepoSerializer	

