from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from .forms import ContactForm
from .models import News, Category
from django.http import HttpResponse


def new_list(request):
    new_list = News.objects.filter(status=News.Status.Draft)
    # new_list = News.objects.all()
    context = {
        "new_list": new_list
    }
    return render(request, "news/news_list.html", context)


def news_detail(request, id):
    print(News.objects.all())
    news = get_object_or_404(News, id=id, status=News.Status.Draft)
    context = {
        'news': news
    }
    return render(request, 'news/news_detail.html', context=context)


class NewsList(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list_class'


def index_page(request):
    return render(request, 'index.html')


def contact_page(request):
    print(request, 'bu request')
    print(request.POST, 'bu post ')
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse("<h2> biz bilan bog'langaningiz uchun tashakkur")

    context = {
        'form': form
    }

    return render(request, 'contact.html', context)


# def contact(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse('ok')
#     context = {
#         'form': form
#     }
#     return render(request, 'contact.html', context)

class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2>Biz bilan boglanagiz uchun rahmat</h2>")
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)
