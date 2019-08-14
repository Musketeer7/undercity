from django.db import models
from django.utils import timezone
from .helper.splitter import imageSplitter
from .helper.splitter2 import imageSplitter2
from .helper.wordsplitter import wordsplitter
from .test import test1

class File(models.Model):

	file = models.FileField(blank=False, null=False)
	# is_deleted = models.BooleanField(default=False, blank=True)
	created_at     = models.DateTimeField(editable=False, default=timezone.now)
	modified_at    = models.DateTimeField(default=timezone.now)


	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created_at = timezone.now()

		self.modified_at = timezone.now()
		
		x = super(File, self).save(*args, **kwargs)

		print("========")
		print(self.file.name)
		print(type(self.file))
		print(type(self))
		print(type(x))
		print("========")
		imageSplitter2(self)

		return x

	def __str__(self):
		return self.file.name

		


class Phrase(models.Model):

	# is_deleted = models.BooleanField(default=False, blank=True)

	file = models.FileField()
	ocr = models.CharField(max_length=30, null=True, blank=True)
	first_catch = models.CharField(max_length=30, null=True)
	# second_catch = models.CharField(max_length=30, null=True)

	created_at     = models.DateTimeField(editable=False, default=timezone.now)
	modified_at    = models.DateTimeField(default=timezone.now)

	page = models.ForeignKey(File, on_delete=models.CASCADE)

	sequence = models.IntegerField(blank=False, null=False, default=0)

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created_at = timezone.now()
		self.modified_at = timezone.now()
		return super(Phrase, self).save(*args, **kwargs)
		
	class Meta:
		ordering = ['created_at']




class Known(models.Model):

	# is_deleted = models.BooleanField(default=False, blank=True)

	img = models.FileField(blank=False, null=False)
	text = models.CharField(max_length=30, null=True, blank=True)
	# second_catch = models.CharField(max_length=30, null=True)

	created_at     = models.DateTimeField(editable=False, default=timezone.now)
	modified_at    = models.DateTimeField(default=timezone.now)


	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created_at = timezone.now()
		self.modified_at = timezone.now()
		return super(Known, self).save(*args, **kwargs)
		
	class Meta:
		ordering = ['created_at']


class KnownRepo(models.Model):

	file = models.FileField(blank=False, null=False)

	created_at     = models.DateTimeField(editable=False, default=timezone.now)
	modified_at    = models.DateTimeField(default=timezone.now)	

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created_at = timezone.now()

		self.modified_at = timezone.now()
		
		x = super(KnownRepo, self).save(*args, **kwargs)

		print("========")
		print(self.file.name)
		print(type(self.file))
		print(type(self))
		print("========")
		# imageSplitter2(self)
		wordsplitter(self)

		return x
		

	class Meta:
		ordering = ['created_at']


class Captcha(models.Model):

	# is_deleted = models.BooleanField(default=False, blank=True)

	phrase = Phrase()
	known = Known()

	# second_catch = models.CharField(max_length=30, null=True)

	created_at     = models.DateTimeField(editable=False, default=timezone.now)
	modified_at    = models.DateTimeField(default=timezone.now)

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created_at = timezone.now()
		self.modified_at = timezone.now()
		return super(Phrase, self).save(*args, **kwargs)
		
	class Meta:
		ordering = ['created_at']

