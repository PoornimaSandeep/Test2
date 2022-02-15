from .models import user_data
from django.http import HttpResponse

def service_data(request,adhar_no,mobile_no,name):
    adhar=user_data.objects.filter(adhar_no=adhar_no).first()
    print(adhar)
    print(adhar_no)

    if adhar==adhar_no:
       data=user_data(adhar_no=adhar_no,Mobile_no=mobile_no,name=name)
       data.save()
       return HttpResponse(request,f'your successfully registered for 2nd dose')
    else:
        data = user_data(adhar_no=adhar_no, Mobile_no=mobile_no, name=name)
        data.save()
        return HttpResponse(request,f'your successfully registered for 1nd dose')
