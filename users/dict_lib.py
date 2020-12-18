BINARY = (
    ("Y","Yes"),
    ("N","No"),
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
    ("2003","2003"),
    ("2004","2004"),
    ("2005","2005"),
    ("2006","2006"),
    ("2007","2007"),
    ("2008","2008"),
    ("2009","2009"),
    ("2010","2010"),
    ("2011","2011"),
    ("2012","2012"),
    ("2013","2013"),
    ("2014","2014"),
    ("2015","2015"),
    ("2016","2016"),
    ("2017","2017"),
    ("2018","2018"),
    ("2019","2019"),
    ("2020","2020"),
    ("2021","2021"),
    ("2022","2022"),
    ("2023","2023"),
    ("2024","2024"),
    ("2025","2025"),
)

ORG_TYPES = (
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

WORK = (
    ("W0","Career Growth"),
    ("W1","Company Culture"),
    ("W2","Company Mission"),
    ("W3","Company Perks"),
    ("W4","Company Presitge"),
    ("W5","Financial Upside"),
    ("W6","Individual Impact"),
    ("W7","Job Security"),
    ("W8","Mentorship"),
    ("W9","Peers"),
    ("W10","Personal Growth"),
    ("W11","Work-Life Balance"),
)

VALUES = (
    ("V0","Committed"),
    ("V1","Curious"),
    ("V2","Easy-Going"),
    ("V3","Flexible"),
    ("V4","Focused"),
    ("V5","Honest"),
    ("V6","Imaginative"),
    ("V7","Independent"),
    ("V8","Methodical"),
    ("V9","Outgoing"),
    ("V10","Persistent"),
    ("V11","Team Player"),
)

ENV = (
    ("E0","Chaotic"),
    ("E1","Collaborative"),
    ("E2","Creative"),
    ("E3","Direct"),
    ("E4","Entrepreneurial"),
    ("E5","Fast Paced"),
    ("E6","Flexible"),
    ("E7","Loud"),
    ("E8","Quiet"),
    ("E9","Relaxed"),
    ("E10","Rewarding"),
    ("E11","Social"),
    ("E12","Structured"),
    ("E13","Supportive"),
    ("E14","Transparent"),
)

ACT = (
    ("A0","Read"),
    ("A1","Watch or Play Sports"),
    ("A2","Exercise"),
    ("A3","Chill with Friends"),
    ("A4","Hang with Family"),
    ("A5","Travel"),
    ("A6","Code"),
    ("A7","Game"),
    ("A8","Cook"),
    ("A9","Watch Movies"),
    ("A10","Dance"),
    ("A11","Arts & Crafts"),
    ("A12","Go Outdoors"),
    ("A13","Photography"),
)

SKILLS = (
    ("S0","Read"),
    ("S1","Watch or Play Sports"),
    ("S2","Exercise"),
    ("S3","Chill with Friends"),
    ("S4","Hang with Family"),
    ("S5","Travel"),
    ("S6","Code"),
)

TYPES = (
    ("IN","Internship"),
    ("SC","Scholarship"),
)

EXTERNAL_TYPES = (
    ("EIN","Internship"),
    ("ESC","Scholarship"),
)

CONFIRM = (
    ("Y","Yes, I Confirm"),
)

STATUS = (
    ("P","Pending"),
    ("A","Accepted"),
    ("D","Denied"),
    ("W","Wait List")
)

GPA  = (
    ("None","None"),
)