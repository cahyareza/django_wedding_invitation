from django.urls import path
from .views import (
    PortofolioList, PortofolioDetail, RekeningList, RekeningDetail, \
    DompetList, DompetDetail, MultiImageList, MultiImageDetail, \
    SpecialInvitationList, SpecialInvitationDetail, PaymentList, \
    PaymentDetail, QuoteList, QuoteDetail, UcapanList, UcapanDetail, \
    HadirList, HadirDetail, FiturList, FiturDetail, \
    ThemeList, ThemeDetail,ThemeProductList, ThemeProductDetail, StoryList, \
    StoryDetail, AcaraList, AcaraDetail,DanaList, DanaDetail, ResumeList, ResumeDetail, \
    MultiImageThemeList, MultiImageThemeDetail, ApiRoot
)

app_name = "portofolio"
urlpatterns = [
    path('', PortofolioList.as_view(), name=PortofolioList.name),
    path('<int:pk>', PortofolioDetail.as_view(), name=PortofolioDetail.name),
    path('rekening/', RekeningList.as_view(), name=RekeningList.name),
    path('rekening/<int:pk>', RekeningDetail.as_view(), name=RekeningDetail.name),

    path('multiimage/', MultiImageList.as_view(), name=MultiImageList.name),
    path('multiimage/<int:pk>', MultiImageDetail.as_view(), name=MultiImageDetail.name),

    path('specialinvitation/', SpecialInvitationList.as_view(), name=SpecialInvitationList.name),
    path('specialinvitation/<int:pk>', SpecialInvitationDetail.as_view(), name=SpecialInvitationDetail.name),

    path('payment/', PaymentList.as_view(), name=PaymentList.name),
    path('payment/<int:pk>', PaymentDetail.as_view(), name=PaymentDetail.name),

    path('dompet/', DompetList.as_view(), name=DompetList.name),
    path('dompet/<int:pk>', DompetDetail.as_view(), name=DompetDetail.name),

    path('quote/', QuoteList.as_view(), name=QuoteList.name),
    path('quote/<int:pk>', QuoteDetail.as_view(), name=QuoteDetail.name),

    path('ucapan/', UcapanList.as_view(), name=UcapanList.name),
    path('ucapan/<int:pk>', UcapanDetail.as_view(), name=UcapanDetail.name),

    path('hadir/', HadirList.as_view(), name=HadirList.name),
    path('hadir/<int:pk>', HadirDetail.as_view(), name=HadirDetail.name),

    path('fitur/', FiturList.as_view(), name=FiturList.name),
    path('fitur/<int:pk>', FiturDetail.as_view(), name=FiturDetail.name),

    path('theme/', ThemeList.as_view(), name=ThemeList.name),
    path('theme/<int:pk>', ThemeDetail.as_view(), name=ThemeDetail.name),

    path('themeproduct/', ThemeProductList.as_view(), name=ThemeProductList.name),
    path('themeproduct/<int:pk>', ThemeProductDetail.as_view(), name=ThemeProductDetail.name),

    path('story/', StoryList.as_view(), name=StoryList.name),
    path('story/<int:pk>', StoryDetail.as_view(), name=StoryDetail.name),

    path('acara/', AcaraList.as_view(), name=AcaraList.name),
    path('acara/<int:pk>', AcaraDetail.as_view(), name=AcaraDetail.name),

    path('dana/', DanaList.as_view(), name=DanaList.name),
    path('dana/<int:pk>', DanaDetail.as_view(), name=DanaDetail.name),

    path('resume/', ResumeList.as_view(), name=ResumeList.name),
    path('resume/<int:pk>', ResumeDetail.as_view(), name=ResumeDetail.name),

    path('multiimagetheme/', MultiImageThemeList.as_view(), name=MultiImageThemeList.name),
    path('multiimagetheme/<int:pk>', MultiImageThemeDetail.as_view(), name=MultiImageThemeDetail.name),

    path('list/', ApiRoot.as_view(), name=ApiRoot.name),
]
