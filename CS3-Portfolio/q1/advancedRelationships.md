# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description: 
As of prior to creating this activity, the system has the "main" class, Video Games, where many Characters are stored. The Video Game class contains general information regarding the game's genre, target audience and creators, as well as what operations initiate it. In the Character class, general information of the character's identity is stored too. Attributes such as the character's name, role and species, and abilities.
## Inheritance Relationship
Parent: Entity
Child: Characters
Explanation: Entities in the game concern status of the character. This includes the character's HP, EXP, and how much damage they respectively receive.
## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Aggregation
Explanation: The characters were created independently from the game class. This ensures the existence of the characters even if game data is erased. 
## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](images/advancedTestRun.png)
## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers: This activity alone was very time-consuming, but, in a way, as much as it was frustrating, it was enjoyable seeing lines of code slowly stitching together. The classes I chose for this activity were certainly bigger than what I could handle but, I managed to find some doable parts even though it sometimes defies video game knowledge. 
