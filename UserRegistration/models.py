from django.db import models



# Create your models here.

class RegDetails(models.Model):
    name = models.CharField(max_length=200)
    mail_address = models.EmailField()



    def __str__(self):
        return '%s %s' % (self.name, self.mail_address)



   # def _get_full_name(self):
    #    "Returns the person's full name."
     #   return '%s %s' % (self.name, self.mail_address)
    #full_name = property(_get_full_name)






