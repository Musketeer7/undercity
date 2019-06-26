from django.db import models
from django.utils import timezone


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
		return super(User, self).save(*args, **kwargs)
	def __str__(self):
		return self.file.name
		

class Phrase(models.Model):

	# is_deleted = models.BooleanField(default=False, blank=True)

	file = models.FileField(blank=False, null=False)
	ocr = models.CharField(max_length=30, null=True)
	first_catch = models.CharField(max_length=30, null=True)
	# second_catch = models.CharField(max_length=30, null=True)

	created_at     = models.DateTimeField(editable=False, default=timezone.now)
	modified_at    = models.DateTimeField(default=timezone.now)

	page = models.ForeignKey(File, on_delete=models.CASCADE)

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created_at = timezone.now()
		self.modified_at = timezone.now()
		return super(Phrase, self).save(*args, **kwargs)
		
	class Meta:
		ordering = ['created_at']
