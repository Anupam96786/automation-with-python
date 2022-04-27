#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Anupam Samanta
# Created Date: 28/04/2022
# ---------------------------------------------------------------------------

import sys
import time

import psutil

while True:
    try:
        cpu_percent = psutil.cpu_percent()
        print('[' + '|' * round(cpu_percent / 2) + ' ' * (50 - round(cpu_percent / 2)) + '] ' + str(cpu_percent) + '%',
              end='')
        time.sleep(0.5)
        print('\r', end='')
    except KeyboardInterrupt:
        print('\r', end='')
        sys.exit(0)
