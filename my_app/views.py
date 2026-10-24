from django.shortcuts import render

from django.views.generic import View

from django.http import JsonResponse

# Create your views here.

class HelloWorldView(View):

    def get(self,request):

        response_data ={"message":"HelloWold"}

        return JsonResponse(response_data)

class GoodMorinigView(View):

    def get(self,request):

        Response_data ={"message":"GoodMorining"}

        return JsonResponse(Response_data)

class GoodAfterView(View):

    def get(self,request):

        respones_data={"massage":"GoodAfter"}
        return JsonResponse(respones_data)

class GoodEvenView(View):

    def get(self,request):

        respones_data ={"message":"GoodEven"}

        return JsonResponse (respones_data)

class GoodNightView(View):

    def get(self,request):

        respones_data ={"message":"Goodnight"}

        return JsonResponse(respones_data)
        

        