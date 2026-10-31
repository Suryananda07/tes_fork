from matplotlib import pyplot as plot
import math as mth

x_value = range(1, 25)

y1 = [x for x in x_value]

y2 = [x**2 for x in x_value]

y3 = [100*x + 5 for x in x_value]


y4 = [(x**2 + 1)**10 for x in x_value]

y5 = [(((10*x)**2) + (7*x) + 3)**(1/2) for x in x_value]

y6 = [(2*x) * (mth.log(x+2)**2) + (x+2)**2 * mth.log(x/2) for x in x_value]

plot.plot(x_value, y1, label="y = 2n + 10")
plot.plot(x_value, y2, label="y = n²")
plot.plot(x_value, y3, label="y = 100n + 5")
plot.plot(x_value, y4, label="y = (n^2 + 1)^10")
plot.plot(x_value, y5, label="y = (10n^2 + 7n + 3)^1/2")
plot.plot(x_value, y6, label="y = 2n log(n+2)^2 + (n+2)^2 log(n/2)")

plot.title("3 Grafik Fungsi")
plot.xlabel("X")
plot.ylabel("Y")

plot.legend()

plot.show()