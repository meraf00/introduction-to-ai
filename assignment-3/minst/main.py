import os
from mnist import MNIST

path = os.path.join(os.path.dirname(__file__), 'dataset')

mndata = MNIST(path)

images, labels = mndata.load_training()

print(type(images), type(labels))