from django.shortcuts import render

def services_page(request):
    return render(request=request,template_name='service.html')
