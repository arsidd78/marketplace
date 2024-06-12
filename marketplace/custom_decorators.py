# custom_decorators.py
import functools
from member.models import Member
from django.shortcuts import get_object_or_404, redirect

def profile_required(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        
        member = Member.objects.filter(user=request.user)
        if member:
            return func(request, *args, **kwargs)
        else:
            # Redirect to the complete profile page
            return redirect('member:register')
    
    return wrapper
