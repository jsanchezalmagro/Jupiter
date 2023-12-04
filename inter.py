# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 19:35:30 2023

@author: jsanchez
"""
Number = 3925
NDwell = 5
index = 0
 
cnt = int(Number / NDwell)
Pos = 0
for i in range(Number):
     print("index : " + str(i) + " --> " + str(Pos))
     
     Pos = Pos + NDwell
     
     
     if cnt == 0:
         
         index += 1
         print("Next : " + str(index))
         Pos = index
         cnt = int(Number / NDwell)
     else:
         cnt -= 1
