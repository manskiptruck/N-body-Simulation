from Body_Class import Body
import numpy as np
import matplotlib.pyplot as plt
from Solar_System_Data import Sol,Mercury,Venus,Earth,Mars,Jupiter

"""
A python script to calculate the trajectories of planets in the solar system.

To get the code to work, create instances of the Body object where each instance has attributes relating 
to the initial conditions of each planet. Then add the instance of each class to the "bodies" list. This
will store the initial conditions of every planet.
"""


fig = plt.figure(figsize = (8,8))
#ax = fig.add_subplot(projection='3d')

bodies = [Sol,Mercury,Venus,Earth,Mars,Jupiter]

position_data = []
ang_momentum_time_data = []

for i in range(len(bodies)):
    position_data.append([])
    ang_momentum_time_data.append([])

t = 0
t_end = 100000
ang_momentum_tot_data = []
time = []
dt = 10

while t < t_end:
    for index in range(len(bodies)):
        #position_data[index].append((bodies[index].position[0],bodies[index].position[1],bodies[index].position[2]))
        ang_momentum_time_data[index].append((np.log(np.linalg.norm(
            bodies[index].ang_momentum(bodies[index].mass, bodies[index].position, bodies[index].velocity))), t))
    for body in bodies:
        body.update_Bodies_acceleration(bodies)
        body.update_Verlet(dt)
    time.append(t)
    t += dt

"""
This takes the entries of each body after the simulation and plots it, this is the only way to do this
if we want it to plot the position data of the bodies successively.
"""

""" BodyNumber = 0
for body in position_data:
    x = []
    y = []
    z = []
    for index in range(len(body)):
        x.append(body[index][0])
        y.append(body[index][1])
        z.append(body[index][2])
    ax.plot3D(x, y, z, label = bodies[BodyNumber].name)
    BodyNumber += 1
 """

BodyNumber = 0
for body_info in ang_momentum_time_data:
    ang = []
    time = []
    for index in range(len(body_info)):
        ang.append(body_info[index][0])
        time.append(body_info[index][1])
    plt.plot(time, ang, label = bodies[BodyNumber].name)
    plt.legend()
    BodyNumber += 1

""" ax.set_xlabel('x')
ax.set_xlim3d([-1.5*abs(np.max(bodies[-1].position)), 1.5*abs(np.max(bodies[-1].position))])
# This ensures that the coordinate limits encase the position of the furthest object
# Provided that the bodies with the largest orbit are at the end of the list of bodies 
ax.set_ylabel('y')
ax.set_ylim3d([-1.5*abs(np.max(bodies[-1].position)), 1.5*abs(np.max(bodies[-1].position))])
ax.set_zlabel('z')
ax.set_zlim3d([-1.5*abs(np.max(bodies[-1].position)), 1.5*abs(np.max(bodies[-1].position))])
ax.set_aspect('equal') """
plt.show()