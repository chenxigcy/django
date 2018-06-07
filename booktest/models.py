from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bprice = models.IntegerField()

    def __str__(self):
        return("%d"%self.pk).encode("utf-8")

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=40)
    hBook = models.ForeignKey('BookInfo')

    def __str__(self):
        return("%d"%self.pk).encode("utf-8")