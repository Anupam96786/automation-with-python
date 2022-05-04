#!/usr/bin/env python3

import re
import csv

err = {}
usr_stat = {}

with open('syslog.log', 'r') as f:
    for line in f:
        if 'INFO' in line:
            res = re.search('\((.*)\)', line)
            user = res.group(1)
            usr_stat[user] = usr_stat.get(user, [0, 0])
            usr_stat[user][0] += 1
        if 'ERROR' in line:
            res = re.search('ERROR (.*) \((.*)\)', line)
            error = res.group(1)
            user = res.group(2)
            err[error] = err.get(error, 0) + 1
            usr_stat[user] = usr_stat.get(user, [0, 0])
            usr_stat[user][1] += 1

err = sorted(list(err.items()), key=lambda x: x[1], reverse=True)
usr_stat = sorted(list(map(lambda x: [x[0], *x[1]], usr_stat.items())), key=lambda x: x[0])

with open('error_message.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Error', 'Count'])
    writer.writerows(err)

with open('user_statistics.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Username', 'INFO', 'ERROR'])
    writer.writerows(usr_stat)
