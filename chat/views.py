from django.shortcuts import render,redirect

# Create your views here.
def chatPage(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'chat/chatPage.html',context)
    return redirect('registration:login')