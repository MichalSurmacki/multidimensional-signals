import numpy as np
import matplotlib.pyplot as plt

depth = 2

drangeMin = -1
drangeMax = 1

resolution = 256

n_iter = 256

N = np.power(2, depth) - 1

prober = np.linspace(0, 8*np.pi, resolution)
prober = np.sin(prober)

perfect_image = prober[:,np.newaxis] * prober[np.newaxis,:]

n_matrix = np.zeros(perfect_image.shape)
o_matrix = np.zeros(perfect_image.shape)

for i in range(n_iter):
    noise = np.random.normal(0, 1, perfect_image.shape)
    n_image = perfect_image + noise
    o_image = np.copy(perfect_image)

    n_image -= np.min(n_image)
    n_image /= np.max(n_image)
    n_digm = np.rint(n_image * N)

    o_image -= np.min(o_image)
    o_image /= np.max(o_image)
    o_digm = np.rint(o_image * N)

    n_matrix += n_digm
    o_matrix += o_digm

    fig, ax = plt.subplots(2, 3, figsize=(12,8))
    
    ax[0,0].imshow(perfect_image, cmap='binary')
    ax[1,0].imshow(noise, cmap='binary')

    ax[0,1].imshow(o_digm, cmap='binary')
    ax[1,1].imshow(n_digm, cmap='binary')

    ax[0,2].imshow(o_matrix, cmap='binary')
    ax[1,2].imshow(n_matrix, cmap='binary')

    plt.savefig('lab1.png')
