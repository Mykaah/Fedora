#!/bin/bash
./get-weekly-user-stats.sh
./create-all-time-userstats-csv.sh
./generate-activity-charts.py
./generate-contributor-charts.py
./new-and-old-users-report.py
