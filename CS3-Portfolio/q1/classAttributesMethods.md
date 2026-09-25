# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
## Design Revision
Describe any changes made to your original class.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Name | String | Public | The game name must be visible to the user for it to be found and identified. |
| Genre | String | Public | The genre helps users know what content is in the game |
| Company | String | Public | Visibility of this attribute allows players to know about what other games are similar or who created the game. |
| Player Audience | String | Public | This allows players to get to know their demographic |
| Debug | String | Private | A player doesn't need to see the lines of code that may disrupt their game. |
## Updated UML Class Diagram
![Class Diagram](q1/images/classDiagramSG5.jpg)
## Python Implementation
![View Python Source](q1/classImplementation.py)
## Test Run
![Test Run](q1/images/classTestRun.png)
## Object Diagram
![Object Diagram](q1/images/objectDiagram(1).jpg)

## Analysis - 
### Why did you make your chosen attribute private? 
 --The visual clutter of lines of code shouldn't be seen by the user. Not only because the code can be vulnerable and dissectable for replicas, but also because the code would distract the player.
### Which method changes the state of your object? 
--The method 'update' updates the version of the game.
### How did your two objects demonstrate that instances are independent? 
--Object 2 wasn't affected by the update in object 1.
### What is the difference between your class diagram and your object diagram? 
--The class diagram shows what comprises the class-- the attributes and methods. While the object diagram shows the blueprint class being used to create objects.

