from django.db import models
from splitter.pagereceiver.models import Known, File, Phrase
from django.utils import timezone
from django.db.models import Max
import random
from django.shortcuts import get_object_or_404


class Captcha(models.Model):

	# unknown = File()
	# known = Known()

	# unknown = models.ManyToManyField(Phrase)
	# known = models.ManyToManyField(Known)

	unknown = models.ForeignKey(Phrase, on_delete=models.CASCADE, null=True, blank=True)
	known = models.ForeignKey(Known, on_delete=models.CASCADE, null=True, blank=True)

	# is_deleted = models.BooleanField(default=False, blank=True)
	created_at     = models.DateTimeField(editable=False, default=timezone.now)
	modified_at    = models.DateTimeField(default=timezone.now)


	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created_at = timezone.now()

		self.modified_at = timezone.now()
		
		# x = super(Captcha, self).save(*args, **kwargs)
		# print("x type")
		# print(type(x))
		print("========")
		# print(self.file.name)
		# print(type(self.file))
		print(type(self))
		print("========")
		# imageSplitter2(self)

		print("===created===")
		print(self.known)
		print(self.unknown)
		# print(type(x))
		print("=============")

		print("test1")
		#get random known
		max_id = Known.objects.all().count()
		while True:
			pk1 = random.randint(1, max_id)
			print(pk1)
			t1 = Known.objects.get(pk=pk1)
			print(type(t1))
			if (t1):
				random_known = t1
				break
		print(type(random_known))
		print(random_known)
		#get random phrase
		max_id2 = Phrase.objects.all().count()

		while True:
			pk2 = random.randint(1, max_id)
			t2 = Phrase.objects.get(pk=pk2)
			if (t2 and t2.first_catch != ""):
				random_unknown = t2
				break
		print(max_id2)
		pk2 = random.randint(1, max_id2)
		print(pk2)

		# self.known.set(random_known)
		# self.unknown.set(random_unknown)



		self.known = random_known
		self.unknown = random_unknown
		print("self")
		print(self.id)
		print(self.known.id)
		# print(self.known)
		# print(self.unknown)


		print("before save")
		# super().save(*args, **kwargs)
		x = super(Captcha, self).save(*args, **kwargs)
		print("saved")

		# self.known()

		return x

	def __str__(self):
		return "captcha"

		