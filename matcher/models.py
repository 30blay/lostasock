from django.db import models
from .feature import extract_features, get_similarity
from numpy.linalg import norm
import json
import numpy as np
from django.contrib.auth.models import User


class Sock(models.Model):
    features = models.TextField()
    image = models.ImageField(null=True, upload_to="static/gallery/")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def similarity(self, other_sock):
        if not self.features or not other_sock.features:
            raise Exception("Features were not calculated yet for this sock")
        this_feature = np.array(json.loads(self.features))
        other_feature = np.array(json.loads(other_sock.features))
        distance = get_similarity(this_feature, other_feature)
        return distance

    def __str__(self):
        return self.image.url


class Match(models.Model):
    sock1 = models.ForeignKey(Sock, related_name="sock1", on_delete=models.CASCADE)
    sock2 = models.ForeignKey(Sock, related_name="sock2", on_delete=models.CASCADE)
    similarity = models.FloatField()

    def __str__(self):
        return str(self.pk)
