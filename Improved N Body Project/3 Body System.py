from Body_Class import Body
import numpy as np
import matplotlib.pyplot as plt

Body1 = Body(name = "Body1", 
           mass = 1e24, 
           position = 1e6*np.array([10,0,0]),
           velocity = 1e3*np.array([0,3,-3]),
           radius = 1e8
           )

Body2 = Body(name = "Body2", 
           mass = 1e24, 
           position = 1e6*np.array([0,10,0]),
           velocity = 1e3*np.array([3,3,0]),
           radius = 1e8
           )

Body3 = Body(name = "Body3", 
           mass = 1e24, 
           position = 1e6*np.array([0,0,10]),
           velocity = 1e3*np.array([0,3,3]),
           radius = 1e8
           )

fig = plt.figure(figsize = (8,8))
#ax = fig.add_subplot(projection='3d')

bodies = [Body1,Body2,Body3]
position_data = []

ang_momentum_time_data = []

for i in range(len(bodies)):
    position_data.append([])
    ang_momentum_time_data.append([])

t = 0
dt = 1

while t < 100000:
    for index in range(len(bodies)):
        position_data[index].append((bodies[index].position[0],bodies[index].position[1],bodies[index].position[2]))
        ang_momentum_time_data[index].append((bodies[index].ang_momentum_norm,t))
    for body in bodies:
        body.update_Bodies_acceleration(bodies)
        body.update_Verlet(dt)
        body.update_Momentum()
        body.update_AngMomentum()
    t += dt

for body in ang_momentum_time_data:
    ang = []
    time = []
    for index in range(len(body)):
        ang.append(body[index][0])
        time.append(body[index][1])
    plt.plot(time, ang)


""" for body in position_data:
    x = []
    y = []
    z = []
    for index in range(len(body)):
        x.append(body[index][0])
        y.append(body[index][1])
        z.append(body[index][2])
    ax.plot3D(x, y, z) """


""" ax.set_xlabel('x')
#ax.set_xlim3d([-5e11, 5e11])
ax.set_ylabel('y')
#ax.set_ylim3d([-5e11,5e11])
ax.set_zlabel('z')
#ax.set_zlim3d([-5e11,5e11])
ax.set_aspect('equal') """
plt.show()