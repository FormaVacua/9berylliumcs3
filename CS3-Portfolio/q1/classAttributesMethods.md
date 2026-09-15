# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
## Design Revision
Describe any changes made to your original class.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Name | String | Public | |
| Genre | String | | |
| Company | String | | |
| Player Audience | String | | |
## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)
## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis - 
### Why did you make your chosen attribute private? 
 --The visual clutter of lines of code shouldn't be seen by the user. Not only because the code can be vulnerable and dissectable for replicas, but also because the code would distract the player.
### Which method changes the state of your object? 
--The method 'update' updates the version of the game.
### How did your two objects demonstrate that instances are independent? 
--Object 2 wasn't affected by the update in object 1.
### What is the difference between your class diagram and your object diagram? 
--The class diagram shows what comprises the class-- the attributes and methods. While the object diagram shows the blueprint class being used to create objects.

