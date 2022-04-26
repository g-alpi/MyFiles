from django.db import models
from django.contrib.auth.models import User


class Directory (models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class File (models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_time = models.DateTimeField(auto_now_add=True)
    father = models.ForeignKey(Directory, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
    
class ShareFile(models.Model):
    file_id = models.ForeignKey(File, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.file_id.name + ' -> ' + self.user_id.username

class ShareDirectory (models.Model):
    directoy_id = models.ForeignKey(Directory, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.directoy_id.name + ' -> ' + self.user_id.username