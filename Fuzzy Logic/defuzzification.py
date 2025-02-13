import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

sicaklik = ctrl.Antecedent(np.arange(20, 81, 1), 'sicaklik')
sicaklikDegisimi = ctrl.Antecedent(np.arange(0, 6, 0.1), 'sicaklikDegisimi')
motorHizi = ctrl.Consequent(np.arange(100, 1001, 1), 'motorHizi')

sicaklik['low'] = fuzz.trapmf(sicaklik.universe, [20, 25, 35, 40])
sicaklik['medium'] = fuzz.trapmf(sicaklik.universe, [30, 42, 55, 80])

sicaklikDegisimi['low'] = fuzz.trapmf(sicaklikDegisimi.universe, [0, 0.3, 1, 2])
sicaklikDegisimi['medium'] = fuzz.trapmf(sicaklikDegisimi.universe, [0.5, 1.3, 2, 3])
sicaklikDegisimi['high'] = fuzz.trapmf(sicaklikDegisimi.universe, [1, 3, 4, 5])

motorHizi['slow'] = fuzz.trapmf(motorHizi.universe, [100, 250, 350, 500])
motorHizi['medium'] = fuzz.trapmf(motorHizi.universe, [300, 400, 500, 700])
motorHizi['fast'] = fuzz.trapmf(motorHizi.universe, [500, 650, 750, 1000])

sicaklik.view()
sicaklikDegisimi.view()
motorHizi.view()

rule1 = ctrl.Rule(sicaklik['low'] & sicaklikDegisimi['low'], motorHizi['fast'])
rule2 = ctrl.Rule(sicaklik['medium'] & sicaklikDegisimi['medium'], motorHizi['slow'])
rule3 = ctrl.Rule(sicaklik['low'] & sicaklikDegisimi['medium'], motorHizi['fast'])
rule4 = ctrl.Rule(sicaklik['medium'] & sicaklikDegisimi['low'], motorHizi['medium'])

motorCalisma_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
#motorCalisma = ctrl.ControlSystemSimulation(motorCalisma_ctrl)

#motorCalisma.input['sicaklik'] = 35
#motorCalisma.input['sicaklikDegisimi'] = 1

#motorCalisma.compute()
#print("", motorCalisma.output['motorHizi'])
#motorHizi.view(sim = motorCalisma)

defuzzMethods = ['centroid', 'bisector', 'mom', 'som', 'lom']

for method in defuzzMethods:
    motorHizi.defuzzify_method = method

    motorCalisma = ctrl.ControlSystemSimulation(motorCalisma_ctrl)
    
    motorCalisma.input['sicaklik'] = 35
    motorCalisma.input['sicaklikDegisimi'] = 1
    
    motorCalisma.compute()
    
    print(f"Durulastirma yontemi: {method}")
    print(f"Motor hizi: {motorCalisma.output['motorHizi']}\n")
    
    motorHizi.view(sim = motorCalisma)

input("aa")