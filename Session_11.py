# import numpy as np
# import matplotlib
#
# # matplotlib.use('TkAgg')
# # matplotlib.use('svg')
# import matplotlib.pyplot as plt
#
# # we will be creating a simple 2D vector a.k.a 2D array
# vec = np.array([1, 1])
#
# # now to plot the above vector we need to create the plot
# axs = plt.axes()
# axs.plot(0, 0, 'r-')
#
# # let's create the arrow representing vector
# axs.arrow(0, 0, *vec, color='b', head_width=0.05, head_length=0.1)
#
# # set the limits of the plot
# axs.set_xlim(-2, 2)
# axs.set_ylim(-2, 2)
#
# # setting major ticks
# axs.set_xticks(np.arange(-2, 2))
# axs.set_yticks(np.arange(-1, 2))
#
# # let's add some labels
# axs.set_xlabel('x')
# axs.set_ylabel('y')
# axs.set_title('2D Vector')
#
# # let's add some grid
# axs.grid()
#
# # let's save the plot
# # plt.savefig('Session_11.svg')
#
# # let's show the plot
# plt.show()

import numpy as np
import pandas as pd

money = open('currency_exchange_rate.csv', 'r')

print(money.read())
