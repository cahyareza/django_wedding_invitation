from myproject.apps.portofolio import views
from django.urls import path
from .views import (
    register, update, myportofolio, \
    PortofolioList, PortofolioDetail, RekeningList, RekeningDetail, \
    DompetList, DompetDetail, MultiImageList, MultiImageDetail, \
    SpecialInvitationList, SpecialInvitationDetail, PaymentList, \
    PaymentDetail, QuoteList, QuoteDetail, UcapanList, UcapanDetail, \
    HadirList, HadirDetail, FiturList, FiturDetail, FiturProductList, FiturProductDetail, \
    ThemeList, ThemeDetail, ApiRoot
)


urlpatterns = [
    path("register/", register, name="register"),
    path('update/<slug:slug>/', update, name='update'),
    path('myportofolio/', myportofolio, name='myportofolio'),

    path('api/portofolio/', PortofolioList.as_view(), name=views.PortofolioList.name),
    path('api/portofolio/<int:pk>', PortofolioDetail.as_view(), name=views.PortofolioDetail.name),
    path('api/rekening/', RekeningList.as_view(), name=views.RekeningList.name),
    path('api/rekening/<int:pk>', RekeningDetail.as_view(), name=views.RekeningDetail.name),

    path('api/multiimage/', MultiImageList.as_view(), name=views.MultiImageList.name),
    path('api/multiimage/<int:pk>', MultiImageDetail.as_view(), name=views.MultiImageDetail.name),

    path('api/specialinvitation/', SpecialInvitationList.as_view(), name=views.SpecialInvitationList.name),
    path('api/specialinvitation/<int:pk>', SpecialInvitationDetail.as_view(), name=views.SpecialInvitationDetail.name),

    path('api/payment/', PaymentList.as_view(), name=views.PaymentList.name),
    path('api/payment/<int:pk>', PaymentDetail.as_view(), name=views.PaymentDetail.name),

    path('api/dompet/', DompetList.as_view(), name=views.DompetList.name),
    path('api/dompet/<int:pk>', DompetDetail.as_view(), name=views.DompetDetail.name),

    path('api/quote/', QuoteList.as_view(), name=views.QuoteList.name),
    path('api/quote/<int:pk>', QuoteDetail.as_view(), name=views.QuoteDetail.name),

    path('api/ucapan/', UcapanList.as_view(), name=views.UcapanList.name),
    path('api/ucapan/<int:pk>', UcapanDetail.as_view(), name=views.UcapanDetail.name),

    path('api/hadir/', HadirList.as_view(), name=views.HadirList.name),
    path('api/hadir/<int:pk>', HadirDetail.as_view(), name=views.HadirDetail.name),

    path('api/fitur/', FiturList.as_view(), name=views.FiturList.name),
    path('api/fitur/<int:pk>', FiturDetail.as_view(), name=views.FiturDetail.name),

    path('api/fiturproduct/', FiturProductList.as_view(), name=views.FiturProductList.name),
    path('api/fiturproduct/<int:pk>', FiturProductDetail.as_view(), name=views.FiturProductDetail.name),

    path('api/theme/', ThemeList.as_view(), name=views.ThemeList.name),
    path('api/theme/<int:pk>', ThemeDetail.as_view(), name=views.ThemeDetail.name),

    path('api/', ApiRoot.as_view(), name=views.ApiRoot.name),
]
