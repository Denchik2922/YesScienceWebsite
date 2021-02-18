from django.db import models


class Question(models.Model):
    title = models.CharField('Вопрос', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class TrueAnswer(models.Model):
    title = models.CharField('Верный ответ', max_length=70)
    question = models.ForeignKey(Question, verbose_name='Вопрос', on_delete=models.CASCADE)

    def __str__(self):
        return 'Верный ответ на вопрос "' + str(self.question) + '"'

    class Meta:
        verbose_name = 'Верный ответ'
        verbose_name_plural = 'Верные ответы'


class WrongAnswer(models.Model):
    title = models.CharField('Неверный ответ', max_length=70)
    question = models.ForeignKey(Question, verbose_name='Вопрос', on_delete=models.CASCADE)

    def __str__(self):
        return 'Неверый ответ на вопрос "' + str(self.question) + '"'

    class Meta:
        verbose_name = 'Неверный ответ'
        verbose_name_plural = 'Неверные ответы'
