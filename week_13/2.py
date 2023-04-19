import matplotlib.pyplot as plt
import numpy as np

N = 100
ms = [5, 10, 20]
xs = np.linspace(0, 1, N)

for m in ms:
    Cs = []
    for x in xs:
        s = 5 / 3
        for i in range(1, m + 1):
            s += 4 / (np.pi * i)**2 * ((-1)**i - 2) * np.cos(np.pi * i * x)
        Cs.append(s)

    # fig = plt.figure()
    plt.plot(xs, Cs, label=f"m is {m}")

plt.legend()
plt.savefig(f"all_ms")
    # plt.show()