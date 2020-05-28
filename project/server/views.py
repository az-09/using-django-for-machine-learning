from django.conf import settings
from django.shortcuts import HttpResponse
from rest_framework import generics

from predict.views import Loader

# Create your views here.

class GetSalaryAPIView(generics.GenericAPIView):
    def post(self, request):
        if request.method == 'POST':
            data = request.data

            exp = float(data['exp'])

            salary = Loader(settings.BASE_DIR + "/predict/model.pkl", [[exp]]).load()

            return HttpResponse(salary)
        else:
            return 'Failed to get model'
