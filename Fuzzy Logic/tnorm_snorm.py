import numpy as np  
import matplotlib.pyplot as plt 

def trapezoidal_membership(x, a, b, c, d):
    return np.maximum(0, np.minimum((x - a) / (b - a), np.minimum(1, (d - x) / (d - c))))

def t_norm_min(a, b):
    return np.minimum(a, b)

def t_norm_algebraic_product(a, b):
    return a * b  

def t_norm_bounded_product(a, b):
    return np.maximum(0, a + b - 1)

def t_norm_drastic_product(a, b):
    return np.where((a == 1) | (b == 1), np.minimum(a, b), 0)

def s_norm_max(a, b):
    return np.maximum(a, b)

def s_norm_algebraic_sum(a, b):
    return a + b - a * b 

def s_norm_bounded_sum(a, b):
    return np.minimum(1, a + b)  

def s_norm_drastic_sum(a, b):
    return np.where((a == 0), b, np.where(b == 0, a, 1))

a_low, b_low, c_low, d_low = 20, 25, 35, 40  

a_medium, b_medium, c_medium, d_medium = 30, 42, 55, 80  

x = np.linspace(20, 80, 500)

low_membership = trapezoidal_membership(x, a_low, b_low, c_low, d_low)

medium_membership = trapezoidal_membership(x, a_medium, b_medium, c_medium, d_medium)

def plot_membership_operation(operation_name, operation_function):
    result = operation_function(low_membership, medium_membership)
    plt.figure(figsize=(10, 6))
    plt.plot(x, low_membership, "--", color="blue", label="Low")
    plt.plot(x, medium_membership, "--", color="orange", label="Medium")
    plt.fill_between(x, result, color="green", alpha=0.5, label=operation_name)
    plt.title(f"{operation_name}")
    plt.xlabel("Sıcaklık")
    plt.ylabel("Üyelik Derecesi")
    plt.legend()  
    plt.grid(True)  
    plt.show()  

plot_membership_operation("(Min)", t_norm_min)