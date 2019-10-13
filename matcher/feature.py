import os
from bipedModel.model import BipedModel

model = BipedModel()


def extract_features(img_path, return_isolated=False):
    APP_ROOT = os.path.dirname(os.path.realpath(__file__))
    return model.extract_features(APP_ROOT + '/..' + img_path, return_isolated)


def get_similarity(feature1, feature2):
    similarity = model.get_similarity(feature1, feature2)
    return similarity
