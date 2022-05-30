from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.views.generic import TemplateView
from django.views import View
from .models import Product
from django.core.mail import send_mail

import hashlib
import base64
import requests
from datetime import datetime
import calendar
import string
from random import *
import hmac
import json

access_key = '23F7E00B653E2FE3DF3E' 
secret_key = '9d45afe25456eebbb323e1249e946679cbab83e9d116fdc9a0fb6384a2d17f1fa07ed84c47532f2f'

d = datetime.utcnow()
timestamp = calendar.timegm(d.utctimetuple())

class SuccessView(TemplateView):
    template_name = "success.html"

class CancelView(TemplateView):
    template_name = "error.html"

class ProductLandingPageView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        product = Product.objects.get(name = "Test Product")
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "product" : product,
            "access_key" : access_key,
            "secret_key" : secret_key
        })

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = Product.objects.get(id = product_id)

        http_method = 'post'                   # get|put|post|delete - must be lowercase
        base_url = 'https://sandboxapi.rapyd.net'
        path = '/v1/checkout'
        
        min_char = 8
        max_char = 12
        allchar = string.ascii_letters + string.punctuation + string.digits
        salt = "".join(choice(allchar)for x in range(randint(min_char, max_char)))

        MY_DOMAIN = "127.0.01:8000/"

        checkout_body = {}
        checkout_body['cart_items'] = product.name
        checkout_body['amount'] = product.price
        checkout_body['country'] = product.country
        checkout_body['currency'] = product.currency
        checkout_body['complete_checkout_url'] = MY_DOMAIN + '/success/'
        checkout_body['error_payment_url'] = MY_DOMAIN + '/error/'
        checkout_body['cancel_checkout_url'] = MY_DOMAIN + '/landing/'
        checkout_body['description'] = product.description

        body = json.dumps(checkout_body, separators = (',',':'))

        checkout_page = {
            "amount": product.price,
            "complete_payment_url": "http://example.com/complete",
            "country": "SG",
            "currency": "SGD",
            "customer": "cus_9761efaa881b6edeab25e9fbfec1ddf5",
            "error_payment_url": "http://example.com/error",
            "merchant_reference_id": "0912-2021",
            "language": "en",
            "metadata": {
                "merchant_defined": True
            },
            "expiration": 1632027189,
            "payment_method_types_include": [
                "sg_grabpay_ewallet"
            ]
        }

        to_sign = http_method + path + salt + str(timestamp) + access_key + secret_key + body

        h = hmac.new(bytes(secret_key, 'utf-8'), bytes(to_sign, 'utf-8'), hashlib.sha256)

        signature = base64.urlsafe_b64encode(str.encode(h.hexdigest()))

        url = base_url + path

        headers = {
            'access_key': access_key,
            'signature': signature,
            'salt': salt,
            'timestamp': str(timestamp),
            'Content-Type': "application\/json"
        }

        response = requests.post(url, headers = headers, json = checkout_body)
        hosted_checkout_url = response.json()['data']['redirect_url']

        return (hosted_checkout_url)
        
