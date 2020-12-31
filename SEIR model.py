import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#times for incubation and infection
incubate= 5.1
infective = 3.3

#R naught value
Ro = 2.4

#Total Population
N = 7900000

#Initial values for the model 
E0 = 1/N #Replace the 1 with the initial exposed
I0 = 0.00
R0 = 0.00
S0 = 1 - e0 - i0 - r0
x0 = [s0,e0,i0,r0]

#Determing the values for the constants
alpha = 1/incubate
gamma = 1/infective
beta = Ro/gamma

def SEIR(x,time):
    #initialize the original values
    S,E,I,R = x
    dx = np.zeros(4)
    #Base equations
    dx[0] = -beta * S * I - beta * E * S
    dx[1] = beta * S * I + beta * E * S - alpha * E
    dx[2] = alpha * E - gamma * I
    dx[3] = gamma * I
    return dx

#Amount of time being tracked (days)
t = np.linspace(0, 200, 101)

#Integration
x = odeint(SEIR,x0,t)
s = x[:,0]; e = x[:,1]; i = x[:,2]; r = x[:,3]

# Plotting the data
plt.figure(figsize=(8,5))

plt.title('SEIR model of Hong Kong flu in New York')
plt.plot(t,s, color='blue', lw=3, label='Susceptible')
plt.plot(t,r, color='red',  lw=3, label='Recovered')
plt.plot(t,i, color='orange', lw=3, label='Infective')
plt.plot(t,e, color='purple', lw=3, label='Exposed')
plt.ylabel('Fraction')
plt.legend()
plt.show()