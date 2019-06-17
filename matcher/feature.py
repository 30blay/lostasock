import os
from bipedModel.model import BipedModel

model = BipedModel()


def extract_features(img_path):
    APP_ROOT = os.path.dirname(os.path.realpath(__file__))
    features = model.extract_features(APP_ROOT + '/..' + img_path)
    return features


def get_similarity(feature1, feature2):
    similarity = model.get_similarity(feature1, feature2)
    return similarity
