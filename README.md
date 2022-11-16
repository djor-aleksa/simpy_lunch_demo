# SimPy Lunchtime Demo
SimPy library used to model the lunchtime process in the office. Simplified demo purpose.

Scenario: Every day, a lunch is organized in the hub for all present people around 1 PM. There are in total 30 people present in hub in the implemented scenario. The number of seating places is limited, as well as the number of functioning dishwashers. 
Every person:
1. Decides to have a lunch with certain delay after the lunch has started;
2. Enters the kitchen, picks the dish and goes to the table, trying to find unoccupied spot;
3. If all the spots are occupied, one has to wait for someone to finish eating;
4. Once the seat is taken comes a random time spent consumming the lunch and socializing with others;
5. After eating phase is done, the person has to pick up the tableware, do the prewash and put it into the dishwasher;
6. If none of the dishwashers is currently available, the person has to wait for it to become available;
7. After the tableware is sorted properly in the dishwaser, the simulated process for an individual is completed.

The goal of the simulation is to measure what is the **Average Waiting Time** during lunchtime with given input parameters:
- **Table Capacity**
- **Number of Functioning Dishwashers**
- **Number of People in Hub**

This demo is part of the internal Python community presentation in Symphony, Niš hub. 

Feel free to copy and use any part of the demo.
