#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 18:05:37 2026

@author: applegolshan
"""

class stack :
    def__init__ (self,limit=1000):
        self.st = []
        self.lim = limit
"""
onsor ra be poshte ezafe mikonad 
"""
    def push (self,x):
        if len(self.st) >= self.lim :
            print('stack is full')
            return -1
        self.st.append(x)
"""
onsore balaii ra hazf va barmigardanad
"""
    def pop(self):
        if len (self.st) == 0 :
            print ('stack is empty')
            return -1
        return self.st.pop()
"""
onsore balaii ra faghat neshan midahad
"""
    def peek (self):
        if len (self.st) == 0 :
            print ('stack is empty')
            return -1
        return self.st [-1]
"""
tamamie x haye darone poshte ra barmigardanad
"""
    def find (self,x) :
        for i in range (len(self.st)) :
            if self.st [i] == x :
                print(i)
"""
avalin indexe shamele x ra bargardandan
"""
    def find (self,x) :
        for i in range (len(self.st)) :
            if self.st [i] == x :
                print(i)
                return
"""
akharin indexe shamele x ra chap konad
"""
    def find2 (self,x) :
        for i in range (len(self.st)-1, -1, -1) :
            if self.st [i] == x :
                print(i)
                return
    def find2 - n (self,x) :
        for i in range (len(self.st)) :
            if self.st[i] == x :
                p = i
        print(p)
    def find2 - n (self,x) :
        list[]
        for i in range (len(self.st)) :
            if self.st[i] == x :
                list.append(i)
        print(list[2])
    def replace (self,x,y) :
        for i in range (len(self.st)) :
            if self.st [i] == x :
                self.st [i] +y
                
    