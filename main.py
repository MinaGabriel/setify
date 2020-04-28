import matplotlib.pyplot as plt
from setify import Setify

x = Setify.country_death_rate('JPN')
y = Setify.country_birth_rate('JPN')
print(x.dtypes)
ax = plt.subplot()

ax.plot(y['year'], y['birth'], '*-')
ax.plot(x['year'], x['death'])
plt.show()

s = Setify.occupancy_data()
print(s.dtypes)