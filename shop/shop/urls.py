"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path

from products_category.views import index
from products_category.views import product
from products_category.views import categories
from django.views.generic import TemplateView
from publishers.views import PublisherList
from feedback.views import FeedbackCreateView
from feedback.views import FeedbackView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(
        template_name="index.html",
        extra_context={"header": "О сайте"}
    )),
    path('publishers/', PublisherList.as_view()),
    path('categories', categories),
    path('products', index),
    path('product/<int:id_product>', product),
    path('feedback', FeedbackView.as_view()),
    path('feedback/create', FeedbackCreateView.as_view()),
]

