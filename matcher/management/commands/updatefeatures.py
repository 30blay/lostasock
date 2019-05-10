from matcher.models import Sock
from django.core.management.base import BaseCommand
from matcher.feature import extract_features
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        allsocks = Sock.objects.all()
        print('Extracting features for ' + str(len(allsocks)) + ' images')
        for sock in allsocks:
            y = extract_features(sock.image.url)
            sock.features = json.dumps(y.tolist())
            sock.save()
