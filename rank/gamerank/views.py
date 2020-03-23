from django.shortcuts import render
from django.http import HttpResponse
from gamerank.models import uprank
from django.db.models import Avg, Sum, Max, Min, Count

# Create your views here.


def upranka(request):
    if request.method == 'GET':
        return render(request, 'rank.html')
    else:
        uname = request.POST.get('username', '')
        ranks = request.POST.get('rank', '')
        try:
            user = uprank.objects.get(uname=uname)
            user.delete()
            upranks = uprank()
            upranks.uname = uname
            upranks.rank = ranks
            upranks.save()
        except:
            upranks = uprank()
            upranks.uname = uname
            upranks.rank = ranks
            upranks.save()
        return HttpResponse('上传分数成功！！！')


def get_query(request, sort1, sort2):
    sort1 = int(sort1)
    sort2 = int(sort2)
    stus = uprank.objects.all().order_by('-rank')[sort1: sort2]
    return render(request, 'query.html', context=locals())