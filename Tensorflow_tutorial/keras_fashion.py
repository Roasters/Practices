import tensorflow as tf 
from tensorflow import keras
import numpy as np 
import matplotlib.pyplot as plt 

# load data
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# show the image of training set
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.gca().grid(False)

# squashes the values under 1
train_images = train_images / 255.0
test_images = test_images / 255.0

# show sets of images
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid('off')
    plt.imsho(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])

# setup layers
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers,Dense(10, activation=tf.nn.softmax)])

# compile the model
model.compile(optimizer=tf.train.AdamOptimizer(),
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy'])

# train the model
model.fit(train_images, train_labels, epochs=5)

# evaluate accuracy
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Test accuracy:", test_acc)

# make predictions
predictions = model.predict(test_images)

