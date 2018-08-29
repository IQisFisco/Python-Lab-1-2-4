# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 05:07:19 2018

@author: IEUser
"""

from WageEmployee import WageEmployee
from CommissionEmployee import CommissionEmployee

myWageEmployee = WageEmployee(name="Sarah", hourly_wage=12)
myWageEmployee.getPay(hours=13)
print (myWageEmployee.name)
print (myWageEmployee.pay)

myCommissionEmployee = CommissionEmployee(name="Adam", percent_commission=.12)
myCommissionEmployee.getPay(sales=13000)
print (myCommissionEmployee.name)
print (myCommissionEmployee.pay)