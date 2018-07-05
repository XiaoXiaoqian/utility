#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 13:26:24 2018
@author: xiaoqian
"""
from __future__ import division
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np

chosed_col=[
'lightcoral',
'palevioletred',
'crimson',
'maroon',
'yellow',
'gold',
'coral',
'sienna',
'turquoise',
'lightskyblue',
'steelblue',
'royalblue',
'mediumslateblue',
'plum',
'mediumorchid',
'rebeccapurple']

#save .txt file
np.savetxt('chosed_color_set.txt', chosed_col, fmt='%s')

#show the color set
sorted_names=chosed_col
n = len(sorted_names)
ncols = 4
nrows = n // ncols + 1

fig, ax = plt.subplots(figsize=(8, 5))

# Get height and width
X, Y = fig.get_dpi() * fig.get_size_inches()
h = Y / (nrows + 1)
w = X / ncols

for i, name in enumerate(sorted_names):
    col = i % ncols
    row = i // ncols
    y = Y - (row * h) - h

    xi_line = w * (col + 0.05)
    xf_line = w * (col + 0.25)
    xi_text = w * (col + 0.3)

    ax.text(xi_text, y, name, fontsize=(h * 0.2),
            horizontalalignment='left',
            verticalalignment='center')

    ax.hlines(y + h * 0.1, xi_line, xf_line,
              color=colors[name], linewidth=(h * 0.6))

ax.set_xlim(0, X)
ax.set_ylim(0, Y)
ax.set_axis_off()

fig.subplots_adjust(left=0, right=1,
                    top=1, bottom=0,
                    hspace=0, wspace=0)
plt.show()
