from matcher.models import Sock
from matcher.feature import extract_features
import json

while True:
    todo = Sock.objects.get(features__isnull=True)
    for sock in todo:
        features = extract_features(sock.image.url)
        features = features.tolist()  # nested lists with same data, indices
        sock.features = json.dumps(features)
        sock.save()
