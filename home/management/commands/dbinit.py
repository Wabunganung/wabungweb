from django.core.management.base import BaseCommand
from home.models import Init

class Command(BaseCommand):
    def handle(self, **options):
        a = Init(project_author="Tyson Lupul", project_year="2020")
        a.save()

