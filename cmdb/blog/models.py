from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Host_Info(models.Model):
    host_id=models.AutoField(primary_key=True)
    host_name=models.CharField(max_length=100,unique=True)
    host_ip=models.GenericIPAddressField()
    host_type=models.CharField(max_length=100)
    host_location=models.CharField(max_length=100)
    host_os=models.CharField(max_length=100)
    host_monitor=models.BooleanField()
    host_ctime=models.DateTimeField(auto_now_add=True)
    host_uptime=models.DateTimeField(auto_now=True)
    host_info=models.TextField()
    host_user=models.ForeignKey(User,bool)
    host_status_choices=(("生产环境","生产环境"),("测试环境","测试环境"))
    host_status=models.CharField(max_length=100,choices=host_status_choices)
    class Meta:
        db_table='hostinfo'
    def __str__(self):
        return self.host_name
# Create your models here.
