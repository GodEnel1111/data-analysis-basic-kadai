import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, tight_layout=True)

#折れ線グラフの表示
y0 = [1, 2, -5, 2]
axes[0,0].plot(y0)

#sin関数の表示
x1 = np.linspace(0, 10, 100)
y1 = 2 + 2 * np.sin(2 * x)
axes[0,1].set(xlim=(0, 10), xticks=np.arange(0, 10),
       ylim=(-1, 5), yticks=np.arange(-1, 6))
axes[0,1].plot(x, y, linewidth=2.0)

#ヒストグラムの表示
x2 = np.random .normal(15, 5, 2000)
axes[1,0].hist(x2, bins=20)

#散布図の表示
np.random.seed(3)
x3 = 4 + np.random.normal(0, 2, 60)
y3 = 4 + np.random.normal(0, 2, len(x))
axes[1,1].scatter(x, y)
