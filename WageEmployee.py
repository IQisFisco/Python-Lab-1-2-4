# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 04:17:26 2018

@author: IEUser
"""

from Employee import Employee

class WageEmployee(Employee):
    
    def __init__(self, name, hourly_wage):
        Employee.__init__ (self, name)
        self.hourly_wage = hourly_wage
    
    def getPay(self, hours):
        self.hours = hours
        self.pay = self.hours * self.hourly_wage
