from django.shortcuts import render
from .models import Company
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):    
    companies = Company.objects.all()
    paginator = Paginator(companies, 8)

    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)
    context = {
        'page_obj': page_obj
    }

    # sending the page object to index.html
    return render(request, 'companies/companies.html', context)


