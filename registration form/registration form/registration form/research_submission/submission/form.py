# submission/forms.py
from django import forms
from .models import PaperSubmission

class PaperSubmissionForm(forms.ModelForm):
    JOURNAL_CHOICES = [
        ('Nature', 'Nature'),
        ('IEEE_CVF', 'IEEE/CVF Conference on Computer Vision and Pattern Recognition'),
        ('IJAIR', 'IJAIR')
    ]
    email = forms.EmailField(required=True)
    class Meta:
        model = PaperSubmission
        fields = ['name','title', 'author_names', 'email','description', 'guide_name', 'is_student', 'college_name', 'journal_options', 'payment_receipt', 'document']  # Add more fields based on your requirements
    journal_options = forms.ChoiceField(choices=JOURNAL_CHOICES)