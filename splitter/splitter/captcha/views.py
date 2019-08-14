from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Captcha
from rest_framework import viewsets
from .serializers import CaptchaSerializer, CheckSerializer
from django.views import View
from django.http import HttpResponse
import json


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

@api_view(['GET', 'PUT'])
def Test(request):
	if request.method == 'PUT':
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		content = body['captchaId']
		print(content)
		return Response(content,status=200)

@api_view(['GET', 'PUT'])
def CheckView(request):

	if request.method == 'PUT':
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		captcha = Captcha.objects.get(id=body['captchaId'])
		print(captcha.known)
		print(captcha.unknown)
		print(captcha.unknown.first_catch)
		unknownInput = body['unknownInput']
		print(unknownInput)
		knownInput = body['knownInput']
		print(knownInput)
		print("equals")
		print(captcha.known.text)

		if (knownInput == captcha.known.text):
			captcha.unknown.first_catch = unknownInput
			print(type(captcha.unknown))
			captcha.unknown.save()
			return HttpResponse(status=200)


		return HttpResponse(status=475)

	if request.method == 'GET':
		return HttpResponse(status=201)
