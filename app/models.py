from django.db import models
from users.models import CustomUser
from datetime import date


class State(models.Model):
    state_title = models.CharField(max_length=128)
    state_description = models.CharField(max_length=255)
    status = models.CharField(max_length=100)

    def __str__(self):
        return str(self.state_title)


#
#
class District(models.Model):
    district_title = models.CharField(max_length=128)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district_description = models.CharField(max_length=255)
    district_status = models.CharField(max_length=100)

    def __str__(self):
        return self.district_title


#
#
class City(models.Model):
    name = models.CharField(max_length=128)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    # districtid=models.CharField(max_length=5)
    # state_id=models.CharField(max_length=5)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cbbo(models.Model):
    cbbo_name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.cbbo_name


class Ia(models.Model):
    ia_name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.ia_name


class terrain_category(models.Model):
    category_name = models.CharField(max_length=128, unique=True)
    delete_status = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name


# Create your models here.
class FPO(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    fpo_name = models.CharField(max_length=50)
    cin = models.CharField(max_length=21)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    block = models.ForeignKey(City, on_delete=models.CASCADE)
    registered_address_line1 = models.CharField(max_length=300)
    registered_address_line2 = models.CharField(max_length=300)
    terrain_category = models.CharField(max_length=10)
    land_mark = models.CharField(max_length=255)
    is_fpo_women_centric=models.CharField(max_length=10)
    date_of_commencement=models.DateField(default=date.today)
    crop_type=models.CharField(max_length=128)
    crop_name=models.CharField(max_length=225)
    fpo_post_office=models.CharField(max_length=225)
    cbbo_name = models.CharField(max_length=20)
    ia_name = models.CharField(max_length=20)
    Pincode = models.CharField(max_length=6)
    fpo_contact_person_name = models.CharField(max_length=128)
    contact_person_mobile_no = models.CharField(max_length=10)
    fpo_email_id = models.CharField(max_length=255)
    office_address_proof = models.ImageField(upload_to='fpo/address_proof/')
    rent_agreement = models.ImageField(upload_to='fpo/rent_agreement/')
    photo_graph_of_the_fpo = models.ImageField(upload_to='fpo/fpo_photo_graph/')
    coi_number = models.CharField(max_length=20)
    coi_doc = models.ImageField(upload_to='fpo/coi_documents/')
    pan_card_of_fpo = models.CharField(max_length=10)
    pan_card_doc_of_fpo = models.ImageField(upload_to='fpo/pan_card_documents/')
    tan_of_fpo = models.CharField(max_length=10)
    tan_doc_of_fpo = models.ImageField(upload_to='fpo/tan_documents/')
    moa = models.ImageField(upload_to='fpo/moa/')
    aoa = models.ImageField(upload_to='fpo/aoa/')
    gst_certificate = models.CharField(max_length=10)
    gst_certificate_doc = models.ImageField(upload_to='fpo/gst_certificate_documents/')
    udhyog_aadhar_number = models.CharField(max_length=10)
    udhyog_aadhar_doc = models.ImageField(upload_to='fpo/udhyog_aadhar_documents/')
    fpo_ceo_first_name = models.CharField(max_length=128)
    fpo_ceo_middle_name = models.CharField(max_length=128)
    fpo_ceo_last_name = models.CharField(max_length=128)
    fpo_ceo_email_id = models.CharField(max_length=255)
    fpo_ceo_contact_number = models.CharField(max_length=10)
    fpo_ceo_joining_date = models.DateField(default=date.today)
    fpo_ceo_aadhar_card_number = models.CharField(max_length=10)
    fpo_ceo_aadhar_card_doc = models.ImageField(upload_to='fpo_ceo/fpo_ceo_aadhar_card_documents/')
    fpo_ceo_pan_card_number = models.CharField(max_length=10)
    fpo_ceo_pan_card_doc = models.ImageField(upload_to='fpo_ceo/fpo_pan_card_documents/')
    # fpo_ceo_education_documents = models.ImageField(upload_to='fpo_ceo/education_documents/')
    fpo_ceo_resume = models.ImageField(upload_to='fpo_ceo/resume/')
    fpo_ceo_appointment_letter = models.ImageField(upload_to='fpo_ceo/appointment_letter/')
    fpo_accountant_first_name = models.CharField(max_length=128)
    fpo_accountant_middle_name = models.CharField(max_length=128)
    fpo_accountant_last_name = models.CharField(max_length=128)
    fpo_accountant_email_id = models.CharField(max_length=255)
    fpo_accountant_contact_number = models.CharField(max_length=10)
    fpo_accountant_joining_date = models.DateField(default=date.today)
    fpo_accountant_aadhar_card_number = models.CharField(max_length=10)
    fpo_accountant_aadhar_card_doc = models.ImageField(upload_to='fpo_accountant/fpo_accountant_aadhar_card_documents/')
    fpo_accountant_pan_card_number = models.CharField(max_length=10)
    fpo_accountant_pan_card_doc = models.ImageField(upload_to='fpo_accountant/fpo_accountant_pan_card_documents/')
    # fpo_accountant_education_documents = models.ImageField(
    #     upload_to='fpo_accountant/fpo_accountant_education_documents/')
    fpo_accountant_resume = models.ImageField(upload_to='fpo_accountant/fpo_accountant_resume/')
    fpo_accountant_appointment_letter = models.ImageField(upload_to='fpo_accountant/fpo_accountant_appointment_letter/')

    class Meta:
        verbose_name_plural = 'fpo'

    def __str__(self):
        return str(self.user_id)

#Fpo accountant education
class FpoAccountantEducation(models.Model):
    fpo = models.ForeignKey(FPO, on_delete=models.CASCADE)
    accountant_education=models.CharField(max_length=50)
    accountant_education_documents = models.ImageField(
        upload_to='fpo_accountant/fpo_accountant_education_documents/')

class FpoCeoEducation(models.Model):
    fpo = models.ForeignKey(FPO, on_delete=models.CASCADE)
    ceo_education=models.CharField(max_length=50)
    ceo_education_documents = models.ImageField(
        upload_to='fpo_ceo/fpo_ceo_education_documents/')

    def __str__(self):
        return self.ceo_education

class SubscriberDetails(models.Model):
    type = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128,null=True,blank=True)
    middle_name = models.CharField(max_length=128,null=True,blank=True)
    last_name = models.CharField(max_length=128,null=True,blank=True)
    contact_number = models.CharField(max_length=10,null=True,blank=True)
    email_id = models.CharField(max_length=225,unique=True,null=True,blank=True)
    photo = models.ImageField(upload_to='subscriberdetails/photo/')
    aadhar_card_number = models.CharField(max_length=10,null=True,blank=True)
    aadhar_card_doc = models.ImageField(upload_to='subscriberdetails/aadhar_card_documents/')
    pan_card_number = models.CharField(max_length=10,null=True,blank=True)
    pan_card_doc = models.ImageField(upload_to='subscriberdetails/pan_card_documents/')
    land_holding = models.CharField(max_length=10,null=True,blank=True)
    land_holding_doc = models.ImageField(upload_to='subscriberdetails/land_holding_documents/')
    khasra_number = models.CharField(max_length=10,null=True,blank=True)
    khasra_number_doc = models.ImageField(upload_to='subscriberdetails/khasra_number_documents/')
    fpo_name = models.ForeignKey(FPO, on_delete=models.CASCADE)
    gender=models.CharField(max_length=10,null=True,blank=True)
    category=models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return self.type

class AuthorisedSharedCapital(models.Model):
    fpo = models.ForeignKey(FPO, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    no_of_share=models.CharField(max_length=5)
    face_value=models.CharField(max_length=10)
    total_value=models.CharField(max_length=15)

    def __str__(self):
        return str(self.fpo)

class IssuedSharedCapital(models.Model):
    fpo = models.ForeignKey(FPO, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    no_of_share=models.CharField(max_length=5)
    face_value=models.CharField(max_length=10)
    total_value=models.CharField(max_length=15)

    def __str__(self):
        return str(self.fpo)

class CompnayMeetingDetails(models.Model):
    fpo=models.ForeignKey(FPO, on_delete=models.CASCADE)
    metting_type=models.CharField(max_length=50)
    date=models.DateField(default=date.today)
    purpose=models.CharField(max_length=128)
    notes=models.TextField()

    def __str__(self):
        return str(self.fpo.name)

class FpoCaInformation(models.Model):
    fpo = models.ForeignKey(FPO, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=255)
    middle_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email_id=models.CharField(max_length=255,unique=True)
    firm_name=models.CharField(max_length=255)

    def __str__(self):
        return self.email_id

class FpoAuthorisedPersonInBank(models.Model):
    fpo_name = models.ForeignKey(FPO, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=10)


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('other', 'Other')
)

class FpoBankDetails(models.Model):
    fpo=models.ForeignKey(FPO, on_delete=models.CASCADE)
    name=models.CharField(max_length=128)
    contact_number=models.CharField(max_length=10)
    bank_name=models.CharField(max_length=255)
    account_number=models.CharField(max_length=16)
    branch=models.CharField(max_length=255)
    full_address=models.CharField(max_length=500)
    ifsc_code=models.CharField(max_length=11)
    authorised_person=models.CharField(max_length=128)
    bank_statement_doc=models.ImageField(upload_to='fpo/bank/bank_statement/')
    passbook_doc=models.ImageField(upload_to='fpo/bank/passbook_doc/')

class Bank(models.Model):
    name=models.CharField(max_length=128)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Farmer(models.Model):
    #     # user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fpo_name = models.ForeignKey(FPO, on_delete=models.CASCADE)
    #     si_no_of_share_holder = models.CharField(max_length=15)
    share_holder_name = models.CharField(max_length=15)

    #     state = models.ForeignKey(State, on_delete=models.CASCADE)
    #     district = models.ForeignKey(District, on_delete=models.CASCADE)
    #     block = models.ForeignKey(City, on_delete=models.CASCADE)
    #     gram_panchayat = models.CharField(max_length=50)
    #     fpo_registration_no = models.CharField(max_length=20)
    #     farmer_name = models.CharField(max_length=128)
    #     fig_name = models.CharField(max_length=128)
    #     village = models.CharField(max_length=50)
    #     pg_name = models.CharField(max_length=50)
    #     hamlet = models.CharField(max_length=50)
    #     hh_name = models.CharField(max_length=50)
    #     father_and_husband_name = models.CharField(max_length=128)
    #     gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    #     age = models.CharField(max_length=3)
    #     category = models.CharField(max_length=10)
    #     member_of_fig = models.BooleanField(null=True)
    #     name_of_the_fig = models.CharField(max_length=128)
    #     bpl_status = models.BooleanField(default=False)
    #     have_you_received_aadhar_card_consent = models.BooleanField(default=False)
    #     aadhar_card_no = models.CharField(max_length=10)
    #     bank_account_no = models.CharField(max_length=255)
    #     number_of_family_member = models.CharField(max_length=3)
    #     annual_income = models.CharField(max_length=8)
    #     livestock_income = models.CharField(max_length=8)
    #     labour = models.CharField(max_length=3)
    #     ntfp = models.CharField(max_length=10)
    #     micro_enterprise = models.CharField(max_length=128)
    #     other_income = models.CharField(max_length=128)
    #     member_of_cooperative_agriculture_societies = models.BooleanField(default=False)
    #     total_land = models.CharField(max_length=128)
    #     land_record_details = models.CharField(max_length=128)
    #     upland_irrigated = models.CharField(max_length=10)
    #     medium_upland_irrigated = models.CharField(max_length=10)
    #     low_land_irrigated = models.CharField(max_length=10)
    #     leased_land = models.BooleanField(default=False)
    #     leased_land_area = models.CharField(max_length=5)
    #     year_of_share_issued = models.DateField(default=date.today)
    #     generate_share_certificate_number = models.BooleanField(default=False)
    #     distinctive_total_number_of_share = models.CharField(max_length=10)
    #     total_capital_amount_deposited = models.CharField(max_length=15)
    #     nominee = models.CharField(max_length=128)
    #     relationship_with_nominee = models.CharField(max_length=128)
    #     address_of_the_nominee = models.CharField(max_length=255)
    #     ivrs_or_other_alerts = models.BooleanField(default=False)
    #     mobile_number = models.CharField(max_length=10)
    #     dob_of_farmer = models.DateField(default=date.today)
    #     social_category = models.CharField(max_length=128)
    #     kharif_crop = models.CharField(max_length=15)
    #     sowing_month = models.CharField(max_length=20)
    #     marketing_month = models.CharField(max_length=20)
    #     robi_crop = models.CharField(max_length=20)
    #     zayed_crop = models.CharField(max_length=30)
    #     names_of_agri_machinery_owner = models.CharField(max_length=30)
    #     name_of_market = models.CharField(max_length=30)
    #     Livestock_activity = models.BooleanField(default=False)
    #     byp_number = models.CharField(max_length=15)
    #     shed_type = models.CharField(max_length=35)
    #     vaccine_interval = models.CharField(max_length=15)
    #     tagging_status = models.BooleanField(default=False)
    #     pig_number = models.CharField(max_length=5)
    #     cow_number = models.CharField(max_length=3)
    #     buffalo_number = models.CharField(max_length=3)
    #     face_value_of_share = models.CharField(max_length=6)
    #     mambers_hip_amount_paid = models.CharField(max_length=6)
    #     premium_amount_paid = models.CharField(max_length=6)
    #     any_entrepreneural_activity = models.CharField(max_length=6)
    #     packhouse_available = models.CharField(max_length=128)
    #     drying_yard_available = models.CharField(max_length=20)
    #     other_livelihood = models.CharField(max_length=30)
    #     poly_or_shed_house = models.CharField(max_length=255)
    #     any_commerical_vehicle = models.CharField(max_length=50)
    #     onwed_vehicle = models.CharField(max_length=50)
    #     house_type = models.CharField(max_length=50)
    #     aadhar_attached = models.BooleanField(default=False)
    #     pan_attached = models.BooleanField(default=False)
    #     bank_details_attached = models.BooleanField(default=False)
    #     land_records_attached = models.BooleanField(default=False)
    #     delete_status = models.BooleanField(default=True)
    #
    def __str__(self):
        return str(self.share_holder_name)


class BankStatementUpload(models.Model):
    fpo = models.ForeignKey(FPO, on_delete=models.CASCADE)
    bank_statement_doc = models.ImageField(upload_to='fpo/bank_statement_documents/')

# class PassBookUpload(models.Model):
#     # fpo = models.ForeignKey(FPO, on_delete=models.CASCADE)
#     bank_statement_doc = models.ImageField(upload_to='fpo/bank_statement_documents/')