from django.shortcuts import redirect, render


def redirect_loggeduser(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            print('IS LOGGED IN')
            return redirect('UserHomepage')
        else:
            print('NOT LOGGED IN')
            return view_func(request, *args, **kwargs)

    return wrapper_func


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        user_group = request.user.groups.all().first()
        if user_group.name == 'Staff':
            print('Authenticated')
            return view_func(request, *args, **kwargs)
        else:
            print('Un-Authenticated')
            return render(request, 'users/unauthorized_template.html')

    return wrapper_func
