#!/usr/bin/python3
import pandas
import datetime
import collections

firstseen = collections.OrderedDict()
lastseen  = collections.OrderedDict()
actioncount = collections.defaultdict(int)
weeksactive = collections.defaultdict(int)
oldschoolornew = {}
totalactions = 0

# blah blah blah leap years this is precise enough for what we're doing
lastyear = datetime.datetime.now() - datetime.timedelta(365)
twoyears = datetime.datetime.now() - datetime.timedelta(730)
years = (lastyear.strftime("%Y"), datetime.datetime.now().strftime("%Y")) 

datasources = ( "org.fedoraproject.prod.bodhi.update.comment",
                "org.fedoraproject.prod.git.receive",
                "org.fedoraproject.prod.irc.karma",
                "org.fedoraproject.prod.wiki.article.edit")

for datasource in datasources:
  for year in years:
    datafragment=pandas.read_csv("data/" + datasource + ".userdata." + year + ".csv",parse_dates=[3,4])
    for index, row in datafragment.iterrows():
      # store only users who have activity in the past 365 days 
      # and were active more than one week
      if row['lastseen'] > lastyear:
        user=row['user']
        totalactions += row['actions']
        actioncount[user]+=row['actions']
        # mostly, we're filtering out users not active at least 3 weeks
        if row['weeks'] > 2:
          firstseen[user]=row['firstseen']
          lastseen[user]=row['lastseen']
          weeksactive[user]=max(weeksactive[user],row['weeks'])
          if row['firstseen'] < twoyears:
            oldschoolornew[user]="old-school"
          elif row['firstseen'] >= lastyear:
            oldschoolornew[user]="new contributor"
          else:
            oldschoolornew[user]=""




oldcount=0
newcount=0
allcount=0

accumulator=0
topusers=[]
for user in sorted(actioncount, key=actioncount.get, reverse=True):
  accumulator+=actioncount[user]
  topusers.append(user)
  #print("{:20} {}".format(user,oldschoolornew[user]))
  if accumulator>totalactions*2.0/3:
    break
  
newcore=0  
oldcore=0
for user in oldschoolornew:
  allcount+=1
  if oldschoolornew[user] == "old-school":
    oldcount+=1
    if user in topusers:
      oldcore+=1
  elif oldschoolornew[user] == "new contributor":
    newcount+=1
    if user in topusers:
      newcore+=1
      
    
print ("Total active contributors:  {:>5}".format(allcount))   
print ("Core contributors (⅔):      {:>5}".format(len(topusers)))
print ("Old-school contributors:    {:>5}".format(oldcount))
print ("New contributors this year: {:>5}".format(newcount))
print ("")
print ("New core contributors:      {:>5}".format(newcore))
print ("Old core contributors:      {:>5}".format(oldcore))
print ("")
print ("Raw total contributors:     {:>5}".format(len(actioncount)))   
print ("\n")
print ("This report is an aggregate of dist-git, bodhi karma, wiki edits,")
print ("and irc cookies. It doesn't measure all Fedora activity.")
print ("")
print ("Active means at least 3 separate weeks of activity.")
print ("Core means part of the set doing about ⅔s of all actions.")
print ("Old-school contributors started at least two years ago.")
print ("New contributors are new in the past 365 days .")
print ("Note that by this metric, \"mattdm\" is not a core contributor.")

#print ("\n-------------------------------------------\n")
#
#for user in topusers:
#  print("{:20} {}".format(user,oldschoolornew[user]))
