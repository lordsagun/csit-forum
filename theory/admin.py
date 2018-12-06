from django.contrib import admin
from .models import OldQuestion,Syllabus,Note,Solution,Result,Semester
# Register your models here.
admin.site.register(OldQuestion)
admin.site.register(Syllabus)
admin.site.register(Note)
admin.site.register(Solution)
admin.site.register(Result)
admin.site.register(Semester)
