from django.db import models

# Create your models here.
#can add group here also
class question(models.Model):
    #id is set automatically
    question_url=models.CharField(max_length=512)
    question_title=models.CharField(max_length=64)
    discussions=models.CharField(blank=True,max_length=512)
    def __str__(self):
        return f"question name : {self.question_title}"

class students(models.Model):
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    student_solved_questions=models.ManyToManyField(question,blank=True,related_name="solved_by")

    def __str__(self):
        return f"{self.first} {self.last}"