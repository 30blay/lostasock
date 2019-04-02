import numpy as np
import os
from keras.layers import Input, Conv2D, Lambda, Dense, Flatten,MaxPooling2D
from keras.models import Model
from keras import backend as K
from keras.optimizers import Adam


def get_siamese():
    input_shape = (4096,)
    left_input = Input(input_shape)
    right_input = Input(input_shape)

    # merge two encoded inputs with the l1 distance between them
    L1_layer = Lambda(lambda tensors: K.abs(tensors[0] - tensors[1]), output_shape=(4096,))
    L1_distance = L1_layer([left_input, right_input])
    prediction = Dense(1, activation='sigmoid')(L1_distance)

    siamese_net = Model(inputs=[left_input, right_input], output=prediction)

    optimizer = Adam(lr=0.0001)
    siamese_net.compile(loss="binary_crossentropy", optimizer=optimizer)

    return siamese_net

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


def get_similarity(feature1, feature2):
    input_tensor = np.vstack((feature1, feature2))

    siamese = get_siamese()
    APP_ROOT = os.path.dirname(os.path.realpath(__file__))
    weights_path = os.path.join(APP_ROOT, "model_weights.h5")
    siamese.load_weights(weights_path)
    similarity = siamese.predict([feature1, feature2])
    return similarity[0][0]
