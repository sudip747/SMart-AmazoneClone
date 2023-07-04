"""ardent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include

from student import views


from django.conf.urls import  url


from django.conf import settings
from django.conf.urls.static import static



admin.site.site_header = 'S-MART'
admin.site.index_title='Workspace'
admin.site.site_title ='Verification'




urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.Signup, name="signup"),
    path('login/', views.Login , name="login"),
    path('index/', views.home, name="index"),
    path('category/<slug:val>', views.CategoryView.as_view(), name="category"),
    path('productdetail/<int:pk>', views.ProductDetail.as_view(), name="productdetail"),
    path('categorytitle/<val>', views.CategoryTitle.as_view(), name="categorytitle"),
    path('about/', views.about, name="about"),
    path('signout/', views.signout, name = 'logout'),
    path('addcart/', views.addcart , name="addcart" ),
    path('showcart/', views.showcart , name="showcart" ),
    path('checkout/', views.checkout.as_view() , name="checkout" ),
    path('pluscart/', views.plus_cart ),
    path('minuscart/', views.minus_cart ),
    path('removecart/', views.remove_cart ),
    path('gateway/',views.gateway,name="gateway"),
    path('orders/', views.home, name="orders"),
    path('profile/', views.profile, name="profile"),

  
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

