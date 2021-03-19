from driver import Driver
import numpy as np
import random
from rules import *

tests_number = 10

weather_val = []
quality_val = []
traffic_val = []
results = []

driver = Driver(params, results, rules)  

for i in range(tests_number):
    weather = random.randint(1, 50)
    quality = random.randint(1, 50)
    traffic = random.randint(1, 50)
    driver.add_input('weather', weather)
    driver.add_input('quality',quality)
    driver.add_input('traffic', traffic)
    result = driver.get_output('time')

    weather_val.append(weather)
    quality_val.append(quality)
    traffic_val.append(traffic)
    results.append(result)



