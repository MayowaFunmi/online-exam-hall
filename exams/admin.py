from django.contrib import admin
from . models import Question, Score, Department, Subjects, StudentLevel, StudentClass, ExamRegistration, ExaminerExamRegistration, SubjectLike
# Register your models here.
admin.site.register(Question)
admin.site.register(Score)
admin.site.register(Department)
admin.site.register(Subjects)
admin.site.register(StudentClass)
admin.site.register(StudentLevel)
admin.site.register(ExamRegistration)
admin.site.register(ExaminerExamRegistration)
admin.site.register(SubjectLike)