from django.http import HttpResponse
""" 
def adnim_restricted(this_is_arg):
    def only_w_permission(func):
        # somehow i get these parameters from previous function
        def wrapper(request,*args, **kwd):
            
            if request.user.is_authenticated:
                return func(request,*args, **kwd)
            else:
                return HttpResponse("Hello, world. You're at the polls index.")
        return wrapper
    return only_w_permission
"""

def only_w_permission(func):
    # somehow i get these parameters from previous function
    def wrapper(request,*args, **kwd):
        
        if request.user.is_authenticated:
            return func(request,*args, **kwd)
        else:
            return HttpResponse("Hello, world. You're at the polls index.")
    return wrapper