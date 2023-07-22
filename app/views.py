import io

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import FpoCreationForm, FpoCreationForm2, FpoBasicDetails, FpoOfficeprofe, FpoRegistration, \
    FpoAddressDetails, RegistrationDocument, SubscriberDetailsForm, FpoCaInformationForm, \
    FpoCeoEducationForm, FpoCeoForm, FpoAccountantForm, FpoBankDetailsForm, FpoBankDetailsForm2, FpoBankDetailsForm3, \
    FpoBankDetailsForm4, AuthorisedShareCapitalForm, IssuedShareCapitalForm, CompnayMeetingform
# , FarmerForm
from users.models import CustomUser
import csv
from django.http import HttpResponse, HttpResponseRedirect
from .models import FPO, Farmer, Cbbo, BankStatementUpload, SubscriberDetails, FpoCaInformation, FpoCeoEducation, \
    FpoBankDetails, AuthorisedSharedCapital, IssuedSharedCapital, CompnayMeetingDetails, State, District, City
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .serializers import FpoSerializer
from django.http import JsonResponse
from functools import wraps


# Create your views here.
@login_required(login_url='/user/login')
def home(request):
    if request.user.is_superuser:
        all_fpo = FPO.objects.all().count()
        print(all_fpo)
        all_farmer = Farmer.objects.all().count()
        print(all_farmer)
        return render(request, 'html/ltr/vertical-menu-template/index.html',
                      {'username': request.user, 'all_fpo': all_fpo, 'all_farmer': all_farmer})
    elif request.user.role == 'admin':
        if (FPO.objects.filter(user_id=request.user.id).exists()):
            fpo = FPO.objects.get(user_id=request.user.id)
            all_farmer = Farmer.objects.filter(fpo_name=fpo.id)
            if fpo.fpo_name == '':
                return redirect('app:profile')
            return render(request, 'html/ltr/vertical-menu-template/index.html',
                          {'username': request.user, 'all_farmer': all_farmer})
    return render(request, 'index1.html')


def profile(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    subs = ''
    if SubscriberDetails.objects.filter(fpo_name=fpo).exists():
        subs = SubscriberDetails.objects.filter(fpo_name=fpo)
    authorisedShare = ''
    total_num_of_share = ''

    num_of_share, num_of_face_value, total_val_of_share = 0, 0, 0
    issuedshare_num_of_share, issuedshare_num_of_face_value, issuedshare_total_val_of_share = 0, 0, 0
    authorisedsharecapitalform = AuthorisedShareCapitalForm()
    if AuthorisedSharedCapital.objects.filter(fpo=fpo).exists():
        authorisedShare = AuthorisedSharedCapital.objects.filter(fpo=fpo)
        for i in authorisedShare:
            num_of_share = num_of_share + int(i.no_of_share)
            num_of_face_value = num_of_face_value + int(i.face_value)
            total_val_of_share = total_val_of_share + int(i.total_value)
        # authorisedsharecapitalform = AuthorisedShareCapitalForm()
    form11 = FpoCaInformationForm()
    if FpoCaInformation.objects.filter(fpo=fpo.id).exists():
        ca = FpoCaInformation.objects.get(fpo=fpo.id)
        form11 = FpoCaInformationForm(instance=ca)

    compnaymeetingform = CompnayMeetingform()
    compnaymeetingdetails = ''
    if CompnayMeetingDetails.objects.filter(fpo=fpo.id).exists():
        compnaymeetingdetails = CompnayMeetingDetails.objects.filter(fpo=fpo.id)

    issuedsharedcapital = ''
    issuedsharedcapitalform = IssuedShareCapitalForm()
    if IssuedSharedCapital.objects.filter(fpo=fpo).exists():
        issuedsharedcapital = IssuedSharedCapital.objects.filter(fpo=fpo)
        for i in issuedsharedcapital:
            issuedshare_num_of_share = issuedshare_num_of_share + int(i.no_of_share)
            issuedshare_num_of_face_value = issuedshare_num_of_face_value + int(i.face_value)
            issuedshare_total_val_of_share = issuedshare_total_val_of_share + int(i.total_value)

    form = FpoRegistration(instance=fpo)
    form2 = FpoBasicDetails(instance=fpo)
    form3 = FpoAddressDetails(instance=fpo)
    form4 = SubscriberDetailsForm()
    form9edu = FpoCeoEducationForm()
    # #for Authorised secound
    form8 = FpoBankDetailsForm()
    if FpoBankDetails.objects.filter(fpo=fpo, authorised_person=1).exists():
        bank = FpoBankDetails.objects.get(fpo=fpo, authorised_person=1)
        form8 = FpoBankDetailsForm(instance=bank)
    # #end for Authorised secound
    # #for Authorised secound
    formpersion2 = FpoBankDetailsForm2()
    if FpoBankDetails.objects.filter(fpo=fpo, authorised_person=2).exists():
        bank = FpoBankDetails.objects.get(fpo=fpo, authorised_person=2)
        formpersion2 = FpoBankDetailsForm2(instance=bank)
    # #end for Authorised secound
    # #for Authorised third

    formpersion3 = FpoBankDetailsForm3()
    if FpoBankDetails.objects.filter(fpo=fpo, authorised_person=3).exists():
        bank = FpoBankDetails.objects.get(fpo=fpo, authorised_person=3)
        formpersion3 = FpoBankDetailsForm3(instance=bank)
    # #end for Authorised third
    # #for Authorised fourth

    formpersion4 = FpoBankDetailsForm4()
    if FpoBankDetails.objects.filter(fpo=fpo, authorised_person=4).exists():
        bank = FpoBankDetails.objects.get(fpo=fpo, authorised_person=4)
        formpersion4 = FpoBankDetailsForm4(instance=bank)
    # #end for Authorised fourth
    # print(form9edu.as_table())
    form10 = FpoAccountantForm(instance=fpo)
    form9 = FpoCeoForm()
    if fpo.fpo_ceo_email_id != '':
        form9 = FpoCeoForm(instance=fpo)
    # if FpoCeoEducation.objects.filter(fpo=fpo.id).exists():
    #     ceo=FpoCeoEducation.objects.get(fpo=fpo.id)
    #     form9edu= FpoCeoEducationForm(instance=ceo)

    return render(request, 'app/fpo_profile.html',
                  {'form': form, 'form2': form2, 'form3': form3, 'fpo': fpo, 'subs': subs, 'form4': form4,
                   'form11': form11, 'form9edu': form9edu, 'form8': form8, 'form9': form9, 'form10': form10,
                   'formpersion2': formpersion2, 'formpersion3': formpersion3, 'formpersion4': formpersion4,
                   'authorisedShare': authorisedShare, 'authorisedsharecapitalform': authorisedsharecapitalform,
                   'num_of_share': num_of_share, 'num_of_face_value': num_of_face_value,
                   'total_val_of_share': total_val_of_share,
                   'issuedshare_num_of_share': issuedshare_num_of_share,
                   'issuedshare_num_of_face_value': issuedshare_num_of_face_value,
                   'issuedshare_total_val_of_share': issuedshare_total_val_of_share,
                   'issuedsharedcapital': issuedsharedcapital,
                   'issuedsharedcapitalform': issuedsharedcapitalform, 'compnaymeetingdetails': compnaymeetingdetails,
                   'compnaymeetingform': compnaymeetingform, 'username': request.user})
    # return render(request, 'app/certificates_try.html', {'form': form})


def compnaymetting(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    print(request.method)
    if request.method == "POST":
        form = CompnayMeetingform(data=request.POST)
        if form.is_valid():
            print('validate')
            form.save()
            print('saved')
        else:
            print(form.errors)
    return redirect('app:profile')


def issuedShare(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    print(request.method)
    if request.method == "POST":
        form = IssuedShareCapitalForm(data=request.POST)
        if form.is_valid():
            print('validate')
            form.save()
            print('saved')
        else:
            print(form.errors)
    return redirect('app:profile')


def AuthorisedShare(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    print('asdasdasd')
    if request.method == "POST":
        form = AuthorisedShareCapitalForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return redirect('app:profile')


def compnaymettingupdate(request, id):
    if CompnayMeetingDetails.objects.filter(id=id).exists():
        subs = CompnayMeetingDetails.objects.get(id=id)
        res = {'metting_type': subs.metting_type, 'purpose': subs.purpose,
               'notes': subs.notes, 'fpo': str(subs.fpo.id), 'date': str(subs.date), 'id': subs.id
               }
        if request.method == 'POST':
            form = CompnayMeetingform(instance=subs, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('app:profile')
            else:
                print(form.errors)
        return HttpResponse(json.dumps(res))


def AuthorisedSharecapitalupdate(request, id):
    if AuthorisedSharedCapital.objects.filter(id=id).exists():
        subs = AuthorisedSharedCapital.objects.get(id=id)
        res = {'no_of_share': subs.no_of_share, 'face_value': subs.face_value,
               'total_value': subs.total_value, 'fpo': str(subs.fpo.id), 'date': str(subs.date), 'id': subs.id
               }
        if request.method == 'POST':
            form = AuthorisedShareCapitalForm(instance=subs, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('app:profile')
            else:
                print(form.errors)
        return HttpResponse(json.dumps(res))


def issuedSharecapitalupdate(request, id):
    if IssuedSharedCapital.objects.filter(id=id).exists():
        subs = IssuedSharedCapital.objects.get(id=id)
        res = {'no_of_share': subs.no_of_share, 'face_value': subs.face_value,
               'total_value': subs.total_value, 'fpo': str(subs.fpo.id), 'date': str(subs.date), 'id': subs.id
               }
        if request.method == 'POST':
            form = IssuedShareCapitalForm(instance=subs, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('app:profile')
            else:
                print(form.errors)
        return HttpResponse(json.dumps(res))


def bankdetals(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    print('asdasdasd')
    if request.method == "POST":
        print('post')
        form = FpoBankDetailsForm(data=request.POST, files=request.FILES)
        if FpoBankDetails.objects.filter(fpo=fpo, authorised_person=1).exists():
            print('exists')
            bank = FpoBankDetails.objects.get(fpo=fpo, authorised_person=1)
            form = FpoBankDetailsForm(instance=bank, data=request.POST, files=request.FILES)
            if form.is_valid():
                print('val')
                form.save()
                print('form saved....')
            else:
                print(form.errors)
        else:
            print('else')
            if form.is_valid():
                print('val')
                form.save()
                print('form saved....')
            else:
                print(form.errors)
    return redirect('app:profile')


def bankdetals2(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    print('asdasdasd')
    if request.method == "POST":
        print('post')
        form = FpoBankDetailsForm2(data=request.POST, files=request.FILES)
        if FpoBankDetails.objects.filter(fpo=fpo, authorised_person=2).exists():
            print('exists')
            bank = FpoBankDetails.objects.get(fpo=fpo, authorised_person=2)
            form = FpoBankDetailsForm2(instance=bank, data=request.POST, files=request.FILES)
            if form.is_valid():
                print('val')
                form.save()
                print('form saved....')
            else:
                print(form.errors)
        else:
            print('else')
            if form.is_valid():
                print('val')
                form.save()
                print('form saved....')
            else:
                print(form.errors)
    return redirect('app:profile')


def bankdetals3(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    print('asdasdasd')
    if request.method == "POST":
        print('post')
        form = FpoBankDetailsForm3(data=request.POST, files=request.FILES)
        if FpoBankDetails.objects.filter(fpo=fpo, authorised_person=3).exists():
            print('exists')
            bank = FpoBankDetails.objects.get(fpo=fpo, authorised_person=3)
            form = FpoBankDetailsForm3(instance=bank, data=request.POST, files=request.FILES)
            if form.is_valid():
                print('val')
                form.save()
                print('form saved....')
            else:
                print(form.errors)
        else:
            print('else')
            if form.is_valid():
                print('val')
                form.save()
                print('form saved....')
            else:
                print(form.errors)
    return redirect('app:profile')


def bankdetals4(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    print('asdasdasd')
    if request.method == "POST":
        print('post')
        form = FpoBankDetailsForm4(data=request.POST, files=request.FILES)
        if FpoBankDetails.objects.filter(fpo=fpo, authorised_person=4).exists():
            print('exists')
            bank = FpoBankDetails.objects.get(fpo=fpo, authorised_person=4)
            form = FpoBankDetailsForm4(instance=bank, data=request.POST, files=request.FILES)
            if form.is_valid():
                print('val')
                form.save()
                print('form saved....')
            else:
                print(form.errors)
        else:
            print('else')
            if form.is_valid():
                print('val')
                form.save()
                print('form saved....')
            else:
                print(form.errors)
    return redirect('app:profile')


def fpoaccountantdetailsView(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    if request.method == "POST":
        form = FpoAccountantForm(instance=fpo, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            print('form saved....')
        else:
            print(form.errors)
    return redirect('app:profile')


def fpoceodetailsView(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    if request.method == "POST":
        ceo_education = request.POST.getlist('ceo_education')
        edu_doc = request.FILES.getlist('ceo_education_documents')
        i_count= 0
        for i in ceo_education:
            if i != '':
                if FpoCeoEducation.objects.filter(fpo=fpo, ceo_education=i).exists():
                    obj = FpoCeoEducation.objects.get(fpo=fpo, ceo_education=i)
                    j_count = 0
                    for j in edu_doc:
                        if (i_count == j_count):
                            print('counter check')
                            image = Image.open(io.BytesIO(j.read()))
                            image.save(settings.BASE_DIR + '/media/fpo_ceo/fpo_ceo_education_documents/' + str(
                                i) + '.png')
                            obj.ceo_education_documents = 'fpo_ceo/fpo_ceo_education_documents/' + i + '.png'
                            obj.save()
                            print('obj saved....')
                        j_count = j_count + 1
                else:
                    j_count = 0
                    for j in edu_doc:
                        print('j loop')
                        if (i_count == j_count):
                            print('counter check')
                            image = Image.open(io.BytesIO(j.read()))
                            image.save(settings.BASE_DIR + '/media/fpo_ceo/fpo_ceo_education_documents/' + str(
                                i) + '.png')
                            obj = FpoCeoEducation.objects.create(fpo=fpo, ceo_education=i,
                                                         ceo_education_documents='fpo_ceo/fpo_ceo_education_documents/' + i + '.png')

                            print('objects saved for creation.')
                        j_count = j_count + 1
                        print('i',i_count,'j',j_count)
            i_count = i_count + 1

        form = FpoCeoForm(instance=fpo, data=request.POST, files=request.FILES)
        if form.is_valid():
            # form.save()
            print('form saved...')
        else:
            print(form.errors)

        # ceo_first_name = request.POST.get('ceo_first_name')
        # ceo_middle_name = request.POST.get('ceo_middle_name')
        # ceo_last_name = request.POST.get('ceo_last_name')
        # ceo_email_id = request.POST.get('ceo_email_id')
        # fpo1 = request.POST.getlist('ceo_education')
        # fpo2 = request.POST.get('fpo[1][ceo_education]')
        # fpo3 = request.POST.getlist('fpo[1][edu]')
        # print('fpo', fpo1, 'fpo2 is: ')

        # education = request.POST.getlist('education')
        # education_doc = request.POST.get('education_doc')
        # pan_card_number_doc = request.POST.get('pan_card_number_doc')
        # print(ceo_first_name, ceo_email_id, ceo_last_name, ceo_middle_name, 'repater is : ', fpo)
        # print('_' * 1000)
        # print(fpo, fpo2, fpo3)


def FpoRegistrationBasicDetailsView(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    form = FpoBasicDetails(instance=fpo)
    if request.method == 'POST':
        form = FpoBasicDetails(instance=fpo, data=request.POST)
        if form.is_valid():
            print('form valid')
            form.save()
            print('form saved')
            messages.success(request, 'FPO details added successfully')
            return redirect('app:profile')
        else:
            print(form.errors)


# fpo ca
def fpocadetailsView(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        form = FpoCaInformationForm(data=request.POST)
        if FpoCaInformation.objects.filter(fpo=fpo.id).exists():
            ca = FpoCaInformation.objects.get(fpo=fpo.id)
            form = FpoCaInformationForm(instance=ca, data=request.POST)
        if form.is_valid():
            print('form valid')
            obj = form.save(commit=False)
            obj.fpo = fpo
            obj.save()
            print('form saved')
            messages.success(request, ' FPO CA details added successfully')
        else:
            print(form.errors)
    return redirect('app:profile')


def FpoAddressDetailsView(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    form = FpoAddressDetails(instance=fpo)
    if request.method == 'POST':
        form = FpoAddressDetails(instance=fpo, data=request.POST)
        if form.is_valid():
            print('form valid')
            form.save()
            print('form saved')
            messages.success(request, 'FPO details added successfully')
            return redirect('app:profile')
        else:
            print(form.errors)


def FpoRegistrationView(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    form = FpoRegistration(instance=fpo)
    if request.method == 'POST':
        form = FpoRegistration(instance=fpo, data=request.POST)
        if form.is_valid():
            print('form valid')
            form.save()
            print('form saved')
            messages.success(request, 'FPO details added successfully')
            return redirect('app:profile')
        else:
            print(form.errors)


def FporegistrationdocumentView(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        coi_number = request.POST.get('coi_number')
        coi_doc = request.POST.get('coi_doc')
        pan_card_of_fpo = request.POST.get('pan_card_of_fpo')
        pan_card_doc_of_fpo = request.POST.get('pan_card_doc_of_fpo')
        tan_of_fpo = request.POST.get('tan_of_fpo')
        tan_doc_of_fpo = request.POST.get('tan_doc_of_fpo')
        moa = request.POST.get('moa')
        aoa = request.POST.get('aoa')
        gst_certificate = request.POST.get('gst_certificate')
        gst_certificate_doc = request.POST.get('gst_certificate_doc')
        udhyog_aadhar_number = request.POST.get('udhyog_aadhar_number')
        udhyog_aadhar_doc = request.POST.get('udhyog_aadhar_doc')
        form = RegistrationDocument(instance=fpo, data=request.POST, files=request.FILES)
        form.coi_number = coi_number
        form.coi_doc = coi_doc
        form.pan_card_of_fpo = pan_card_of_fpo
        form.pan_card_doc_of_fpo = pan_card_doc_of_fpo
        form.tan_of_fpo = tan_of_fpo
        form.tan_doc_of_fpo = tan_doc_of_fpo
        form.moa = moa
        form.aoa = aoa
        form.gst_certificate = gst_certificate
        form.gst_certificate_doc = gst_certificate_doc
        form.udhyog_aadhar_number = udhyog_aadhar_number
        form.udhyog_aadhar_doc = udhyog_aadhar_doc
        form.save()
        print('img saved')
        messages.success(request, 'FPO details added successfully')
        return redirect('app:profile')
    return redirect('app:profile')


def FpoofficeprofeView(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        address_profe = request.POST.get('office_address_proof')
        print(address_profe)
        print(type(address_profe))
        rent_agreement = request.POST.get('rent_agreement')
        fpo_photograph = request.POST.get('photo_graph_of_the_fpo')
        print('pass 1')
        if address_profe != '':  # and rent_agreement!='' and fpo_photograph!='':
            print('pass 2')
            # fpo.save()
            form = FpoOfficeprofe(instance=fpo, data=request.POST, files=request.FILES)
            if form.is_valid():
                print('val')
            else:
                print(form.errors)
            form.office_address_proof = address_profe
            form.rent_agreement = rent_agreement
            form.photo_graph_of_the_fpo = fpo_photograph
            if form.is_valid():
                print('val2')
            print('pass 3')
            form.save()
            print('img saved')
            messages.success(request, 'FPO details added successfully')
            return redirect('app:profile')
        return redirect('app:profile')
    return redirect('app:profile')


def subscriberdetailsView(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    print('fpo id is ', fpo.id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        contact_number = request.POST.get('contact_number')
        email_id = request.POST.get('email_id')
        photo = request.POST.get('photo')
        type = request.POST.get('inlineRadioOptions')
        print('the type is ', type)
        # if SubscriberDetails.objects.filter(fpo_name=fpo.id).exists():
        #     subs = SubscriberDetails.objects.get(fpo_name=fpo.id)
        #     form = SubscriberDetailsForm(instance=subs, data=request.POST, files=request.FILES)
        #     if form.is_valid():
        #         form.first_name = first_name
        #         form.middle_name = middle_name
        #         form.last_name = last_name
        #         form.contact_number = contact_number
        #         form.email_id = email_id
        #         form.photo = photo
        #         form.save()
        #         subs = SubscriberDetails.objects.get(email_id=email_id)
        #         subs.fpo_name = fpo
        #         subs.type = type
        #         subs.save()
        #         print('fpo Update')
        #     else:
        #         print(form.errors)
        # else:
        form = SubscriberDetailsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            subs = SubscriberDetails.objects.get(email_id=email_id)
            subs.fpo_name = fpo
            subs.type = type
            subs.save()
            print('fpo saved')
        else:
            print(form.errors)
        messages.success(request, 'FPO details added successfully')
    return redirect('app:profile')


import json
import PIL.Image as Image


def viewsubscriberdocdetailsView(request, id):
    if SubscriberDetails.objects.filter(id=id).exists():
        subs = SubscriberDetails.objects.get(id=id)
        # res = {'first_name': subs.first_name, 'middle_name': subs.middle_name, 'last_name': subs.last_name,
        #        'contact_number': str(subs.contact_number), 'email_id': subs.email_id, 'photo': subs.photo.url,
        #        'aadhar_card_number': subs.aadhar_card_number, 'aadhar_card_doc': subs.aadhar_card_doc.url,
        #        'pan_card_number': subs.pan_card_number, 'pan_card_doc': subs.pan_card_doc.url,
        #        'land_holding': subs.land_holding, 'land_holding_doc': subs.land_holding_doc.url,
        #        'khasra_number': subs.khasra_number, 'khasra_number_doc': subs.khasra_number_doc.url,
        #        'gender': subs.gender, 'category': subs.category,  # 'fpo_name': subs.fpo_name
        #        }
        print(request.method)
        if request.method == 'POST':
            updateaadhar = request.POST.get('updateaadhar')
            update_aadhar_doc = request.FILES['update_aadhar_doc'].read()
            update_pan = request.POST.get('update_pan')
            update_pan_doc = request.FILES['update_pan_doc'].read()
            update_land_holding = request.POST.get('update_land_holding')
            update_land_holding_doc = request.FILES['update_land_holding_doc'].read()
            khasra_number = request.POST.get('khasra_number')
            khasra_number_doc = request.FILES['khasra_number_doc'].read()
            if updateaadhar != '':
                subs.aadhar_card_number = updateaadhar
            if update_aadhar_doc != '':
                image = Image.open(io.BytesIO(update_aadhar_doc))
                image.save(settings.BASE_DIR + '/media/subscriberdetails/aadhar_card_documents/' + str(
                    subs.first_name) + '.png')
                subs.aadhar_card_doc = '/subscriberdetails/aadhar_card_documents/' + str(subs.first_name) + '.png'
            if update_pan != '':
                subs.pan_card_number = update_pan
            if update_pan_doc != '':
                image = Image.open(io.BytesIO(update_pan_doc))
                image.save(settings.BASE_DIR + '/media/subscriberdetails/pan_card_documents/' + str(
                    subs.first_name) + '.png')
                subs.pan_card_doc = '/subscriberdetails/pan_card_documents/' + str(subs.first_name) + '.png'
            if update_land_holding != '':
                subs.land_holding = update_land_holding
            if update_land_holding_doc != '':
                image = Image.open(io.BytesIO(update_land_holding_doc))
                image.save(settings.BASE_DIR + '/media/subscriberdetails/land_holding_documents/' + str(
                    subs.first_name) + '.png')
                subs.land_holding_doc = '/subscriberdetails/land_holding_documents/' + str(subs.first_name) + '.png'
            if khasra_number != '':
                subs.khasra_number = khasra_number
            if khasra_number_doc != '':
                image = Image.open(io.BytesIO(khasra_number_doc))
                image.save(settings.BASE_DIR + '/media/subscriberdetails/khasra_number_documents/' + str(
                    subs.first_name) + '.png')
                subs.khasra_number_doc = '/subscriberdetails/khasra_number_documents/' + str(subs.first_name) + '.png'
            subs.save()
            print('form saved')
            return redirect('app:profile')

        # return HttpResponse(json.dumps(res))


def viewsubscriberdetailsView(request, id):
    if SubscriberDetails.objects.filter(id=id).exists():
        subs = SubscriberDetails.objects.get(id=id)
        res = {'first_name': subs.first_name, 'middle_name': subs.middle_name, 'last_name': subs.last_name,
               'contact_number': subs.contact_number, 'email_id': subs.email_id, 'photo': subs.photo.url,
               'aadhar_card_number': subs.aadhar_card_number, 'aadhar_card_doc': subs.aadhar_card_doc.url,
               'pan_card_number': subs.pan_card_number, 'pan_card_doc': subs.pan_card_doc.url,
               'land_holding': subs.land_holding, 'land_holding_doc': subs.land_holding_doc.url,
               'khasra_number': subs.khasra_number, 'khasra_number_doc': subs.khasra_number_doc.url,
               'gender': subs.gender, 'category': subs.category, 'id': subs.id  # 'fpo_name': subs.fpo_name
               }
        if request.method == 'POST':
            fusername = request.POST.get('updatefirstname')
            musername = request.POST.get('updatemiddlename')
            lusername = request.POST.get('updatelastname')
            useremail = request.POST.get('updateemail')
            subscategory = request.POST.get('updatecategory')
            usergender = request.POST.get('updategender')
            usercontact = request.POST.get('updatecontact')
            userphoto = request.FILES['updatephoto'].read()
            image = Image.open(io.BytesIO(userphoto))
            image.save(settings.BASE_DIR + '/media/subscriberdetails/photo/' + fusername + '.png')
            if fusername != '':
                subs.first_name = fusername
            if musername != '':
                subs.middle_name = musername
            if lusername != '':
                subs.last_name = lusername
            if usercontact != '':
                subs.contact_number = usercontact
            if useremail != '':
                subs.email_id = useremail
            if userphoto != '':
                subs.photo = '/subscriberdetails/photo/' + fusername + '.png'
            if usergender != '':
                subs.gender = usergender
            if subscategory != '':
                subs.category = subscategory
            subs.save()
            print('form saved')
            return redirect('app:profile')
        return HttpResponse(json.dumps(res))

        # return HttpResponse(form.as_p())


def profileaddressprofe(request):
    fpo = FPO.objects.get(user_id=request.user.id)
    form = FpoOfficeprofe(instance=fpo)
    if request.method == 'POST':
        form = FpoOfficeprofe(instance=fpo, data=request.POST, files=request.FILES)

        img = request.FILES.getlist('office_address_proof')
        # print(request.FILES.getlist('office_address_proof'))
        for i in img:
            # print(i)
            BankStatementUpload(fpo=fpo, bank_statement_doc=i).save()
        if 10 > 5:
            pass
            # if form.is_valid():
            # img = form.cleaned_data['office_address_proof']
            # print('val of img is :',img)
            # for i in img:
            #     print(i)
            #     BankStatementUpload(fpo=fpo,bank_statement_doc=i).save()
            # form.save()
            # print('form saved')
            messages.success(request, 'FPO details added successfully')
            return redirect('app:home')
        else:
            print(form.errors)
    return render(request, 'app/try.html', {'form': form})


# @login_required(login_url='/user/login')
# def Fpo(request):
#     if request.user.is_superuser:
#         # fpo = FPO.objects.all()
#         fpo=CustomUser.objects.filter(role='admin', )
#         return render(request, 'app/FPO.html', {'username': request.user, 'fpo': fpo})
#     else:
#         return redirect('app:home')


class Fpo(ListView):
    context_object_name = 'fpo'
    template_name = 'app/FPO.html'
    paginate_by = 10
    model = FPO

    def get_queryset(self):
        object_list = ''
        # if self.model.objects.filter(status=True).exists():
        #     object_list = self.model.objects.filter(status=True)
        object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Fpo, self).get_context_data(**kwargs)
        context['username'] = self.request.user
        return context

    @method_decorator(login_required(login_url='/user/login'))
    def dispatch(self, request, *args, **kwargs):
        return super(Fpo, self).dispatch(request, *args, **kwargs)


@login_required(login_url='/user/login')
def farmer(request):
    farmer = ''
    if request.user.role == 'admin':
        if (FPO.objects.filter(user_id=request.user.id).exists()):
            fpo = FPO.objects.get(user_id=request.user.id)
            if Farmer.objects.filter(fpo_name=fpo).exists():
                farmer = Farmer.objects.filter(fpo_name=fpo, delete_status=True)
            else:
                return Response()
    if request.user.is_superuser:
        farmer = Farmer.objects.filter(delete_status=True)
    paginator = Paginator(farmer, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/Farmer.html', {'username': request.user, 'farmer': farmer, 'page_obj': page_obj})


def pageaccount(request):
    form2 = FpoCreationForm2()
    form = FpoCreationForm()
    if request.user.role == 'admin':
        user = CustomUser.objects.get(id=request.user.id)
        fpo = FPO.objects.get(user_id=user)
        form2 = FpoCreationForm2(instance=fpo)
        form = FpoCreationForm(instance=user)
    return render(request, 'html/ltr/vertical-menu-template/page-account-settings.html',
                  {'username': request.user, 'form': form, 'form2': form2
                   })


def createfpo(request):
    if request.user.is_superuser:
        form = FpoCreationForm()
        # form2 = FpoCreationForm2()
        # print(request.method)
        if request.method == "POST":
            form = FpoCreationForm(request.POST, request.FILES)
            # form2 = FpoCreationForm2(request.POST, request.FILES)
            email = request.POST.get('email')

            if (CustomUser.objects.filter(email=email).exists()):
                messages.error(request, 'Email already register')
            else:
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.role = 'admin'
                    obj.save()
                    user = CustomUser.objects.get(email=email)
                    state = State.objects.get(id=1)
                    district = District.objects.get(id=1)
                    block = City.objects.get(id=1)
                    fpo = FPO(user_id=user, state=state, district=district, block=block)
                    fpo.save()

                # if form2.is_valid():
                #     print('form2 is valid')
                #     first_name = form.cleaned_data['first_name']
                #     print('form one is valid', first_name)
                #     email = request.POST.get('email')
                #     password = request.POST.get('password1')
                #     company_name = form2.cleaned_data['company_name']
                #     implementing_agency = form2.cleaned_data['implementing_agency']
                #     state_category = form2.cleaned_data['state_category']
                #     state = form2.cleaned_data['state']
                #     district = form2.cleaned_data['district']
                #     block = form2.cleaned_data['block']
                #     full_address = form2.cleaned_data['full_address']
                #     date_of_incorporation = form2.cleaned_data['date_of_incorporation']
                #     no_of_bods = form2.cleaned_data['no_of_bods']
                #     pan_card_no = form2.cleaned_data['pan_card_no']
                #     pan_docs = form2.cleaned_data['pan_docs']
                #     tan_no = form2.cleaned_data['tan_no']
                #     tan_docs = form2.cleaned_data['tan_docs']
                #     gst_no = form2.cleaned_data['gst_no']
                #     cin_no = form2.cleaned_data['cin_no']
                #     authorise_share_capital = form2.cleaned_data['authorise_share_capital']
                #     issued_shared_capital = form2.cleaned_data['issued_shared_capital']
                #     mca_docs = form2.cleaned_data['mca_docs']
                #     bank_name = form2.cleaned_data['bank_name']
                #     branch_name = form2.cleaned_data['branch_name']
                #     ifsc_code = form2.cleaned_data['ifsc_code']
                #     bank_account = form2.cleaned_data['bank_account']
                #     account_holder_name = form2.cleaned_data['account_holder_name']
                #     bank_docs = form2.cleaned_data['bank_docs']
                #     authorise_signatory_in_bank = form2.cleaned_data['authorise_signatory_in_bank']
                #     mobile_number = form2.cleaned_data['mobile_number']
                #     mobile_no_registered_with_email = form2.cleaned_data['mobile_no_registered_with_email']
                #     email_created_by = form2.cleaned_data['email_created_by']
                #     company_moa = form2.cleaned_data['company_moa']
                #     company_aoa = form2.cleaned_data['company_aoa']
                #     fpo_registration_no = form2.cleaned_data['fpo_registration_no']
                #     fpo_registration_remarks = form2.cleaned_data['fpo_registration_remarks']
                #     villages_covered_under_fpo = form2.cleaned_data['villages_covered_under_fpo']
                #     dmc_approval_status = form2.cleaned_data['dmc_approval_status']
                #     special_allocation = form2.cleaned_data['special_allocation']
                #     primary_crop_approved_by_dmc_or_as_per_dpr = form2.cleaned_data[
                #         'primary_crop_approved_by_dmc_or_as_per_dpr']
                #     secondary_crop_approved_by_dmc_or_as_per_dpr = form2.cleaned_data[
                #         'secondary_crop_approved_by_dmc_or_as_per_dpr']
                #     status_of_baseline_survey = form2.cleaned_data['status_of_baseline_survey']
                #     status_board_meamber_identification = form2.cleaned_data['status_board_meamber_identification']
                #     is_woman_centric = form2.cleaned_data['is_woman_centric']
                #     fpo_formed = form2.cleaned_data['fpo_formed']
                #     registration_act = form2.cleaned_data['registration_act']
                #     fpo_office_village_name = form2.cleaned_data['fpo_office_village_name']
                #     fpo_office_post_office = form2.cleaned_data['fpo_office_post_office']
                #     pin_code = form2.cleaned_data['pin_code']
                #     fpo_udyog_aadhaar = form2.cleaned_data['fpo_udyog_aadhaar']
                #     status_of_ca_appointing = form2.cleaned_data['status_of_ca_appointing']
                #     name_of_ca = form2.cleaned_data['name_of_ca']
                #     mobile_no_of_ca = form2.cleaned_data['mobile_no_of_ca']
                #     email_id_of_ca = form2.cleaned_data['email_id_of_ca']
                #     status_ceo_appointment = form2.cleaned_data['status_ceo_appointment']
                #     fpo_ceo_name = form2.cleaned_data['fpo_ceo_name']
                #     fpo_ceo_mobile_number = form2.cleaned_data['fpo_ceo_mobile_number']
                #     fpo_ceo_email_id = form2.cleaned_data['fpo_ceo_email_id']
                #     status_accountant_appointment = form2.cleaned_data['status_accountant_appointment']
                #     fpo_accountant_name = form2.cleaned_data['fpo_accountant_name']
                #     fpo_accountant_mobile_number = form2.cleaned_data['fpo_accountant_mobile_number']
                #     fpo_accountant_email_id = form2.cleaned_data['fpo_accountant_email_id']
                #     no_of_farmer_mobilized = form2.cleaned_data['no_of_farmer_mobilized']
                #     no_of_share_member = form2.cleaned_data['no_of_share_member']
                #     total_equity_amount = form2.cleaned_data['total_equity_amount']
                #     register_on_enam = form2.cleaned_data['register_on_enam']
                #     name_of_mandi = form2.cleaned_data['name_of_mandi']
                #     no_of_board_meetings = form2.cleaned_data['no_of_board_meetings']
                #     dates_of_board_meeting = form2.cleaned_data['dates_of_board_meeting']
                #     first_general_board_meetings = form2.cleaned_data['first_general_board_meetings']
                #     obtained_commencement_end_of_bussiness_certificate = form2.cleaned_data[
                #         'obtained_commencement_end_of_bussiness_certificate']
                #     additional_services_proposed_by_fpo = form2.cleaned_data['additional_services_proposed_by_fpo']
                #     bussiness_plan = form2.cleaned_data['bussiness_plan']
                #     bussiness_transation_details = form2.cleaned_data['bussiness_transation_details']
                #     bussiness_transation_ammount_details = form2.cleaned_data['bussiness_transation_ammount_details']
                #     fig_creation_remarks = form2.cleaned_data['fig_creation_remarks']
                #     if (CustomUser.objects.filter(email=email).exists()):
                #         messages.error(request, 'Email already register')
                #     else:
                #         pass
                #         user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name,
                #                                               role='admin')
                #         user.save()
                #         pre_email = CustomUser.objects.get(email=email)
                #         print(pre_email)
                #         fpo = FPO(user_id=pre_email, created_by=request.user, account_holder_name=account_holder_name,
                #                   additional_services_proposed_by_fpo=additional_services_proposed_by_fpo,
                #                   authorise_share_capital=authorise_share_capital,
                #                   authorise_signatory_in_bank=authorise_signatory_in_bank, bank_name=bank_name,
                #                   bank_account=bank_account, block=block, branch_name=branch_name,
                #                   bussiness_plan=bussiness_plan,
                #                   bussiness_transation_ammount_details=bussiness_transation_ammount_details,
                #                   bussiness_transation_details=bussiness_transation_details,
                #                   cin_no=cin_no, company_aoa=company_aoa, company_moa=company_moa,
                #                   company_name=company_name, date_of_incorporation=date_of_incorporation,
                #                   dates_of_board_meeting=dates_of_board_meeting,
                #                   dmc_approval_status=dmc_approval_status, email_created_by=email_created_by,
                #                   email_id_of_ca=email_id_of_ca,
                #                   fig_creation_remarks=fig_creation_remarks,
                #                   first_general_board_meetings=first_general_board_meetings,
                #                   fpo_accountant_name=fpo_accountant_name,
                #                   fpo_accountant_email_id=fpo_accountant_email_id,
                #                   fpo_accountant_mobile_number=fpo_accountant_mobile_number,
                #                   fpo_ceo_email_id=fpo_ceo_email_id,
                #                   fpo_ceo_mobile_number=fpo_ceo_mobile_number, fpo_ceo_name=fpo_ceo_name,
                #                   fpo_formed=fpo_formed, fpo_office_village_name=fpo_office_village_name,
                #                   fpo_office_post_office=fpo_office_post_office,
                #                   fpo_registration_no=fpo_registration_no,
                #                   fpo_registration_remarks=fpo_registration_remarks,
                #                   fpo_udyog_aadhaar=fpo_udyog_aadhaar, full_address=full_address, gst_no=gst_no,
                #                   ifsc_code=ifsc_code, implementing_agency=implementing_agency,
                #                   is_woman_centric=is_woman_centric, issued_shared_capital=issued_shared_capital,
                #                   mca_docs=mca_docs, mobile_no_of_ca=mobile_no_of_ca,
                #                   mobile_no_registered_with_email=mobile_no_registered_with_email,
                #                   name_of_ca=name_of_ca, name_of_mandi=name_of_mandi,
                #                   no_of_board_meetings=no_of_board_meetings,
                #                   no_of_bods=no_of_bods, no_of_farmer_mobilized=no_of_farmer_mobilized,
                #                   no_of_share_member=no_of_share_member, pan_docs=pan_docs,
                #                   obtained_commencement_end_of_bussiness_certificate=obtained_commencement_end_of_bussiness_certificate,
                #                   pan_card_no=pan_card_no,
                #                   pin_code=pin_code,
                #                   primary_crop_approved_by_dmc_or_as_per_dpr=primary_crop_approved_by_dmc_or_as_per_dpr,
                #                   register_on_enam=register_on_enam,
                #                   registration_act=registration_act,
                #                   secondary_crop_approved_by_dmc_or_as_per_dpr=secondary_crop_approved_by_dmc_or_as_per_dpr,
                #                   special_allocation=special_allocation,
                #                   state=state, state_category=state_category,
                #                   status_accountant_appointment=status_accountant_appointment,
                #                   status_board_meamber_identification=status_board_meamber_identification,
                #                   status_ceo_appointment=status_ceo_appointment,
                #                   status_of_baseline_survey=status_of_baseline_survey,
                #                   status_of_ca_appointing=status_of_ca_appointing, tan_docs=tan_docs,
                #                   tan_no=tan_no, total_equity_amount=total_equity_amount,
                #                   villages_covered_under_fpo=villages_covered_under_fpo, district=district,
                #                   mobile_number=mobile_number)
                #         fpo.save()
                #         print('form saved...')
                #         messages.success(request, 'FPO added successfully')
                # else:
                #     print(form2.errors)
                # return redirect('app:Fpo')
            # else:
            #     print(form.errors)
            #     messages.warning(request, form.errors)
        return render(request, 'app/fpocreation.html', {'username': request.user, 'form': form})
    else:
        return redirect('app:home')


# def createfarmer(request):
#     form=FarmerForm()
#     print(request.method)
#     # print(request.user.FPO)
#     fpo = FPO.objects.all()
#     if request.method == "POST":
#         form = FpoCreationForm(request.POST)
#         if form.is_valid():
#             print('form validate')
#             # form.save()
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             print(first_name)
#             email = request.POST.get('email')
#             password = request.POST.get('password1')
#             user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name,
#                                                   last_name=last_name)
#             user.save()
#             pre_email = CustomUser.objects.get(email=email)
#             if request.user.role == 'admin':
#                 fpo = FPO.objects.get(user_id=request.user.id)
#                 print('asdasdasdasdadad', fpo.id)
#                 farmer = Farmer(user_id=pre_email, fpo_id=fpo)
#                 farmer.save()
#                 print('form saved...')
#                 messages.success(request, 'Farmer added successfully')
#                 return redirect('app:farmer')
#             if request.user.is_superuser:
#                 fpo = request.POST.get('exampleFormControlSelect1')
#                 print('rjbnkjahajlhj', fpo)
#                 fpo1 = FPO.objects.get(id=fpo)
#                 print('asdasdasdasdadad', fpo1.id)
#                 farmer = Farmer(user_id=pre_email, fpo_id=fpo1)
#                 farmer.save()
#                 print('form saved...')
#                 messages.success(request, 'Farmer added successfully')
#                 return redirect('app:farmer')
#         else:
#             print(form.errors)
#     return render(request, 'app/farmercreation.html', {'username': request.user, 'form': form, 'fpo': fpo})

def createfarmer(request):
    form = FarmerForm()
    fpo = FPO.objects.get(user_id=request.user.id)
    print(request.method)
    if request.method == "POST":
        form = FarmerForm(request.POST)
        print('first')
        if form.is_valid():
            print('form Validate')
            obj = form.save(commit=False)
            obj.fpo_name = fpo
            obj.fpo_registration_no = fpo.fpo_registration_no
            obj.save()
            print('form saved')
            messages.success(request, 'Farmer added successfully')
            return redirect('app:farmer')
        else:
            print(form.errors)
    return render(request, 'app/farmercreation.html', {'username': request.user, 'form': form, })


def inactivatefpo(request, id):
    if FPO.objects.filter(id=id).exists():
        fpo = FPO.objects.get(id=id)
        print('fpo get')
        if CustomUser.objects.filter(id=fpo.user_id.id).exists():
            user = CustomUser.objects.get(id=fpo.user_id.id)
            print('user get', user.is_active)
            if user.is_active:
                user.is_active = 0
                user.save()
                messages.success(request, 'FPO inactivate')
            else:
                user.is_active = 1
                user.save()
                messages.success(request, 'FPO activate.')
        else:
            return redirect('app:Fpo')
    else:
        return redirect('app:Fpo')
    # fpo.status = False
    # fpo.save()

    return redirect('app:Fpo')


def inactivatefarmer(request, id):
    if Farmer.objects.filter(id=id).exists():
        farmer = Farmer.objects.get(id=id)
        farmer.delete_status = False
        farmer.save()
    else:
        return redirect('app:farmer')
    messages.success(request, 'Farmer remove successfully.')
    return redirect('app:farmer')


def editfpo(request, id):
    print('the fpo id is ', id)
    if FPO.objects.filter(id=id).exists():
        if request.user.is_superuser:
            user = ''
            fpo = FPO.objects.get(id=id)
            if CustomUser.objects.filter(email=fpo.user_id).exists():
                user = CustomUser.objects.get(email=fpo.user_id)
            form2 = FpoCreationForm2(instance=fpo)
            form = FpoCreationForm(instance=user)
            if request.method == "POST":
                form2 = FpoCreationForm2(instance=fpo, data=request.POST)
                form = FpoCreationForm(instance=user, data=request.POST)
                if form2.is_valid():
                    form2.save()
                    user.first_name = request.POST.get('first_name')
                    email = request.POST.get('email')
                    if email != '':
                        user.email = request.POST.get('email')
                    user.save()
                    messages.success(request, 'FPO updated successfully')
                    return redirect('app:Fpo')
                else:
                    messages.warning(request, 'FPO not updated')
                    return redirect('app:Fpo')
            return render(request, 'app/editfpo.html', {'username': request.user, 'form2': form2, 'form': form})
        else:
            return redirect('app:home')
    else:
        return redirect('app:home')


def delfpo(request, id):
    if request.user.is_superuser:
        if FPO.objects.filter(id=id).exists():
            fpo = FPO.objects.get(id=id)
            if CustomUser.objects.filter(id=fpo.user_id.id).exists():
                user = CustomUser.objects.get(id=fpo.user_id.id)
                user.delete_status = False
                user.is_active = False
                user.save()
                messages.success(request, 'FPO deleted successfully')
                return redirect('app:Fpo')
            else:
                messages.success(request, 'FPO user account not found')
                return redirect('app:Fpo')
        else:
            messages.success(request, 'FPO not found')
            return redirect('app:Fpo')
    else:
        messages.success(request, "you are not authorised to perform this operations ")
        return redirect('app:Fpo')


from django.shortcuts import get_object_or_404


def editfarmer(request, id):
    print(id)
    if Farmer.objects.filter(id=id).exists():
        farmer = get_object_or_404(Farmer, pk=id)
        print(farmer)
        form = FarmerForm(instance=farmer)
        if request.method == "POST":
            form = FarmerForm(instance=farmer, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Farmer updated successfully')
                return redirect('app:Fpo')
            else:
                print(form.errors)
        return render(request, 'app/editfarmer.html', {'username': request.user, 'form': form})
    else:
        return redirect('app:home')


def report(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    for i in range(10):
        writer.writerow(['Second row', 'A', 'B', 'C'])

    return response


def fporeport(request):
    fpo = FPO.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Fpo_report.csv"'

    writer = csv.writer(response)
    writer.writerow(
        ['Name', 'Email', 'Company Name', 'Implementing Agency', 'State Category', 'State', 'District', 'Block',
         'Full Address', 'Date of Incorporation',
         'No of Bods', 'Pan Card No', 'Pan Docs', 'Tan No', 'Tan Docs', 'Gst No', 'Cin No', 'Authorise Share Capital',
         'Issued Shared Capital',
         'Mca Docs', 'Bank Name', 'Branch Name', 'IFSC Code', 'Bank Account', 'Account Holder Name', 'Bank Docs',
         'Authorise Signatory In Bank',
         'Mobile Number', 'Mobile No Registered With Email', 'Email Created By', 'Company Moa', 'Company Aoa',
         'Fpo Registration No', 'Fpo Registration Remarks',
         'Villages Covered Under Fpo', 'Dmc Approval Status', 'Special Allocation',
         'Primary Crop Approved By Dmc Or As Per Dpr',
         'Secondary Crop Approved By Dmc Or As Per Dpr', 'Status Of Baseline Survey',
         'Status Board Meamber Identification',
         'Is Woman Centric', 'Fpo Formed', 'Registration Act', 'Fpo Office Village Name', 'Fpo Office Post Office',
         'Pin Code', 'Fpo Udyog Aadhaar', 'Status Of Ca Appointing', 'Name Of Ca', 'Mobile No Of Ca', 'Email Id Of Ca',
         'Status Ceo Appointment',
         'Fpo Ceo Name', 'Fpo Ceo Mobile Number', 'Fpo Ceo Email Id', 'Status Aaccountant Appointment',
         'Fpo Accountant Name', 'Fpo Accountant Mobile Number',
         'Fpo Accountant Email Id', 'No Of_Farmer Mobilized', 'No Of Share Member', 'Total Equity Amount',
         'Register On Enam', 'Name Of Mandi',
         'No Of Board Meetings', 'Dates Of Board Meeting', 'First General Board Meetings',
         'Obtained Commencement End Of Bussiness Certificate',
         'Additional Services Proposed By Fpo', 'Bussiness Plan', 'Bussiness Transation Details',
         'Bussiness Transation Ammount Details', 'Fig Creation Remarks'])
    for i in fpo:
        date_of_incorporation = str(i.date_of_incorporation)
        writer.writerow(
            [i.user_id.first_name, i.user_id.email, i.company_name, i.implementing_agency, i.state_category, i.state,
             i.district, i.block,
             i.full_address, date_of_incorporation,
             i.no_of_bods, i.pan_card_no, i.pan_docs, i.tan_no, i.tan_docs, i.gst_no, i.cin_no,
             i.authorise_share_capital,
             i.issued_shared_capital,
             i.mca_docs, i.bank_name, i.branch_name, i.ifsc_code, i.bank_account, i.account_holder_name, i.bank_docs,
             i.authorise_signatory_in_bank,
             i.mobile_number, i.mobile_no_registered_with_email, i.email_created_by, i.company_moa, i.company_aoa,
             i.fpo_registration_no, i.fpo_registration_remarks,
             i.villages_covered_under_fpo, i.dmc_approval_status, i.special_allocation,
             i.primary_crop_approved_by_dmc_or_as_per_dpr,
             i.secondary_crop_approved_by_dmc_or_as_per_dpr, i.status_of_baseline_survey,
             i.status_board_meamber_identification,
             i.is_woman_centric, i.fpo_formed, i.registration_act, i.fpo_office_village_name, i.fpo_office_post_office,
             i.pin_code, i.fpo_udyog_aadhaar, i.status_of_ca_appointing, i.name_of_ca, i.mobile_no_of_ca,
             i.email_id_of_ca,
             i.status_ceo_appointment,
             i.fpo_ceo_name, i.fpo_ceo_mobile_number, i.fpo_ceo_email_id, i.status_accountant_appointment,
             i.fpo_accountant_name, i.fpo_accountant_mobile_number,
             i.fpo_accountant_email_id, i.no_of_farmer_mobilized, i.no_of_share_member, i.total_equity_amount,
             i.register_on_enam, i.name_of_mandi,
             i.no_of_board_meetings, i.dates_of_board_meeting, i.first_general_board_meetings,
             i.obtained_commencement_end_of_bussiness_certificate,
             i.additional_services_proposed_by_fpo, i.bussiness_plan, i.bussiness_transation_details,
             i.bussiness_transation_ammount_details, i.fig_creation_remarks])
    return response


def farmerreport(request):
    if request.user.is_superuser:
        farmer = Farmer.objects.filter(delete_status=True)
    elif request.user.role == 'admin':
        fpo = FPO.objects.get(user_id=request.user.id)
        farmer = Farmer.objects.filter(fpo_name=fpo, delete_status=True)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Fpo_report.csv"'

    writer = csv.writer(response)
    writer.writerow(
        ['fpo_name', 'si_no_of_share_holder', 'share_holder_name', 'state', 'district', 'block', 'gram_panchayat',
         'fpo_registration_no', 'farmer_name', 'fig_name', 'village', 'pg_name', 'hamlet', 'hh_name',
         'father_and_husband_name',
         'gender', 'age', 'category', 'member_of_fig', 'name_of_the_fig', 'bpl_status',
         'have_you_received_aadhar_card_consent',
         'aadhar_card_no', 'bank_account_no', 'number_of_family_member', 'annual_income', 'livestock_income',
         'labour', 'ntfp', 'micro_enterprise', 'other_income', 'member_of_cooperative_agriculture_societies',
         'total_land', 'land_record_details', 'upland_irrigated', 'medium_upland_irrigated', 'low_land_irrigated',
         'leased_land', 'leased_land_area', 'year_of_share_issued', 'generate_share_certificate_number',
         'distinctive_total_number_of_share', 'total_capital_amount_deposited', 'nominee', 'relationship_with_nominee',
         'address_of_the_nominee', 'ivrs_or_other_alerts', 'mobile_number', 'dob_of_farmer', 'social_category',
         'kharif_crop', 'sowing_month', 'marketing_month', 'robi_crop', 'zayed_crop', 'names_of_agri_machinery_owner',
         'name_of_market', 'Livestock_activity', 'byp_number', 'shed_type', 'vaccine_interval', 'tagging_status',
         'pig_number', 'cow_number', 'buffalo_number', 'face_value_of_share', 'mambers_hip_amount_paid',
         'premium_amount_paid', 'any_entrepreneural_activity', 'packhouse_available', 'drying_yard_available',
         'other_livelihood', 'poly_or_shed_house', 'any_commerical_vehicle', 'onwed_vehicle', 'house_type',
         'aadhar_attached', 'pan_attached', 'bank_details_attached', 'land_records_attached'])
    for i in farmer:
        writer.writerow(

            [i.fpo_name, i.si_no_of_share_holder, i.share_holder_name, i.state, i.district, i.block, i.gram_panchayat,
             i.fpo_registration_no, i.farmer_name, i.fig_name, i.village, i.pg_name, i.hamlet, i.hh_name,
             i.father_and_husband_name,
             i.gender, i.age, i.category, i.member_of_fig, i.name_of_the_fig, i.bpl_status,
             i.have_you_received_aadhar_card_consent,
             i.aadhar_card_no, i.bank_account_no, i.number_of_family_member, i.annual_income, i.livestock_income,
             i.labour, i.ntfp, i.micro_enterprise, i.other_income, i.member_of_cooperative_agriculture_societies,
             i.total_land, i.land_record_details, i.upland_irrigated, i.medium_upland_irrigated, i.low_land_irrigated,
             i.leased_land, i.leased_land_area, i.year_of_share_issued, i.generate_share_certificate_number,
             i.distinctive_total_number_of_share, i.total_capital_amount_deposited, i.nominee,
             i.relationship_with_nominee,
             i.address_of_the_nominee, i.ivrs_or_other_alerts, i.mobile_number, i.dob_of_farmer, i.social_category,
             i.kharif_crop, i.sowing_month, i.marketing_month, i.robi_crop, i.zayed_crop,
             i.names_of_agri_machinery_owner,
             i.name_of_market, i.Livestock_activity, i.byp_number, i.shed_type, i.vaccine_interval, i.tagging_status,
             i.pig_number, i.cow_number, i.buffalo_number, i.face_value_of_share, i.mambers_hip_amount_paid,
             i.premium_amount_paid, i.any_entrepreneural_activity, i.packhouse_available, i.drying_yard_available,
             i.other_livelihood, i.poly_or_shed_house, i.any_commerical_vehicle, i.onwed_vehicle, i.house_type,
             i.aadhar_attached, i.pan_attached, i.bank_details_attached, i.land_records_attached])
    return response


@api_view()
def lsa(request):
    fpo = FPO.objects.all()
    se = FpoSerializer(fpo, many=True)
    return JsonResponse(se.data, safe=False)


import base64
from django.core.files.base import ContentFile
import os


def videocapture(request):
    image_data = 'data:image/png;base64,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'
    format, imgstr = image_data.split(';base64,')
    print("format", format)
    ext = format.split('/')[-1]

    data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
    file_name = "'myphoto." + ext
    print(file_name)
    fpo = FPO.objects.get(user_id=request.user.id)
    form = FpoOfficeprofe(instance=fpo)
    BankStatementUpload(fpo=fpo, bank_statement_doc=data).save()
    return render(request, 'app/demo.html')
