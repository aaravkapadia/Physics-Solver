# Physics-Solver
This project uses an object-oriented approach to solve physics problems in the realm of mechanics, specifically vector problems, work probelms, problems relating to newtons laws, and problems to find friction.
How it works:

Vector Class-Based on a given list that corresponds to the components of a vector, where i, j, and k are the first, second, and third index of a list, the magnitude of the vector, angle of the vector with respect to the origin can be calculated, and if given a scalar as well, the vector can be scaled. Further, if given 2 vectors, the dot product of the vectors, angle between the vectors, and the sum of the vectors can be calculated. Furthermore, the class has different functionalities, which are converting an angle to radians, asking the user for an angle, and asking the user for the vector itself.

Force class- This class inherets from the vector class in order to use the vector class' useful function. It can calculate the force(given mass and an acceleration vector), mass(given a force vector and an acceleration vector), acceleration(given a force vector and mass), or the normal force(given the mass and given theta- the angle of elevation. It can return the values for acceleration an force in both vector or magnitude format depending on user input. The Normal Force is always given by 1 number, as it is always in the y direction, so putting it in a vector overcomplicates the program. 

Friction class- The reason for the creation of an entire seperate friction class is because it correlates to a seperate chapter in the physics course. Its 1 function calculates the force of friction given the mass of the object and the angle of elevation.


