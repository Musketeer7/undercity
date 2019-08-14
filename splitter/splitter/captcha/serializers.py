from rest_framework import serializers
from .models import Captcha

class CaptchaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Captcha
		fields = ('id', 'created_at', 'modified_at', 'known', 'unknown',)
		# fields = "__all__"

class CheckSerializer(serializers.ModelSerializer):
	class Meta:
		model = Captcha
		fields = ('captchaId', 'knownInput', 'unknownInput',)
		# fields = "__all__"
