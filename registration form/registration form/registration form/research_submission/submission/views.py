# submission/views.py
from django.shortcuts import render, redirect
from .form import PaperSubmissionForm
from .models import PaperSubmission
from django.http import HttpResponse
from django.core.mail import send_mail

def submit_paper(request):
    if request.method == 'POST':
        form = PaperSubmissionForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request,'submission/submit_paper.html',{})
    else:
        form = PaperSubmissionForm()
    return render(request, 'submission/submit_paper.html', {'form': form})
def home(request):
    all_members = PaperSubmission.objects.all
    return render(request,'home.html',{'all':all_members})
def send_email(request):
            form = PaperSubmissionForm(request.POST)
            title = form.cleaned_data['title']
            author_names = form.cleaned_data['author_names']
            email = form.cleaned_data['email']
            description = form.cleaned_data['description']
            guide_name = form.cleaned_data['guide_name']
            is_student = form.cleaned_data['is_student']
            college_name = form.cleaned_data['college_name']
            journal_options = form.cleaned_data['journal_options']

            # Construct the email message
            message = f"Title: {title}\nAuthor Names: {author_names}\nEmail: {email}\nDescription: {description}\nGuide Name: {guide_name}\nIs Student: {is_student}\nCollege Name: {college_name}\nJournal Options: {journal_options}"

            # Send the email
            send_mail(
                'Research Paper Submission',
                message,
                'yspednekar_mc22@gmail.com',  # Replace with your email
                [email,'yashpednekar60@gmail.com','yspednekar_mc22@mc.vjti.ac.in'],  # Replace with the recipient's email
                fail_silently=False,
            )