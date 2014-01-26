from django.db import models

class FileOwner(models.Model):
    username = models.CharField(max_length=250)
    def __unicode__(self):
        return self.username

class CodeFile(models.Model):
    name = models.CharField(max_length=250)
    number = models.IntegerField(default=1)
    trueorfalse = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(FileOwner, null=True, blank=True)

    def __unicode__(self):
        return "CodeFile: " + self.name

    def mymethod(self):
        return "MYMETHOD CALLED"


