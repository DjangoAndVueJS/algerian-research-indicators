import email
from django.test import TestCase
from .models import Researcher


class CreateResearcherTests(TestCase):

    def setUpTestData():
        # create a user
        user1 = Researcher.objects.create_user(
            first_name="Benmeddour", last_name="yahia",
            google_scholar_account="https://scholar.google.com/citations?hl=en&user=TnIU-bAAAAAJ", 
            email="ben@ilyes.com", password="abc123")
        user1.save()
# Create your tests here.
