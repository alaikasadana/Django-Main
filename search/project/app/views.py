from django.shortcuts import render

# Create your views here.

from .models import QueryData

def page(request):
    data = None

    if request.method == "POST":
        if "submit_form" in request.POST:
            QueryData.objects.create(
                name=request.POST.get("name"),
                email=request.POST.get("email"),
                contact=request.POST.get("contact"),
                query=request.POST.get("query"),
            )

        elif "search_data" in request.POST:
            keyword = request.POST.get("search")
            data = QueryData.objects.filter(name__icontains=keyword)

    return render(request, "search.html", {"data": data})
