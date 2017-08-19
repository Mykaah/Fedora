#!/bin/bash

# INCREDIBLY IMPORTANT: This report generates a per-week stat for number of users active _over the past 52 weeks_,
# not just in the current week; it is a rolling average.

# This script is silly and inefficient. Should include directly in new-and-old-users-report.py and make that
# not re-read all the data over and over (ring buffers FTW!)

#STARTWEEK=105
STARTWEEK=1
ENDWEEK=$(( ( $(date +'%s') - $(date -ud '2012-01-01 0:0:0' +'%s') )/60/60/24/7 -1 ))

./new-and-old-users-report.py --csvh $(( $STARTWEEK - 1 )) | tee data/contributor-count.csv
for week in $(seq $STARTWEEK $ENDWEEK ); do
  ./new-and-old-users-report.py --csv $week | tee -a data/contributor-count.csv
done

