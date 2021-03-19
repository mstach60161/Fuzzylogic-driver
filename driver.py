import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from rules import *

class Driver:
    def __init__(self, params, results, rules):
        self.params = params
        self.results = results
        self.rules = rules
        self.driver = None
        self.update()
        
    def update(self):
        system_ctrl = ctrl.ControlSystem(rules=self.rules)
        self.driver = ctrl.ControlSystemSimulation(system_ctrl)

    def add_rule(self, rule):
        rules.append(rule)
        self.update()
    
    def add_parameter(self, name, antecedent):
        self.params[name] = antecedent
        self.update()

    def add_input(self, parameter, value):
        self.driver.input[parameter] = value

    def get_output(self, consequent):
        self.driver.compute()
        return self.driver.output[consequent]
    
# quick test    
# dr = Driver(params, results, rules)        
# dr.add_input('weather', 40)
# dr.add_input('quality', 20)
# dr.add_input('traffic', 0)
# print(dr.get_output('time'))
