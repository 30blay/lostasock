from django.core.management.base import BaseCommand
from matcher.models import Sock, Match
from matcher.feature import extract_features
import json
from time import sleep


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            todo = Sock.objects.filter(features="")
            if not todo:
                print("Nothing to do", flush=True)
                sleep(2)
            else:
                print('Extracting features for ' + str(len(todo)) + ' images', flush=True)

            # extract features for new socks
            for sock in todo:
                y = extract_features(sock.image.url)
                y = y.tolist()  # nested lists with same data, indices
                sock.features = json.dumps(y)
                sock.save()

            # find matches for new socks
            allsocks = Sock.objects.all()
            for sock in todo:
                for othersock in allsocks:
                    if sock == othersock:
                        continue
                    distance = sock.distance(othersock)
                    threshold = 999
                    if distance < threshold:
                        match = Match(sock1=sock, sock2=othersock, distance=distance)
                        match.save()
                        print("Found a match!", flush=True)
