from django.db import models

# class Adhar(models.Model):
#     adhar_no = models.IntegerField()
#     created_date = models.DateField(auto_now=True)
#     created_by = models.CharField(max_length=50)

#     def __str__(self):
#         return str(self.adhar_no)


# class Student(models.Model):
#     name = models.CharField(max_length=150)
#     email = models.EmailField()
#     contact = models.IntegerField()
#     adhar_no = models.OneToOneField(Adhar, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


# class Student(models.Model):
#  name = models.CharField(max_length=50)
#  father_name = models.CharField(max_length=50, default="Not Provided")
#  mobile = models.CharField(max_length=10)
#  email = models.EmailField(unique=True)
#  course = models.CharField(max_length=50 ,default="Not Assigned")

#  def __str__(self):
#    return self.name
 

# class UniversityRoll(models.Model):
#  roll_no = models.CharField(max_length=20, unique=True)
#  allotted_date = models.DateField(auto_now_add=True)
#  student_name = models.OneToOneField(Student, on_delete=models.CASCADE)


#  def __str__(self):
#     return f"{self.roll_no} {self.student_name.name}"


class Department(models.Model):
 d_name = models.CharField(max_length=50)
 d_disc = models.TextField()


 def __str__(self):
     return self.d_name
 


class Employee(models.Model):
 name = models.CharField(max_length=50)
 city = models.CharField(max_length=50)
 mobile = models.CharField(max_length=10)
 email = models.EmailField(unique=True)
 course = models.CharField(max_length=50)
 dep_data = models.ForeignKey(Department,on_delete=models.CASCADE)


 def __str__(self):
    return self.name





