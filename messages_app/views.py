from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Thread, Message

@login_required
def inbox(request):
    threads = Thread.objects.filter(Q(user1=request.user)|Q(user2=request.user)).order_by('-updated_at')
    return render(request, 'messages_app/inbox.html', {'threads': threads})

@login_required
def new_message(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        text     = request.POST.get('text')
        recipient = get_object_or_404(User, username=username)
        u1, u2 = sorted([request.user, recipient], key=lambda x: x.id)
        thread, _ = Thread.objects.get_or_create(user1=u1, user2=u2)
        if text:
            Message.objects.create(thread=thread, sender=request.user, text=text)
        return redirect('messages_app:thread_detail', pk=thread.pk)
    return render(request, 'messages_app/new.html')

@login_required
def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.user not in [thread.user1, thread.user2]:
        return redirect('messages_app:inbox')
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Message.objects.create(thread=thread, sender=request.user, text=text)
            return redirect('messages_app:thread_detail', pk=pk)
    msgs = thread.messages.order_by('sent_at')
    return render(request, 'messages_app/thread.html', {'thread': thread, 'messages': msgs})
