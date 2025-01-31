import skfuzzy as fuzz
import skfuzzy.membership as mf
import numpy as np
import matplotlib.pyplot as plt

def create_membership_functions(variable_range, low_points, medium_points, high_points):
    low = mf.trimf(variable_range, low_points)
    medium = mf.trimf(variable_range, medium_points)
    high = mf.trimf(variable_range, high_points)
    return low, medium, high

def plot_membership_functions(ax, variable_range, memberships, title, labels):
    colors = ['r', 'g', 'b']
    for membership, label, color in zip(memberships, labels, colors):
        ax.plot(variable_range, membership, color, linewidth=2, label=label)  
    ax.set_title(title)  
    ax.legend()  

def calculate_memberships(variable_range, memberships, input_value):
    return [fuzz.interp_membership(variable_range, membership, input_value) for membership in memberships]

def plot_membership_lines(ax, input_value, memberships, variable_range):
    for membership in memberships:
        membership_value = fuzz.interp_membership(variable_range, membership, input_value)
        ax.plot([input_value, input_value], [0, membership_value], 'r', linewidth=1, linestyle='--')
        ax.plot([variable_range[0], input_value], [membership_value, membership_value], 'r', linewidth=1, linestyle='--')

def main():
    var_year = np.arange(2002, 2013, 1)  
    var_km = np.arange(0, 100001, 1)  
    var_price = np.arange(0, 40001, 1)  

    year_memberships = create_membership_functions(var_year, [2002, 2002, 2007], [2002, 2007, 2012], [2007, 2012, 2012])
    km_memberships = create_membership_functions(var_km, [0, 0, 50000], [0, 50000, 100000], [50000, 100000, 100000])
    price_memberships = create_membership_functions(var_price, [0, 0, 20000], [0, 20000, 40000], [20000, 40000, 40000])

    fig, axes = plt.subplots(nrows=5, figsize=(15, 20))
    plot_membership_functions(axes[0], var_year, year_memberships, "Model", ["Düşük", "Orta", "Yüksek"])
    plot_membership_functions(axes[1], var_km, km_memberships, "Kilometre", ["Düşük", "Orta", "Yüksek"])
    plot_membership_functions(axes[2], var_price, price_memberships, "Fiyat", ["Düşük", "Orta", "Yüksek"])

    input_year = 2011  
    input_km = 25000  

    year_fits = calculate_memberships(var_year, year_memberships, input_year)
    km_fits = calculate_memberships(var_km, km_memberships, input_km)

    plot_membership_lines(axes[0], input_year, year_memberships, var_year)
    plot_membership_lines(axes[1], input_km, km_memberships, var_km)

    rule1 = np.fmin(np.fmin(year_fits[0], km_fits[2]), price_memberships[0])  
    rule2 = np.fmin(np.fmin(year_fits[1], km_fits[1]), price_memberships[1])  
    rule3 = np.fmin(np.fmin(year_fits[2], km_fits[0]), price_memberships[2])  

    axes[3].plot(var_price, rule1, 'r', linestyle='--', linewidth=1, label='Rule-1')
    axes[3].plot(var_price, rule2, 'b', linestyle='-.', linewidth=2, label='Rule-2')
    axes[3].plot(var_price, rule3, 'g', linestyle=':', linewidth=2, label='Rule-3')
    axes[3].set_title("Her bir kuraldan elde edilen çıkış kümeleri")
    axes[3].legend()

    aggregated = np.fmax(np.fmax(rule1, rule2), rule3)
    axes[4].fill_between(var_price, aggregated, 'b', linestyle=':', linewidth=2, label='out')
    axes[4].set_title("Çıkış-Bulanık Küme Birleşimi")

    methods = ['centroid', 'bisector', 'mom', 'lom', 'som']
    defuzzified_results = {method: fuzz.defuzz(var_price, aggregated, method) for method in methods}

    for method, value in defuzzified_results.items():
        print(f"Fiyat({method})=", value)

    selected_value = defuzzified_results['centroid']  
    result = fuzz.interp_membership(var_price, aggregated, selected_value)
    axes[4].plot([0, selected_value], [result, result], 'r')  
    axes[4].plot([selected_value, selected_value], [0, result], 'r')

    for label, membership in zip(["Düşük", "Orta", "Yüksek"], price_memberships):
        print(f"Çıkışın {label} Kümesine Üyeliği=", fuzz.interp_membership(var_price, membership, selected_value))

    plt.tight_layout()  
    plt.show()  

if __name__ == "__main__":
    main()  
