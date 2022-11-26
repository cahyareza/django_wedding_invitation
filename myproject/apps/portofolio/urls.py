from myproject.apps.portofolio import views
from django.urls import path
from .views import (
    register_awal,configurasi_porto, myportofolio, step1, step2, step3, step4, step5, step6,\
    step7, step8, step9, step10, step11, step12,\
    step1_update, step2_update, step3_update, step4_update,step5_update, step6_update,\
    step7_update, step8_update, step9_update, step10_update, step11_update, step12_update,\
    PortofolioList, PortofolioDetail, RekeningList, RekeningDetail, \
    DompetList, DompetDetail, MultiImageList, MultiImageDetail, \
    SpecialInvitationList, SpecialInvitationDetail, PaymentList, \
    PaymentDetail, QuoteList, QuoteDetail, UcapanList, UcapanDetail, \
    HadirList, HadirDetail, FiturList, FiturDetail, \
    ThemeList, ThemeDetail,ThemeProductList, ThemeProductDetail, StoryList, \
    StoryDetail, AcaraList, AcaraDetail, ApiRoot
)


urlpatterns = [
    # path("register/", register, name="register"),
    path("register_awal/", register_awal, name="register_awal"),
    path("configurasi/", configurasi_porto, name="configurasi"),

    path("step1/", step1, name="step1"),
    path("step2/", step2, name="step2"),
    path("step3/", step3, name="step3"),
    path("step4/", step4, name="step4"),
    path("step5/", step5, name="step5"),
    path("step6/", step6, name="step6"),
    path("step7/", step7, name="step7"),
    path("step8/", step8, name="step8"),
    path("step9/", step9, name="step9"),
    path("step10/", step10, name="step10"),
    path("step11/", step11, name="step11"),
    path("step12/", step12, name="step12"),

    # UPDATE
    path("step1_update/<slug:slug>/", step1_update, name="step1_update"),
    path("step2_update/<slug:slug>/", step2_update, name="step2_update"),
    path("step3_update/<slug:slug>/", step3_update, name="step3_update"),
    path("step4_update/<slug:slug>/", step4_update, name="step4_update"),
    path("step5_update/<slug:slug>/", step5_update, name="step5_update"),
    path("step6_update/<slug:slug>/", step6_update, name="step6_update"),
    path("step7_update/<slug:slug>/", step7_update, name="step7_update"),
    path("step8_update/<slug:slug>/", step8_update, name="step8_update"),
    path("step9_update/<slug:slug>/", step9_update, name="step9_update"),
    path("step10_update/<slug:slug>/", step10_update, name="step10_update"),
    path("step11_update/<slug:slug>/", step11_update, name="step11_update"),
    path("step12_update/<slug:slug>/", step12_update, name="step12_update"),

    # path('info_update/<slug:slug>/', info_update, name='info_update'),
    # path('update/<slug:slug>/', update, name='update'),
    # path('tampilan_update/<slug:slug>/', theme_update, name='tampilan_update'),
    # path('cover_update/<slug:slug>/', cover_update, name='cover_update'),
    # path('pasangan_update/<slug:slug>/', pasangan_update, name='pasangan_update'),
    # path('quote_update/<slug:slug>/', quote_update, name='quote_update'),
    # path('acara_update/<slug:slug>/', acara_update, name='acara_update'),
    # path('moment_update/<slug:slug>/', moment_update, name='moment_update'),
    # path('stories_update/<slug:slug>/', stories_update, name='stories_update'),
    # path('map_update/<slug:slug>/', map_update, name='map_update'),
    # path('dompet_update/<slug:slug>/', dompet_update, name='dompet_update'),
    # path('specialinvite_update/<slug:slug>/', specialinvite_update, name='specialinvite_update'),
    # path('countdown_update/<slug:slug>/', countdown_update, name='countdown_update'),
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

    path('api/acara/', AcaraList.as_view(), name=views.AcaraList.name),
    path('api/acara/<int:pk>', AcaraDetail.as_view(), name=views.AcaraDetail.name),

    path('api/', ApiRoot.as_view(), name=views.ApiRoot.name),
]
