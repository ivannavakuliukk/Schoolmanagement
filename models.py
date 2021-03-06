# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Class(models.Model):
    class_id = models.AutoField(db_column='class_Id', primary_key=True)  # Field name made lowercase.
    teacher_id = models.IntegerField(blank=True, null=True)
    number_of_students = models.IntegerField()
    cabinet = models.IntegerField()
    class_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'class'


class Lessons(models.Model):
    lesson_id = models.AutoField(db_column='lesson_Id', primary_key=True)  # Field name made lowercase.
    lesson_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'lessons'


class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=50)
    pay = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'position'


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    week_day = models.CharField(max_length=30)
    cabinet = models.IntegerField()
    lesson_id = models.IntegerField(db_column='lesson_Id', blank=True, null=True)  # Field name made lowercase.
    teacher_id = models.IntegerField(blank=True, null=True)
    class_id = models.IntegerField(blank=True, null=True)
    lesson_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'schedule'


class School(models.Model):
    school_id = models.AutoField(db_column='school_Id', primary_key=True)  # Field name made lowercase.
    teacher_id = models.IntegerField(db_column='teacher_Id', blank=True, null=True)  # Field name made lowercase.
    number_of_classes = models.IntegerField()
    adress = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)
    email_adress = models.CharField(max_length=50)
    study_level = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'school'


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    phone_number = models.IntegerField(blank=True, null=True)
    school_id = models.IntegerField(db_column='school_Id', blank=True, null=True)  # Field name made lowercase.
    email_adress = models.CharField(max_length=30, blank=True, null=True)
    adress = models.CharField(max_length=30, blank=True, null=True)
    birthday_date = models.CharField(max_length=30, blank=True, null=True)
    student_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Teacher(models.Model):
    teacher_id = models.AutoField(db_column='teacher_Id', primary_key=True)  # Field name made lowercase.
    teacher_name = models.CharField(max_length=50)
    lesson_id = models.IntegerField(db_column='lesson_Id', blank=True, null=True)  # Field name made lowercase.
    phone_number = models.IntegerField()
    email_adress = models.CharField(max_length=50)
    experience = models.IntegerField()
    position = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'teacher'
