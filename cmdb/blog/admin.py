from django.contrib import admin
from .models import Host_Info
class HostifoAdmin(admin.ModelAdmin):
    list_display = ("host_name","host_ip","host_type","host_location","host_os","host_ctime","host_info","host_monitor")
    search_fields=("host_ip","host_name","host_type")
    list_filter=("host_os","host_location")
    ordering=['host_ctime','host_uptime']

# Register your models here.
admin.site.register(Host_Info,HostifoAdmin)