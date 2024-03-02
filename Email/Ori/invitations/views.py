# invitations/views.py
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm

def send_invitation(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email_list = form.cleaned_data['email_list'].split('\n')
            subject = 'Invitation to INNOVATION MEET'
            message = ('You are invited to attend the Project orientation session '
                       'at MLA HOUSE which is going to condected by '
                       'yasir to discuss our invonation ideas.'
                       'IT IS AN INSTRUCTION TO YOU THAT YOU NEED TO ATTEND THIS SESSION')
            sender = 'skyasirahmed07@gmail.com'
            for email in email_list:
                send_mail(subject, message, sender, [email.strip()])
            return render(request, 'invitation_sent.html')
    else:
        form = EmailForm()
    return render(request, 'send_invitation.html', {'form': form})
