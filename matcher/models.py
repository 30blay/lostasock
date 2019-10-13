from django.db import models
from .feature import get_similarity, extract_features
import json
import numpy as np
from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import StringIO, BytesIO
from django.core.files.base import ContentFile
from PIL import Image


class Sock(models.Model):
    features = models.TextField()
    image = models.ImageField(null=True, upload_to="static/gallery/")
    isolated_image = models.ImageField(null=True, upload_to="static/gallery/")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def update_features(self):
        features, isolated = extract_features(self.image.url, return_isolated=True)
        self.features = json.dumps(features.tolist())

        isolated = np.uint8(isolated)
        pil_image = Image.fromarray(isolated)
        f = BytesIO()
        try:
            pil_image.save(f, format='png')
            self.isolated_image.save(f'{self.id}.png', ContentFile(f.getvalue()))
        finally:
            f.close()
        self.save()

    def similarity(self, other_sock):
        if not self.features or not other_sock.features:
            raise Exception("Features were not calculated yet for this sock")
        this_feature = np.array(json.loads(self.features))
        other_feature = np.array(json.loads(other_sock.features))
        distance = get_similarity(this_feature, other_feature)
        return distance

    # save with compression
    def save(self, *args, **kwargs):
        if not self.pk:
            # the sock is new -> Compress it's image
            # first save the sock with original image so that we have it on file
            super(Sock, self).save(*args, **kwargs)
            if self.image:
                image_file = Image.open(self.image.path)
                image_file.save(self.image.path, quality=20, optimize=True)
        else:
            super(Sock, self).save(*args, **kwargs)

    def __str__(self):
        return self.image.url


class Match(models.Model):
    sock1 = models.ForeignKey(Sock, related_name="sock1", on_delete=models.CASCADE)
    sock2 = models.ForeignKey(Sock, related_name="sock2", on_delete=models.CASCADE)
    similarity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
