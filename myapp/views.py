from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
import time
# Create your views here.

def index(request,group_name):
    return render(request, 'index.html',{'groupname':group_name})
