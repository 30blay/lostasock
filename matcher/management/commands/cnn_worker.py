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
                sleep(2)
                continue

            print(str(len(todo)) + ' images are pending extraction', flush=True)

            # extract features for new socks
            sock = todo[0]
            done_socks = Sock.objects.exclude(features="")
            y = extract_features(sock.image.url)
            sock.features = json.dumps(y.tolist())
            sock.save()

            # find matches for new socks
            for other_sock in done_socks:
                distance = sock.distance(other_sock)
                threshold = 999
                if distance < threshold:
                    match = Match(sock1=sock, sock2=other_sock, distance=distance)
                    match.save()
                    print("Found a match!", flush=True)
