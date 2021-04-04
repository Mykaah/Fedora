#!/bin/bash
./get-weekly-user-stats.sh
./create-all-time-userstats-csv.sh
python generate-activity-charts.py
python generate-contributor-charts.py
python new-and-old-users-report.py
