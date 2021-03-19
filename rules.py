import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# ANTECEDENTS

weather = ctrl.Antecedent(np.arange(0, 50, 1), 'weather') 
traffic = ctrl.Antecedent(np.arange(0, 50, 1), 'traffic')
quality = ctrl.Antecedent(np.arange(0, 50, 1), 'quality')

weather_names = ['rain', 'small rain', 'sun']
traffic_names = ['high', 'medium', 'small']
quality_names = ['bad', 'normal', 'high']

weather.automf(names=weather_names)
quality.automf(names=quality_names)
traffic.automf(names=traffic_names)

params = {
    'weather' : weather,
    'traffic' : traffic,
    'quality' : quality
}   

# CONSEQUENTS
time = ctrl.Consequent(np.arange(0, 50, 1), 'time')   
time_names = ['long', 'medium', 'short', 'very short']
time.automf(names=time_names)

results = {
    'time' : time
}

# RULES

rules = []

rules.append(ctrl.Rule(weather['rain'] & quality['bad'], time['long']))
rules.append(ctrl.Rule(weather['rain'] & quality['normal'], time['medium']))
rules.append(ctrl.Rule(weather['rain'] & quality['high'], time['short']))
rules.append(ctrl.Rule(weather['rain'] & quality['bad'], time['long']))
rules.append(ctrl.Rule(weather['rain'] & quality['high'] & traffic['medium'], time['medium']))
rules.append(ctrl.Rule(weather['rain'] & traffic['high'], time['long']))
rules.append(ctrl.Rule(weather['rain'] & traffic['medium'], time['long']))
rules.append(ctrl.Rule(weather['rain'] & traffic['small'], time['short']))
rules.append(ctrl.Rule(weather['rain'] & traffic['small'], time['short']))
rules.append(ctrl.Rule(weather['small rain'] & traffic['high'], time['long']))
rules.append(ctrl.Rule(weather['small rain'] & quality['bad'] & traffic['small'], time['short']))
rules.append(ctrl.Rule(weather['small rain'] & quality['high'] & traffic['small'], time['short']))
rules.append(ctrl.Rule(weather['small rain'] & quality['high'] & traffic['medium'], time['medium']))
rules.append(ctrl.Rule(weather['small rain'] & quality['high'] & traffic['medium'], time['medium']))
rules.append(ctrl.Rule(weather['small rain'] & quality['normal'] & traffic['high'], time['medium']))
rules.append(ctrl.Rule(weather['small rain'] & quality['high'] & traffic['medium'], time['medium']))
rules.append(ctrl.Rule(weather['sun'] & quality['bad'] & traffic['small'], time['short']))
rules.append(ctrl.Rule(weather['sun'] & quality['high'] & traffic['small'], time['very short']))
rules.append(ctrl.Rule(weather['sun'] & quality['normal'] & traffic['small'], time['short']))
rules.append(ctrl.Rule(weather['sun'] & quality['high'] & traffic['medium'], time['medium']))
rules.append(ctrl.Rule(weather['sun'] & quality['high'] & traffic['high'], time['long']))
rules.append(ctrl.Rule(weather['sun'] & quality['bad'] & traffic['small'], time['short']))
rules.append(ctrl.Rule(weather['sun'] & quality['high'] & traffic['high'], time['long']))
rules.append(ctrl.Rule(weather['sun'] & quality['normal'] & traffic['high'], time['long']))
rules.append(ctrl.Rule(weather['sun'] & quality['high'] & traffic['small'], time['very short']))
rules.append(ctrl.Rule(weather['sun'] & quality['high'] & traffic['small'], time['very short']))
