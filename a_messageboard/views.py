from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import MessageBoard, Message
from .forms import MessageCreationForm

# Create your views here.
@login_required
def messageboard_view(request):
    user = request.user
    messageboard = get_object_or_404(MessageBoard, id=1)
    form = MessageCreationForm()

    if request.method == 'POST':
        if user in messageboard.subscribers.all():
            form = MessageCreationForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.author = request.user
                message.messageboard = messageboard
                message.save()
                send_email(message)
        else:
            messages.warning(request, 'You need to be Subscribed to send a message!')
        return redirect('messageboard')
        
    context = {'messageboard': messageboard, 'form': form, 'user': user}
    return render(request, 'a_messageboard/index.html', context)


@login_required
def subscribe_view(request):
    user = request.user
    messageboard = get_object_or_404(MessageBoard, id=1)

    if user not in messageboard.subscribers.all():
        messageboard.subscribers.add(user)
    else:
        messageboard.subscribers.remove(user)
    return redirect('messageboard')



def send_email(message):
    messageboard = message.messageboard
    subscribers = messageboard.subscribers.all()

    for subscriber in subscribers:
        subject = f"New Message from {message.author.profile.name}"
        body = f"{message.author.profile.name}: {message.body}\n\nRegards from\nMy Message Board"
        email = EmailMessage(subject, body, to=[subscriber.email])
        email.send()