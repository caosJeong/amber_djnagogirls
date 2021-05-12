from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django import forms

from members.models import Member


def future_date_validator(value):
    print(value, date.today())
    if value < date.today():
        raise forms.ValidationError('오늘 날짜 이전은 선택할 수 없어요!')


class Todo(models.Model):
    PLAN, ING, DONE, PUTOFF, RUN = (
        '계획', '수행중', '할일완료', '미루기', '도망가기'
    )
    PROCESS_CHOICES = (
        (PLAN, _('계획단계')),
        (ING, _('수행중')),
        (DONE, _('할일완료')),
        (PUTOFF, _('미루기')),
        (RUN, _('도망가기')),
    )

    todo_title = models.CharField(max_length=100, verbose_name=_('할일 제목'))
    todo_content = models.TextField(max_length=100, verbose_name=_('할일 내용'), blank=True)
    todo_deadline_date = models.DateField(verbose_name=_('할일 마감 날짜'), default=timezone.now, blank=True,
                                          validators=[future_date_validator])
    todo_assign = models.ManyToManyField(Member, verbose_name=_('할일 수행자'), related_name='assign')
    todo_watcher = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name=_('감시자'), blank=True,
                                     related_name='watcher')
    todo_progressing = models.CharField(verbose_name=_('진행 상태'), choices=PROCESS_CHOICES,
                                        max_length=10, default=PLAN)
    todo_reject_text = models.CharField(max_length=100, verbose_name=_('할일 거절 사유'), blank=True)

    class Meta:
        verbose_name = _("구성원 할일")
        verbose_name_plural = _("구성원 할일 목록")
        ordering = ('-todo_deadline_date',)

    def __str__(self):
        return f'{self.todo_title}'
