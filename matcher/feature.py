
def extract_features(img_path):
    from keras.applications.vgg16 import VGG16
    from keras.preprocessing import image
    from keras.preprocessing.image import ImageDataGenerator
    import numpy as np
    from keras import models
    import os.path

    APP_ROOT = os.path.dirname(os.path.realpath(__file__))

    vgg16_model = VGG16(weights='imagenet', include_top=True, input_shape=(224, 224, 3))
    model = models.Sequential()
    for layer in vgg16_model.layers[:-1]:  # just exclude last layer from copying
        model.add(layer)

    val_datagen = ImageDataGenerator(rescale=1. / 255)

    img = image.load_img(APP_ROOT + '/..' + img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    generator = val_datagen.flow(x)

    for inputs_batch in generator:
        features_batch = model.predict(inputs_batch)
        return features_batch
