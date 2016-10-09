#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""practicing for loop"""

import decimal

def lexicographics(to_analyze):

    list = to_analyze.split('\n')
    
    stats = []

    for item in list:
        
        value = len(item.split())
        stats.append(value)
        
    return(max(stats), min(stats), sum(stats)/decimal.Decimal(len(stats)))
    
