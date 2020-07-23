# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:31:38 2020

@author: mcsbi
"""
"""
Pergunta 5

Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one. 
"""
def car_listing(car_prices):
  result = ""
  for names in car_prices.items():
    result += "{} costs {} dollars".format(names[0], names[1]) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))
