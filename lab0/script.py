import numpy as np
import matplotlib.pyplot as plt

res = [4, 8, 16, 32, 128]
pi_num = 8
fig, ax = plt.subplots(len(res), 5, figsize=(20,15))


mu, sigma = 0, 0.1 # mean and standard deviation


for y_index, i in enumerate(res):    
    samp = np.linspace(0, pi_num*np.pi, i)
    signal = np.sin(samp) #spróbkowany sygnał sinusa linspacem-samp    

    s = np.random.normal(mu, sigma, i)
    signal = signal + s

    ax[y_index, 0].plot(samp, signal)
    ax[y_index, 0].set_title(i)
    
    img = signal[:,np.newaxis] * signal[np.newaxis,:]
    ax[y_index, 1].imshow(img, cmap='binary')

    #c1 = np.round(np.amin(signal), 3)  #normalizacja sposób 1 
    #c2 = np.round(np.amax(signal), 3)
    #img_norm = (img + c2) / (c2 - c1)
    img_norm = img                      #normalizacja sposób 2
    img_norm -= np.min(img_norm)
    img_norm /= np.max(img_norm)
    
    #obcięcie tego co wyżej niż 1 i niżej niż 0 - upewnienie się, że napewno wartości są znormalizowane
    img_norm = np.clip(img_norm, 0 , 1) 
    
    depth = [2, 4, 8]
    for x_index, i in enumerate(depth):
        dmin, dmax = (0, np.power(2,i)-1)
        digital_image = np.rint(img_norm * dmax)
        ax[y_index, x_index + 2].imshow(digital_image, cmap='binary')
        ax[y_index, x_index + 2].set_title(
                '{mini} - {maxi}'.format(
                    mini=np.round(np.min(digital_image), 3), 
                    maxi=np.round(np.max(digital_image), 3)
                    )
                )

plt.tight_layout()
plt.savefig('lab0.png')