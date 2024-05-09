import os
import csv
import uuid
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction
from school_app.models import School, Class, AssessmentArea, Student, Answer, Award, Subject, Summary

class Command(BaseCommand):
    help = 'Import data from CSV files into the database'

    def handle(self, *args, **kwargs):
        data_directory = os.path.join(settings.BASE_DIR, 'data')
        csv_files = [
            os.path.join(data_directory, 'ganison_dataset_1.csv'),
            os.path.join(data_directory, 'ganison_dataset_2.csv'),
            os.path.join(data_directory, 'ganison_dataset_3.csv'),
            os.path.join(data_directory, 'ganison_dataset_4.csv'),
            os.path.join(data_directory, 'ganison_dataset_5.csv'),
            os.path.join(data_directory, 'ganison_dataset_6.csv')
        ]

        for csv_file in csv_files:
            print(f"Processing file: {csv_file}")
            self.process_csv_file(csv_file)
            print(f"Completed processing file: {csv_file}")

        print("Data import completed!")

    def process_csv_file(self, file_path):
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Print the first three lines of each CSV file
            print("First three lines of the CSV file:")
            for i, row in enumerate(reader):
                if i < 3:
                    print(row)
                
                data = self.process_row(row)
                if data:
                    with transaction.atomic():
                        Summary.objects.create(**data)
                
    def process_row(self, row):
        try:
            school_name = row.get('school_name')
            school = School.objects.filter(name=school_name).first()
            if not school:
                school = School(id=uuid.uuid4(), name=school_name)
                school.save()

            class_name = row.get('Class')
            cls = Class.objects.filter(name=class_name).first()
            if not cls:
                cls = Class(id=uuid.uuid4(), name=class_name)
                cls.save()

            assessment_area_name = row.get('Assessment Areas')
            assessment_area = AssessmentArea.objects.filter(name=assessment_area_name).first()
            if not assessment_area:
                assessment_area = AssessmentArea(id=uuid.uuid4(), name=assessment_area_name)
                assessment_area.save()

            first_name = row.get('First Name')
            last_name = row.get('Last Name')
            fullname = f"{first_name} {last_name}"
            student = Student.objects.filter(fullname=fullname).first()
            if not student:
                student = Student(id=uuid.uuid4(), fullname=fullname)
                student.save()

            subject_name = row.get('Subject')
            subject_score = float(row.get('student_score', 0))
            subject = Subject.objects.filter(name=subject_name, score=subject_score).first()
            if not subject:
                subject = Subject(id=uuid.uuid4(), name=subject_name, score=subject_score)
                subject.save()

            answer_text = row.get('Answers')
            question_number = row.get('Question Number')
            answer_id = f"{question_number}-{uuid.uuid4()}"
            answer = Answer.objects.filter(id=answer_id).first()
            if not answer:
                answer = Answer(id=answer_id, answer=answer_text)
                answer.save()

            award_name = row.get('award')
            award = Award.objects.filter(name=award_name).first()
            if not award:
                award = Award(id=uuid.uuid4(), name=award_name)
                award.save()

            summary_data = {
                'school_id': school.id,
                'class_id': cls.id,
                'student_id': student.id,
                'subject_id': subject.id,
                'assessment_area_id': assessment_area.id,
                'award_id': award.id,
                'year_level_name': row.get('Year Level'),
                'sydney_participant': int(row.get('sydney_participant', 0)),
                'sydney_percentile': float(row.get('sydney_percentile', 0)),
                'sydney_average_score': float(row.get('sydney_average_score', 0)),
                'student_score': float(row.get('student_score', 0)),
                'student_total_assessed': float(row.get('student_total_assessed', 0)),
                'student_area_assessed_score': float(row.get('student_area_assessed_score', 0)),
                'total_area_assessed_score': float(row.get('total_area_assessed_score', 0)),
                'participant': row.get('participant', ''),
                'correct_answer_percentage_per_class': float(row.get('correct_answer_percentage_per_class', 0)),
                'average_score': float(row.get('average_score', 0)),
                'school_percentile': int(row.get('school_percentile', 0)),
                'correct_answer': row.get('Correct Answers', ''),
                'category_id': uuid.uuid4().int,
                'correct_answer_id': answer.id,
            }

            return summary_data
        
        except Exception as e:
            print(f"An error occurred while processing row: {e}")
            return None
