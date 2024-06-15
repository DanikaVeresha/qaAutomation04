Let's imagine that we have such an application on the phone and a person
wants to understand what is the most convenient time for him to get to the desired point.

Thus, a person sets a starting point and an ending point, and the application gives him the result!

The essence of the project is that there are three objects: a train, a car and an airplane.
Each object has the same methods except the static method `calculate_speed()`
which randomly receives the speed of an object and returns it.

There are 2 options for launching the application:
1 -> This is via facade.py file
2 -> This is via the factory.py file

Description of files:
1 -> In the facade.py file there is a Facade class which accepts a starting point and an ending point
and depending on these points, creates objects and calls methods and shows the constructed
route with speed and travel time

2 -> In the factory.py file there is a class Factory which accepts a starting point and an ending
point and depending on these points, creates objects and calls methods and shows the constructed
route with speed and travel time

At my discretion, it was final to do and accept that factory.py is the main file.
Since the factory.py and facade.py files are independent of each other, they are not integrated
in this implementation of the application.


the factory.py file is the main one which pulls up all other files (airplane.py, car.py, train.py)
and depending on the parameters of the starting point and ending point, creates objects and calls
methods showing the constructed route with speed and travel time, depending on the class of the
object

If this is a train, then its speed will vary -> 140 - 200 km/h
Car -> 60 -120 km/h,
Airplane -> 800 - 1000 km/h
Travel time also changes accordingly.

I did it according to the example from the lectures (design patterns) -> partially Façade and Factory

You can run the program through the factory.py file and also through the facade.py file
and it will work either way - my personal initiative was to mix two types of patterns in one project
facade method files(airplane.py, car.py, train.py) and factory method files(factory.py)

Distance between points: real calculated using the Governors formula
Travel time is calculated using the formula -> distance/speed
Random only the speed of the object, but the start and end speed is taken from Google in
accordance with real data