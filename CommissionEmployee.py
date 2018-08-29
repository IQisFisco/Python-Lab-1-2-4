# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 05:00:30 2018

@author: IEUser
"""

from Employee import Employee

class CommissionEmployee(Employee):
    def __init__ (self, name, percent_commission):
        Employee.__init__(self, name)
        self.percent_commission = percent_commission
    
    def getPay (self, sales):
        self.sales = sales
        self.pay = self.sales * self.percent_commission
