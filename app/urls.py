from django.urls import path
from . import views
from .views import Fpo


urlpatterns = [
    path('',views.home,name='home'),
    path('fpo/',Fpo.as_view(),name='Fpo'),
    path('fporeport/',views.fporeport,name='fporeport'),
    path('farmerreport/',views.farmerreport,name='farmerreport'),
    path('delfpo/<int:id>',views.delfpo,name='delFpo'),
    # path('fpo/',views.Fpo,name='Fpo'),
    # path('farmer/',FarmerView,name='farmer'),
    path('farmer/',views.farmer,name='farmer'),
    path('pageaccount/',views.pageaccount,name='pageaccount'),
    path('profile/',views.profile,name='profile'),
    path('profileaddressprofe/',views.profileaddressprofe,name='profileaddressprofe'),
    path('createfpo/',views.createfpo,name='createfpo'),
    path('editfpo/<int:id>',views.editfpo,name='editfpo'),
    path('editfarmer/<int:id>',views.editfarmer,name='editfarmer'),
    path('createfarmer/',views.createfarmer,name='createfarmer'),
    path('inactivatefpo/<int:id>',views.inactivatefpo,name='inactivatefpo'),
    path('inactivatefarmer/<int:id>',views.inactivatefarmer,name='inactivatefarmer'),
    path('someview/',views.report,name='some_view'),
    path('lsa/',views.lsa,name='some_view'),


    path('videocapture/',views.videocapture,name='videocapture'),


    path('FpoRegistration/',views.FpoRegistrationView,name='FpoRegistration'),
    path('FpoRegistrationBasicDetails/',views.FpoRegistrationBasicDetailsView,name='FpoRegistrationBasicDetails'),
    path('FpoAddressDetails/',views.FpoAddressDetailsView,name='FpoAddressDetails'),
    path('Fpoofficeprofe/',views.FpoofficeprofeView,name='Fpoofficeprofe'),
    path('Fporegistrationdocument/',views.FporegistrationdocumentView,name='Fporegistrationdocument'),
    path('subscriberdetails/',views.subscriberdetailsView,name='subscriberdetails'),
    path('viewsubscriberdetails/<int:id>',views.viewsubscriberdetailsView,name='viewsubscriberdetails'),
    path('viewsubscriberdocdetails/<int:id>',views.viewsubscriberdocdetailsView,name='viewsubscriberdocdetails'),
    path('fpocadetails/',views.fpocadetailsView,name='fpocadetails'),
    path('fpoceodetails/',views.fpoceodetailsView,name='fpoceodetails'),
    path('fpoaccountantdetails/',views.fpoaccountantdetailsView,name='fpoaccountantdetails'),



    # bank urls
    path('bankdetals/',views.bankdetals,name='bankdetals'),
    path('bankdetals2/',views.bankdetals2,name='bankdetals2'),
    path('bankdetals3/',views.bankdetals3,name='bankdetals3'),
    path('bankdetals4/',views.bankdetals4,name='bankdetals4'),

    #authorised shared capital
    path('authorisedShare/',views.AuthorisedShare,name='AuthorisedShare'),
    path('authorisedShare/<int:id>',views.AuthorisedSharecapitalupdate,name='AuthorisedShare'),
    path('issuedShare/',views.issuedShare,name='issuedShare'),
    path('issuedShare/<int:id>',views.issuedSharecapitalupdate,name='issuedShare'),
    path('compnaymetting/',views.compnaymetting,name='compnaymetting'),
    path('compnaymetting/<int:id>',views.compnaymettingupdate,name='compnaymetting'),
]
