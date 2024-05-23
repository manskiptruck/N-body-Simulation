from Body_Class import Body
import numpy as np
import matplotlib.pyplot as plt

""" This is a script that calculates the trajectory of a particle round the Earth """

G = 6.67408E-11
M_Earth = 5.974e24
R_Earth = 6.38e6
Tday = 24*3600


fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection='3d')


""" Below are the initial conditions, they determine where the Body starts from on the Earth with an initial velocity """

theta_i = float(input("Initial \u03B8 angle (Must be between 0 and 2\u03C0): "))
phi_i = float(input("Initial \u03C6 angle (Must be between 0 and \u03C0): "))
h = float(input("Input the inital height of the particle above the Earth's surface: ")) #Initial height above the Earth of the particle
v_Up = float(input("Input the initial Upward velocity: "))
v_North = float(input("Input the initial Northward velocity: "))
v_East = float(input("Input the initial Eastward velocity: "))

xi = (R_Earth + h)*np.cos(theta_i)*np.sin(phi_i) # The initial Cartesian coordinates in terms of initial angles 
yi = (R_Earth + h)*np.sin(theta_i)*np.sin(phi_i)
zi = (R_Earth + h)*np.cos(phi_i)

""" This takes the initial Northward, Eastward, and Upward velocities and converts them to Cartesian coordinates """

v_xi_input = v_Up*np.cos(theta_i)*np.sin(phi_i) - v_North*np.cos(theta_i)*np.cos(phi_i) - v_East*np.sin(theta_i)
v_yi_input = v_Up*np.sin(theta_i)*np.sin(phi_i) - v_North*np.sin(theta_i)*np.cos(phi_i) + v_East*np.cos(theta_i)
v_zi_input = v_Up*np.cos(phi_i) + v_North*np.sin(phi_i)

""" This accounts for the Earth's rotation in the initial velocity, if it starts on Earth it gets extra tangential velocity """

vrotx = R_Earth*np.sin(theta_i)*np.sin(phi_i)*2*np.pi/Tday
vroty = R_Earth*np.cos(theta_i)*np.sin(phi_i)*2*np.pi/Tday

if h != 0:    # This condition gives the particle's initial velocity an additional velocity due to the
              # Earth if it starts on the Earth's surface
    vrotx = 0
    vroty = 0

v_xi = v_xi_input - vrotx
v_yi = v_yi_input - vroty
v_zi = v_zi_input # Assuming that earth only rotates in x-y plane


x_positions = []
y_positions = []
z_positions = []
time = []

v_esc = np.sqrt(2*G*M_Earth/R_Earth) # Escape velocity of the Earth

t = 0
t_end = 100000
dt = 0.1


test_particle = Body('test_particle', 1, np.array([xi,yi,zi]), np.array([v_xi,v_yi,v_zi]))

norm_v = np.sqrt(v_xi**2 + v_yi**2 + v_zi**2)

#if norm_v > v_esc:
#    raise Exception("That boi is gone, it is no longer affected by Earth's graviational pull")

""" A while loop that carries out the numerical integration, updating the particle's velocity and 
    position given the acceleration due to the Earth """

while t <= t_end:
    x_positions.append(test_particle.position[0])
    y_positions.append(test_particle.position[1])
    z_positions.append(test_particle.position[2])
    test_particle.update_Earth_acceleration()
    test_particle.update_Verlet(dt)
    time.append(t)
    norm = np.sqrt(test_particle.position[0]**2 + test_particle.position[1]**2 + test_particle.position[2]**2)
    t += dt

    if norm < R_Earth:
        break

""" This draws a sphere mesh """

theta = np.arange(0, np.pi, np.pi/100)
for i in theta:
    phi = np.arange(0, (2+1/100)*np.pi, np.pi/100)
    x = R_Earth*np.sin(i)*np.cos(phi)
    y = R_Earth*np.sin(i)*np.sin(phi)
    z = R_Earth*np.cos(i)
    ax.plot3D(x, y, z, color = 'b')
phi1 = np.arange(0, np.pi, np.pi/100)
for i in phi1:
    theta1 = np.arange(0, (2+1/100)*np.pi, np.pi/100)
    x = R_Earth*np.sin(theta1)*np.cos(i)
    y = R_Earth*np.sin(theta1)*np.sin(i)
    z = R_Earth*np.cos(theta1)
    ax.plot3D(x, y, z, color = 'b')

""" This plots the data """

ax.set_xlabel('x')
ax.set_xlim3d([-2*R_Earth, 2*R_Earth])
ax.set_ylabel('y')
ax.set_xlim3d([-2*R_Earth, 2*R_Earth])
ax.set_zlabel('z')
ax.set_xlim3d([-2*R_Earth, 2*R_Earth])

ax.plot3D(x, y, z)
ax.plot3D(x_positions, y_positions, z_positions, color = 'black')

ax.set_aspect('equal')

plt.show()