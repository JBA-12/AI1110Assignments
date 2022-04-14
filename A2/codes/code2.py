#ICSE 2019,Class 12
#Question 3-A
#Verifying whether obtained x values are correct solutions or not for the given trigonometric equation

#Python libraries for math 
import numpy as np

#Substituting the x value in LHS
a = np.arctan((1-2**(0.5))/(1-2*(2**(0.5))))
b = np.arctan((1+2**(0.5))/(1+2*(2**(0.5))))
z = a+b
#Verifying for one x implies the other, because both solutions just differ in sign(i.e.,a and b are interchanged for other x).

#RHS of the equation
s = 22/28

if z == s:
  print("x is a solution to the given equation")
else:
  print("x is not a solution")