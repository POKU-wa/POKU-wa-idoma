# speed = d/t
# 'input' keyword is used to get data from a user
print('this is for calculating speed')
d = float(input('input distance: '))
t = float(input('input time: '))
speed = d / t
print('the speed is = ', speed, ' km/hr')

#accaleration = v-u/t
print('this is for accaleration')
v = float(input('input final velocity: '))
u = float(input('input initial: '))
t = float(input('input time: '))
accleration = (v - u) / t
print('the accaleration is =', accleration, ' m/s')

#gravitational force = gmm/r**2
print('this is for gravitational_force')
g = 6.77 * 10 ** -11
m1 = float(input('input mass of body 1: '))
m2 = float(input('input mass of body 2: '))
r = float(input('input distance between 2 bodies: '))
gravitational_force = (g * m1 * m2) / r ** 2
print("the gravitational force is =", gravitational_force, 'N')

#energy=1/2mv**2
print('this is for kinetic energy')
m = float(input('input mass: '))
v = float(input('input velocity:'))
kinetic_energy = 0.5 * m * v ** 2
print('the energy is =', kinetic_energy, 'J')

#potential energy=.mgh
print('this is for potential_energy')
m = float(input('input mass:'))
g = 10
h = float(input('this height'))
potential_energy = m * g * h
print('the potential energy is =', potential_energy, 'J')
