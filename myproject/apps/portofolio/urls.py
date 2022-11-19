from myproject.apps.portofolio import views
from django.urls import path
from .views import (
    register, register_awal, configurasi_porto, theme_update, cover_update, pasangan_update, quote_update, update, \
    myportofolio, acara_update, moment_update, stories_update, map_update, dompet_update, specialinvite_update,\
    info_update, PortofolioList, PortofolioDetail, RekeningList, RekeningDetail, \
    DompetList, DompetDetail, MultiImageList, MultiImageDetail, \
    SpecialInvitationList, SpecialInvitationDetail, PaymentList, \
    PaymentDetail, QuoteList, QuoteDetail, UcapanList, UcapanDetail, \
    HadirList, HadirDetail, FiturList, FiturDetail, \
    ThemeList, ThemeDetail,ThemeProductList, ThemeProductDetail, StoryList, \
    StoryDetail, ApiRoot
)


urlpatterns = [
    path("register/", register, name="register"),
    path("register_awal/", register_awal, name="register_awal"),
    path("configurasi/", configurasi_porto, name="configurasi"),
    path('update/<slug:slug>/', update, name='update'),
    path('tampilan_update/<slug:slug>/', theme_update, name='tampilan_update'),
    path('cover_update/<slug:slug>/', cover_update, name='cover_update'),
    path('pasangan_update/<slug:slug>/', pasangan_update, name='pasangan_update'),
    path('quote_update/<slug:slug>/', quote_update, name='quote_update'),
    path('acara_update/<slug:slug>/', acara_update, name='acara_update'),
    path('moment_update/<slug:slug>/', moment_update, name='moment_update'),
    path('stories_update/<slug:slug>/', stories_update, name='stories_update'),
    path('map_update/<slug:slug>/', map_update, name='map_update'),
    path('dompet_update/<slug:slug>/', dompet_update, name='dompet_update'),
    path('specialinvite_update/<slug:slug>/', specialinvite_update, name='specialinvite_update'),
    path('info_update/<slug:slug>/', info_update, name='info_update'),
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

    path('api/theme/', ThemeList.as_view(), name=views.ThemeList.name),
    path('api/theme/<int:pk>', ThemeDetail.as_view(), name=views.ThemeDetail.name),

    path('api/themeproduct/', ThemeProductList.as_view(), name=views.ThemeProductList.name),
    path('api/themeproduct/<int:pk>', ThemeProductDetail.as_view(), name=views.ThemeProductDetail.name),

    path('api/story/', StoryList.as_view(), name=views.StoryList.name),
    path('api/story/<int:pk>', StoryDetail.as_view(), name=views.StoryDetail.name),

    path('api/', ApiRoot.as_view(), name=views.ApiRoot.name),
]
