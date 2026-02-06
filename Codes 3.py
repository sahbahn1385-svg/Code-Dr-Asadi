#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 18:06:36 2026

@author: applegolshan
"""

def del (self) :
    if self.front == -1:
        print ('Queue is empty')
        return
    if self.front == self.rear :
        k = self.list[self.front]
        self.front = -1
        self.rear = -1
        return k
    k = self.list[self.front]
    self.front += 1
    return k
test = Queue(3)
test.insert(57)
test.insert(32)
test.insert(44)
test.insert(39) #Queue is Full
test.Del()
test.insert(39) #Queue is Full





class C_Queue:
    def __init__(self, max):
        self.list = [] * max
        self.front = -1
        self.rear = -1
    def  insert(self , x):
        if (self.rear +1) % len(self.list) == self.front:
            print("Queue is full")
            return
        if  self.front == -1:
            self.front = 0
            self.rear = 0
            self.list[0] = x
            return
        self.rear=(self.rear +1) % len(self.list)
        self.list[self.rear] = x
    def delete(self):
        if self.front == -1:
            print("Queue is empty")
            return
        if self.front == self.rear:
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k
        k = self.list[self.front]
        self.front = (self.front +1) % len (self.list)
        return k
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear +1) % len (self.list) == self.front