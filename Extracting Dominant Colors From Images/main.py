
#import paskage
from colorthief import ColorThief
import matplotlib.pyplot as plt

ct = ColorThief('Extracting Dominant Colors From Images\img1.png')


#The most common color in the image
print(ct.get_color(quality=1))
domainant_color = ct.get_color(quality=1)

plt.imshow([[domainant_color]])
plt.show()