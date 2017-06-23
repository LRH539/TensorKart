from utils import resize_image, prepare_image
import model
import tensorflow as tf
import matplotlib as mp
import matplotlib.pyplot as plt
import sys
import math
from skimage.color import rgb2gray
from skimage.transform import resize
from skimage.io import imread
from skimage.util import img_as_float


sess = None

class Visualizer:

    def __init__(self):
        # Start session
        self.sess = tf.InteractiveSession()
        self.sess.run(tf.global_variables_initializer())

        # Load Model
        saver = tf.train.Saver()
        saver.restore(self.sess, "./model.ckpt")

    def getActivations(self, layer, stimuli):
        units = self.sess.run(layer,feed_dict={model.x: stimuli, model.keep_prob:1.0})
        self.plotNNFilter(units)
    

    def plotNNFilter(self, units):
        filters = units.shape[3]
        plt.figure(1, figsize=(20,20))
        n_columns = 6
        n_rows = math.ceil(filters / n_columns) + 1
        for i in range(filters):
            plt.subplot(n_rows, n_columns, i+1)
            plt.title('Filter ' + str(i))
            plt.imshow(units[0,:,:,i], interpolation="nearest", cmap="gray")

    def visualizeImage(self, layer, image_file):
        image = imread(image_file)
        vec = resize_image(image)
        self.getActivations(layer, [vec])

        

visualizer = Visualizer()
visualizer.visualizeImage(model.h_conv4, sys.argv[1])
plt.show()
