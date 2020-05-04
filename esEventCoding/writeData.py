#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:12:12 2019

@author: karen
"""
import os

def writeData(dataHead, dataList, filename):
    
    headerToSave = ''
    dataToSave = ''
    
    for head in dataHead: 
        headerToSave = headerToSave + head + '\t'
    
    headerToSave = headerToSave + '\n'
        
    for data in dataList: 
        dataToSave = dataToSave + data + '\t'
    
    dataToSave = dataToSave + '\n'
        
    with open(filename, 'a+') as saveFile:
        if os.stat(filename).st_size==0:
            saveFile.write(headerToSave)
        else:
            saveFile.write(dataToSave)
                    
        