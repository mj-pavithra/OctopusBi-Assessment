from django.shortcuts import render
from .models import School, Class, AssessmentArea, Student, Answer, Award, Subject, Summary

def data_view(request):
    # Fetch data from tables
    schools = School.objects.all()
    classes = Class.objects.all()
    assessment_areas = AssessmentArea.objects.all()
    students = Student.objects.all()
    answers = Answer.objects.all()
    awards = Award.objects.all()
    subjects = Subject.objects.all()
    summaries = Summary.objects.all()
    
    context = {
        'schools': schools,
        'classes': classes,
        'assessment_areas': assessment_areas,
        'students': students,
        'answers': answers,
        'awards': awards,
        'subjects': subjects,
        'summaries': summaries,
    }
    
    # Render the data in the template
    return render(request, 'school_app/data_view.html', context)
