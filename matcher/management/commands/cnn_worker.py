from django.core.management.base import BaseCommand
from matcher.models import Sock
from matcher.feature import extract_features
import json
from time import sleep


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            todo = Sock.objects.filter(features="")
            if not todo:
                print("Nothing to do")
                sleep(2)
            else:
                print('Extracting features for ' + str(len(todo)) + ' images')

            for sock in todo:
                y = extract_features(sock.image.url)
                y = y.tolist()  # nested lists with same data, indices
                sock.features = json.dumps(y)
                sock.save()
