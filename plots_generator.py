import matplotlib.pyplot as plt
from main import weather_val, quality_val, traffic_val, results

X = [i+1 for i in range(10)]

plt.clf()
y1 = plt.scatter(X, weather_val, label='weather')
y2 = plt.scatter(X, quality_val, label='quality')
y3 = plt.scatter(X, traffic_val, label='traffic')
y4 = plt.scatter(X, results, label='time-result')
plt.legend(handles = [y1, y2, y3, y4])
plt.title('Driver')
plt.xlabel("number of test")
plt.ylabel("logic value")
plt.savefig("driver.png")


