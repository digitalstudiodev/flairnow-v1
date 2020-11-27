from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from PIL import Image
from django.urls import reverse
from django.utils import timezone
from multiselectfield import MultiSelectField
from phone_field import PhoneField

BINARY = (
    ("Y","Yes"),
    ("N","No"),
)

GPA = (
    ("N","None"),
    ("G0","Below 1.0"),
    ("G1","Between 1.0 and 1.5"),
    ("G2","Between 1.5 and 2.0"),
    ("G3","Between 2.0 and 2.5"),
    ("G4","Between 2.5 and 3.0"),
    ("G5","Between 3.0 and 3.5"),
    ("G6","Between 3.5 and 4.0"),
)

ORGANIZATION_TYPES = (
    ("LLC","Limited Liability Company"),
    ("NPC","Non-Profit Corporation"),
    ("HSS","High School"),
    ("EDU","College or University"),
    ("SDS","School District"),
    ("TWN","City or Town"),
    ("OTH","Other"),
)

US_STATES = (
    ("AL","Alabama"),
    ("AK","Alaska"),
    ("AZ","Arizona"),
    ("AR","Arkansas"),
    ("CA","California"),
    ("CO","Colorado"),
    ("CT","Connecticut"),
    ("DE","Delaware"),
    ("FL","Florida"),
    ("GA","Georgia"),
    ("HI","Hawaii"),
    ("ID","Idaho"),
    ("IL","Illinois"),
    ("IN","Indiana"),
    ("IA","Iowa"),
    ("KS","Kansas"),
    ("KY","Kentucky"),
    ("LA","Louisiana"),
    ("ME","Maine"),
    ("MD","Maryland"),
    ("MA","Massachusetts"),
    ("MI","Michigan"),
    ("MN","Minnesota"),
    ("MS","Mississippi"),
    ("MO","Missouri"),
    ("MT","Montana"),
    ("NE","Nebraska"),
    ("NV","Nevada"),
    ("NH","New Hampshire"),
    ("NJ","New Jersey"),
    ("NM","New Mexico"),
    ("NY","New York"),
    ("NC","North Carolina"),
    ("ND","North Dakota"),
    ("OH","Ohio"),
    ("OK","Oklahoma"),
    ("OR","Oregon"),
    ("PA","Pennsylvania"),
    ("RI","Rhode Island"),
    ("SC","South Carolina"),
    ("SD","South Dakota"),
    ("TN","Tennessee"),
    ("TX","Texas"),
    ("UT","Utah"),
    ("VT","Vermont"),
    ("VA","Virginia"),
    ("WA","Washington"),
    ("WV","West Virginia"),
    ("WI","Wisconsin"),
    ("WY","Wyoming"),
    ("DC","District of Columbia"),
)

HOUSE_INCOME = (
    ("N","None"),
    ("HI0","Less than $10,000"),
    ("HI1","Between $10,000 - $25,000"),
    ("HI2","Between $25,000 - $50,000"),
    ("HI3","Between $50,000 - $100,000"),
    ("HI4","Between $100,000 - $150,000"),
    ("HI5","Between $150,000 - $200,000"),
    ("HI6","Over $200,000"),
)

HOUSE_SIZE = (
    ("N","None"),
    ("HS0","Small (Less than 3)"),
    ("HS1","Midsize (3-5)"),
    ("HS2","Large (Over 5)"),
    ("HS3","X-Large (Over 10)"),
)

CITIZENSHIP = (
    ("N","None"),
    ("C0","U.S. Citizen"),
    ("C1","U.S. Permanent Resident"),
    ("C2","DACA"),
    ("C3","TPS"),
    ("OTH","Other"),
)

RACE = (
    ("N","None"),
    ("R0","American Indian or Alaska Native"),
    ("R1","Asian"),
    ("R2","Black or African American"),
    ("R3","Hispanic or Latino"),
    ("R4","Native Hawaiian or Other Pacific Islander"),
    ("R5","White"),
)

SEX = (
    ("N","None"),
    ("HO","Heterosexual"),
    ("HE","Homosexual"),
    ("BI","Bisexual"),
    ("AS","Asexual"),
    ("NB","Non-Binary"),
)

GENDERS = (
    ("N","None"),
    ("M","Male"),
    ("F","Female"),
    ("O","Other"),
)

YEARS = (
    ("N","None"),
    ("1990","1990"),
    ("1991","1991"),
    ("1992","1992"),
    ("1993","1993"),
    ("1994","1994"),
    ("1995","1995"),
    ("1996","1996"),
    ("1997","1997"),
    ("1998","1998"),
    ("1999","1999"),
    ("2000","2000"),
    ("2001","2001"),
    ("2002","2002"),
    ("2003",'2003'),
    ("2004","2004"),
    ("2005","2005"),
    ("2006","2006"),
    ("2007",'2007'),
    ('2008','2008'),
    ('2009','2009'),
    ('2010','2010'),
    ('2011','2011'),
    ('2012','2012'),
    ("2013","2013"),
    ('2014',"2014"),
    ("2015",'2015'),
    ('2016','2016'),
    ('2017','2017'),
    ('2018','2018'),
    ('2019','2019'),
    ('2020','2020'),
    ('2021','2021'),
    ('2022','2022'),
    ('2023','2023'),
    ('2024','2024'),
    ('2025','2025'),
    ('2026','2026'),
    ('2027','2027'),
    ('2028','2028'),
    ('2029','2029'),
    ('2030',"2030"),
    ("2031","2031"),
    ("2032","2032"),
    ("2033",'2033'),
    ("2034","2034"),
    ("2035","2035"),
    ('2036','2036'),
    ('2037','2037'),
    ('2038',"2038"),
    ('2039','2039'),
    ('2040',"2040"),
)

EDU_LEVEL = (
    ("N","None"),
    ("L0","Middle School (7, 8 Grades)"),
    ("L1","Grade 9 High School"),
    ("L2","Grade 10 High School"),
    ("L3","Grade 11 High School"),
    ("L4","Grade 12 High School"),
    ("L5","First Year Undergraduate"),
    ("L6","Second Year Undergraduate"),
    ("L7","Third Year Undergraduate"),
    ("L8","Fourth Year Undergraduate"),
    ("L9","Five Year or More Undergraduate"),
    ("L10","Graduate Student"),
    ("L11","Vocational Education"),
)

DEGREES = (
    ("N","None"),
    ("L0","High School Diploma (or Equivalent)"),
    ("L1","Associate Degree"),
    ("L2","Bachelor's Degree"),
    ("L3","Master's Degree"),
    ("L4","Doctoral Degree"),
)

#based from https://www.collegemajors101.com/ with over 150 majors listed
MAJORS = (
    ##F level for "Medical & Life Sciences"
    ("F0","Athletic Training"),
    ("F1","Biology"),
    ("F2","Chemistry"),
    ("F3","Phyics"),
    ("F4","Environmental Science"),
    ("F5","Exercise Sci/Kinesiology"),
    ("F6","Fisheries and Wildlife"),
    ("F7","Food Science"),
    ("F8","Forest Management"),
    ("F9","Marine Science"),
    ("F10","Nursing (RN/BSN)"),
    ("F11","Organic/Urban Farming"),
    ("F12","Pharmacy"),
    ("F13","Physicians Assistant"),
    ("F14","Pre - Dental"),
    ("F15","Pre - Medical"),
    ("F15","Pre - Veterinary Medicine"),
    #L level for "Visual & Performance Arts"
    ("L0","Apparel/Textile Design"),
    ("L1","Dance"),
    ("L2","Film/Broadcast"),
    ("L3","Fine/Studio Art"),
    ("L4","Graphic Design"),
    ("L5","Industrial Design"),
    ("L6","Interior Design"),
    ("L7","Landscape Architecture"),
    ("L8","Music"),
    ("L9","Theatre"),
    ("L10","Urban Planning"),
    ("L11","Video Game Design"),
    ("L12","Web Design/Digital Media"),
    #A level for "Liberal Arts"
    ("A0","Arts Management"),
    ("A1","Education"),
    ("A2","Emergency Management"),
    ("A3","English/Writing"),
    ("A4","Equine Science/Mgmt"),
    ("A5","Family & Child Science"),
    ("A6","History"),
    ("A7","Journalism"),
    ("A8","Language Studies"),
    ("A9","Non-Profit Management"),
    ("A10","Parks and Recreation Management"),
    ("A11","Peace/Conflict Studies"),
    ("A12","Philosophy"),
    ("A13","Political Science"),
    ("A14","Psychology / Sociology"),
    ("A15","Sports Turf/Golf Mgmt"),
    ("A16","Women/Gender Studies"),
    #I level for "Engineering & Technology"
    ("I0","Aerospace Engineering"),
    ("I1","Astronomy / Physics"),
    ("I2","Aviation/Aeronautics"),
    ("I3","Biomedical Engineering"),
    ("I4","Chemical Engineering"),
    ("I5","Civil Engineering"),
    ("I6","Computer Science"),
    ("I7","Cyber Security"),
    ("I8","Electrical Engineering"),
    ("I9","Energy Science"),
    ("I10","Industrial Engineering"),
    ("I11","Industrial Technology"),
    ("I12","Materials Science"),
    ("I13","Mathematics"),
    ("I14","Mechanical Engineering"),
    #R level for "Business"
    ("R0","Accounting - General"),
    ("R1","Business - General"),
    ("R2","Construction Management"),
    ("R3","Data Science - Analytics"),
    ("R4","Economics (National + Global)"),
    ("R5","Finance"),
    ("R6","Hospitality Management"),
    ("R7","Human Resources Mgmt"),
    ("R8","Information Systems (MIS)"),
    ("R9","Insurance & Risk Mgmt"),
    ("R10","Marketing / Advertising"),
    ("R11","Public Health Administration"),
    ("R12","Sport Management"),
    ("R13","Supply Chain Mgmt (Logistics)"),
)

class Manager(BaseUserManager):
    def create_user(self, first_name, last_name, org_name, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not org_name:
            raise ValueError("Users must have an organization name")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            org_name=org_name,
            email=self.normalize_email(email),
            password=password,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, org_name, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            org_name=org_name,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email Address", max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name="Date Joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(max_length=30, default=None, null=True, verbose_name="First Name")
    last_name = models.CharField(max_length=30, default=None, null=True, verbose_name="Last Name")
    org_name = models.CharField(max_length=30, default=None, null=True, verbose_name="Organization Name")
    is_student = models.BooleanField(default=True)
    is_organization = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'org_name']

    objects = Manager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics', verbose_name="Profile Picture")

    def __str__(self):
        return f'{self.user.email} Profile'

class Academic(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    school = models.CharField(max_length=1000, default="", null=True, verbose_name="Current or Preferred Institution")
    edu_level = models.CharField(max_length=1000, choices=EDU_LEVEL, default="", null=True, verbose_name="Edu Level")
    degree = models.CharField(max_length=1000, choices=DEGREES, default="", null=True, verbose_name="Degree You Are Currently Pursuing")
    field = models.CharField(max_length=1000, choices=MAJORS, default="", null=True, verbose_name="Current Major or Field")
    gpa = models.CharField(max_length=1000, choices=GPA, verbose_name="GPA", default="", null=True)
    grad_year = models.CharField(max_length=1000, choices=YEARS, default="", null=True, verbose_name="Class")
    
    def __str__(self):
        return self.student.email

    def get_absolute_url(self):
        return reverse('users:academic_detail', kwargs={'pk': self.pk})

class Background(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    gender = models.CharField(max_length=1000, choices=GENDERS, default="", null=True, verbose_name="Gender")
    sex = models.CharField(max_length=1000, choices=SEX, default="", null=True, verbose_name="Sexual Orientation")
    race = models.CharField(max_length=1000, choices=RACE, default="", null=True, verbose_name="Race")
    citizenship = models.CharField(max_length=1000, choices=CITIZENSHIP, default="", null=True, verbose_name="Citizenship")
    household_size = models.CharField(max_length=1000, choices=HOUSE_SIZE, default="", null=True, verbose_name="Household Size")
    household_income = models.CharField(max_length=1000, choices=HOUSE_INCOME, default="", null=True, verbose_name="Household Income")
    first_gen = models.CharField(max_length=1000, choices=BINARY, default="", null=True, verbose_name="Are you the first in your family to go to college?")
    
    def __str__(self):
        return self.student.email

    def get_absolute_url(self):
        return reverse('users:background_detail', kwargs={'pk': self.pk})

class Contact(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    phone = models.CharField(default="", null=True, max_length=10, verbose_name="Phone Number")
    dob = models.CharField(max_length=10, default="", null=True, verbose_name="Date of Birth")
    primary_address = models.CharField(max_length=1000, default="", null=True, verbose_name="Primary Address")
    secondary_address = models.CharField(max_length=1000, default="", null=True, verbose_name="Secondary Address")
    zip_code = models.CharField(max_length=5, default="", null=True, verbose_name="Zip Code", help_text="Example 07102")
    city = models.CharField(max_length=1000, default="", null=True, verbose_name="City")
    state = models.CharField(max_length=1000, choices=US_STATES, default="", null=True, verbose_name="State")
    
    def __str__(self):
        return self.student.email

    def get_absolute_url(self):
        return reverse('users:contact_detail', kwargs={'pk': self.pk})

class OrgContact(models.Model):
    organization = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Organization")
    phone = models.CharField(max_length=10, default="", null=True, verbose_name="Phone Number")
    primary_address = models.CharField(max_length=1000, default="", null=True, verbose_name="Primary Address")
    secondary_address = models.CharField(max_length=1000, default="", null=True, verbose_name="Secondary Address")
    zip_code = models.CharField(max_length=5, default="", null=True, verbose_name="Zip Code", help_text="Example 07102")
    city = models.CharField(max_length=1000, default="", null=True, verbose_name="City")
    state = models.CharField(max_length=1000, choices=US_STATES, default="", null=True, verbose_name="State")
    website_link = models.CharField(max_length=1000, default="", null=True, verbose_name="Website Link")

    def __str__(self):
        return self.phone_number

    def get_absolute_url(self):
        return reverse('users:orgcontact_detail', kwargs={'pk': self.pk})

class OrgBackground(models.Model):
    organization = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Organization")
    size = models.IntegerField(default=1, null=True, verbose_name="Number of Individuals")
    industry = models.CharField(max_length=1000, choices=MAJORS, default="", null=True, verbose_name="Industry")
    org_type = models.CharField(max_length=1000, choices=ORGANIZATION_TYPES, default="", null=True, verbose_name="Organization Type")


    def __str__(self):
        return self.organization.email

    def get_absolute_url(self):
        return reverse('users:orgbackground_detail', kwargs={'pk': self.pk})

class UInternshipApp(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    date_posted = models.DateTimeField(default=timezone.now)
    q1 = models.TextField(max_length=1000, verbose_name="What’s the Best Team You’ve Ever Been a Part of, and Why?/What’s Your Ideal Team?", help_text="Max Length (1000 characters)")
    q2 = models.TextField(max_length=1000, verbose_name="What are your academic and/or career goals?", help_text="Max Length (1000 characters)")

    def __str__(self):
        return self.student.email

    def get_absolute_url(self):
        return reverse('users:u_internship_app_detail', kwargs={'pk': self.pk})

class UScholarshipApp(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    q1 = models.TextField(max_length=1000, verbose_name="How have you contributed to your community?", help_text="Max Length (1000 characters)")
    q2 = models.TextField(max_length=1000, verbose_name="Who has been a role model for you?", help_text="Max Length (1000 characters)")

    def __str__(self):
        return self.student.email

    def get_absolute_url(self):
        return reverse('users:u_scholarship_app_detail', kwargs={'pk': self.pk})