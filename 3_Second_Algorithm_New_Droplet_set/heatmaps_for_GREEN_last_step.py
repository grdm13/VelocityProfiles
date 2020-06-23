import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import time
import os
import seaborn as sns



df = pd.read_csv(
    "/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/3_Second_Algorithm_New_Droplet_set/ONE ARRAY (1D) FULL VELOCITY PROFILE of 67 frames.csv"
)


fig = plt.figure()
plt.subplot(2, 1, 1)
ax1 = sns.heatmap(df)
plt.subplot(2, 1, 2)
ax2 = sns.distplot(df)
#fig.savefig('full_figure.png')
plt.tight_layout()
plt.show()





