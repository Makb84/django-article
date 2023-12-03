from django.http import Http404

def fields_dispatch(view_func):
    def wrapper(request, *args, **kwargs):
        # print(**kwargs)
        if request.user.is_superuser:
            print("this is superuser check")
            fields = [
                "author", "title", "slug", "category", "description", "thumbnail", "publish", "status"
            ]
        elif request.user.is_author:
            print("this is author check")
            fields = [
                "title", "slug", "category", "description", "thumbnail", "publish"
            ]
        else:
            raise Http404("You don't have permission to access this page.")

        return view_func(request, fields, *args, **kwargs)

    return wrapper
