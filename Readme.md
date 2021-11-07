# **Elevator Scheduling**
![Builds](https://github.com/project-chip/connectedhomeip/workflows/Builds/badge.svg)
#### A part of university assignment 


</br>



## Project Overview
Giving a Bulding with elevators and a set of calls , the program needs to allocate the calls to the elevators 
in a way that minimizes the avrage waiting time.



### What is needed 
- allocate calls algorithm 
- elevator movement
- elevator data structure 
- use json files 
- main function to spin the program 

</br>





## How to RUN 
In the cmd : 
</br>
`python Ex1.py B1.json C2.csv out.csv`
</br>

C2 - Elevator calls 
B1 - Building


## Built With

* Pycharm 
* Python

</br>



## Algorithm Breakdown


### Allocation algorithm
- Picking the elevator with the best time to get to the given call , taking in considiration the elevator current calls 
- For testing -> Round Robin (circular allocation)

</br>

### Elevator scheduling
Idea : Keep moving in one direction until possible, then reverse direction 



</br>
</br>
<img src="https://www.engineering.columbia.edu/files/seas/styles/816x460/public/content/cs_image/2021/05/newtemplate.jpg?itok=PMitgeiw" width="600" height="400" />


</br>
</br>

## Authors

* **Tarik Husin**  - linkedin -> https://www.linkedin.com/in/tarik-husin-706754184/
* **Wisam Kabha**  - github -> https://github.com/Wissam111

