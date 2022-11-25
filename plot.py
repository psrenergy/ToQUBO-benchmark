import matplotlib.pyplot as plt
from pandas import read_csv

toqubo_data = read_csv("ToQUBO/tsp_ToQUBO.csv")
pyqubo_current_data = read_csv("pyqubo/tsp_pyqubo.csv")
pyqubo_040_data = read_csv("pyqubo/tsp_pyqubo_0_4_0.csv")


plt.plot(toqubo_data["n_var"], toqubo_data["time"], label = "ToQUBO 0.1.3", marker='o')
plt.plot(pyqubo_current_data["n_var"], pyqubo_current_data["time"], label = "PyQUBO 1.3.1", marker='o')
plt.plot(pyqubo_040_data["n_var"], pyqubo_040_data["time"], label = "PyQUBO 0.4.0", marker='o')



plt.xscale('symlog')
plt.yscale('symlog')
plt.xlabel("#variables")
plt.ylabel("Execution Time(sec)")
plt.grid(True)

plt.legend()

plt.savefig('benchmark.png')

plt.show()