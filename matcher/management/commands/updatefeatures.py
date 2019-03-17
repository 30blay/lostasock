from matcher.models import Sock
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        allsocks = Sock.objects.all()
        print('Extracting features for ' + str(len(allsocks)) + ' images')
        for sock in allsocks:
            sock.save()