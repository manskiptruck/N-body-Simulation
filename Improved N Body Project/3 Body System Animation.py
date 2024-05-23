from Body_Class import Body
import numpy as np
import matplotlib.pyplot as plt

Body1 = Body(name = "Body1", 
           mass = 1e22, 
           position = 1e5*np.array([10,0,0]),
           velocity = 1e2*np.array([0,3,-3]),
           )

Body2 = Body(name = "Body2", 
           mass = 1e22, 
           position = 1e5*np.array([0,10,0]),
           velocity = 1e2*np.array([3,-3,0]),
           )

Body3 = Body(name = "Body3", 
           mass = 1e22, 
           position = 1e5*np.array([0,0,10]),
           velocity = 1e2*np.array([0,3,3]),
           )


#creating a blank window for the animation
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

#creating an animation function
def func(num, data, line):
    line.set_data(data[:2, :num]) #this draws a line from one point to another
    line.set_3d_properties(data[2, :num])

bodies = [Body1,Body2,Body3]
position_data = []


for i in range(len(bodies)):
    position_data.append([i])


t = 0
dt = 1

while t < 10000:
    for index in range(len(bodies)):
        position_data[index].append((bodies[index].position[0],bodies[index].position[1],bodies[index].position[2]))
    for body in bodies:
        body.update_Bodies_acceleration(bodies)
        body.update_Verlet(dt)
    t += dt

print(position_data[0])

x = []
for body in position_data:
    x.append(body[0][0])
    
print(x)
"""
x1 = []
y1 = []
z1 = []
for index in range(len(body)):
    x1.append(body[index][0])
    y1.append(body[index][1])
    z1.append(body[index][2])
    
x2 = []
y2 = []
z2 = []
for index in range(len(body)):
    x2.append(body[index][0])
    y2.append(body[index][1])
    z2.append(body[index][2])

x3 = []
y3 = []
z3 = []
for index in range(len(body)):
    x3.append(body[index][0])
    y3.append(body[index][1])
    z3.append(body[index][2]) """

""" ax.set_xlabel('x')
#ax.set_xlim3d([-5e11, 5e11])
ax.set_ylabel('y')
#ax.set_ylim3d([-5e11,5e11])
ax.set_zlabel('z')
#ax.set_zlim3d([-5e11,5e11])
ax.set_aspect('equal')
plt.show() """
