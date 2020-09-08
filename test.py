#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Zhanghui  time:2020/9/2
#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-

import os
import sys
import netifaces as netifaces


#获得本机网关
routingGateway = netifaces.gateways()['default'][netifaces.AF_INET][0]     #字符串
print(routingGateway)
