#! /usr/bin/python 
# -*- coding: utf-8 -*- 
u""" 
author Atsushi Sakai
"""
import numpy
import random

def SearchOnONN(target,datalist):
    print("SearchOnONN")
    for data1 in datalist:
        for data2 in datalist:
            if (data1+data2) == target:
                print((data1,data2,target))
                return(data1)
    raise ValueNotFoundException('ValueNotFoundException')

def SearchOnONlogN(target,datalist):
    print("SearchOnONLogN")
    i=0
    j=len(datalist)-1

    datalist.sort()

    while i!=j:
        sumdata=datalist[i]+datalist[j]
        if sumdata>target:
            j-=1
        elif sumdata<target:
            i+=1
        else:
            print((datalist[i],datalist[j],target))
            return (datalist[i])
    raise ValueNotFoundException('ValueNotFoundException')


def SearchOnON(target,datalist):
    print("SearchOnON")
    hashset={}

    for data in datalist:
        d=target-data
        if d in hashset:
            print(data,d,target)
            return (data)
        else:
            hashset[data]=data
    raise ValueNotFoundException('ValueNotFoundException')

if __name__ == '__main__':
    target=70
    datalist=numpy.arange(50)
    random.shuffle(datalist)
    print(SearchOnONN(target,datalist))
    print(SearchOnONlogN(target,datalist))
    print(SearchOnON(target,datalist))

