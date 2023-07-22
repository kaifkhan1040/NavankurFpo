from users.models import CustomUser
from django import forms
from django.forms import ModelForm, TextInput, EmailInput, CharField, PasswordInput, ChoiceField, BooleanField, \
    NumberInput, DateInput,Textarea
from django.contrib.auth.forms import UserCreationForm
from .models import State, District, FPO, Farmer, Cbbo, Ia, SubscriberDetails, FpoCaInformation, FpoCeoEducation, \
    FpoBankDetails, Bank, AuthorisedSharedCapital, IssuedSharedCapital, CompnayMeetingDetails


# use both fpo and farmer creation
# form for FPO registation
class FpoCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = ['email', 'password1', 'password2']
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        # fields="__all__"
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name',
                'required': 'required',
            }),
            'last_name': TextInput(attrs={
                'class': "form-control mb-2",
                'style': 'max-width: 100%;',
                'placeholder': 'Name'
            }),
            'email': EmailInput(attrs={
                'class': "form-control ",
                'style': 'max-width: 100%;',
                'placeholder': 'Your Email'
            }),

        }


state_choise = [(i.state_title, i) for i in State.objects.all()]
district_choise = [(i.district_title, i) for i in District.objects.all()]
# block_choise = [(i.name, i) for i in City.objects.all()]
block_choise = ''
pandos = (
    (True, 'Yes'),
    (False, 'No')
)
tandos = (
    (True, 'Yes'),
    (False, 'No')
)
mcados = (
    (True, 'Yes'),
    (False, 'No')
)
bankdos = (
    (True, 'Yes'),
    (False, 'No')
)
moa = (
    (True, 'Yes'),
    (False, 'No')
)
dmc_approval = (
    (True, 'Yes'),
    (False, 'No')
)
baseline_survey = (
    (True, 'Yes'),
    (False, 'No')
)
board_meamber_identification = (
    (True, 'Yes'),
    (False, 'No')
)
woman_centric = (
    (True, 'Yes'),
    (False, 'No')
)
fpoformed = (
    (True, 'Yes'),
    (False, 'No')
)
ca_appointing = (
    (True, 'Yes'),
    (False, 'No')
)
accountant_appointment = (
    (True, 'Yes'),
    (False, 'No')
)
enam = (
    (True, 'Yes'),
    (False, 'No')
)
plan_bussiness = (
    (True, 'Yes'),
    (False, 'No')
)

## form for basic information recived by FPO models

class FpoCreationForm2(forms.ModelForm):
    class Meta:
        model = FPO
        fields = "__all__"
        exclude = ('created_by', 'user_id', 'status')
        widgets = {
            'company_name': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter compnay name',
                'required': 'required',
            }),
            'implementing_agency': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter implementing_agency',
                'required': 'required',
            }),
            'state_category': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter State type eg. hilly',
                'required': 'required',
            }),
            'state': forms.Select(choices=state_choise, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'district': forms.Select(choices=district_choise, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'block': forms.Select(choices=block_choise, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'full_address': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter Full address',
                'required': 'required',
            }),
            'date_of_incorporation': DateInput(attrs={
                'type': 'date',
                'class': "form-control mb-2",
                'placeholder': 'Enter Date of Incorporation',
                'required': 'required',
            }),
            'no_of_bods': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '5',
                'minlength': '1',
                'class': "form-control mb-2",
                'placeholder': '12321122',
                'required': 'required',
            }),
            'pan_card_no': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '10',
                'class': "form-control mb-2",
                'placeholder': ' Enter pan card number eg:12321122',
                'required': 'required',
            }),
            'pan_docs': forms.Select(choices=pandos, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'tan_no': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter tan number',
                'required': 'required',
            }),
            'tan_docs': forms.Select(choices=tandos, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'gst_no': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter gst number',
                'required': 'required',
            }),
            'cin_no': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter cin number',
                'required': 'required',
            }),
            'authorise_share_capital': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '15',
                'minlength': '1',
                'class': "form-control mb-2",
                'placeholder': ' Enter Authorise share capital eg:12321122',
                'required': 'required',
            }),
            'issued_shared_capital': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '15',
                'minlength': '1',
                'class': "form-control mb-2",
                'placeholder': ' Enter Authorise share capital eg:12321122',
                'required': 'required',
            }),
            'mca_docs': forms.Select(choices=mcados, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'bank_name': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter Bank name ',
                'required': 'required',
            }),
            'branch_name': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter branch name',
                'required': 'required',
            }),
            'ifsc_code': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter IFSC code',
                'required': 'required',
            }),
            'bank_account': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter bank account',
                'required': 'required',
            }),
            'account_holder_name': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter account holder name',
                'required': 'required',
            }),
            'bank_docs': forms.Select(choices=mcados, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'authorise_signatory_in_bank': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter cin number',
                'required': 'required',
            }),
            'mobile_number': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '10',
                'class': "form-control mb-2",
                'placeholder': '12321122',
                'required': 'required',
            }),
            'mobile_no_registered_with_email': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '10',
                'class': "form-control mb-2",
                'placeholder': '12321122',
                'required': 'required',
            }),
            'email_created_by': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter email creater namne',
                'required': 'required',
            }),
            'company_moa': forms.Select(choices=moa, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'company_aoa': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter company aoa',
                'required': 'required',
            }),
            'fpo_registration_no': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter fpo registration number',
                'required': 'required',
            }),
            'fpo_registration_remarks': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter fpo registration remarks',
                'required': 'required',
            }),
            'villages_covered_under_fpo': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter villages covered under fpo',
                'required': 'required',
            }),
            'dmc_approval_status': forms.Select(choices=dmc_approval, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'special_allocation': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter special allocation',
                'required': 'required',
            }),
            'primary_crop_approved_by_dmc_or_as_per_dpr': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter primary crop approved by dmc or as per dpr',
                'required': 'required',
            }),
            'secondary_crop_approved_by_dmc_or_as_per_dpr': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter secondary crop approved by dmc or as per dpr',
                'required': 'required',
            }),
            'status_of_baseline_survey': forms.Select(choices=baseline_survey, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'status_board_meamber_identification': forms.Select(choices=board_meamber_identification, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'is_woman_centric': forms.Select(choices=woman_centric, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'fpo_formed': forms.Select(choices=fpoformed, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'registration_act': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter registration act',
                'required': 'required',
            }),
            'fpo_office_village_name': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter fpo office village name',
                'required': 'required',
            }),
            'fpo_office_post_office': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter fpo office post office',
                'required': 'required',
            }),
            'pin_code': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter pin code',
                'required': 'required',
            }),
            'fpo_udyog_aadhaar': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter fpo udyog aadhaar',
                'required': 'required',
            }),
            'status_of_ca_appointing': forms.Select(choices=ca_appointing, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'name_of_ca': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter name of ca',
                'required': 'required',
            }),
            'mobile_no_of_ca': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '10',
                'class': "form-control mb-2",
                'placeholder': '12321122',
                'required': 'required',
            }),
            'email_id_of_ca': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter email id of ca',
                'required': 'required',
            }),
            'status_ceo_appointment': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter status ceo appointment',
                'required': 'required',
            }),
            'fpo_ceo_name': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter fpo ceo name',
                'required': 'required',
            }),
            'fpo_ceo_mobile_number': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '10',
                'class': "form-control mb-2",
                'placeholder': '12321122',
                'required': 'required',
            }),
            'fpo_ceo_email_id': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter fpo ceo email id',
                'required': 'required',
            }),
            'status_accountant_appointment': forms.Select(choices=accountant_appointment, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'fpo_accountant_name': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter fpo accountant name',
                'required': 'required',
            }),
            'fpo_accountant_mobile_number': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '10',
                'class': "form-control mb-2",
                'placeholder': '12321122',
                'required': 'required',
            }),
            'fpo_accountant_email_id': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter fpo accountant email id',
                'required': 'required',
            }),
            'no_of_farmer_mobilized': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter no of farmer mobilized',
                'required': 'required',
            }),
            'no_of_share_member': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter no of share member',
                'required': 'required',
            }),
            'total_equity_amount': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter total equity amount',
                'required': 'required',
            }),
            'register_on_enam': forms.Select(choices=enam, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'name_of_mandi': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter name of mandi',
                'required': 'required',
            }),
            'no_of_board_meetings': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter no of board meetings',
                'required': 'required',
            }),
            'dates_of_board_meeting': DateInput(attrs={
                'type': 'date',
                'class': "form-control mb-2",
                'placeholder': 'Enter dates of board meeting',
                'required': 'required',
            }),
            'first_general_board_meetings': DateInput(attrs={
                'type': 'date',
                'class': "form-control mb-2",
                'placeholder': 'Enter first general board meetings',
                'required': 'required',
            }),
            'obtained_commencement_end_of_bussiness_certificate': DateInput(attrs={
                'type': 'date',
                'class': "form-control mb-2",
                'placeholder': 'Enter obtained commencement end of bussiness certificate',
                'required': 'required',
            }),
            'additional_services_proposed_by_fpo': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter additional services proposed by fpo',
                'required': 'required',
            }),
            'bussiness_plan': forms.Select(choices=plan_bussiness, attrs={
                'class': 'form-control mb-2',
                'required': 'required',
            }),
            'bussiness_transation_details': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter bussiness transation details',
                'required': 'required',
            }),
            'bussiness_transation_ammount_details': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter bussiness transation ammount details',
                'required': 'required',
            }),
            'fig_creation_remarks': TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Enter fig creation remarks',
                'required': 'required',
            }),

        }


metting_type_choise = (
    ('Board Meeting', 'Board Meeting'),
    ('Annual General Meeting', 'Annual General Meeting'),
    ('General Body Meeting', 'General Body Meeting'),
    ('Others', 'Others'),
)
class CompnayMeetingform(forms.ModelForm):
    class Meta:
        model=CompnayMeetingDetails
        fields = "__all__"
        widgets = {
            'fpo': TextInput(attrs={
                'class': "form-control com_metting",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'id': 'CompnayMeetingformfpo',
                # 'value': '2',
                'hidden': 'hidden',
            }),
            'metting_type': forms.Select(choices=metting_type_choise, attrs={
                'class': 'select2 form-select com_metting',
                'required': 'required',
                'disabled': 'disabled',

            }),

            'date': DateInput(attrs={
                'type': 'date',
                'class': "form-control com_metting flatpickr-basic",
                'required': 'required',
                'disabled': 'disabled',

            }),
            'purpose':TextInput(attrs={
                'type': 'text',
                'class': "form-control com_metting",
                'placeholder': 'Enter CEO first name',
                'required': 'required',
                'disabled': 'disabled',

            }),
            'notes':Textarea(attrs={
                'class': "form-control com_metting",
                'placeholder': 'Enter CEO first name',
                'required': 'required',
                'style' : "height: 100px",
                'disabled': 'disabled',

        }),
        }
# state_choise = [(i.state_title, i) for i in State.objects.all()]
# district_choise = [(i.district_title, i) for i in District.objects.all()]
# # block_choise = [(i.name, i) for i in City.objects.all()]
# block_choise = ['']
# gender_choise = (
#     (0, 'male'),
#     (1, 'female'),
#     (2, 'not specified'),
# )
# # bpl_choise = (
# #     (True, 'Yes'),
# #     (False, 'No')
# # )
# bpl_choise = [('True', 'yes'),
#               ('False', 'no')]
# aadharcard_choise = (
#     (True, 'Yes'),
#     (False, 'No')
# )
# agriculture_societies = (
#     (True, 'Yes'),
#     (False, 'No')
# )
# ivrs_societies = (
#     (True, 'Yes'),
#     (False, 'No')
# )
# livestock = (
#     (True, 'Yes'),
#     (False, 'No')
# )
# tagging = (
#     (True, 'Yes'),
#     (False, 'No')
# )
# aadhar = (
#     (True, 'Yes'),
#     (False, 'No')
# )
# panattached = (
#     (True, 'Yes'),
#     (False, 'No')
# )
# bank_details = (
#     (True, 'Yes'),
#     (False, 'No')
# )
# land_records = (
#     (True, 'Yes'),
#     (False, 'No')
# )
# certificate_number = (
#     (True, 'Yes'),
#     (False, 'No')
# )
#
#
# class FarmerForm(forms.ModelForm):
#     class Meta:
#         model = Farmer
#         exclude = ('delete_status', 'fpo_registration_no', 'fpo_name')
#         widgets = {
#             'si_no_of_share_holder': TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'Enter number of share holder',
#                 'required': 'required',
#             }),
#             'share_holder_name': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter share holder name'
#             }),
#             # 'fpo_name':forms.ModelChoiceField(queryset=FPO.objects.all()),
#             'state': forms.Select(choices=state_choise, attrs={
#                 'class': 'form-control mb-2',
#                 'required': 'required',
#             }),
#             'district': forms.Select(choices=district_choise, attrs={
#                 'class': 'form-control mb-2',
#                 'required': 'required',
#             }),
#             'block': forms.Select(choices=block_choise, attrs={
#                 'class': 'form-control mb-2',
#                 'required': 'required',
#             }),
#             'gram_panchayat': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter gram panchayat',
#             }),
#             'farmer_name': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter farmer name',
#             }),
#             'fig_name': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter fig name',
#             }),
#             'village': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter village',
#             }),
#             'pg_name': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter pg name',
#             }),
#             'hamlet': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter hamlet',
#             }),
#             'hh_name': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter hh name',
#             }),
#             'father_and_husband_name': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter father or husband name',
#             }),
#             'gender': forms.Select(choices=gender_choise, attrs={
#                 'class': 'form-control mb-2',
#                 'required': 'required',
#             }),
#             'age': TextInput(attrs={
#                 'type': 'number',
#                 'maxlength': '3',
#                 'minlength': '1',
#                 'class': "form-control mb-2",
#                 'placeholder': 'enter age eg. 25',
#                 'required': 'required',
#             }),
#             'category': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter category',
#             }),
#             'member_of_fig': TextInput(attrs={
#                 'type': 'number',
#                 # 'MaxValueValidator':"10",
#                 'maxlength': '3',
#                 'minlength': '1',
#                 'class': "form-control mb-2",
#                 'placeholder': 'Member should be in 3 digites',
#                 'required': 'required',
#             }),
#             'name_of_the_fig': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter name of fig',
#             }),
#             'bpl_status':forms.Select(choices=bpl_choise, attrs={
#                     'class': 'form-control mb-2',
#                     'required': 'required',
#                 }),
#             'have_you_received_aadhar_card_consent': forms.Select(choices=aadharcard_choise, attrs={
#                 'class': 'form-control mb-2',
#                 'required': 'required',
#             }),
#             'aadhar_card_no': TextInput(attrs={
#                 'type': 'number',
#                 # 'MaxValueValidator':"10",
#                 'maxlength': '10',
#                 'minlength': '1',
#                 'class': "form-control mb-2",
#                 'placeholder': 'Aadhar card number should be in 10 digites.',
#                 'required': 'required',
#             }),
#             'bank_account_no': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'number_of_family_member': TextInput(attrs={
#                 'type': 'number',
#                 # 'MaxValueValidator':"10",
#                 'maxlength': '2',
#                 'minlength': '1',
#                 'class': "form-control mb-2",
#                 'placeholder': '12321122',
#                 'required': 'required',
#             }),
#             'annual_income': TextInput(attrs={
#                 'type': 'number',
#                 # 'MaxValueValidator':"10",
#                 'maxlength': '10',
#                 'minlength': '1',
#                 'class': "form-control mb-2",
#                 'placeholder': '12321122',
#                 'required': 'required',
#             }),
#             'livestock_income': TextInput(attrs={
#                 'type': 'number',
#                 # 'MaxValueValidator':"10",
#                 'maxlength': '10',
#                 'minlength': '1',
#                 'class': "form-control mb-2",
#                 'placeholder': '12321122',
#                 'required': 'required',
#             }),
#             'labour': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter labour',
#             }),
#             'ntfp': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter ntfp',
#             }),
#             'micro_enterprise': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter micro enterprise',
#             }),
#             'other_income': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter other income',
#             }),
#             'member_of_cooperative_agriculture_societies': forms.Select(choices=agriculture_societies, attrs={
#                 'class': 'form-control mb-2',
#                 'required': 'required',
#             }),
#             'total_land': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter total land',
#             }),
#             'land_record_details': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter land record details',
#             }),
#             'upland_irrigated': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter upland irrigated',
#             }),
#             'medium_upland_irrigated': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'low_land_irrigated': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'leased_land': forms.Select(choices=agriculture_societies, attrs={
#                 'class': 'form-control mb-2',
#                 'required': 'required',
#             }),
#             'leased_land_area': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'year_of_share_issued': DateInput(attrs={
#                 'type': 'date',
#                 'class': "form-control mb-2",
#                 'placeholder': 'Enter first general board meetings',
#                 'required': 'required',
#             }),
#             'generate_share_certificate_number': forms.Select(choices=certificate_number, attrs={
#                 'class': 'form-control mb-2',
#                 'required': 'required',
#             }),
#             'distinctive_total_number_of_share': TextInput(attrs={
#                 'type': 'number',
#                 # 'MaxValueValidator':"10",
#                 'maxlength': '10',
#                 'minlength': '1',
#                 'class': "form-control mb-2",
#                 'placeholder': '12321122',
#                 'required': 'required',
#             }),
#             'total_capital_amount_deposited': TextInput(attrs={
#                 'type': 'number',
#                 # 'MaxValueValidator':"10",
#                 'maxlength': '10',
#                 'minlength': '1',
#                 'class': "form-control mb-2",
#                 'placeholder': '12321122',
#                 'required': 'required',
#             }),
#             'nominee': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'relationship_with_nominee': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'address_of_the_nominee': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'ivrs_or_other_alerts': forms.Select(choices=ivrs_societies, attrs={
#                 'class': 'form-control mb-2',
#                 'required': 'required',
#             }),
#             'mobile_number': TextInput(attrs={
#                 'type': 'number',
#                 # 'MaxValueValidator':"10",
#                 'maxlength': '10',
#                 'minlength': '10',
#                 'class': "form-control mb-2",
#                 'placeholder': 'Mobile number should be 10 digites.',
#                 'required': 'required',
#             }),
#             'dob_of_farmer': DateInput(attrs={
#                 'type': 'date',
#                 'class': "form-control mb-2",
#                 'placeholder': 'Enter first general board meetings',
#                 'required': 'required',
#             }),
#             'social_category': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'kharif_crop': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'sowing_month': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'marketing_month': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'robi_crop': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'zayed_crop': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'names_of_agri_machinery_owner': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'name_of_market': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'Livestock_activity': forms.Select(choices=livestock, attrs={
#                 'class': 'form-control mb-2',
#                 'required': 'required',
#             }),
#             'byp_number': TextInput(attrs={
#                 'type': 'number',
#                 # 'MaxValueValidator':"10",
#                 'maxlength': '10',
#                 'minlength': '1',
#                 'class': "form-control mb-2",
#                 'placeholder': '12321122',
#                 'required': 'required',
#             }),
#             'shed_type': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'vaccine_interval': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'tagging_status': forms.Select(choices=tagging, attrs={
#                 'class': 'form-control mb-2',
#                 'required': 'required',
#             }),
#             'pig_number': TextInput(attrs={
#                 'type': 'number',
#                 # 'MaxValueValidator':"10",
#                 'maxlength': '4',
#                 'minlength': '1',
#                 'class': "form-control mb-2",
#                 'placeholder': 'Pig number should be in 4 digites',
#                 'required': 'required',
#             }),
#             'cow_number': TextInput(attrs={
#                 'type': 'number',
#                 # 'MaxValueValidator':"10",
#                 'maxlength': '3',
#                 'minlength': '1',
#                 'class': "form-control mb-2",
#                 'placeholder': 'Cow number should be in 3 digites',
#                 'required': 'required',
#             }),
#             'buffalo_number': TextInput(attrs={
#                 'type': 'number',
#                 # 'MaxValueValidator':"10",
#                 'maxlength': '3',
#                 'minlength': '1',
#                 'class': "form-control mb-2",
#                 'placeholder': 'Buffalo number should be in 3 digites',
#                 'required': 'required',
#             }),
#             'face_value_of_share': TextInput(attrs={
#                 'type': 'number',
#                 # 'MaxValueValidator':"10",
#                 'maxlength': '6',
#                 'minlength': '1',
#                 'class': "form-control mb-2",
#                 'placeholder': 'face value of share should be in 6 digites',
#                 'required': 'required',
#             }),
#             'mambers_hip_amount_paid': TextInput(attrs={
#                 'type': 'number',
#                 # 'MaxValueValidator':"10",
#                 'maxlength': '6',
#                 'minlength': '1',
#                 'class': "form-control mb-2",
#                 'placeholder': 'mambers hip amount should be in 6 digites',
#                 'required': 'required',
#             }),
#             'premium_amount_paid': TextInput(attrs={
#                 'type': 'number',
#                 # 'MaxValueValidator':"10",
#                 'maxlength': '6',
#                 'minlength': '1',
#                 'class': "form-control mb-2",
#                 'placeholder': 'premium amount should be in 6 digites',
#                 'required': 'required',
#             }),
#             'any_entrepreneural_activity': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'packhouse_available': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter any entrepreneural activity',
#             }),
#             'drying_yard_available': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter drying yard available',
#             }),
#             'other_livelihood': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Name',
#             }),
#             'poly_or_shed_house': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter other livelihood',
#             }),
#             'any_commerical_vehicle': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter any commerical vehicle',
#             }),
#             'onwed_vehicle': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter onwed vehicle',
#             }),
#             'house_type': TextInput(attrs={
#                 'class': "form-control mb-2",
#                 'style': 'max-width: 100%;',
#                 'placeholder': 'Enter house type',
#             }),
#             'aadhar_attached': forms.Select(choices=aadhar, attrs={
#                 'class': 'form-control mb-2',
#                 'required': 'required',
#             }),
#             'pan_attached': forms.Select(choices=panattached, attrs={
#                 'class': 'form-control mb-2',
#                 'required': 'required',
#             }),
#             'bank_details_attached': forms.Select(choices=bank_details, attrs={
#                 'class': 'form-control mb-2',
#                 'required': 'required',
#             }),
#             'land_records_attached': forms.Select(choices=land_records, attrs={
#                 'class': 'form-control mb-2',
#                 'required': 'required',
#             }),
#
#         }

terrain_category_choise = (
    ('Hilly', 'Hilly'),
    ('Plain', 'Plain')
)
women_choise = (
    ('yes', 'yes'),
    ('no', 'no'),
)
crop = [
    ('Special', 'Special'),
    ('Non-Special', 'Non-Special'),
    ('Honey', 'Honey'),

]
cbbo_choise = [(i.cbbo_name, i.cbbo_name) for i in Cbbo.objects.all()]
ia_choise = [(i.ia_name, i) for i in Ia.objects.all()]


class FpoBasicDetails(forms.ModelForm):
    class Meta:
        model = FPO
        fields = ['fpo_name', 'state', 'district', 'block', 'terrain_category', 'is_fpo_women_centric',
                  'date_of_commencement', 'crop_type', 'cbbo_name', 'ia_name']
        # exclude = ('created_by', 'user_id', 'status')
        widgets = {
            'fpo_name': TextInput(attrs={
                'class': "form-control f2",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'date_of_commencement': DateInput(attrs={
                'type': 'date',
                'class': "form-control f2",
                'id': 'pd-months-year',
                'placeholder': ' Mention date from FORM INC 20 A',
                'required': 'required',
                'disabled': 'disabled',
            }),
            'state': forms.Select(choices=state_choise, attrs={
                'class': 'form-control f2',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'crop_type': forms.Select(choices=crop, attrs={
                'class': 'form-control f2',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'district': forms.Select(choices=district_choise, attrs={
                'class': 'form-control f2',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'block': forms.Select(choices=block_choise, attrs={
                'class': 'form-control f2',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'terrain_category': forms.Select(choices=terrain_category_choise, attrs={
                'class': 'form-control f2',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'is_fpo_women_centric': forms.Select(choices=women_choise, attrs={
                'class': 'form-control f2',
                'required': 'required',
                'disabled': 'disabled',
            }),
            'cbbo_name': forms.Select(choices=cbbo_choise, attrs={
                'class': 'form-control f2',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'ia_name': forms.Select(choices=ia_choise, attrs={
                'class': 'select2 form-select f2',
                'required': 'required',
                'disabled': 'disabled'
            }),
        }


gender_choise = (
    ('male', 'male'),
    ('female', 'female'),
    ('not specified', 'not specified'),
)
category_choise = (
    ('General', 'General'),
    ('MBC', 'MBC'),
    ('OBC', 'OBC'),
    ('SC', 'SC'),
    ('ST', 'ST'),
    ('Others', 'Others'),
)


# for update subscriber details form

class SubscriberDetailsForm(forms.ModelForm):
    class Meta:
        model = SubscriberDetails
        fields = ['fpo_name', 'first_name', 'middle_name', 'last_name', 'contact_number', 'email_id', 'photo',
                  'aadhar_card_number', 'aadhar_card_doc',
                  'pan_card_number', 'pan_card_doc', 'land_holding', 'land_holding_doc', 'khasra_number',
                  'khasra_number_doc', 'gender', 'category']
        # exclude = ('created_by', 'user_id', 'status')
        widgets = {
            'fpo_name': TextInput(attrs={
                'class': "form-control f6",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'value': '2',
                'hidden': 'hidden',
            }),
            'type': TextInput(attrs={
                'class': "form-control f6",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required'
            }),
            'first_name': TextInput(attrs={
                'class': "form-control f6",
                'placeholder': 'Enter first Name',
                'required': 'required',
                'disabled': 'disabled',
                'onkeydown': "return /[a-z]/i.test(event.key)",
            }),
            'middle_name': TextInput(attrs={
                'class': "form-control f6",
                'placeholder': 'Enter middle Name',
                'required': 'required',
                'disabled': 'disabled',
                'onkeydown': "return /[a-z]/i.test(event.key)",
            }),
            'last_name': TextInput(attrs={
                'class': "form-control f6",
                'placeholder': 'Enter last Name',
                'required': 'required',
                'disabled': 'disabled',
                'onkeydown': "return /[a-z]/i.test(event.key)",
            }),
            'contact_number': TextInput(attrs={
                'class': "form-control f6",

                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '10',
                # 'min':'10',
                # 'max':'10',
                # "oninput" : "javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);",
                'placeholder': '9999999999',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'email_id': TextInput(attrs={
                'class': "form-control f6",
                'type': 'email',
                'placeholder': 'Enter email id',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f6',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'aadhar_card_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f6',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'gender': forms.Select(choices=gender_choise, attrs={
                'class': 'select2 form-select f6',
                'required': 'required',
                'disabled': 'disabled',

            }),
            'category': forms.Select(choices=category_choise, attrs={
                'class': 'select2 form-select f6',
                'required': 'required',
                'disabled': 'disabled',
            }),

            'aadhar_card_number': TextInput(attrs={
                'class': "form-control f6",
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '10',
                # 'min':'10',
                # 'max':'10',
                # "oninput" : "javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);",
                'placeholder': 'xxxxxxxxxx',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'pan_card_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f6',
                'disabled': 'disabled',
                'required': 'required',
            }),

            'pan_card_number': TextInput(attrs={
                'class': "form-control f6",
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '10',
                # 'min':'10',
                # 'max':'10',
                # "oninput" : "javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);",
                'placeholder': 'xxxxxxxxxx',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'land_holding_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f6',
                'disabled': 'disabled',
                'required': 'required',
            }),

            'land_holding': TextInput(attrs={
                'class': "form-control f6",
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '10',
                # 'min':'10',
                # 'max':'10',
                # "oninput" : "javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);",
                'placeholder': 'Enter Land Holding (in acres)',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'khasra_number_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f6',
                'disabled': 'disabled',
                'required': 'required',
            }),

            'khasra_number': TextInput(attrs={
                'class': "form-control f6",
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '10',
                # 'min':'10',
                # 'max':'10',
                # "oninput" : "javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);",
                'placeholder': 'xxxxx',
                'required': 'required',
                'disabled': 'disabled'
            }),
        }


class SubscriberDetailsDocumentsForm(forms.ModelForm):
    class Meta:
        model = SubscriberDetails
        fields = ['aadhar_card_number', 'aadhar_card_doc', 'pan_card_number', 'pan_card_doc', 'land_holding',
                  'land_holding_doc', 'khasra_number', 'khasra_number_doc']
        # exclude = ('created_by', 'user_id', 'status')
        # widgets = {
        #     'fpo_name': TextInput(attrs={
        #         'class': "form-control f6",
        #         'placeholder': 'Enter FPO Name',
        #         'disabled':'disabled',
        #         'value':'2',
        #         'hidden':'hidden',
        #     }),
        # }


class FpoOfficeprofe(forms.ModelForm):
    class Meta:
        model = FPO
        fields = ['office_address_proof', 'rent_agreement', 'photo_graph_of_the_fpo']
        # exclude = ('created_by', 'user_id', 'status')
        widgets = {
            'office_address_proof': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f4',
                'required': 'required',
            }),
            'rent_agreement': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f4',
                'required': 'required',
            }),
            'photo_graph_of_the_fpo': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f4',
                'required': 'required',
            }),
        }


# class FpoBankDetails(forms.ModelForm):
#     class Meta:
#         model = FPO
#         fields=['name','contact_number','bank_name','account_number','branch','full_address','ifsc_code','authorised_person']

class AuthorisedShareCapitalForm(forms.ModelForm):
    class Meta:
        model=AuthorisedSharedCapital
        fields=['fpo','date','no_of_share','face_value','total_value']
        widgets={

            'fpo': TextInput(attrs={
                'class': "form-control fasc",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'id':'authcapfpo',
               # 'value': '2',
                'hidden': 'hidden',
            }),

            'date': TextInput(attrs={
                'type': 'date',
                'class': "form-control fasc flatpickr-basic",
                'placeholder': 'Select Your date',
                'disabled': 'disabled',
                'required': 'required',

            }),
            'no_of_share': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '5',
                'minlength': '1',
                'class': "form-control fasc",
                'placeholder': '12321122',
                'required': 'required',
                'disabled': 'disabled',
            }),
            'face_value': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '1',
                'class': "form-control fasc",
                'placeholder': '12321122',
                'required': 'required',
                'disabled': 'disabled',
            }),
            'total_value': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '15',
                'minlength': '1',
                'class': "form-control fasc",
                'placeholder': '12321122',
                'required': 'required',
                'disabled': 'disabled',
                'readonly':'readonly',
            }),

        }

class IssuedShareCapitalForm(forms.ModelForm):
    class Meta:
        model=IssuedSharedCapital
        fields=['fpo','date','no_of_share','face_value','total_value']
        widgets={

            'fpo': TextInput(attrs={
                'class': "form-control fasc1",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'id':'issuedcapfpo',
               # 'value': '2',
                'hidden': 'hidden',
            }),

            'date': TextInput(attrs={
                'type': 'date',
                'id':'issueddate',
                'class': "form-control fasc1 flatpickr-basic",
                'placeholder': 'Select Your date',
                'disabled': 'disabled',
                'required': 'required',

            }),
            'no_of_share': TextInput(attrs={
                'type': 'number',
                'id': 'issued_no_of_share',
                # 'MaxValueValidator':"10",
                'maxlength': '5',
                'minlength': '1',
                'class': "form-control fasc1",
                'placeholder': '12321122',
                'required': 'required',
                'disabled': 'disabled',
            }),
            'face_value': TextInput(attrs={
                'type': 'number',
                'id': 'issued_face_value',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '1',
                'class': "form-control fasc1",
                'placeholder': '12321122',
                'required': 'required',
                'disabled': 'disabled',
            }),
            'total_value': TextInput(attrs={
                'type': 'number',
                'id': 'issued_total_value',
                # 'MaxValueValidator':"10",
                'maxlength': '15',
                'minlength': '1',
                'class': "form-control fasc1",
                'placeholder': '12321122',
                'required': 'required',
                'disabled': 'disabled',
                'readonly':'readonly',
            }),

        }

class AccountantInformation(forms.ModelForm):
    class Meta:
        model = FPO
        fields = ['coi_number', 'coi_doc', 'pan_card_of_fpo', 'pan_card_doc_of_fpo', 'tan_of_fpo', 'tan_doc_of_fpo',
                  'moa', 'aoa', 'gst_certificate', 'gst_certificate_doc', 'udhyog_aadhar_number', 'udhyog_aadhar_doc']
        # exclude = ('created_by', 'user_id', 'status')
        widgets = {
            'coi_number': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '13',
                'minlength': '1',
                'class': "form-control mb-2",
                'placeholder': '12321122',
                'required': 'required',
            }),
        }


ceoeducation = (
    ('10th', '10th'),
    ('12th', '12th'),
    ('Graduation', 'Graduation'),
    ('PostGraduation', 'PostGraduation'),
)


class FpoAccountantForm(forms.ModelForm):
    class Meta:
        model = FPO
        fields = ['fpo_accountant_first_name', 'fpo_accountant_middle_name', 'fpo_accountant_last_name',
                  'fpo_accountant_email_id',
                  'fpo_accountant_contact_number', 'fpo_accountant_joining_date', 'fpo_accountant_aadhar_card_number',
                  'fpo_accountant_aadhar_card_doc', 'fpo_accountant_pan_card_number', 'fpo_accountant_pan_card_doc',
                  'fpo_accountant_resume',
                  'fpo_accountant_appointment_letter']
        widgets = {
            'fpo_accountant_first_name': TextInput(attrs={
                'class': "form-control f10",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'fpo_accountant_middle_name': TextInput(attrs={
                'class': "form-control f10",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'fpo_accountant_last_name': TextInput(attrs={
                'class': "form-control f10",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'fpo_accountant_email_id': TextInput(attrs={
                'class': "form-control f10",
                'type': 'email',
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'fpo_accountant_contact_number': TextInput(attrs={
                'class': "form-control f10",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'fpo_accountant_joining_date': TextInput(attrs={
                'class': "form-control f10",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
                'type': 'date',
            }),
            'fpo_accountant_aadhar_card_number': TextInput(attrs={
                'class': "form-control f10",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
                'type': 'number',
            }),
            'fpo_accountant_aadhar_card_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f10',
                'disabled': 'disabled',
            }),
            'fpo_accountant_pan_card_number': TextInput(attrs={
                'class': "form-control f10",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
                'type': 'number',
            }),
            'fpo_accountant_pan_card_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f10',
                'disabled': 'disabled',
            }),
            'fpo_accountant_resume': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f10',
                'disabled': 'disabled',
            }),
            'fpo_accountant_appointment_letter': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f10',
                'disabled': 'disabled',
            }),
        }


class FpoCeoForm(forms.ModelForm):
    class Meta:
        model = FPO
        fields = ['fpo_ceo_first_name', 'fpo_ceo_middle_name', 'fpo_ceo_last_name', 'fpo_ceo_email_id',
                  'fpo_ceo_contact_number', 'fpo_ceo_joining_date', 'fpo_ceo_aadhar_card_number',
                  'fpo_ceo_aadhar_card_doc', 'fpo_ceo_pan_card_number', 'fpo_ceo_pan_card_doc', 'fpo_ceo_resume',
                  'fpo_ceo_appointment_letter']
        widgets = {
            'fpo': TextInput(attrs={
                'class': "form-control f9",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'value': '2',
                'hidden': 'hidden',
            }),
            'fpo_ceo_first_name': TextInput(attrs={
                'class': "form-control f9",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'fpo_ceo_middle_name': TextInput(attrs={
                'class': "form-control f9",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'fpo_ceo_last_name': TextInput(attrs={
                'class': "form-control f9",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'fpo_ceo_email_id': TextInput(attrs={
                'class': "form-control f9",
                'type': 'email',
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'fpo_ceo_contact_number': TextInput(attrs={
                'class': "form-control f9",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'fpo_ceo_joining_date': TextInput(attrs={
                'class': "form-control f9",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
                'type': 'date',
            }),
            'fpo_ceo_aadhar_card_number': TextInput(attrs={
                'class': "form-control f9",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
                'type': 'number',
            }),
            'fpo_ceo_aadhar_card_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f9',
                'disabled': 'disabled',
            }),
            'fpo_ceo_pan_card_number': TextInput(attrs={
                'class': "form-control f9",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'required': 'required',
                'type': 'number',
            }),
            'fpo_ceo_pan_card_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f9',
                'disabled': 'disabled',
            }),
            'fpo_ceo_resume': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f9',
                'disabled': 'disabled',
            }),
            'fpo_ceo_appointment_letter': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f9',
                'disabled': 'disabled',
            }),
        }


class FpoCeoEducationForm(forms.ModelForm):
    class Meta:
        model = FpoCeoEducation
        fields = '__all__'
        widgets = {
            'fpo': TextInput(attrs={
                'class': "form-control f9",
                'placeholder': 'Enter FPO Name',
                'disabled': 'disabled',
                'hidden': 'hidden',
            }),
            'ceo_education': forms.Select(choices=ceoeducation, attrs={
                'class': 'form-control f9',
                'required': 'required',
                'disabled': 'disabled',
                'name': 'option[]'
            }),
            'ceo_education_documents': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f9',
                'required': 'required',
            }),
        }


class CeoInformation(forms.ModelForm):
    class Meta:
        model = FPO
        fields = ['fpo_ceo_first_name', 'fpo_ceo_middle_name', 'fpo_ceo_last_name', 'fpo_ceo_email_id',
                  'fpo_ceo_contact_number',
                  'fpo_ceo_joining_date', 'fpo_ceo_aadhar_card_number', 'fpo_ceo_aadhar_card_doc',
                  'fpo_ceo_pan_card_number', 'fpo_ceo_pan_card_doc', 'fpo_ceo_resume', 'fpo_ceo_appointment_letter']
        # exclude = ('created_by', 'user_id', 'status')
        widgets = {
            'fpo_ceo_first_name': TextInput(attrs={
                'type': 'text',
                'class': "form-control f12",
                'placeholder': 'Enter CEO first name',
                'required': 'required',
            }),
            'fpo_ceo_middle_name': TextInput(attrs={
                'type': 'text',
                'class': "form-control f12",
                'placeholder': 'Enter CEO middle name',
                'required': 'required',
            }),
            'fpo_ceo_last_name': TextInput(attrs={
                'type': 'text',
                'class': "form-control f12",
                'placeholder': 'Enter CEO last name',
                'required': 'required',
            }),
            'fpo_ceo_email_id': TextInput(attrs={
                'type': 'email',
                'class': "form-control f12",
                'placeholder': 'Enter CEO email id',
                'required': 'required',
            }),
            'fpo_ceo_contact_number': TextInput(attrs={
                'type': 'number',
                'maxlength': '13',
                'minlength': '1',
                'class': "form-control f12",
                'placeholder': '12321122',
                'required': 'required',
            }),
            'fpo_ceo_joining_date': TextInput(attrs={
                'type': 'date',
                'class': "form-control f12",
                'placeholder': 'dd/mm/yyyy',
                'required': 'required',
            }),
            'fpo_ceo_aadhar_card_number': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '13',
                'minlength': '1',
                'class': "form-control f12",
                'placeholder': '12321122',
                'required': 'required',
            }),
            'fpo_ceo_aadhar_card_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f12',
                'required': 'required',
                'currently': 'None',
            }),
            'fpo_ceo_pan_card_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f12',
                'required': 'required',
            }),
            'fpo_ceo_resume': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f12',
                'required': 'required',
            }),
            'fpo_ceo_appointment_letter': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f12',
                'required': 'required',
            }),
            'fpo_ceo_pan_card_number': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '13',
                'minlength': '1',
                'class': "form-control f12",
                'placeholder': '12321122',
                'required': 'required',
            }),
        }


class RegistrationDocument(forms.ModelForm):
    class Meta:
        model = FPO
        fields = ['coi_number', 'coi_doc', 'pan_card_of_fpo', 'pan_card_doc_of_fpo', 'tan_of_fpo', 'tan_doc_of_fpo',
                  'moa', 'aoa', 'gst_certificate', 'gst_certificate_doc', 'udhyog_aadhar_number', 'udhyog_aadhar_doc']
        # exclude = ('created_by', 'user_id', 'status')
        widgets = {
            'coi_number': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '13',
                'minlength': '1',
                'class': "form-control mb-2",
                'placeholder': '12321122',
                'required': 'required',
            }),
            'coi_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f4',
                'required': 'required',
            }),
            'pan_card_of_fpo': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '1',
                'class': "form-control mb-2",
                'placeholder': '12321122',
                'required': 'required',
            }),
            'pan_card_doc_of_fpo': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f4',
                'required': 'required',
            }),
            'tan_of_fpo': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '1',
                'class': "form-control mb-2",
                'placeholder': '12321122',
                'required': 'required',
            }),
            'tan_doc_of_fpo': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f4',
                'required': 'required',
            }),
            'moa': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f4',
                'required': 'required',
            }),
            'aoa': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f4',
                'required': 'required',
            }),
            'gst_certificate': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '1',
                'class': "form-control mb-2",
                'placeholder': '12321122',
                'required': 'required',
            }),
            'gst_certificate_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f4',
                'required': 'required',
            }),
            'udhyog_aadhar_number': TextInput(attrs={
                'type': 'number',
                # 'MaxValueValidator':"10",
                'maxlength': '10',
                'minlength': '1',
                'class': "form-control mb-2",
                'placeholder': '12321122',
                'required': 'required',
            }),
            'udhyog_aadhar_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f4',
                'required': 'required',
            }),
        }


class FpoRegistration(forms.ModelForm):
    class Meta:
        model = FPO
        fields = ['fpo_name', 'cin']
        widgets = {
            'fpo_name': TextInput(attrs={
                'class': "form-control f1",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
                'onkeydown': "return /[a-z]/i.test(event.key)",
            }),
            'cin': TextInput(attrs={
                'class': "form-control f1",
                'placeholder': 'Enter CIN',
                'required': 'required',
                'disabled': 'disabled'
            }),
        }

# kaif


bank_choise = [(i.name, i) for i in Bank.objects.all()]
class FpoBankDetailsForm(forms.ModelForm):
    class Meta:
        model = FpoBankDetails
        fields = ['fpo', 'name', 'contact_number', 'bank_name', 'account_number', 'branch', 'full_address', 'ifsc_code',
                  'authorised_person', 'bank_statement_doc', 'passbook_doc']
        widgets = {
            'fpo': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
                'hidden':'hidden',
                'onkeydown': "return /[a-z]/i.test(event.key)",
            }),
            'name': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
                'onkeydown': "return /[a-z]/i.test(event.key)",
            }),
            'contact_number': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                'minlength': '10',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'branch': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
                'onkeydown': "return /[a-z]/i.test(event.key)",
            }),
            'account_number': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                'minlength': '10',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'bank_name': forms.Select(choices=bank_choise, attrs={
                'class': 'form-control f8',
                'required': 'required',
                'disabled': 'disabled'
            }),

            'full_address': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
            }),
            'ifsc_code': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                'minlength': '10',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'authorised_person': TextInput(attrs={
                'class': "form-control f8",
                'value':'1',
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                # 'minlength': '10',
                'hidden':'hidden',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'bank_statement_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f8',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'passbook_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f8',
                'disabled': 'disabled',
                'required': 'required',
            }),

        }

class FpoBankDetailsForm2(forms.ModelForm):
    class Meta:
        model = FpoBankDetails
        fields = ['fpo', 'name', 'contact_number', 'bank_name', 'account_number', 'branch', 'full_address', 'ifsc_code',
                  'authorised_person', 'bank_statement_doc', 'passbook_doc']
        widgets = {
            'fpo': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
                'id':'001',
                'hidden':'hidden',
            }),
            'name': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
                'onkeydown': "return /[a-z]/i.test(event.key)",
            }),
            'contact_number': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                'minlength': '10',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'branch': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
                'onkeydown': "return /[a-z]/i.test(event.key)",
            }),
            'account_number': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                'minlength': '10',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'bank_name': forms.Select(choices=bank_choise, attrs={
                'class': 'form-control f8',
                'required': 'required',
                'disabled': 'disabled'
            }),

            'full_address': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
            }),
            'ifsc_code': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                'minlength': '10',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'authorised_person': TextInput(attrs={
                'class': "form-control f8",
                'value':'2',
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                # 'minlength': '10',
                'hidden':'hidden',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'bank_statement_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f8',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'passbook_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f8',
                'disabled': 'disabled',
                'required': 'required',
            }),

        }
class FpoBankDetailsForm3(forms.ModelForm):
    class Meta:
        model = FpoBankDetails
        fields = ['fpo', 'name', 'contact_number', 'bank_name', 'account_number', 'branch', 'full_address', 'ifsc_code',
                  'authorised_person', 'bank_statement_doc', 'passbook_doc']
        widgets = {
            'fpo': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
                'id':'003',
                'hidden':'hidden',
            }),
            'name': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
                'onkeydown': "return /[a-z]/i.test(event.key)",
            }),
            'contact_number': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                'minlength': '10',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'branch': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
                'onkeydown': "return /[a-z]/i.test(event.key)",
            }),
            'account_number': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                'minlength': '10',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'bank_name': forms.Select(choices=bank_choise, attrs={
                'class': 'form-control f8',
                'required': 'required',
                'disabled': 'disabled'
            }),

            'full_address': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
            }),
            'ifsc_code': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                'minlength': '10',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'authorised_person': TextInput(attrs={
                'class': "form-control f8",
                'value':'3',
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                # 'minlength': '10',
                'hidden':'hidden',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'bank_statement_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f8',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'passbook_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f8',
                'disabled': 'disabled',
                'required': 'required',
            }),

        }
class FpoBankDetailsForm4(forms.ModelForm):
    class Meta:
        model = FpoBankDetails
        fields = ['fpo', 'name', 'contact_number', 'bank_name', 'account_number', 'branch', 'full_address', 'ifsc_code',
                  'authorised_person', 'bank_statement_doc', 'passbook_doc']
        widgets = {
            'fpo': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
                'id':'004',
                'hidden':'hidden',
            }),
            'name': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
                'onkeydown': "return /[a-z]/i.test(event.key)",
            }),
            'contact_number': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                'minlength': '10',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'branch': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
                'onkeydown': "return /[a-z]/i.test(event.key)",
            }),
            'account_number': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                'minlength': '10',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'bank_name': forms.Select(choices=bank_choise, attrs={
                'class': 'form-control f8',
                'required': 'required',
                'disabled': 'disabled'
            }),

            'full_address': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
            }),
            'ifsc_code': TextInput(attrs={
                'class': "form-control f8",
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                'minlength': '10',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'authorised_person': TextInput(attrs={
                'class': "form-control f8",
                'value':'4',
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                # 'minlength': '10',
                'hidden':'hidden',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'bank_statement_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f8',
                'disabled': 'disabled',
                'required': 'required',
            }),
            'passbook_doc': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg',
                'class': 'form-control f8',
                'disabled': 'disabled',
                'required': 'required',
            }),

        }


class FpoAddressDetails(forms.ModelForm):
    class Meta:
        model = FPO
        fields = ['fpo_contact_person_name', 'contact_person_mobile_no', 'fpo_post_office', 'fpo_email_id', 'Pincode',
                  'registered_address_line1', 'registered_address_line2', 'district', 'block', 'land_mark']
        # exclude = ('created_by', 'user_id', 'status')
        widgets = {
            'fpo_contact_person_name': TextInput(attrs={
                'class': "form-control f3",
                'placeholder': 'Enter FPO contact person Name',
                'required': 'required',
                'disabled': 'disabled',
                'onkeydown': "return /[a-z]/i.test(event.key)",
            }),
            'fpo_post_office': TextInput(attrs={
                'class': "form-control f3",
                'placeholder': 'Enter Post Office',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'contact_person_mobile_no': TextInput(attrs={
                'class': "form-control f3",
                'placeholder': 'Enter contact person mobile no',
                'required': 'required',
                'disabled': 'disabled',
                'minlength': '10',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",
            }),
            'registered_address_line1': TextInput(attrs={
                'class': "form-control f3",
                'placeholder': 'Enter registered address line1',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'registered_address_line2': TextInput(attrs={
                'class': "form-control f3",
                'placeholder': 'Enter registered address line2',
                'disabled': 'disabled'
            }),
            'land_mark': TextInput(attrs={
                'class': "form-control f3",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'fpo_email_id': TextInput(attrs={
                'class': "form-control f3",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
                'type': 'email',
            }),
            'Pincode': TextInput(attrs={
                'class': "form-control f3",
                'placeholder': 'Enter FPO Name',
                'required': 'required',
                'disabled': 'disabled',
                'type': 'text',
                'maxlenth': '6',
                'onkeypress': "return event.charCode >= 48 && event.charCode <= 57",

            }),
            'district': forms.Select(choices=district_choise, attrs={
                'class': 'form-control f3',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'block': forms.Select(choices=block_choise, attrs={
                'class': 'select2 form-select f3',
                'required': 'required',
                'disabled': 'disabled'
            }),
        }


class FpoCaInformationForm(forms.ModelForm):
    class Meta:
        model = FpoCaInformation
        fields = ['fpo', 'first_name', 'middle_name', 'last_name', 'email_id', 'firm_name']
        # exclude = ('created_by', 'user_id', 'status')
        widgets = {
            'fpo': TextInput(attrs={
                'class': "form-control f11",
                'placeholder': 'Enter FPO CA first name',
                'value': '2',
                'required': 'required',
                'disabled': 'disabled',
                'hidden': 'hidden',
            }),
            'first_name': TextInput(attrs={
                'class': "form-control f11",
                'placeholder': 'Enter FPO CA first name',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'middle_name': TextInput(attrs={
                'class': "form-control f11",
                'placeholder': 'Enter FPO CA middle Name',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'last_name': TextInput(attrs={
                'class': "form-control f11",
                'placeholder': 'Enter FPO CA last Name',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'email_id': TextInput(attrs={
                'class': "form-control f11",
                'type': 'email',
                'placeholder': 'Enter FPO CA email id',
                'required': 'required',
                'disabled': 'disabled'
            }),
            'firm_name': TextInput(attrs={
                'class': "form-control f11",
                'placeholder': 'Enter FPO CA firm name',
                'required': 'required',
                'disabled': 'disabled'
            }),
        }
