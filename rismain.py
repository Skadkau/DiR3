import os
from matplotlib import pyplot as plt   
#ploting our canvas   
#plt.plot([-20,-10,0, 10, 20],[20,10,0, -10, -20])
plt.plot([0, 35.2],[28, 0])
plt.plot([19, 19],[0, 20])
plt.plot([0, 25],[17, 17])
plt.plot([0, 21.25],[17, 0])
plt.arrow(0, 0, 7.7, 11)
plt.text(5, 25, 'y <= -0.8x + 28.2')
plt.text(20, 5, 'x <= 19')