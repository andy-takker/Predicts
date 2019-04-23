import numpy as np
from bokeh.plotting import figure


def forecast_k(a, b, x0, k):
    return (1 - (np.e ** a)) * (x0 - b / a) * (np.e ** (-a * k))


def coeffs_ab(x, x_ago):
    if len(x) - 1 > 1:
        b = np.array([[-0.5 * (x_ago[i]+x_ago[i+1]), 1] for i in range(len(x) - 1)])
    else:
        b = np.array([-0.5 * (x_ago[0]+x_ago[1]), 1])
    y = x[1:]
    b_t = b.transpose()
    return np.linalg.inv(b_t.dot(b)).dot(b_t).dot(y)


def x_ago(x):
    return np.array([np.sum(x[:i + 1]) for i in range(len(x))])


def grey_method_prediction(x, n=0):
    if n == 0:
        n = len(x)
    return np.array([forecast_k(*coeffs_ab(x, x_ago(x)), x[0], k) for k in range(1, n)])


def metabolic_grey_method_prediction(x, n=5):
    l = len(x)
    output = x.tolist()
    res = []
    for i in range(n):
        x = np.array(output[len(output)-l:])

        a, b = coeffs_ab(x, x_ago(x))
        predict = forecast_k(a, b, x[0], l)
        res.append(np.array([np.round(a,4), np.round(b,4), predict]))
        output.append(predict)
    return res

def mser(x, x_predict):
    d = [abs(x[i]-x_predict[i])/x_predict[i] for i in range(len(x_predict))]
    return sum(d)/len(x_predict)*100

def plot(x, y, title):
    p = figure(x_axis_type="auto", title = title)
    p.grid.grid_line_alpha = 0.3
    p.xaxis.axis_label = 'x'
    p.yaxis.axis_label = 'y'
    p.line(x, y, color='#96AAF3', legend='Прогноз')
    p.legend.location = "top_right"
    return p
