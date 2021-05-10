from datetime import datetime, date

from django import forms
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


def min_length_3_validator(value):
    if len(value) < 2:
        raise forms.ValidationError('최소 두글자 이상을 입력해 주세요!')


def past_date_validator(value):
    print(value, date.today())
    if value > date.today():
        raise forms.ValidationError('오늘 날짜 이후는 선택할 수 없어요!')


class Legs(models.Model):
    PEOPLE, CAT, DOG, ANOTHER = (
        '휴먼', '애옹쓰', '멍뭉이', '?!?!'
    )
    LEGS_BIG_TYPE_CHOICES = (
        (PEOPLE, _('휴먼')),
        (CAT, _('애옹쓰')),
        (DOG, _('멍뭉이')),
        (ANOTHER, _('?!?!')),
    )

    legs_type = models.CharField(verbose_name=_('종류'), choices=LEGS_BIG_TYPE_CHOICES,
                                 max_length=10, default=PEOPLE)
    legs_sub1_type = models.CharField(verbose_name=_('서브1 분류'), max_length=100, default='한국땅')
    legs_sub2_type = models.CharField(verbose_name=_('서브2 분류'), max_length=100, default='대구병원')

    class Meta:
        verbose_name = _("종족")
        verbose_name_plural = _("종족 목록")
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.legs_type} - {self.legs_sub1_type} - {self.legs_sub2_type}'


class Member(models.Model):
    member_legs = models.ForeignKey(Legs, on_delete=models.CASCADE, verbose_name=_('종족'))
    member_name = models.CharField(unique=True, max_length=32, verbose_name=_('이름'),
                                   validators=[min_length_3_validator])
    member_gender = models.CharField(max_length=10, blank=False, verbose_name=_('성별'))
    member_birthday = models.DateField(verbose_name=_('생년월일'), default=timezone.now, blank=False,
                                       validators=[past_date_validator])
    member_description = models.TextField(verbose_name=_("소개"), max_length=1000, blank=False)
    member_regular = models.BooleanField(_('정규 구성원 여부'), default=False)
    member_feature = models.TextField(_('특색'), blank=True, max_length=5000)
    member_neuter = models.BooleanField(_('중성화여부'), default=False)
    member_color = models.CharField(verbose_name=_("고유 색깔"), max_length=100, blank=True)
    member_language = models.CharField(verbose_name=_("사용하는 언어"), max_length=1000, blank=True)
    member_sleep_time = models.FloatField(verbose_name=_('수면시간'), default=18.5)
    member_talent = models.TextField(_('재능 소개'), blank=True, max_length=5000)
    member_img_name = models.CharField(_('대표이미지 파일명'), blank=True, max_length=30)

    class Meta:
        verbose_name = _("구성원")
        verbose_name_plural = _("구성원 목록")
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.member_name}'

    def get_absolute_url(self):
        return reverse('member:member_detail', args=[self.id])
