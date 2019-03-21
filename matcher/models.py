from django.db import models
from .feature import extract_features
from numpy.linalg import norm
import json
import numpy as np
from django.contrib.auth.models import User

class Sock(models.Model):
    features = models.TextField()
    image = models.ImageField(null=True, upload_to="static/gallery/")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def distance(self, otherSock):
        thisFeatures = np.array(json.loads(self.features))
        otherFeatures = np.array(json.loads(otherSock.features))
        distance = norm(thisFeatures - otherFeatures)
        return distance

    def __str__(self):
        return self.image.url
