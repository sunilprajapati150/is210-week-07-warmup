#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""a good docstirng"""

"""creating a function """
def fibonacci(maxint):
    lastnum, curnum = 0,1
    list = [lastnum,]
    
    """creating a while loop """

    while curnum < maxint:
        list.append(curnum)
        lastnum, curnum = curnum, lastnum + curnum
        """printing the result """

    return(list)

    
