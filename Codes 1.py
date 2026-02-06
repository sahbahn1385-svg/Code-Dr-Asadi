#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 23:11:12 2026

@author: applegolshan
"""

class Queue :
    def __init__ (self,max=100) :
        self.list = [] * max
        self.front = -1
        self.rear = -1
    def insert (self,x) :
"""
        estesna por budan
"""
        if self.rear >= len(self.list)-1 :
            print ("Queue is full")
            return
"""
estesna khali budan
"""
        if self.front == -1 :
            self.front = 0
            self.rear = 0
            self.list[0] = x
            return
"""
halate addi
"""
        self.rear += 1
        self.list [self.rear] = x