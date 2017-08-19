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

datagit=pandas.read_csv("data/org.fedoraproject.prod.git.receive.bucketed-activity.csv",parse_dates=[0])
datagit.set_index('weekstart',inplace=True)

graph=datagit[['users1','users9','users40','userrest']].rename(columns={"users1": "Top 1%","users9":"Top 9%","users40":"Top 40%","userrest":"Remaining 50%"}).plot.area(figsize=(16, 9),
                                                              color=['#579d1c','#ffd320', '#ff420e', '#004586' ],
                                                              grid=True,yticks=range(0,301,25))
#graph.legend(ncol=4)
# totally abusing this.
plt.suptitle("Number of Contributors Making Changes to Packages Each Week",fontsize=24)
graph.set_title("Grouped by Quarterly Activity Level of Each Contributor",fontsize=16)
graph.set_xlabel('')
fig=graph.get_figure()
fig.savefig('images/git.user.count.svg',dpi=300)

#############################################

datagit['msgstotal']=datagit[['msgs1','msgs9','msgs40','msgsrest']].sum(1)
datagit['msgs1%']=100*datagit['msgs1']/datagit['msgstotal']
datagit['msgs9%']=100*datagit['msgs9']/datagit['msgstotal']
datagit['msgs40%']=100*datagit['msgs40']/datagit['msgstotal']
datagit['msgsrest%']=100*datagit['msgsrest']/datagit['msgstotal']




m.rcParams['legend.frameon'] = True
graph=datagit[['msgs1%','msgs9%','msgs40%','msgsrest%']].rename(columns={"msgs1%": "Top 1%","msgs9%":"Top 9%","msgs40%":"Top 40%","msgsrest%":"Remaining 50%"}).plot.area(figsize=(16, 9),
                                                              color=['#579d1c','#ffd320', '#ff420e', '#004586' ],
                                                              grid=True,ylim=(0,100))
plt.suptitle("Percent of Package Changes Each Week From Each Activity Level Group",fontsize=24)
graph.set_title("",fontsize=16)
graph.set_xlabel('')

fig=graph.get_figure()
fig.savefig('images/git.activity.share.svg',dpi=300)

###############################################

graph=datagit[['newusercount']].rename(columns={"newusercount": "New Users"}).plot.area(figsize=(16, 9),
                                                              color='#579d1c',
                                                              grid=True,legend=False)
plt.suptitle("New Packaging Contributor Count Per Week",fontsize=24)
graph.set_title('')
graph.set_xlabel('')
fig=graph.get_figure()
fig.savefig('images/git.newusers.svg',dpi=300)

#############################################

datagit['newuseractions%']=100*datagit['newuseractions']/datagit['msgstotal']
datagit['monthuseractions%']=100*datagit['monthuseractions']/datagit['msgstotal']
datagit['yearuseractions%']=100*datagit['yearuseractions']/datagit['msgstotal']
datagit['olderuseractions%']=100*datagit['olderuseractions']/datagit['msgstotal']




m.rcParams['legend.frameon'] = True
graph=datagit[['newuseractions%','monthuseractions%','yearuseractions%','olderuseractions%']][42:].rename(columns={"newuseractions%": "New This Week","monthuseractions%":"New This Month","yearuseractions%":"New This Year","olderuseractions%":"Old School"}).plot.area(figsize=(16, 9),
                                                              color=['#579d1c','#ffd320', '#ff420e', '#004586' ],
                                                              grid=True,ylim=(0,100))
plt.suptitle("Percent of Package Changes Each Week By Time Since Packager's First Action",fontsize=24)
graph.set_title("",fontsize=16)
graph.set_xlabel('')

fig=graph.get_figure()
fig.savefig('images/git.activity.length.svg',dpi=300)

################################################################################################################
################################################################################################################

databodhi=pandas.read_csv("data/org.fedoraproject.prod.bodhi.update.comment.bucketed-activity.csv",parse_dates=[0])
databodhi.set_index('weekstart',inplace=True)

graph=databodhi[['users1','users9','users40','userrest']].rename(columns={"users1": "Top 1%","users9":"Top 9%","users40":"Top 40%","userrest":"Remaining 50%"}).plot.area(figsize=(16, 9),
                                                              color=['#579d1c','#ffd320', '#ff420e', '#004586' ],
                                                              grid=True,yticks=range(0,301,25))
#graph.legend(ncol=4)
# totally abusing this.
plt.suptitle("Number of Contributors Providing Feedback on Package Updates Each Week",fontsize=24)
graph.set_title("Grouped by Quarterly Activity Level of Each Contributor",fontsize=16)
graph.set_xlabel('')
fig=graph.get_figure()
fig.savefig('images/bodhi.user.count.svg',dpi=300)

#############################################

databodhi['msgstotal']=databodhi[['msgs1','msgs9','msgs40','msgsrest']].sum(1)
databodhi['msgs1%']=100*databodhi['msgs1']/databodhi['msgstotal']
databodhi['msgs9%']=100*databodhi['msgs9']/databodhi['msgstotal']
databodhi['msgs40%']=100*databodhi['msgs40']/databodhi['msgstotal']
databodhi['msgsrest%']=100*databodhi['msgsrest']/databodhi['msgstotal']




m.rcParams['legend.frameon'] = True
graph=databodhi[['msgs1%','msgs9%','msgs40%','msgsrest%']].rename(columns={"msgs1%": "Top 1%","msgs9%":"Top 9%","msgs40%":"Top 40%","msgsrest%":"Remaining 50%"}).plot.area(figsize=(16, 9),
                                                              color=['#579d1c','#ffd320', '#ff420e', '#004586' ],
                                                              grid=True,ylim=(0,100))
plt.suptitle("Percent of Update Feedback Each Week From Each Activity Level Group",fontsize=24)
graph.set_title("",fontsize=16)
graph.set_xlabel('')

fig=graph.get_figure()
fig.savefig('images/bodhi.activity.share.svg',dpi=300)

###############################################

graph=databodhi[['newusercount']].rename(columns={"newusercount": "New Users"}).plot.area(figsize=(16, 9),
                                                              color='#579d1c',
                                                              grid=True,legend=False)
plt.suptitle("New Update Testing Contributor Count Per Week",fontsize=24)
graph.set_title('')
graph.set_xlabel('')
fig=graph.get_figure()
fig.savefig('images/bodhi.newusers.svg',dpi=300)

#############################################

databodhi['newuseractions%']=100*databodhi['newuseractions']/databodhi['msgstotal']
databodhi['monthuseractions%']=100*databodhi['monthuseractions']/databodhi['msgstotal']
databodhi['yearuseractions%']=100*databodhi['yearuseractions']/databodhi['msgstotal']
databodhi['olderuseractions%']=100*databodhi['olderuseractions']/databodhi['msgstotal']




m.rcParams['legend.frameon'] = True
graph=databodhi[['newuseractions%','monthuseractions%','yearuseractions%','olderuseractions%']][42:].rename(columns={"newuseractions%": "New This Week","monthuseractions%":"New This Month","yearuseractions%":"New This Year","olderuseractions%":"Old School"}).plot.area(figsize=(16, 9),
                                                              color=['#579d1c','#ffd320', '#ff420e', '#004586' ],
                                                              grid=True,ylim=(0,100))
plt.suptitle("Percent of Update Feedback Each Week By Time Since Packager's First Action",fontsize=24)
graph.set_title("",fontsize=16)
graph.set_xlabel('')

fig=graph.get_figure()
fig.savefig('images/bodhi.activity.length.svg',dpi=300)


################################################################################################################
################################################################################################################

datawiki=pandas.read_csv("data/org.fedoraproject.prod.wiki.article.edit.bucketed-activity.csv",parse_dates=[0])
datawiki.set_index('weekstart',inplace=True)

graph=datawiki[['users1','users9','users40','userrest']].rename(columns={"users1": "Top 1%","users9":"Top 9%","users40":"Top 40%","userrest":"Remaining 50%"}).plot.area(figsize=(16, 9),
                                                              color=['#579d1c','#ffd320', '#ff420e', '#004586' ],
                                                              grid=True,yticks=range(0,301,25))
#graph.legend(ncol=4)
# totally abusing this.
plt.suptitle("Number of Wiki Editors Each Week",fontsize=24)
graph.set_title("Grouped by Quarterly Activity Level of Each Contributor",fontsize=16)
graph.set_xlabel('')
fig=graph.get_figure()
fig.savefig('images/wiki.user.count.svg',dpi=300)

#############################################

datawiki['msgstotal']=datawiki[['msgs1','msgs9','msgs40','msgsrest']].sum(1)
datawiki['msgs1%']=100*datawiki['msgs1']/datawiki['msgstotal']
datawiki['msgs9%']=100*datawiki['msgs9']/datawiki['msgstotal']
datawiki['msgs40%']=100*datawiki['msgs40']/datawiki['msgstotal']
datawiki['msgsrest%']=100*datawiki['msgsrest']/datawiki['msgstotal']




m.rcParams['legend.frameon'] = True
graph=datawiki[['msgs1%','msgs9%','msgs40%','msgsrest%']].rename(columns={"msgs1%": "Top 1%","msgs9%":"Top 9%","msgs40%":"Top 40%","msgsrest%":"Remaining 50%"}).plot.area(figsize=(16, 9),
                                                              color=['#579d1c','#ffd320', '#ff420e', '#004586' ],
                                                              grid=True,ylim=(0,100))
plt.suptitle("Percent of Wiki Edits Each Week From Each Activity Level Group",fontsize=24)
graph.set_title("",fontsize=16)
graph.set_xlabel('')

fig=graph.get_figure()
fig.savefig('images/wiki.activity.share.svg',dpi=300)

###############################################

graph=datawiki[['newusercount']].rename(columns={"newusercount": "New Users"}).plot.area(figsize=(16, 9),
                                                              color='#579d1c',
                                                              grid=True,legend=False)
plt.suptitle("New Wiki Contributor Count Per Week",fontsize=24)
graph.set_title('')
graph.set_xlabel('')
fig=graph.get_figure()
fig.savefig('images/wiki.newusers.svg',dpi=300)
###############################################

graph=datawiki[['newusercount']].rename(columns={"newusercount": "New Users"}).plot.area(figsize=(16, 9),
                                                              color='#579d1c',
                                                              grid=True,legend=False)
plt.suptitle("New Wiki Contributor Count Per Week",fontsize=24)
graph.set_title('')
graph.set_xlabel('')
fig=graph.get_figure()
fig.savefig('images/wiki.newusers.svg',dpi=300)

#############################################

datawiki['newuseractions%']=100*datawiki['newuseractions']/datawiki['msgstotal']
datawiki['monthuseractions%']=100*datawiki['monthuseractions']/datawiki['msgstotal']
datawiki['yearuseractions%']=100*datawiki['yearuseractions']/datawiki['msgstotal']
datawiki['olderuseractions%']=100*datawiki['olderuseractions']/datawiki['msgstotal']




m.rcParams['legend.frameon'] = True
graph=datawiki[['newuseractions%','monthuseractions%','yearuseractions%','olderuseractions%']][42:].rename(columns={"newuseractions%": "New This Week","monthuseractions%":"New This Month","yearuseractions%":"New This Year","olderuseractions%":"Old School"}).plot.area(figsize=(16, 9),
                                                              color=['#579d1c','#ffd320', '#ff420e', '#004586' ],
                                                              grid=True,ylim=(0,100))
plt.suptitle("Percent of Wiki Edits Each Week By Time Since Editor's First Edit",fontsize=24)
graph.set_title("",fontsize=16)
graph.set_xlabel('')

fig=graph.get_figure()
fig.savefig('images/wiki.activity.length.svg',dpi=300)

###############################################

graph=datawiki[['spamactions']][146:].rename(columns={"spamactions": "Spam Edits"}).plot.area(figsize=(16, 9),
                                                              color='#e00000',
                                                              grid=True,legend=False)
plt.suptitle("Spam Edits Per Week",fontsize=24)
graph.set_title('')
graph.set_xlabel('')
fig=graph.get_figure()
fig.savefig('images/wiki.spam.svg',dpi=300)

###############################################
###############################################
datapagure=pandas.read_csv("data/io.pagure.prod.pagure.git.receive.bucketed-activity.csv",parse_dates=[0])
datapagure.set_index('weekstart',inplace=True)

graph=datapagure[['users1','users9','users40','userrest']].rename(columns={"users1": "Top 1%","users9":"Top 9%","users40":"Top 40%","userrest":"Remaining 50%"}).plot.area(figsize=(16, 9),
                                                              color=['#579d1c','#ffd320', '#ff420e', '#004586' ],
                                                              grid=True,yticks=range(0,25,5))
#graph.legend(ncol=4)
# totally abusing this.
plt.suptitle("Number of Contributors Making Commits to Pagure Each Week",fontsize=24)
graph.set_title("Grouped by Quarterly Activity Level of Each Contributor",fontsize=16)
graph.set_xlabel('')
fig=graph.get_figure()
fig.savefig('images/pagure.user.count.svg',dpi=300)

#############################################

datapagure['msgstotal']=datapagure[['msgs1','msgs9','msgs40','msgsrest']].sum(1)
datapagure['msgs1%']=100*datapagure['msgs1']/datapagure['msgstotal']
datapagure['msgs9%']=100*datapagure['msgs9']/datapagure['msgstotal']
datapagure['msgs40%']=100*datapagure['msgs40']/datapagure['msgstotal']
datapagure['msgsrest%']=100*datapagure['msgsrest']/datapagure['msgstotal']




m.rcParams['legend.frameon'] = True
graph=datapagure[['msgs1%','msgs9%','msgs40%','msgsrest%']].rename(columns={"msgs1%": "Top 1%","msgs9%":"Top 9%","msgs40%":"Top 40%","msgsrest%":"Remaining 50%"}).plot.area(figsize=(16, 9),
                                                              color=['#579d1c','#ffd320', '#ff420e', '#004586' ],
                                                              grid=True,ylim=(0,100))
plt.suptitle("Percent of Pagure Commits Each Week From Each Activity Level Group",fontsize=24)
graph.set_title("",fontsize=16)
graph.set_xlabel('')

fig=graph.get_figure()
fig.savefig('images/pagure.activity.share.svg',dpi=300)

###############################################

graph=datapagure[['newusercount']].rename(columns={"newusercount": "New Users"}).plot.area(figsize=(16, 9),
                                                              color='#579d1c',
                                                              grid=True,legend=False)
plt.suptitle("New Pagure Contributor Count Per Week",fontsize=24)
graph.set_title('')
graph.set_xlabel('')
fig=graph.get_figure()
fig.savefig('images/pagure.newusers.svg',dpi=300)

#############################################

datapagure['newuseractions%']=100*datapagure['newuseractions']/datapagure['msgstotal']
datapagure['monthuseractions%']=100*datapagure['monthuseractions']/datapagure['msgstotal']
datapagure['yearuseractions%']=100*datapagure['yearuseractions']/datapagure['msgstotal']
datapagure['olderuseractions%']=100*datapagure['olderuseractions']/datapagure['msgstotal']




m.rcParams['legend.frameon'] = True
graph=datapagure[['newuseractions%','monthuseractions%','yearuseractions%','olderuseractions%']][42:].rename(columns={"newuseractions%": "New This Week","monthuseractions%":"New This Month","yearuseractions%":"New This Year","olderuseractions%":"Old School"}).plot.area(figsize=(16, 9),
                                                              color=['#579d1c','#ffd320', '#ff420e', '#004586' ],
                                                              grid=True,ylim=(0,100))
plt.suptitle("Percent of Pagure Commits Each Week By Time Since Packager's First Action",fontsize=24)
graph.set_title("",fontsize=16)
graph.set_xlabel('')

fig=graph.get_figure()
fig.savefig('images/pagure.activity.length.svg',dpi=300)
