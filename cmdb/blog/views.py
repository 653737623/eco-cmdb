from django.shortcuts import render,get_object_or_404
from .models import Host_Info
#所有设备信息
def index(request):
    name=Host_Info.objects.all()
    return render(request,"index.html",{"name":name})
def tables(request):
    name=Host_Info.objects.all()
    return render(request,"tables.html",{"name":name})
def stats(request):
    name=Host_Info.objects.all()
    return render(request,"stats.html",{"name":name})
#单个设备详细信息
def list(request,id):
    netlist=get_object_or_404(Host_Info,host_id=id)
#    netlist=Host_Info.objects.get(host_id=id)
    pub=netlist.host_ip
    return render(request,"blog/content.html",{"netlist":netlist,"publish":pub})
# Create your views here.
