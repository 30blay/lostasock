import os
from bipedModel.model import get_encoder, get_siamese


def extract_features(img_path):
    from keras.preprocessing import image
    from keras.preprocessing.image import ImageDataGenerator
    import numpy as np
    import os.path

    APP_ROOT = os.path.dirname(os.path.realpath(__file__))

    encoder = get_encoder()

    val_datagen = ImageDataGenerator(rescale=1. / 255)

    img = image.load_img(APP_ROOT + '/..' + img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    generator = val_datagen.flow(x)

    for inputs_batch in generator:
        features_batch = encoder.predict(inputs_batch)
        return features_batch


def get_similarity(feature1, feature2):
    siamese = get_siamese()
    similarity = siamese.predict([feature1, feature2])
    return similarity[0][0]
