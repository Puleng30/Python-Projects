
'''1. Add another method in the Course class that prints the head office location: Woodstock, Cape Town'''
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office_location = "Woodstock, Cape Town"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def head_office(self):
        print("Our head office location is:", self.head_office_location)

'''2. Create a subclass of the Course class named OOPCourse'''
class OOPCourse(Course):
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"
        self.course_id = "#12345"
    
    '''3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse".
      4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
   5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345'''
    def trainer_details(self):
        print("This course is about", self.description, "and the trainer is", self.trainer)
    def show_course_id(self):
        print("Course ID:", self.course_id)


'''6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal'''
course_1 = OOPCourse()

course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()


