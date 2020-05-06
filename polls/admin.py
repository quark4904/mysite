from django.contrib import admin
from .models import Question, Choice

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text'] # 필드 순서 변경
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        #('Date information', {'fields': ['pub_date']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] # Choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_date') # tuple : 불변, 딕셔너리의 key값으로 사용 가능, iteration을 도는 속도가 더 빠르다.
    list_filter = ['pub_date'] # list : 가변, 딕셔너리의 key값으로 사용 불가능
    search_fields = ('question_text', 'pub_date')

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {'fields': ['question']}),
        ('Choice Text', {'fields': ['choice_text']}),
        ('Votes', {'fields': ['votes']}),
    ]
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)