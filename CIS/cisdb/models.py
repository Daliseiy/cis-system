from django.db import models
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

MARITIAL_STATUS = (
    ("Single","Single"),
    ("Married","Married"),
    ("Divorced","Divorced"),
    ("Widowed","Widowed"),
)

STATE = (
    ("Abia","Abia"),
    ("Adamawa","Adamawa"),
    ("Akwa Ibom","Akwa Ibom"),
    ("Anambra","Anambra"),
    ("Bauchi","Bauchi"),
    ("Bayelsa","Bayelsa"),
    ("Benue","Benue"),
    ("Borno","Cross River"),
    ("Cross River","Cross River"),
    ("Delata","Delta"),
    ("Ebonyi","Ebonyi"),
    ("Edo","Edo"),
    ("Ekiti","Ekiti"),
    ("Enugu","Enugu"),
    ("Gombe","Gombe"),
    ("Imo","Imo"),
    ("Jigawa","Jigawa"),
    ("Kaduna","Kano"),
    ("Katsina","Katsina"),
    ("Kebbi","Kebbi"),
    ("Kogi","Kogi"),
    ("Kwara","Kwara"),
    ("Lagos","Lagos"),
    ("Nasarawa","Nasarawa"),
    ("Niger","Niger"),
    ("Ogun","Ogun"),
    ("Ondo","Ondo"),
    ("Osun","Osun"),
    ("Oyo","Oyo"),
    ("Plateau","Plateau"),
    ("Rivers","Rivers"),
    ("Sokoto","Taraba"),
    ("Yobe",'Yobe'),
    ("Zamfara","Zamfara"),
)

GENDER = (
    ("Male","Male"),
    ("Female","Female")
)

BLOOD_TYPE = (
    ("A", 'A'),
    ("B", "B"),
    ("AB", "AB"),
    ("O", "O")
)

GENOTYPE = (
    ("AA","AA"),
    ("AS","AS"),
    ("SS","SS"),
    ("Other","Others: CC, AC..")
)



class Citizen(models.Model):
    '''Name Data'''
    first_name = models.CharField(max_length=50,blank=False,null=False,help_text='First Name')
    surname = models.CharField(max_length=50,help_text='Surname')
    other_name = models.CharField(max_length=50, help_text='Other Name')
    sex = models.CharField(choices=GENDER,blank=False,null=False,max_length=7)
    date_of_birth = models.DateField()
    image = models.ImageField(default="default.jpg", upload_to="images")

    '''Basic Family Data'''
    name_of_father = models.CharField(max_length=50,help_text="Father\'s name",blank=True,default="None")
    name_of_mother = models.CharField(max_length=50,help_text="Mother\'s name",blank=True,default="None")
    name_of_siblings = models.CharField(max_length=1250,help_text="Name of Brother\'s / Sister\'s",blank=True,default="None")
    marital_status = models.CharField(choices=MARITIAL_STATUS,max_length=15)
    name_of_spouse = models.CharField(max_length=50,help_text="Spouse name if any",blank=True,default="None")
    marriage_information = models.TextField(help_text='Leave Blank if Single' )
    name_of_children = models.CharField(max_length=1000,default="None")
    '''Contact Information'''
    state_of_origin = models.CharField(choices=STATE,max_length=15)
    LGA = models.CharField(max_length=50,help_text='Local Goverment Area')
    state_of_residence = models.CharField(choices=STATE,max_length=15)
    residential_address = models.CharField(max_length=500,help_text='Home Address')
    phone_number = PhoneNumberField()
    other_number = PhoneNumberField(blank=True)
    email = models.EmailField()
    language_spoken = models.CharField(max_length=350,help_text='Language(s) spoken')
    national_id = models.CharField(max_length=50)
    

    '''Health Information'''
    blood_type = models.CharField(choices=BLOOD_TYPE,blank=False,null=False, max_length=3)
    genotype = models.CharField(choices=GENOTYPE,blank=True,null=True, max_length=3)
    disability = models.CharField(max_length=1000,
        help_text='Specify disability and cause and time of disablity \n e.g Blindess-Car Accident 2012',
        default="No Disablilites"
    )
    allergies = models.CharField(max_length=1000,default="No Allegries")
    height = models.FloatField()
    weight = models.FloatField()

    '''Academic Qualifications'''
    primary_education = models.TextField(help_text='Nigerian Primary School - (2000-2009)', default='None',)
    secondary_education = models.TextField(help_text='Nigerian Secondary School - (2009-2015)', default='None',)
    university_education = models.CharField(max_length=250,help_text="University of Technology, Nigeria - (2019-2024)",default="None")
    academic_qualifications = models.TextField(help_text='Bsc - Nigerian University(2020)',default='None',)
    occupation = models.CharField(max_length=250,help_text='Pilot')
    work_experience = models.TextField(help_text='Worked as a Consultant at Shell (2021-2023)')

    def __str__(self):
        return f'%s %s %s' % (self.surname,self.first_name,self.other_name)
    
    def get_fields(self):
        return [(field.verbose_name,field.value_from_objects(self))]

    def get_absolute_url(self):
            return reverse("detail_data", args=[str(self.pk)])