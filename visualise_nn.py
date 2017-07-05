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
import numpy as np

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
        return units

    def plotNNFilter(self, units, filters):
        plt.figure(1, figsize=(20,20))
        
        # count filters with activations, and add their indeces
        activation_index = []
        
        for i in range(filters):
            if(np.count_nonzero(units[0,:,:,i]) > 0):
                activation_index.append(i)

        print(filters)
        
        n_columns = 3
        n_rows = math.ceil(len(activation_index) / n_columns) + 1

        for i in range(len(activation_index)):
            p = activation_index[i]            

            plt.subplot(n_rows, n_columns, i+1)
            plt.title('Filter ' + str(i))
            plt.imshow(units[0,:,:,p], interpolation="nearest", cmap="gray")

    def visualizeImage(self, layer, image_file):
        image = imread(image_file)
        vec = resize_image(image)
        units = self.getActivations(layer, [vec])
        self.plotNNFilter(units, units.shape[3])

    def saveActivations(self, layer, image_file):
        image = imread(image_file)
        vec = resize_image(image)
        units = self.getActivations(layer, [vec])
        self.plotNNFilter(units, min(units.shape[3], 20))

visualizer = Visualizer()
visualizer.visualizeImage(model.h_conv3, sys.argv[1])
#visualizer.saveActivations(model.h_conv3, sys.argv[1])

plt.show()
