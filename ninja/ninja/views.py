from django.shortcuts import HttpResponse,render,redirect
from article.models import arti
from django.contrib.auth import logout
import datetime
from django.contrib import messages
from django.utils.timezone import now
import  datetime
day=datetime.date.today()
yestarday=day-datetime.timedelta(days=1)

print(day)
def index(request):
    params=arti.objects.filter(datee=day).order_by('timeStamp').reverse()
    if params.count()==0:
        no1=''
        no="There is no article published today. so displaying old articles"
        params=arti.objects.filter(datee=yestarday).order_by('timeStamp').reverse()
        if params.count()==0:
            no1=''

            print('all articles are null')
            server=arti(heading='built in exception',content='''
New Features Assignment expressions There is new syntax := that assigns values to variables as part of a larger expression. It is affectionately known as “the walrus operator” due to its resemblance to the eyes and tusks of a walrus. In t…
''',cUser=request.user)
            server.save()
            params=arti.objects.filter(datee=day).order_by('timeStamp').reverse()
            no1='server'

    else:
        no="Displaying today's articles"
        no1=''
    context={'params':params,'no':no,'no1':no1}
    return render(request,'index.html',context)

def readmore(request,id,slug):
    read=arti.objects.filter(sno=id)
    params={'params':read}
    return render(request,'readmore.html',params)

def search(request):
    if request.method=="GET":
        se=request.GET.get('search','')
        query1=arti.objects.filter(heading__icontains=se)
        query2=arti.objects.filter(content__icontains=se)
        query=query1.union(query2)
        if query.count()==0:
            messages.error(request,'there is no item,which matches your keyword pls right keyword .....')
        
        params1={'params':query}
            
    
    return render(request,'search.html',params1)
            
def logoutt(request):
    logout(request)
    return redirect('/')