#!/bin/bash

# This script is silly and inefficient. Should include directly in new-and-old-users-report.py and make that
# not re-read all the data over and over (ring buffers FTW!)

# start on week 156, which is the end of 2014, because first-seen dates start in the end of 2012 because
# that's when fedmsg starts. So the old-vs-mid-vs-new metrics are only really meaningful starting two years
# after that. (Actually, push back to 158 because the data looks ugly with low points before that.)
STARTWEEK=158

ENDWEEK=$(( ( $(date +'%s') - $(date -ud '2012-01-01 0:0:0' +'%s') )/60/60/24/7 -1 ))

./new-and-old-users-report.py --csvh $(( $STARTWEEK - 1 )) | tee data/contributor-count.csv
for week in $(seq $STARTWEEK $ENDWEEK ); do
  ./new-and-old-users-report.py --csv $week | tee -a data/contributor-count.csv
done

