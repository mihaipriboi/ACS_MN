# Nume student:
####################################
# DVS: Compresia de imagini alb negru
####################################
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Functie de conversie din RGB in GRAY
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

        
#Cititi o imagine rgb la alagere
Img =  mpimg.imread('nume_imagine.png') # remarca: matplotlib accepta doar imagini .png
fig1 =plt.figure(1)
plt.imshow(Img)

fig2 =plt.figure(2)
grayImg = rgb2gray(Img)
plt.imshow(grayImg, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)

plt.show()
#1. Aplicati svd pe imaginea gray 
#2. Plotati valorile singulare pe scala logaritmica utilizand plt.semilogy
#    Adaugati comentariu cu ce observati

#3. Plotati graficul procent informatie vs valori singulare
#Hint: utilizati functia np.cumsum.
#Adaugati comentariu cu ce observati

#4. In urma analizei graficului procent informatie vs valori singulare generati
#un vector de dimensiune minim 

#5. Utilizati elementele vectorului pentru a reconstrui imaginile

