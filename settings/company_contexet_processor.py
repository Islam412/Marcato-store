from .models import Company


def get_company_data(request):
    data = Company.objects.latest()
    return {'company_data': data}