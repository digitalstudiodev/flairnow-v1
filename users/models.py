from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from PIL import Image
from django.urls import reverse
from django.utils import timezone
from multiselectfield import MultiSelectField

BINARY = (
    ("Y","Yes"),
    ("N","No"),
)

GPA = (
    ("N","I don't have a GPA"),
    ("G0","Below 1.0"),
    ("G1","Between 1.0 and 1.5"),
    ("G2","Between 1.5 and 2.0"),
    ("G3","Between 2.0 and 2.5"),
    ("G4","Between 2.5 and 3.0"),
    ("G5","Between 3.0 and 3.5"),
    ("G6","Between 3.5 and 4.0"),
    ("P","Prefer Not To Say"),
)

ACT_SCORES = (
    ("N","Did not take the ACT"),
    ("A0","Below 5"),
    ("A1","Between 5 and 7"),
    ("A2","Between 7 and 9"),
    ("A3","Between 9 and 11"),
    ("A4","Between 11 and 13"),
    ("A5","Between 13 and 15"),
    ("A6","Between 15 and 17"),
    ("A7","Between 17 and 19"),
    ("A8","Between 19 and 21"),
    ("A9","Between 21 and 23"),
    ("A10","Between 23 and 25"),
    ("A11","Between 25 and 27"),
    ("A12","Between 27 and 29"),
    ("A13","Between 29 and 31"),
    ("P","Prefer Not To Say"),
)

SAT_SCORES = (
    ("N","Did not take the SAT"),
    ("S0","Below 500"),
    ("S1","Between 500 and 550"),
    ("S2","Between 550 and 600"),
    ("S3","Between 600 and 650"),
    ("S4","Between 650 and 700"),
    ("S5","Between 700 and 750"),
    ("S6","Between 750 and 800"),
    ("S7","Between 800 and 850"),
    ("S8","Between 850 and 900"),
    ("S9","Between 900 and 950"),
    ("S10","Between 950 and 1000"),
    ("S11","Between 1000 and 1050"),
    ("S12","Between 1050 and 1100"),
    ("S13","Between 1100 and 1150"),
    ("S14","Between 1150 and 1200"),
    ("S15","Between 1200 and 1250"),
    ("S16","Between 1250 and 1300"),
    ("S17","Between 1300 and 1350"),
    ("S18","Between 1350 and 1400"),
    ("S19","Between 1400 and 1450"),
    ("S20","Between 1450 and 1500"),
    ("S21","Between 1500 and 1550"),
    ("S22","Between 1550 and 1600"),
    ("P","Prefer Not To Say"),
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
    ("HI0","Less than $10,000"),
    ("HI1","Between $10,000 - $25,000"),
    ("HI2","Between $25,000 - $50,000"),
    ("HI3","Between $50,000 - $100,000"),
    ("HI4","Between $100,000 - $150,000"),
    ("HI5","Between $150,000 - $200,000"),
    ("HI6","Over $200,000"),
    ("P","Prefer Not To Say"),
)

HOUSE_SIZE = (
    ("HS0","Small (Less than 3)"),
    ("HS1","Midsize (3-5)"),
    ("HS2","Large (Over 5)"),
    ("HS3","X-Large (Over 10)"),
    ("P","Prefer Not To Say"),
)

CITIZENSHIP = (
    ("C0","U.S. Citizen"),
    ("P","Prefer Not To Say"),
)

RACE = (
    ("R0","American Indian or Alaska Native"),
    ("R1","Asian"),
    ("R2","Black or African American"),
    ("R3","Hispanic or Latino"),
    ("R4","Native Hawaiian or Other Pacific Islander"),
    ("R5","White"),
    ("P","Prefer Not To Say"),
)

SEX = (
    ("HO","Heterosexual"),
    ("HE","Homosexual"),
    ("BI","Bisexual"),
    ("AS","Asexual"),
    ("NB","Non-Binary"),
    ("P","Prefer Not To Say"),
)

GENDERS = (
    ("M","Male"),
    ("F","Female"),
    ("O","Other"),
    ("P","Prefer Not To Say"),
)

YEARS = (
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
    ("P","Prefer Not To Say"),
)

CURRENT_GRADE_LEVEL = (
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
    ("P","Prefer Not To Say"),
)

DEGREES = (
    ("L0","High School Diploma (or Equivalent)"),
    ("L1","Associate Degree"),
    ("L2","Bachelor's Degree"),
    ("L3","Master's Degree"),
    ("L4","Doctoral Degree"),
    ("P","Prefer Not To Say"),
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
    '''
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    '''

##student resume
class Resume(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    date_posted = models.DateTimeField(default=timezone.now)
    resume = models.FileField(default="sample_resume.pdf", upload_to='resumes', verbose_name="Resume")
    
    def __str__(self):
        return self.date_posted

    def get_absolute_url(self):
        return reverse('users:resume-detail', kwargs={'pk': self.pk})

##student academic information
class Academic(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    date_posted = models.DateTimeField(default=timezone.now)
    college = models.CharField(max_length=1000, default="", null=True, verbose_name="Current or Preferred College/University")
    current_grade_level = models.CharField(max_length=1000, choices=CURRENT_GRADE_LEVEL, default=None, null=True, verbose_name="Current Grade Level")
    degree_in_pursuit = models.CharField(max_length=1000, choices=DEGREES, default=None, null=True, verbose_name="Degree You Are Currently Pursuing")
    field = models.CharField(max_length=1000, choices=MAJORS, default=None, null=True, verbose_name="Current Major or Field")
    sat_score = models.CharField(max_length=1000, choices=SAT_SCORES, verbose_name="SAT Score", default=None, null=True)
    act_score = models.CharField(max_length=1000, choices=ACT_SCORES, verbose_name="ACT Score", default=None, null=True)
    gpa = models.CharField(max_length=1000, choices=GPA, verbose_name="GPA", default=None, null=True)
    expected_grad_year = models.CharField(max_length=1000, choices=YEARS, default=None, null=True, verbose_name="Expected Graudation Year")
    
    def __str__(self):
        return self.date_posted

    def get_absolute_url(self):
        return reverse('users:academic-detail', kwargs={'pk': self.pk})

##student background information
class Background(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    date_posted = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=1000, choices=GENDERS, default=None, null=True, verbose_name="Gender")
    sexual_orientation = models.CharField(max_length=1000, choices=SEX, default=None, null=True, verbose_name="Sexual Orientation")
    race = models.CharField(max_length=1000, choices=RACE, default=None, null=True, verbose_name="Race")
    citizenship = models.CharField(max_length=1000, choices=CITIZENSHIP, default=None, null=True, verbose_name="Citizenship")
    household_size = models.CharField(max_length=1000, choices=HOUSE_SIZE, default=None, null=True, verbose_name="Household Size")
    household_income = models.CharField(max_length=1000, choices=HOUSE_INCOME, default=None, null=True, verbose_name="Household Income")
    first_gen = models.CharField(max_length=1000, choices=BINARY, default=None, null=True, verbose_name="Are you the first in your family to go to college?")
    
    def __str__(self):
        return self.date_posted

    def get_absolute_url(self):
        return reverse('users:background-detail', kwargs={'pk': self.pk})

##student contact information
class Contact(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    date_posted = models.DateTimeField(default=timezone.now)
    phone_number = models.CharField(max_length=10, default="", null=True, verbose_name="Phone Number", help_text="Please enter in the following format: 9734568456, with no spaces or special characters.")
    date_of_birth = models.CharField(max_length=10, default="", null=True, verbose_name="Date of Birth", help_text="Please enter in the following format: MM/DD/YYY or MM-DD-YYY")
    primary_address = models.CharField(max_length=1000, default="", null=True, verbose_name="Primary Address")
    zip_code = models.CharField(max_length=1000, default="", null=True, verbose_name="Zip Code")
    city = models.CharField(max_length=1000, default="", null=True, verbose_name="City")
    state = models.CharField(max_length=1000, choices=US_STATES, default=None, null=True, verbose_name="State")
    
    def __str__(self):
        return self.date_posted

    def get_absolute_url(self):
        return reverse('users:contact-detail', kwargs={'pk': self.pk})

##organization contact information
class OrganizationContact(models.Model):
    organization = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Organization")
    date_posted = models.DateTimeField(default=timezone.now)
    phone_number = models.CharField(max_length=10, default="", null=True, verbose_name="Phone Number", help_text="Please enter in the following format: 9734568456")
    primary_address = models.CharField(max_length=1000, default="", null=True, verbose_name="Primary Address")
    zip_code = models.CharField(max_length=1000, default="", null=True, verbose_name="Zip Code")
    city = models.CharField(max_length=1000, default=None, null=True, verbose_name="City")
    state = models.CharField(max_length=1000, choices=US_STATES, default=None, null=True, verbose_name="State")
    website_link = models.CharField(max_length=1000, default="", null=True, verbose_name="Website Link")
    facebook_link = models.CharField(max_length=1000, default="", null=True, verbose_name="Facebook Link")
    linkedin_link = models.CharField(max_length=1000, default="", null=True, verbose_name="LinkedIn Link")
    twitter_link = models.CharField(max_length=1000, default="", null=True, verbose_name="Twitter Link")

    def __str__(self):
        return self.phone_number

    def get_absolute_url(self):
        return reverse('users:organizationcontact-detail', kwargs={'pk': self.pk})

##organization background information
class OrganizationBackground(models.Model):
    organization = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Organization")
    date_posted = models.DateTimeField(default=timezone.now)
    size = models.IntegerField(default=None, null=True, verbose_name="Number of Individuals")
    industry = models.CharField(max_length=1000, choices=MAJORS, default=None, null=True, verbose_name="Industry")
    type = models.CharField(max_length=1000, choices=ORGANIZATION_TYPES, default=None, null=True, verbose_name="Organization Type")


    def __str__(self):
        return self.date_posted

    def get_absolute_url(self):
        return reverse('users:organizationbackground-detail', kwargs={'pk': self.pk})

##internship common application
class InternCommonApp(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    date_posted = models.DateTimeField(default=timezone.now)
    q1 = models.TextField(max_length=1000, verbose_name="Tell Us About a Situation Where You Took Initiative or Took on a Leadership Role.", help_text="Max Length (1000 characters)")
    q2 = models.TextField(max_length=1000, verbose_name="What’s the Best Team You’ve Ever Been a Part of, and Why?/What’s Your Ideal Team?", help_text="Max Length (1000 characters)")
    q3 = models.TextField(max_length=1000, verbose_name="Why Are You Interested in This Internship/Company/Industry, and What Skills or Experiences Do You Hope to Gain?", help_text="Max Length (1000 characters)")

    def __str__(self):
        return self.date_posted

    def get_absolute_url(self):
        return reverse('users:internship-common-application-detail', kwargs={'pk': self.pk})

##scholarship common application
class ScholarCommonApp(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    date_posted = models.DateTimeField(default=timezone.now)
    q1 = models.TextField(max_length=1000, verbose_name="Tell us about yourself.", help_text="Max Length (1000 characters)")
    q2 = models.TextField(max_length=1000, verbose_name="What is your greatest strength/weakness?", help_text="Max Length (1000 characters)")
    q3 = models.TextField(max_length=1000, verbose_name="Who has been a role model for you?", help_text="Max Length (1000 characters)")

    def __str__(self):
        return self.date_posted

    def get_absolute_url(self):
        return reverse('users:scholarship-common-application-detail', kwargs={'pk': self.pk})