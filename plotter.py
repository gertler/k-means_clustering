import matplotlib.pyplot as plt

class BadDataError(IOError):
    def __init__(self, arg):
        self.args = arg

def show_data(param_data_x, param_data_y):
    # assume param_data_x/y are both lists
    if len(param_data_x) != len(param_data_y):
        raise BadDataError("X and Y lists are not the same length")
    plt.plot(param_data_x, param_data_y)
    x_min = min(param_data_x)
    x_max = max(param_data_x)
    y_min = min(param_data_y)
    y_max = max(param_data_y)
    plt.axis([x_min, x_max, y_min, y_max])
    plt.show()

plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()