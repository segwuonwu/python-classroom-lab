# More Classes and OOP in Python
Use your knowledge of Python Classes to create a homework tracker!

Create your classes in the provided `classroom.py` file.

## Exercise: Write the following classes
Let's practice writing classes with useful functionalities

* Create an **Assignment** class
  * Assignments have `name`, `github_url`, `completed`, and `grade` properties
  * `completed`'s initial value should be set to `False`
  * `grade`'s initial value should be set to `None`
  * Assignments have a `mark_done` method that take in the grade as an argument, and sets `grade` and `completed`

* Create a **Student** class
  * Students have `name`, `pending_homeworks` and `completed_homeworks` properties
  * Students have a `assign_homework` method
  * Students have a `complete_homework` method 
  * Students have a `print_outstanding_homeworks` method
  * The `assign_homework` method takes in the name of the assignment as a string and adds a new `Assignment` instance to their `pending_homeworks`
  * The `complete_homework` method takes in the name of the homework, and the grade as an argument. It finds the specified homework in the `pending_homeworks` list and calls it's `mark_done` method. The method removes the `Assignment` from `pending_homeworks` and adds it to `completed_homeworks` 
    * Returns `True` if assignment was found and modified, `False` if not found
  * `print_outstanding_homeworks` prints out the name of each of the `pending_homeworks`


* Create a **SeiClass** class
  * SeiClass has `name`, and `students` properties
  * SeiClass has an `add_student` method that takes in a `Student` object
  * SeiClass has an `assign_homework` method that takes in an `Assignment` object and assigns that assignment to every student
  * BONUS - What would need to be changed in our classes to facilitate a `print_avg_grade` function? Implement it!

    
Sample Input:
```python
henry = Student('Henry')
sarah = Student('Sarah')
mike = Student('Mike')

sei26 = SeiClass('sei26')
sei26.add_student(henry)
sei26.add_student(sarah)
sei26.add_student(mike)

assignment1 = Assignment('Bounty Hunters', 'https://github.com/WDI-SEA/mongoose-practice')

sei26.assign_homework(assignment1)

henry.complete_homework('Bounty Hunters', 98)
sarah.complete_homework('Bounty Hunters', 95)

henry.print_outstanding_homeworks()
sarah.print_outstanding_homeworks()
mike.print_outstanding_homeworks()

```

Sample Output
```
Henry has no outstanding homeworks!
Sarah has no outstanding homeworks!
Mike still needs to turn in: Bounty Hunters
```