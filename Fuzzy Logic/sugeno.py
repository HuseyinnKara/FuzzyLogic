import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

oxi = ctrl.Antecedent(np.arange(0, 3.1, 0.1), 'OXI')

power = ctrl.Consequent(np.arange(0, 26, 0.1), 'POWER')

oxi['low_flow'] = fuzz.trapmf(oxi.universe, [0, 0, 1, 1.5])
oxi['medium_flow'] = fuzz.trapmf(oxi.universe, [0.5, 1.5, 2.5, 3])
oxi['high_flow'] = fuzz.trapmf(oxi.universe, [2, 2.5, 3, 3])

power['low_power'] = fuzz.trimf(power.universe, [0, 0, 0])
power['medium_power'] = fuzz.trimf(power.universe, [12.5, 12.5, 12.5])
power['high_power'] = fuzz.trimf(power.universe, [25, 25, 25])

rule1 = ctrl.Rule(oxi['low_flow'], power['low_power'])
rule2 = ctrl.Rule(oxi['medium_flow'], power['medium_power'])
rule3 = ctrl.Rule(oxi['high_flow'], power['high_power'])

system = ctrl.ControlSystem([rule1, rule2, rule3])
sim = ctrl.ControlSystemSimulation(system)

oxi_input = 0.51
sim.input['OXI'] = oxi_input
sim.compute()

print("OXI Girişi:", oxi_input)
print("Sugeno Çıkışı (POWER):", sim.output['POWER'])
