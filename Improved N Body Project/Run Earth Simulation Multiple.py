from Body_Class import Body
import numpy as np
import matplotlib.pyplot as plt

""" This is a script that calculates the trajectories of multiple particles round the Earth """

G = 6.67408E-11
M_Earth = 5.974e24
R_Earth = 6.38e6

integration_method = input("Input one of the integration methods available:\nEuler\nEuler-Cromer\nVerlet\nInput: ")

fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')

v_xi = [7000,8000,9000,10000]
v_yi = 0
v_zi = 0
h = 20000

time = []

v_esc = np.sqrt(2*G*M_Earth/R_Earth)

"""This calculates the trajectory of a particle for different inital velocities"""
for v in v_xi:

    x_positions = []
    y_positions = []
    z_positions = []

    test_particle = Body('test_particle', 1, np.array([0,0,h + R_Earth]), np.array([v,v_yi,v_zi]))

    norm_v = np.sqrt(v**2 + v_yi**2 + v_zi**2)

    if norm_v > v_esc:
        raise Exception("That boi is gone, it is not longer affected by Earth's graviational pull")

    t = 0
    t_end = 50000
    dt = 0.1

    """This if statement determines which integration method to use"""

    if integration_method.lower() == "euler":
        while t <= t_end:
            x_positions.append(test_particle.position[0])
            y_positions.append(test_particle.position[1])
            z_positions.append(test_particle.position[2])
            test_particle.update_Earth_acceleration(dt)
            test_particle.update_Euler(dt)
            norm = np.sqrt(test_particle.position[0]**2 + test_particle.position[1]**2 + test_particle.position[2]**2)
            t += dt

            if norm < R_Earth:
                break

        ax.plot3D(x_positions, y_positions, z_positions, color = 'black')

    elif integration_method.lower() == "euler-cromer":
        while t <= t_end:
            x_positions.append(test_particle.position[0])
            y_positions.append(test_particle.position[1])
            z_positions.append(test_particle.position[2])
            test_particle.update_Earth_acceleration(dt)
            test_particle.update_EulerCromer(dt)
            norm = np.sqrt(test_particle.position[0]**2 + test_particle.position[1]**2 + test_particle.position[2]**2)
            t += dt

            if norm < R_Earth:
                break
        ax.plot3D(x_positions, y_positions, z_positions, color = 'black')

    elif integration_method.lower() == "verlet":
        while t <= t_end:
            x_positions.append(test_particle.position[0])
            y_positions.append(test_particle.position[1])
            z_positions.append(test_particle.position[2])
            test_particle.update_Earth_acceleration(dt)
            test_particle.update_Verlet(dt)
            norm = np.sqrt(test_particle.position[0]**2 + test_particle.position[1]**2 + test_particle.position[2]**2)
            t += dt

            if norm < R_Earth:
                break
        ax.plot3D(x_positions, y_positions, z_positions, color = 'black')

"""This draws a sphere mesh"""
theta = np.arange(0, np.pi, np.pi/50)
for i in theta:
    phi = np.arange(0, (2+1/50)*np.pi, np.pi/50)
    x = R_Earth*np.sin(i)*np.cos(phi)
    y = R_Earth*np.sin(i)*np.sin(phi)
    z = R_Earth*np.cos(i)
    ax.plot3D(x, y, z, color = 'b')
phi1 = np.arange(0, np.pi, np.pi/50)
for i in phi1:
    theta1 = np.arange(0, (2+1/50)*np.pi, np.pi/50)
    x = R_Earth*np.sin(theta1)*np.cos(i)
    y = R_Earth*np.sin(theta1)*np.sin(i)
    z = R_Earth*np.cos(theta1)
    ax.plot3D(x, y, z, color = 'b')

ax.set_xlim3d([-2*R_Earth, 2*R_Earth])
ax.set_xlim3d([-2*R_Earth, 2*R_Earth])
ax.set_xlim3d([-2*R_Earth, 2*R_Earth])

ax.grid(False)

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

ax.plot3D(x, y, z)
ax.set_aspect('equal')

plt.show()