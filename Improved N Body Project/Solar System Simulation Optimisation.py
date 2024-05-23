# Don't need to import Body_Class since it's in Solar_System_Data
import numpy as np
import matplotlib.pyplot as plt
from Solar_System_Data import Sol,Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune

fig = plt.figure(figsize = (8,8))
#ax = fig.add_subplot(projection='3d')

bodies = [Sol,Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune]

position_data = []

for index in range(len(bodies)):
    position_data.append([])

t = 0
dt = 100

ang_momentum_data = []

integration_method = input()

while t < 100000:
    for index in range(len(bodies)):
        position_data[index].append((bodies[index].position[0],bodies[index].position[1],bodies[index].position[2]))
        
    ang_momentum_tot = np.array([0.0,0.0,0.0])

    for body in bodies:
        ang_momentum = body.ang_momentum(body.mass, body.position, body.velocity)
        ang_momentum_tot += ang_momentum
        body.update_Bodies_acceleration(bodies)
        if integration_method.lower() == "verlet":
            body.update_Verlet(dt)
        elif integration_method.lower() == "euler":
            body.update_Euler(dt)
    ang_momentum_data.append((np.linalg.norm(ang_momentum_tot), t))
    t += dt

""" for body_position in position_data:
    x = []
    y = []
    z = []
    for index in range(len(body_position)):
        x.append(body[index][0])
        y.append(body[index][1])
        z.append(body[index][2])
    ax.plot3D(x, y, z) """

ang_momentum = []
time = []

for index in range(len(ang_momentum_data)):
    ang_momentum.append((ang_momentum_data[index][0]-ang_momentum_data[0][0])/ang_momentum_data[0][0])
    time.append(ang_momentum_data[index][1])

plt.plot(time, ang_momentum)

""" ax.set_xlabel('x')
ax.set_xlim3d([-1.5*abs(np.max(bodies[-1].position)), 1.5*abs(np.max(bodies[-1].position))])
ax.set_ylabel('y')
ax.set_ylim3d([-1.5*abs(np.max(bodies[-1].position)), 1.5*abs(np.max(bodies[-1].position))])
ax.set_zlabel('z')
ax.set_zlim3d([-1.5*abs(np.max(bodies[-1].position)), 1.5*abs(np.max(bodies[-1].position))])
ax.set_aspect('equal') """
plt.show()
