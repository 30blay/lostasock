from matcher.models import Sock
from django.core.management.base import BaseCommand
from matcher.feature import extract_features
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        allsocks = Sock.objects.all()
        print('Extracting features for ' + str(len(allsocks)) + ' images')
        for sock in allsocks:
            sock.update_features()
