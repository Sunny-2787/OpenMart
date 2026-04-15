from django.shortcuts import  redirect

def api_view_a(request):
    return redirect('api/v1/')