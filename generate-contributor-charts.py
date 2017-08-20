#!/usr/bin/python3
import os
import pandas
import matplotlib as m
m.use("Agg")
import matplotlib.pyplot as plt 
m.rcParams['font.size'] = 12
m.rcParams['font.family'] = 'Overpass'
m.rcParams['legend.frameon'] = False

try:
    os.makedirs('./images')
except OSError:
    pass

data=pandas.read_csv("data/contributor-count.csv",parse_dates=[0])
data.set_index('weekstart',inplace=True)

m.rcParams['legend.frameon'] = True
graph=data[['oldactive','midactive','newactive']].rename(columns={"oldactive": "Old School","midactive":"Intermediate","newactive":"New Contributors"}).plot.area(figsize=(16, 9),
                                                              color=[ '#ffd320', '#ff420e', '#579d1c' ], # '#004586'
                                                              grid=True,stacked=True ,yticks=range(0,301,25))
data[['rawcount']].rename(columns={"rawcount": "All Contributors"}).plot(figsize=(16, 9),
                                                              ax=graph ,yticks=range(0,301,25))
                                                              
                                                              
#graph.legend(ncol=4)
# totally abusing this.
plt.suptitle("Fedora Contributors by Week",fontsize=24)
graph.set_title("Stacked graph of contributors with activity this week and at least two other weeks in the last year.\nOld school contributors have been active for longer than two years; new contributors, less than one.\nBlue line shows all contributors active this week regardless of amount of other activity.",fontsize=12)
graph.set_xlabel('')
fig=graph.get_figure()
fig.savefig('images/active-contributors-by-week.svg',dpi=300)

