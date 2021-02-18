from django.contrib import admin
from .models import Question, TrueAnswer, WrongAnswer


class ReviewTrueAnswer(admin.StackedInline):
    model = TrueAnswer
    extra = 1


class ReviewWrongAnswer(admin.StackedInline):
    model = WrongAnswer
    extra = 1


@admin.register(Question)
class QustionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    inlines = [ReviewTrueAnswer, ReviewWrongAnswer]


@admin.register(WrongAnswer,TrueAnswer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'question')
    list_display_links = ('title',)
    list_filter = ('question',)

