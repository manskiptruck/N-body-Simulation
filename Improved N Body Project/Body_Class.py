import numpy as np
import copy


class Body:

    """
    A class that stores the parameters of a particle/body such as position, velocity and acceleration.

    The methods of this class act on these parameters and determine how the parameters change through
    numerical integration.

    For example:: 
    
        Sol = Body( name = "Sol", 
                    mass = 198e24, 
                    position = 1e3*np.array([-1.173e6,-4.607e5,3.128e4]),
                    velocity = 1e3*np.array([8.736e-3,-1.186e-2,-8.588e-5]),)

     
    Parameters
    ----------
    name : str
        The name of the body
    mass : float 
        The mass of the body
    position : ndarray
        The position of the body
    velocity : ndarray
        The velocity of the body
    acceleration : ndarray
        The acceleration of the body

    """

    M_Earth = 5.974e24
    G = 6.67408E-11
    g = -9.81

    def __init__(self, 
                 name = "", 
                 mass = 0.0, 
                 position = np.array([0.0,0.0,0.0]), 
                 velocity = np.array([0.0,0.0,0.0]), 
                 acceleration = np.array([0.0,0.0,0.0]),
                 ):
        
        self.name = name
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        
        
    def update_Euler(self, dt):
        """
        Calculate the position and velocity of a body after a given time step using the Euler method.

        Parameters:
        ----------
        dt : float
            The value of the time step

        """

        self.position = self.position + self.velocity * dt
        self.velocity = self.velocity + self.acceleration * dt

    def update_EulerCromer(self, dt):
        
        self.velocity = self.velocity + self.acceleration * dt
        self.position = self.position + self.velocity * dt

    def update_Verlet(self, dt):
        """
        Calculate the position and velocity of a body after a given time step using the Verlet method.

        Parameters:
        ----------
        dt : float
            The value of the time step

        """

        updateobjects = copy.deepcopy(self)
        updateobjects.update_Euler(dt)

        self.position = self.position + self.velocity*dt + 0.5*self.acceleration*dt**2
        self.velocity = self.velocity + 0.5*(updateobjects.acceleration + self.acceleration)*dt

    def uniform_field(self):
        """
        Calculates the linear gravitational field strength close to the Earth's surface.
        """

        g = -9.81
        self.acceleration = np.array([0,g,0])

    def update_Earth_acceleration(self):
        """
        Calculates the gravitational field strength of the Earth at a distance from the center.
        """

        r_vector = np.array(self.position)
        r = np.linalg.norm(r_vector)
        self.acceleration = -(self.G*self.M_Earth) * self.position / r**3
        self.force = self.acceleration / self.mass

    def update_Bodies_acceleration(self, bodies):
        """
        Calculates the Newtonian gravitational acceleration of one body due to every
        other body in the system at one moment in time.

        Parameters:
        ----------
        dt : float
            The value of the time step
        bodies : list 
            A list containing Body class instances as entries
        """

        acceleration = np.array([0.0,0.0,0.0])

        for body in bodies: #this loops through a list containing the instances of each Body class
            if self == body: #this prevents calculation of the position vector for the Body itself which would divide by 0
                continue
            r_vector = self.position - body.position #position vector pointing from one Body to another
            r_norm = np.linalg.norm(r_vector) #magnitude of the position vector
            acceleration += -Body.G*body.mass*r_vector / r_norm**3 #this will add each acceleration due to another Body
        self.acceleration = acceleration #this ensures that the Body in question has an attribute that equals its total acceleration due to every other Body

    def momentum(self, mass, velocity):
        """
        Calculates the momentum of a body at a moment in time.

        Parameters:
        ----------
        mass : float
            The mass of the body
        velocity : ndarray
            The velocity of the body

        Returns
        -------
        momentum : ndarray
            The momentum of the body
        """

        momentum = mass * velocity
        return momentum
    
    def ang_momentum(self, mass, position, velocity):

        """
        Calculates the angular momentum of a body at a moment in time.

        Parameters:
        ----------
        mass : float
            The mass of the body
        position : ndarray
            The position of the body
        velocity : ndarray
            The velocity of the body

        Returns
        -------
        angular_momentum : ndarray
            The angular momentum of the body
        """

        momentum = mass * velocity
        angular_momentum = np.cross(position, momentum)
        return angular_momentum