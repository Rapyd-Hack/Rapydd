from django.shortcuts import render
from django.views import View

import uuid

from .models import Organization

class CreateBeneficiaryView(View):
    def post(self, request, *args, **kwargs):
        user_id = self.kwargs["pk"]
        user = Organization.objects.get(id = user_id)

        beneficiary_details = {}
        beneficiary_details["company_name"] = user.company_name
        beneficiary_details["beneficiary"] = "beneficiary_" + str(uuid.uuid4())

        beneficiary_details["category"] = user.category
        beneficiary_details['country'] = user.country
        beneficiary_details["currency"] = user.currency
        beneficiary_details["phone_number"] = user.phone_number



        
# Create your views here.
def process_payment(request):
    pass