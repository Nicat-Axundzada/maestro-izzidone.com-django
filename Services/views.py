from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, SubService
from .forms import ServiceForm, SubServiceFormSet


def index(request):
    services = Service.objects.all()
    data = {
        'services': [
            {
                'id': str(service.id),
                'title_en': service.title,
                'cover_img': {'publicUrl': service.image.url},
                'subServices': [
                    {
                        'id': str(subservice.id),
                        'title_en': subservice.title_en,
                        'image': subservice.image.url,
                    }
                    for subservice in service.subservice_set.all()
                ]
            }
            for service in services
        ]
    }
    return render(request, 'Services/index.html', {'data_from_database': data})


def services(request, service_name):

    service = get_object_or_404(Service, title=service_name)
    sub_services = SubService.objects.filter(service=service)
    content = {
        'sub_services': sub_services,
    }

    return render(request, 'Services/service.html', content)


def create_service(request):
    if request.method == 'POST':
        service_form = ServiceForm(request.POST, request.FILES)
        sub_service_formset = SubServiceFormSet(
            request.POST, request.FILES, instance=Service())

        if service_form.is_valid() and sub_service_formset.is_valid():
            service = service_form.save()
            sub_service_formset.instance = service
            sub_service_formset.save()

            return redirect('index')
    else:
        service_form = ServiceForm()
        sub_service_formset = SubServiceFormSet(instance=Service())

    return render(request, 'Services/form.html', {
        'service_form': service_form,
        'sub_service_formset': sub_service_formset
    })
