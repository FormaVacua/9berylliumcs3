# ACTIVITY 1
//Instruction:
//For each situation below, decide whether the attribute should be public, protected, or private,
//then write the correct Python statement to declare the attribute inside the __init__()
//constructor method. Do these on your notebook.

1. A GameCharacter class has a username that can be displayed and accessed by anyone.
     - Public
2. A BankAccount class has a balance that should NOT be accessed directly outside the
class.
     - Private
3. A Vehicle class has an engineCode that should only be accessed within the class and its
subclasses.
     - Protected
5. A Student class has a schoolName that is safe for everyone to view and modify.
     - Public
  
7. A VotingSystem class has a voterID that must be hidden for security reasons.
     - Private
# ACTIVITY 2
//Question:
// How does using @property make your code easier to read compared to using traditional get_ and set_ methods?
- From experience, the @property allows the code to be easily readable if the @property decorator is understood as a separate method on its own. The property can be understood as the one that can be modified and the one that can verify new values. Compared to other methods outside OOP, from the activity given, it's shorter and more efficient.
