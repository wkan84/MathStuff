# Plotting a bifurcation map
import matplotlib.pyplot as plt

class bifurcator:

    def __init__ (self, func, low_bound, up_bound, delta_x, init_x):
        self.func = func
        self.lb = low_bound
        self.num_pts = int((up_bound - low_bound) // delta_x)
        self.delta_x = delta_x
        self.x = init_x

    # Computes 100 iterations after discarding the first 200 iterations for a particular input a
    def single_comp(self, a):
        val_set = set()
        cur_val = self.func(a, self.x)
        for _ in range(200): # discards
            cur_val = self.func(a, cur_val)
        for _ in range(100): # stores
            cur_val = self.func(a, cur_val)
            val_set.add(round(cur_val, 6))
        return val_set

    # Keeps track of the x and y values of the bifurcation plot
    def bifur_plot(self):
        scatter_x = []
        scatter_y = []
        for i in range(self.num_pts):
            a_val = self.lb + i * self.delta_x
            y_of_a_val = self.single_comp(a_val)
            x_of_a_val = [a_val] * len(y_of_a_val)
            scatter_x.extend(x_of_a_val)
            scatter_y.extend(list(y_of_a_val))
        plt.scatter(scatter_x, scatter_y, s=0.5)
        plt.title('Bifurcation')
        plt.xlabel('a')
        plt.ylabel('y')
        plt.show()

def logistic_map (a, x):
    return a * x * (1 - x)

lm = bifurcator(logistic_map, 2.5, 4, 0.002, 0.5)
lm.bifur_plot()

##def tent_map (a, x):
##    return a * min(x, (1 - x))
##
##tm = bifurcator(tent_map, 1, 2, 0.002, 0.5)
##tm.bifur_plot()

##import math

##def guass_map (a, x):
##    return math.exp(-6.2 * x**2) + a
##
##gm = bifurcator(guass_map, -1, 1, 0.002, 0.5)
##gm.bifur_plot()

##def circle_map (a, x):
##    return x + 1/3 - a * math.sin(2*math.pi * x) / (2 * math.pi)
##
##cm = bifurcator(circle_map, 0, 4 * math.pi, 0.002, 0.5)
##cm.bifur_plot()
