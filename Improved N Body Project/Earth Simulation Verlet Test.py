from Body_Class import Body
import numpy as np
import matplotlib.pyplot as plt

G = 6.67408E-11
M_Earth = 5.974e24
R_Earth = 6.38e6
Tday = 24*3600


fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(projection='3d')

theta_i = 0 #must be between 0 and 2 pi
phi_i = np.pi/4 #must be between 0 and pi

h = 20000 #initial height above the Earth

"""These are the initial Cartesian positions based on the initial angles"""
xi = (R_Earth + h)*np.cos(theta_i)*np.sin(phi_i)
yi = (R_Earth + h)*np.sin(theta_i)*np.sin(phi_i)
zi = (R_Earth + h)*np.cos(phi_i)


"""This determines the initial speed of the Body in North, East and Away from Earth"""
v_Up = 3000
v_North = 3000
v_East = 0


v_xi = v_Up*np.cos(theta_i)*np.sin(phi_i) - v_North*np.cos(theta_i)*np.cos(phi_i) - v_East*np.sin(theta_i)
v_yi = v_Up*np.sin(theta_i)*np.sin(phi_i) - v_North*np.sin(theta_i)*np.cos(phi_i) + v_East*np.cos(theta_i)
v_zi = v_Up*np.cos(phi_i) + v_North*np.sin(phi_i)

x_positions = []
y_positions = []
z_positions = []
time = []

v_esc = np.sqrt(2*G*M_Earth/R_Earth)

t = 0
t_end = 10000
dt = 1

x_positions = []
y_positions = []
z_positions = []

test_particle = Body('test_particle', 1, np.array([xi,yi,zi]), np.array([v_xi,v_yi,v_zi]))

norm_v = np.sqrt(v_xi**2 + v_yi**2 + v_zi**2)

#if norm_v > v_esc:
#    raise Exception("That boi is gone, it is no longer affected by Earth's graviational pull")

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


ax.set_xlabel('x')
ax.set_xlim3d([-2*R_Earth, 2*R_Earth])
ax.set_ylabel('y')
ax.set_xlim3d([-2*R_Earth, 2*R_Earth])
ax.set_zlabel('z')
ax.set_xlim3d([-2*R_Earth, 2*R_Earth])
ax.plot3D(x_positions, y_positions, z_positions, color = 'black')

ax.set_aspect('equal')

plt.show()