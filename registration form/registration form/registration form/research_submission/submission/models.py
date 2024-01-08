# submission/models.py
from django.db import models

class PaperSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=255)
    author_names = models.CharField(max_length=255)
    description = models.TextField()
    guide_name = models.CharField(max_length=255, blank=True, null=True)
    # Add new fields
    is_student = models.BooleanField(default=True)
    
    college_name = models.CharField(max_length=255, blank=True, null=True)
    journal_options = models.CharField(max_length=255, blank=True, null=True)
    payment_receipt = models.FileField(upload_to='payment_receipts/', blank=True, null=True)
    document = models.FileField(upload_to='research_documents/')

    def __str__(self):
        return self.title
    

