from django.db import models


class Sender(models.Model):
    country = models.CharField(max_length = 20)
    currency = models.CharField(max_length = 5)
    entity_type = models.CharField(max_length = 40)
    company_name = models.CharField(max_length = 30)
    identification_type = models.CharField(max_lenght = 20)
    identification_value = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 20)
    occupation = models.CharField(max_length = 50, help_text= "Industry Section")
    source_of_income = models.CharField(max_length = 20)
    date_of_birth = models.CharField(max_length = 10, help_text= "Date of establishment")
    address = models.CharField(max_length = 256)
    purpose_code = models.CharField(max_length = 100)
    beneficiary_relationship = models.CharField(max_length = 20)



class Beneficiary(models.Model):
    category = models.CharField(max_length = 10)
    country = models.CharField(max_lenght = 50)
    currency = models.CharField(max_length = 5)
    entity_type = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    account_name = models.CharField(max_length = 30)
    identification_type = models.CharField(max_length = 50)
    identification_value = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 20)


class Payout(models.Model):
    ewallet = models.CharField(max_length = 100)
    payout_amount = models.DecimalField()
    payout_method_type = models.CharField(max_lenght = 50)
    sender_currency = models.CharField(max_length = 5)
    sender_country = models.CharField(max_length= 50)
    beneficiary_country = models.CharField(max_length = 5)
    payout_currency = models.CharField(max_length= 5)
    sender_entity_type = models.CharField(max_length = 50)
    beneficiary_entity_type = models.CharField(max_length = 10)
    beneficiary = models.CharField(max_length = 50)
    sender = models.CharField(max_length = 50)
    description = models.CharField(max_length = 512)

    