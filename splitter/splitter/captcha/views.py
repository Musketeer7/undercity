from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Captcha
from rest_framework import viewsets
from .serializers import CaptchaSerializer


# @api_view(['GET', 'POST'])
# def snippet_list(request):
# 	"""
# 	List all code snippets, or create a new snippet.
# 	"""
# 	if request.method == 'GET':
# 		captchas = Captcha.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return Response(serializer.data)

# 	elif request.method == 'POST':
# 		serializer = SnippetSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CaptchaView(viewsets.ModelViewSet):
	queryset = Captcha.objects.all()
	serializer_class = CaptchaSerializer

	# @detail_route(methods=['post'])
	# def upload_docs(request):
	# 	try:
	# 		file = request.data['file']
	# 	except KeyError:
	# 		raise ParseError('Request has no resource file attached')
	# 	product = Product.objects.create(image=file)
		
	# def post(self, request, *args, **kwargs):
	# 	print ("inside post")
	# 	captcha_serializer = CaptchaSerializer(data=request.data)

	# 	if captcha_serializer.is_valid():

	# 		print ("if")



	# 		max_id = Known.objects.all().aggregate(max_id=Max("id"))['max_id']
	# 		pk = random.randint(1, max_id)
	# 		random_known = Known.objects.get(pk=pk)

	# 		max_id = File.objects.all().aggregate(max_id=Max("id"))['max_id']
	# 		pk = random.randint(1, max_id)
	# 		random_unknown = File.objects.get(pk=pk)

	# 		captcha_serializer.save(uknown=random_unknown ,known=random_known )

	# 		print (type(random_unknown))
	# 		print (type(random_known))

	# 		print (type(random_known.img))


	# 		# test1("inside view")
	# 		# f = open("text.txt", "a")
	# 		# f.write("Now the file has more content! ")
	# 		# f.close()


	# 		return Response(captcha_serializer.data, status=status.HTTP_201_CREATED)
	# 	else:
	# 		return Response(captcha_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
