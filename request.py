# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:35:54 2020

@author: Sunshine
"""

import requests

url = '/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())