from Body_Class import Body
import numpy as np
import matplotlib.pyplot as plt

y0 = 0
vy0 = 1000
vx0 = 1000

test_particle = Body('Particle1', 1, np.array([0,y0,0]), np.array([vx0,vy0,0]))

y_pos0 = []
x_pos0 = []
y_pos1 = []
x_pos1 = []

y_error = []

t_end = 100
dt = 1

t_list = []
t = 0

test_particle.uniform_field()

while t < t_end:

    y = y0 + vy0*t + 0.5*Body.g*t**2
    x = vx0*t
    y_pos1.append(test_particle.position[1])
    x_pos1.append(test_particle.position[0])

    ydiff = test_particle.position[1] - y
    y_error.append(ydiff)

    y_pos0.append(y)
    x_pos0.append(x)

    test_particle.update_Euler(dt)

    t_list.append(t)
    t += dt


plt.plot(x_pos0, y_pos0, label = 'true')
plt.plot(x_pos1, y_pos1, label = 'approx')
#plt.plot(t_list, y_error, label = f'error for dt = {dt}')
plt.legend()
plt.show()