from django.db import models

class School(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  
    name = models.CharField(max_length=100)

class Class(models.Model):
    id = models.CharField(max_length=50, primary_key=True)    
    name = models.CharField(max_length=100)

class AssessmentArea(models.Model):
    id = models.CharField(max_length=50, primary_key=True)    
    name = models.CharField(max_length=100)

class Student(models.Model):
    id = models.CharField(max_length=50, primary_key=True)    
    fullname = models.CharField(max_length=100)

class Answer(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  
    answer = models.CharField(max_length=500)

class Award(models.Model):
    id = models.CharField(max_length=50, primary_key=True)    
    name = models.CharField(max_length=100)

class Subject(models.Model):
    id = models.CharField(max_length=50, primary_key=True)    
    name = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=5, decimal_places=2)

class Summary(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    assessment_area_id = models.ForeignKey(AssessmentArea, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    award_id = models.ForeignKey(Award, on_delete=models.CASCADE)
    year_level_name = models.CharField(max_length=100)
    sydney_participant = models.IntegerField(default=0)
    sydney_percentile = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    sydney_average_score = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    student_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    student_total_assessed = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    student_area_assessed_score = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_area_assessed_score = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    participant = models.CharField(max_length=100, default='')
    correct_answer_percentage_per_class = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    average_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    school_percentile = models.IntegerField(default=0)
    correct_answer = models.CharField(max_length=3, default='')
    category_id = models.CharField(max_length=50, default='0')
    correct_answer_id = models.CharField(max_length=50, default='0')

