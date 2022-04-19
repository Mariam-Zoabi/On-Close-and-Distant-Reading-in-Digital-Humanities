import numpy as np
import matplotlib.pyplot as plt

villages_map = {}

def get_data(names, number_of_vill):
    # Choose the height of the bars
    height = number_of_vill

    # Choose the names of the bars
    bars = names
    x_pos = np.arange(len(bars))

    # Create bars
    plt.bar(x_pos, height)

    # Create names on the x-axis
    plt.xticks(x_pos, bars, color = 'orange')
    plt.yticks(color = 'orange')

    # Save plot
    plt.savefig('foo.png')
    
