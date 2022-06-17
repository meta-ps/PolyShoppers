from django.shortcuts import render,redirect
from .models import User
from django.http import JsonResponse

# Create your views here.
def Home(request):

    context={}
    return render(request,'seller_home.html',context)


def CreateOrValidateUser(request):

    if request.POST:
        t_username = request.POST.get('username-id')
        try:
            temp = User.objects.get(username=t_username)
        except:
            temp=False
        if temp:
            return redirect('userpage',temp)
        else:
            print('update userdetails')
            t_username = request.POST.get('username-id')
            t_wallet = request.POST.get('wallet-address')
            t_about = request.POST.get('about')
            t_youtube = request.POST.get('youtube')
            
            t_user = User.objects.create(username=t_username,walletid=t_wallet,about=t_about,youtube=t_youtube)
            return redirect('userpage',t_username)
    else:
        return redirect('home')



def check_username(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
        print(username)
        data = {
            'username': User.objects.filter(username=username).count()
        }
        return JsonResponse(data)
    return redirect('home')


def UserPage(request,username):
    
    temp = User.objects.get(username=username)

    context={
        'username':username,
        'walletaddr':temp.walletid,
        'about':temp.about,
        'youtube':temp.youtube,

    }
    return render(request,'seller_page.html',context)