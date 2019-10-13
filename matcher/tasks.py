from background_task import background
from .models import Sock, Match
from .feature import extract_features
import json


@background(schedule=0)
def find_matches(sock_id):
    sock = Sock.objects.get(pk=sock_id)
    sock.update_features()

    done_socks = Sock.objects.exclude(features="")
    # find matches for new socks
    for other_sock in done_socks:
        if other_sock == sock:  # never match a sock to itself
            continue
        similarity = sock.similarity(other_sock)
        threshold = 0.25
        if similarity > threshold:
            match = Match(sock1=sock, sock2=other_sock, similarity=similarity)
            match.save()
            print("Found a match!", flush=True)
