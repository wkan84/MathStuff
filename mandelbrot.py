# This is my attempt to plot the Mandelbrot set
import matplotlib.pyplot as plt


def mandelbrot_func(z, c):
    return z*z + c


def iteration(z, c, limit):
    cnt = 0
    while abs(z) < limit and cnt <= 20:
        z = mandelbrot_func(z, c)
        cnt += 1
    return cnt


def colour_map(n, m):
    return [1-n / m, 1-n / m, 1-n / m]


def complex_map_gen(low_c, upper_c, delta):
    real_change = 0
    val = low_c
    while val.real <= upper_c.real:
        yield val
        val = val + delta*1j
        if val.imag > upper_c.imag:
            real_change += 1
            val = low_c.real + real_change * delta + low_c.imag * 1j


def draw_mandelbrot(lower_c, upper_c, delta):
    x = []
    y = []
    c = []
    cmg = complex_map_gen(lower_c,upper_c,delta)
    while(1):
        try:
            val = next(cmg)
            x.append(val.real)
            y.append(val.imag)
            c.append(colour_map(iteration(0,val,21),21))
        except:
            break
    plt.scatter(x, y, s=0.5, c=c)
    plt.show()

draw_mandelbrot(-2.5-1.5j,1+1.5j,0.005)
