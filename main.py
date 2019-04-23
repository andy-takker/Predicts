import numpy as np
import grey_functions as gf
from bokeh.plotting import show


# read from input.txt file
data = np.loadtxt("input.txt", delimiter=' ', dtype=np.float)


d_mgm = []
d_gm = []
for j in range(3,8):
    predict = []
    for i in range(3):
        predict.append(gf.metabolic_grey_method_prediction(data[len(data)-3-j+i:len(data)-3+i],1)[0][2])
    d_mgm.append([gf.mser(data[len(data) - 3:], np.array(predict)), j])
    gm_pred = gf.grey_method_prediction(data[len(data)-3-j:len(data)-3],j+2)
    d_gm.append([gf.mser(data[len(data)-3:], gm_pred[len(gm_pred)-3:]), j])

k_mgm = min(d_mgm)[0]
k_gm = min(d_gm)[0]
print(k_gm, k_mgm)
