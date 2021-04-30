from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


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
        return '{} - {} - {}'.format(self.legs_type, self.legs_sub1_type, self.legs_sub2_type)


class Member(models.Model):
    member_legs = models.ForeignKey(Legs, on_delete=models.CASCADE, verbose_name=_('종족'))
    member_name = models.CharField(unique=True, max_length=32, verbose_name=_('이름'))
    member_gender = models.CharField(max_length=10, blank=True, verbose_name=_('성별'))
    member_birthday = models.DateField(default=timezone.now)
    member_description = models.TextField(verbose_name=_("소개"), max_length=1000, blank=True)
    member_regular = models.BooleanField(_('정규 구성원 여부'), default=False)
    member_feature = models.TextField(_('특색'), blank=True, max_length=5000)
    member_neuter = models.BooleanField(_('중성화여부'), default=False)
    member_color = models.CharField(verbose_name=_("고유 색깔"), max_length=100, blank=True)
    member_language = models.CharField(verbose_name=_("사용하는 언어"), max_length=1000, blank=True)
    member_sleep_time = models.FloatField(verbose_name=_('수면시간'), default=18.5)
    member_talent = models.TextField(_('재능 소개'), blank=True, max_length=5000)

    class Meta:
        verbose_name = _("구성원")
        verbose_name_plural = _("구성원 목록")
        ordering = ('-pk',)

    def __str__(self):
        return '{}'.format(self.member_name)
