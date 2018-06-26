from django.db import models
import random
import string

class MiniURL(models.Model):
	url = models.URLField(unique=True, verbose_name="URL to shorten")
	code = models.CharField(unique=True, max_length=6)
	date = models.DateTimeField(auto_now_add=True, 
								verbose_name="Date of register")
	pseudo = models.CharField(max_length=255, blank=True, null=True)
	n_access = models.IntegerField(default=0, 
								verbose_name="Number of access to the URL")

	def __str__(self):
		return "[{0}] {1}".format(self.code, self.url)

	def save(self, *args, **kwargs):
		if self.pk is None:
			self.generate(6)

		super(MiniURL, self).save(*args, **kwargs)	

	def generate(self, n_caracters):
		caracters = string.ascii_letters + string.digits
		random = [random.choice(caracters) for _ in range(n_caracters)]
		
		self.code = ''.join(random)
		

	class Meta:
		verbose_name = "Mini URL"
		verbose_name_plural = "Minis URL"
