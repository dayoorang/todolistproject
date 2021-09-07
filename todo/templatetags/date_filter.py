from datetime import datetime,timedelta
from django import template
from django.utils import timezone

from django.utils.timesince import timesince

register = template.Library()

@register.filter
def date(value):
    now = timezone.now()
    # now = datetime.today()
    difference = now - value

    try:
        difference = now - value
    except:
        return value


    # return difference
    if difference <= timedelta(minutes=1):
        return '방금 전'
    # return '%(time)s 전' % {'time': timesince(value)}
    elif ',' not in str(difference):
        return 'Today'

    return str(difference).split(',')[0].replace('days','일전')