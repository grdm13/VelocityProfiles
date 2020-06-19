import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import time
import os
import seaborn as sns

df = pd.read_csv(
    "/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/tamal_Dense_Flow_CSV_velocities/velocity matrix from 74 frame.csv"
)
img = cv2.imread("/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/tamal_Dense_Flow_Snipets_to_male_Velocities/frame number 75.jpg")
#cv2.imshow("initial", img)
#cv2.waitKey()
#cv2.destroyAllWindows()

plt.subplot(3, 1, 1)
ax = sns.heatmap(df)

plt.subplot(3, 1, 2)
sns.distplot(df)

plt.subplot(3, 1, 3)
plt.imshow(img)

plt.tight_layout()
plt.show()
