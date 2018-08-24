#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import censys.ipv4

UID=""
SECRET=""

fields = ["ip", "protocols"]
query = ("21.ftp.banner: 220 \(vsFTPd 2.3.4\) " "and location.country_code: ES")

ipv4s = censys.ipv4.CensysIPv4(UID, SECRET)
for ip in ipv4s.search(query):
    print("IP Address:", ip["ip"], "  ",   "Protocols: ", ip["protocols"])
