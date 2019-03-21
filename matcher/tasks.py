from mysite.celery import celery
from matcher.feature import extract_features as run_cnn
import json


@celery.task
def extact_features(sock_id):
    from matcher.models import Sock
    sock = Sock.objects.get(pk=sock_id)
    features = run_cnn(sock.image.url)
    features = features.tolist()
    sock.features = json.dumps(features)

    sock.save()
