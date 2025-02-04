from rest_framework.decorators import api_view
from companies.models import Company
from .serializers import CompanySerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def company_list(request):
    # GET all companies
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)

        return Response(serializer.data)