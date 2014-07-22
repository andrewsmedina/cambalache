# from: http://stackoverflow.com/questions/1819124/image-comparison-algorithm
import scipy as sp
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d

def get(i):
    # get JPG image as Scipy array, RGB (3 layer)
    data = imread('im%s.jpg' % i)
    # convert to grey-scale using W3C luminance calc
    data = sp.inner(data, [299, 587, 114]) / 1000.0
    # normalize per http://en.wikipedia.org/wiki/Cross-correlation
    return (data - data.mean()) / data.std()

im1 = get(1)
im2 = get(2)
im3 = get(3)
c11 = c2d(im1, im1, mode='same')  # baseline
c12 = c2d(im1, im2, mode='same')
c13 = c2d(im1, im3, mode='same')
c23 = c2d(im2, im3, mode='same')
print c11.max(), c12.max(), c13.max(), c23.max()
