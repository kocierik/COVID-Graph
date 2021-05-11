import matplotlib.pyplot as plt
import numpy as np
import json
from matplotlib import pyplot
import Genera

EMILIA_ROMAGNA = 8
LOMBARDIA = 3
genera = Genera.Genera('regioni.json')

[xItalia, yItalia] = genera.genera_xy()
plt.plot(xItalia, yItalia, color='tab:orange', label="Italia")

[xEmilia, yEmilia] = genera.genera_xy(EMILIA_ROMAGNA)
plt.plot(xEmilia, yEmilia, color='tab:blue', label="Emilia Romagna")

[xLombardia, yLombardia] = genera.genera_xy(LOMBARDIA)
plt.plot(xLombardia, yLombardia, color='tab:red', label="LOMBARDIA")

plt.show()
