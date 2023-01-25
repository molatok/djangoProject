import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ads.models import Ads, Categories


def home_page(request):
    return HttpResponse(200, {"status": "ok"})


@method_decorator(csrf_exempt, name="dispatch")
class AdsView(View):
    def get(self, request):
        ads = Ads.objects.all()
        response = []
        for ad in ads:
            response.append({"статус": ad.status,
                             "название": ad.name,
                             "автор": ad.author,
                             "цена": ad.price,
                             "описание": ad.description,
                             "адрес": ad.address,
                             "опубликовано?": ad.is_published
                             })
        return JsonResponse(response, safe=False)

    def get_by_pk(self, ads_id):
        ad = Ads.objects.get(pk=ads_id)
        return JsonResponse({"статус": ad.status,
                             "название": ad.name,
                             "автор": ad.author,
                             "цена": ad.price,
                             "описание": ad.description,
                             "адрес": ad.address,
                             "опубликовано?": ad.is_published
                             })

    def post(self, request):
        ad_data = json.loads(request.body)
        ad = Ads()
        ad.name = ad_data["name"]
        ad.author = ad_data["author"]
        ad.price = ad_data["price"]
        ad.status = ad_data["status"]
        ad.address = ad_data["address"]
        ad.description = ad_data["description"]
        ad.is_published = ad_data["is_published"]
        ad.save()

        return JsonResponse({"статус": ad.status,
                             "название": ad.name,
                             "описание": ad.description
                             })




@method_decorator(csrf_exempt, name="dispatch")
class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()
        response = []
        for categorie in categories:
            response.append({"статус": categorie.status,
                             "название": categorie.name,
                             })
        return JsonResponse(response, safe=False)

    def get_by_pk(self, category_id):

        category = Categories.objects.get(pk=category_id)

        return JsonResponse({"статус": category.status,
                             "название": category.name,
                             })

    def post(self, request):
        category_data = json.loads(request.body)
        category = Categories()
        category.name = category_data["name"]
        category.save()

        return JsonResponse({"статус": category.status,
                             "название": category.name,
                             })