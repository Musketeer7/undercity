from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import File, Known, KnownRepo


class UserSerializer(serializers.HyperlinkedModelSerializer):
	# users = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')
		# fields = "__all__"


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class FileSerializer(serializers.ModelSerializer):
	class Meta:
		model = File
		# fields = ('file',)
		fields = "__all__"
		
class PhraseSerializer(serializers.ModelSerializer):
	class Meta:
		model = File
		fields = "__all__"

class KnownSerializer(serializers.ModelSerializer):

	img = serializers.FileField(read_only=True)
	text = serializers.CharField(read_only=True)

	class Meta:
		model = Known
		fields = "__all__"

	def create(self, validated_data):
		return Known.objects.create(**validated_data)


class KnownRepoSerializer(serializers.ModelSerializer):
	class Meta:
		model = KnownRepo
		fields = "__all__"