from django.db import models
from numpy.linalg import norm
import json
import numpy as np
from django.contrib.auth.models import User
from matcher.tasks import extact_features


class Sock(models.Model):
    features = models.TextField()
    image = models.ImageField(null=True, upload_to="static/gallery/")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def distance(self, otherSock):
        thisFeatures = np.array(json.loads(self.features))
        otherFeatures = np.array(json.loads(otherSock.features))
        distance = norm(thisFeatures - otherFeatures)
        return distance

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        #save the image first
        super(Sock, self).save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

        features = extact_features.delay(self.pk)

        super(Sock, self).save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self):
        return self.image.url
