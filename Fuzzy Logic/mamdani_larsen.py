import numpy as np  
import matplotlib.pyplot as plt  

def trapezoidal_membership(x, a, b, c, d):
    return np.maximum(0, np.minimum((x - a) / (b - a), np.minimum(1, (d - x) / (d - c))))

def mamdani_inference(membership, alpha):
    return np.minimum(membership, alpha)

def larsen_inference(membership, alpha):
    return membership * alpha

a_low, b_low, c_low, d_low = 20, 25, 35, 40  

a_medium, b_medium, c_medium, d_medium = 30, 42, 55, 80

x = np.linspace(20, 80, 500)

low_membership = trapezoidal_membership(x, a_low, b_low, c_low, d_low)

medium_membership = trapezoidal_membership(x, a_medium, b_medium, c_medium, d_medium)

alpha_low = 0.4  
alpha_medium = 0.75  

mamdani_low = mamdani_inference(low_membership, alpha_low)  
mamdani_medium = mamdani_inference(medium_membership, alpha_medium)  

mamdani_max = np.maximum(mamdani_low,mamdani_medium)

larsen_low = larsen_inference(low_membership, alpha_low)  
larsen_medium = larsen_inference(medium_membership, alpha_medium)

larsen_max = np.maximum(larsen_low, larsen_medium)

plt.figure(figsize=(12, 10))  

plt.subplot(2, 1, 1)
plt.fill_between(x, mamdani_max, color="red", alpha=0.3, label="Mamdani")
plt.plot(x, low_membership, "--", color="blue", label="Low")
plt.plot(x, medium_membership, "--", color="green", label="Medium")
plt.title("Mamdani Yöntemi")
plt.xlabel("Sıcaklık")  
plt.ylabel("Üyelik Derecesi")  
plt.legend()  
plt.grid(True)  

plt.subplot(2, 1, 2)
plt.fill_between(x, larsen_max, color="purple", alpha=0.3, label="Larsen")
plt.plot(x, low_membership, "--", color="blue", label="Low")
plt.plot(x, medium_membership, "--", color="green", label="Medium")
plt.title("Larsen Yöntemi")
plt.xlabel("Sıcaklık")  
plt.ylabel("Üyelik Derecesi")  
plt.legend()  
plt.grid(True)  
plt.tight_layout()
plt.show()
