from matcher.models import Sock, Match
from django.core.management.base import BaseCommand
import itertools


class Command(BaseCommand):
    def handle(self, *args, **options):
        # delete all existing matches
        Match.objects.all().delete()

        # try every possible pair
        allsocks = Sock.objects.all()
        allpairs = itertools.combinations(allsocks, 2)
        print('Finding matches in ' + str(len(list(allpairs))) + ' possible pairs')

        for pair in itertools.combinations(allsocks, 2):
            similarity = pair[0].similarity(pair[1])
            threshold = 0.25
            if similarity > threshold:
                match = Match(sock1=pair[0], sock2=pair[1], similarity=similarity)
                match.save()

        print('Found ' + str(Match.objects.count()) + ' matches')
