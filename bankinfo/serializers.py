from rest_framework import serializers

from .models import *

class BankInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankInfo
        exclude = ()