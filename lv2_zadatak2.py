import numpy as np
import matplotlib.pyplot as plt    

array = np.loadtxt('data.csv', skiprows=1, delimiter=',', dtype=float)

spol, visina, masa = array.T


print(spol.shape)
plt.scatter(visina, masa)

plt.scatter(visina[0:-1:50], masa[0:-1:50])

plt.xlabel('Visina')
plt.ylabel('Masa')
print("Minimalna visina: ", min(visina))
print("Maximalna visina: ", max(visina))
print("Srednja visina: ", np.average(visina))



muskarci = (array[:,0] == 1)
zene = (array[:,0] == 0)

print(array[muskarci, 1].min())
print(array[muskarci, 1].max())
print(array[muskarci, 1].mean())

print(array[zene, 1].min())
print(array[zene, 1].max())
print(array[zene, 1].mean())


plt.show()
