#!/usr/bin/python3
import pandas
import datetime
import collections
import sys

# INCREDIBLY IMPORTANT: This report generates a per-week stat for number of users active _over the past 52 weeks_,
# not just in the current week; it is a rolling average.

# BUT if --csv (or --csvh, for csv with header) is given, it gives the number for _that week only_

firstseen = collections.OrderedDict()
lastseen  = collections.OrderedDict()
actioncount = collections.defaultdict(int)
weeksactive = collections.defaultdict(int)
oldschoolornew = {}
totalactions = 0


n = len(sys.argv[1:])
csvoutput=False
if n == 0:
  reportweek = int((datetime.datetime.now()-datetime.datetime.strptime("2012-01-01", "%Y-%m-%d")).days/7)
elif n == 1:
   reportweek=int(sys.argv[1])
elif sys.argv[1] == "--csv":
   reportweek=int(sys.argv[2])
   csvoutput=True
   csvheader=False
elif sys.argv[1] == "--csvh":
   reportweek=int(sys.argv[2])
   csvoutput=True
   csvheader=True
else:
  sys.exit(1)



reporttime = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d") + datetime.timedelta(reportweek*7)
# 52 weeks is precise enough for metrics gathering :)
lastyear = reporttime - datetime.timedelta(364)
twoyears = reporttime - datetime.timedelta(728)
   
weeks = range(reportweek-51,reportweek+1)

datasources = ( "org.fedoraproject.prod.bodhi.update.comment",
                "org.fedoraproject.prod.git.receive",
                "org.fedoraproject.prod.irc.karma",
                "org.fedoraproject.prod.wiki.article.edit",
                "org.fedoraproject.prod.infragit.receive")

for datasource in datasources:
  for week in weeks:
    try:
      datafragment=pandas.read_csv("data/weekly/{}.userdata.{:05}.csv".format(datasource,week),parse_dates=[2,3])
    except FileNotFoundError:
      # ignore missing data.... probably should errror on _everything_ missing (FIXME)
      continue
      
    for index, row in datafragment.iterrows():
      user=row['user']

      totalactions += row['actions']
      actioncount[user]+=row['actions']

      if not user in weeksactive:
        weeksactive[user]=set()
      weeksactive[user].add(week)

      if not user in firstseen:
        firstseen[user]=row['firstseen']
      else:
        if row['firstseen'] < firstseen[user]:
          firstseen[user]=row['firstseen']

      if not user in lastseen:
        lastseen[user]=row['lastseen']
      else:
        if row['lastseen'] < lastseen[user]:
          lastseen[user]=row['lastseen']
          
      if row['firstseen'] < twoyears:
        oldschoolornew[user]="old-school"
      elif row['firstseen'] >= lastyear:
        oldschoolornew[user]="new contributor"
      else:
        oldschoolornew[user]=""

rawcount=0
oldcount=0
midcount=0
newcount=0
allactive=0

accumulator=0
topusers=[]
for user in sorted(actioncount, key=actioncount.get, reverse=True):
  accumulator+=actioncount[user]
  topusers.append(user)
  #print("{:20} {}".format(user,oldschoolornew[user]))
  if accumulator>totalactions*2.0/3:
    break
  
newcore=0  
midcore=0
oldcore=0

for user in oldschoolornew:

  # in csv mode, only report on activity *this* week
  if csvoutput and not reportweek in weeksactive[user]:
    continue

  rawcount+=1

  # only count users who are active
  # at least 4 distinct weeks in the past year
  if len(weeksactive[user]) < 4:
    continue

    
  allactive+=1
  if oldschoolornew[user] == "old-school":
    oldcount+=1
    if user in topusers:
      oldcore+=1
  elif oldschoolornew[user] == "new contributor":
    newcount+=1
    if user in topusers:
      newcore+=1
  else:
    midcount+=1
    if user in topusers:
      midcore+=1
  

if csvoutput:
  if csvheader:
    print("weekstart,rawcount,oldactive,midactive,newactive,oldcore,midcore,newcore")
  print("{0:%Y-%m-%d}".format(reporttime),rawcount,
        oldcount,midcount,newcount,
        oldcore,midcore,newcore,
        sep=",")
  sys.exit(0)

      
print ("Report for year ending the week of {0:%Y-%m-%d}:".format(reporttime))
print ("")
print ("Raw total contributors:        {:>5}".format(rawcount))   
print ("Total active contributors:     {:>5}".format(allactive))   
print ("Core contributors (⅔ actions)  {:>5}".format(len(topusers)))
print ("")
print ("Old-school contributors:       {:>5}".format(oldcount))
print ("Intermediate contributors:     {:>5}".format(midcount))
print ("New contributors this year:    {:>5}".format(newcount))
print ("")
print ("Old core contributors:         {:>5}".format(oldcore))
print ("Intermediate core contributors:{:>5}".format(midcore))
print ("New core contributors:         {:>5}".format(newcore))
print ("\n")
print ("This report is an aggregate of dist-git, bodhi karma, wiki edits,")
print ("infra git, and irc cookies. It doesn't measure all Fedora activity.")
print ("")
print ("Active means at least four separate weeks of activity.")
print ("Core means part of the set doing about ⅔s of all actions.")
print ("Old-school contributors started at least two years (104 weeks) ago.")
print ("New contributors are new in the past 52 weeks.")
print ("Note that by this metric, \"mattdm\" is not a core contributor.")

#print ("\n-------------------------------------------\n")
#
#for user in topusers:
#  print("{:20} {}".format(user,oldschoolornew[user]))
