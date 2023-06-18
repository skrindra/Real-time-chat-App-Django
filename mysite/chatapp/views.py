from django.shortcuts import render
from .models import ChatRoom,ChatMessage
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request,'chatapp/index.html',{'chatrooms':chatrooms})

@login_required
def chatroom(request,slug):
    chatroom = ChatRoom.objects.get(slug=slug)

    # retrieve the latest 30 messages
    messages = ChatMessage.objects.filter(room=chatroom)[0:30]
    return render(request,'chatapp/room.html',
                  {'chatroom':chatroom,'messages':messages})
