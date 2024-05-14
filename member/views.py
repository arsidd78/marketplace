from django.shortcuts import render
from .models import Member
from django.shortcuts import get_object_or_404,redirect
# Create your views here.
def profile(request,pk):
    if request.user.is_authenticated:
        member = get_object_or_404(Member,id = pk)
        context = {'member': member,'request':request}
        return render(request,'member/user_page.html',context)
    else:
        return redirect('login')