# Don't need to import Body_Class since it's in Solar_System_Data
import numpy as np
import astropy.units as u
import matplotlib.pyplot as plt
from Solar_System_Data import Sol,Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune

"""
A python script to calculate the trajectories and physical properties of planets in the solar system.

In "Solar_System_Data", instances of the Body class were created where each instance has attributes relating 
to the initial conditions of each planet. To use the script, add the instance of each class to the "bodies" list. This
will store the initial conditions of every planet.

"""


bodies = [Sol,Mercury,Venus,Earth,Mars,Jupiter]

position_data = []
ang_momentum_body_data = []
ang_momentum_tot_data = []

integration_method = input("Input the integration method you would like to use, the options are\nVerlet\nEuler\nInput: ")
plot_method = input("Input what you would like to plot, the options are\nOrbits\nAngular Momentum\nTotal Angular Momentum\nInput: ")

fig = plt.figure(figsize = (8,8))
if plot_method == "orbits":
    ax = fig.add_subplot(projection='3d')

for i in range(len(bodies)):
    position_data.append([])
    ang_momentum_body_data.append([])

distance_units = {
    "m": 1,
    "km": u.m.to(u.km),
    "au": u.m.to(u.au)
}

if integration_method.lower() != "orbits":
    unit_input = input("Input the distance units you would like to use: ")

t = 0
t_end = 100000000
time = []
dt = 1000


while t < t_end:
    for index in range(len(bodies)):

        if plot_method == "orbits":
            position_data[index].append((distance_units.get(str(unit_input))*bodies[index].position[0],
                                        distance_units.get(str(unit_input))*bodies[index].position[1],
                                        distance_units.get(str(unit_input))*bodies[index].position[2]))
        elif plot_method == "angular momentum": # This is for plotting the angular momentum of each body
            ang_momentum_body_data[index].append((np.log(np.linalg.norm(
            bodies[index].ang_momentum(bodies[index].mass, bodies[index].position, bodies[index].velocity))), t))

    ang_momentum_tot = np.array([0.0,0.0,0.0])

    for body in bodies:
        
        if plot_method.lower() == "total angular momentum":
            ang_momentum = body.ang_momentum(body.mass, body.position, body.velocity)
            ang_momentum_tot += ang_momentum

        body.update_Bodies_acceleration(bodies)

        if integration_method.lower() == "verlet":
                body.update_Verlet(dt)
        elif integration_method.lower() == "euler":
                body.update_Euler(dt)

    if plot_method.lower() == "total angular momentum":
        ang_momentum_tot_data.append((np.linalg.norm(ang_momentum_tot), t))

    time.append(t)
    t += dt

"""
This takes the entries of each body after the simulation and plots it, this is the only way to do this
if we want it to plot the position data of the bodies successively.
"""

if plot_method == "orbits":
    BodyNumber = 0
    for body in position_data:
        x = []
        y = []
        z = []
        for index in range(len(body)):
            x.append(body[index][0])
            y.append(body[index][1])
            z.append(body[index][2])
        ax.plot3D(x, y, z, label = bodies[BodyNumber].name)
        ax.legend()
        BodyNumber += 1
    
    ax.set_xlabel('x')
    ax.set_xlim3d([-1.5*abs(np.max(distance_units.get(str(unit_input))*bodies[-1].position)), 
                   1.5*abs(np.max(distance_units.get(str(unit_input))*bodies[-1].position))])
    # This ensures that the coordinate limits encase the position of the furthest object
    # Provided that the bodies with the largest orbit are at the end of the list of bodies 
    ax.set_ylabel('y')
    ax.set_ylim3d([-1.5*abs(distance_units.get(str(unit_input))*np.max(bodies[-1].position)), 
                   1.5*abs(distance_units.get(str(unit_input))*np.max(bodies[-1].position))])
    ax.set_zlabel('z')
    ax.set_zlim3d([-1.5*abs(distance_units.get(str(unit_input))*np.max(bodies[-1].position)), 
                   1.5*abs(distance_units.get(str(unit_input))*np.max(bodies[-1].position))])
    ax.set_aspect('equal')


# This plot is for the angular momentum of each body after each time step
elif plot_method.lower() == "angular momentum":
    BodyNumber = 0
    for body_info in ang_momentum_body_data:
        ang = []
        time = []
        for index in range(len(body_info)):
            ang.append(body_info[index][0])
            time.append(body_info[index][1])
        plt.plot(time, ang, label = bodies[BodyNumber].name)
        plt.legend(loc = 'upper right')
        BodyNumber += 1
    plt.xlabel('$t$', fontsize = 12)
    plt.ylabel('$log(L)$', fontsize = 12)
    plt.title('Log plot of the angular momentum of each body')


elif plot_method.lower() == "total angular momentum":

    ang_momentum = []
    time = []

    for index in range(len(ang_momentum_tot_data)):
        ang_momentum.append((ang_momentum_tot_data[index][0]-ang_momentum_tot_data[0][0])/ang_momentum_tot_data[0][0])
        time.append(ang_momentum_tot_data[index][1])

    plt.plot(time, ang_momentum)
    plt.xlabel("$t$", fontsize = 12)
    plt.ylabel("$L$", fontsize = 12)
    plt.title('Fractional change in total angular momentum')

plt.show()