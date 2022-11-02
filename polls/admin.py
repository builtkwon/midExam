from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    #필드 순서 변경
    #fields = ['pub_date','question_text']
    fieldsets=[
        ('Question Statement', {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
    ]

    #Choice 모델 클래스 같이 보기
    inlines = [ChoiceInline]

    #레코드 리스트 컬럼 지정
    list_display = ('question_text','pub_date','was_published_recently')

    #필터 사이드바
    list_filter = ['pub_date']

    #검색박스
    search_fields = ['question_text']



admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)

