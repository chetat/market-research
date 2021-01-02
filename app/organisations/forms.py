from app.models import *
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import Length, Required, ValidationError, InputRequired, Email, Optional




class OrganisationForm(FlaskForm):
    org_name = StringField('Organisation name', validators=[InputRequired(), Length(1, 64)])
    mobile_phone = IntegerField('Phone Number', validators=[InputRequired()])
    #logo = FileField('Organisation Logo', validators=[FileAllowed(images, 'Images only!')])
    #logo = FileField('Organisation Logo', validators=[Required(), FileAllowed(images, 'Images only!')])
    org_industry = SelectField(u'Select Industry', choices=[('Accountants', 'Accountants'),
                                                            ('Advertising/Public Relations',
                                                             'Advertising/Public Relations'),
                                                            ('Aerospace', 'Aerospace'),
                                                            ('Agribusiness', 'Agribusiness'),
                                                            ('Agricultural Services & Products',
                                                             'Agricultural Services & Products'),
                                                            ('Agriculture', 'Agriculture'),
                                                            ('Air Transport', 'Air Transport'),
                                                            ('Alternative Energy Production & Services',
                                                             'Alternative Energy Production & Services'),
                                                            ('Architectural Services', 'Architectural Services'),
                                                            ('Auto Manufacturers', 'Auto Manufacturers'),
                                                            ('Automotive', 'Automotive'),
                                                            ('Building Materials & Equipment',
                                                             'Building Materials & Equipment'),
                                                            ('Business Services', 'Business Services'),
                                                            ('Car Manufacturers', 'Car Manufacturers'),
                                                            ('Clothing Manufacturing', 'Clothing Manufacturing'),
                                                            ('Coal Mining', 'Coal Mining'),
                                                            ('Commercial Banks', 'Commercial Banks'),
                                                            (
                                                                'Communications/Electronics',
                                                                'Communications/Electronics'),
                                                            ('Computer Software', 'Computer Software'),
                                                            ('Construction', 'Construction'),
                                                            ('Construction Services', 'Construction Services'),
                                                            ('Crop Production & Basic Processing',
                                                             'Crop Production & Basic Processing'),
                                                            ('Defense Aerospace', 'Defense Aerospace'),
                                                            ('Defense Contractors', 'Defense Contractors'),
                                                            ('Drug Manufacturers', 'Drug Manufacturers'),
                                                            ('Education', 'Education'),
                                                            ('Electric Utilities', 'Electric Utilities'),
                                                            ('Electronics Manufacturing & Equipment',
                                                             'Electronics Manufacturing & Equipment'),
                                                            (
                                                                'Energy & Natural Resources',
                                                                'Energy & Natural Resources'),
                                                            ('Entertainment Industry', 'Entertainment Industry'),
                                                            ('Food Processing & Sales', 'Food Processing & Sales'),
                                                            ('Food Products Manufacturing',
                                                             'Food Products Manufacturing'),
                                                            ('For-profit Education', 'For-profit Education'),
                                                            (
                                                                'Forestry & Forest Products',
                                                                'Forestry & Forest Products'),
                                                            ('Funeral Services', 'Funeral Services'),
                                                            ('General Contractors', 'General Contractors'),
                                                            ('Health', 'Health'),
                                                            ('Health Services/HMOs', 'Health Services/HMOs'),
                                                            ('Hedge Funds', 'Hedge Funds'),
                                                            ('Health Care Services', 'Health Care Services'),
                                                            ('Home Builders', 'Home Builders'),
                                                            ('Industrial Unions', 'Industrial Unions'),
                                                            ('Insurance', 'Insurance'),
                                                            ('Labor', 'Labor'),
                                                            ('Legal', 'Legal'),
                                                            ('Livestock', 'Livestock'),
                                                            ('Lobbyists', 'Lobbyists'),
                                                            ('Lodging / Tourism', 'Lodging / Tourism'),
                                                            ('Manufacturing, Misc', 'Manufacturing, Misc'),
                                                            ('Marine Transport', 'Marine Transport'),
                                                            (
                                                                'Meat processing & products',
                                                                'Meat processing & products'),
                                                            ('Medical Supplies', 'Medical Supplies'),
                                                            ('Mining', 'Mining'),
                                                            ('Misc Business', 'Misc Business'),
                                                            ('Misc Finance', 'Misc Finance'),
                                                            ('Misc Manufacturing & Distributing',
                                                             'Misc Manufacturing & Distributing'),
                                                            ('Misc Unions', 'Misc Unions'),
                                                            ('Miscellaneous Defense', 'Miscellaneous Defense'),
                                                            ('Miscellaneous Services', 'Miscellaneous Services'),
                                                            (
                                                                'Mortgage Bankers & Brokers',
                                                                'Mortgage Bankers & Brokers'),
                                                            ('Non-profits, Foundations & Philanthropists',
                                                             'Non-profits, Foundations & Philanthropists'),
                                                            ('Nurses', 'Nurses'),
                                                            ('Nursing Homes/Hospitals', 'Nursing Homes/Hospitals'),
                                                            ('Nutritional & Dietary Supplements',
                                                             'Nutritional & Dietary Supplements'),
                                                            ('Oil & Gas', 'Oil & Gas'),
                                                            ('Payday Lenders', 'Payday Lenders'),
                                                            ('Pharmaceutical Manufacturing',
                                                             'Pharmaceutical Manufacturing'),
                                                            ('Pharmaceuticals / Health Products',
                                                             'Pharmaceuticals / Health Products'),
                                                            ('Phone Companies', 'Phone Companies'),
                                                            ('Postal Unions', 'Postal Unions'),
                                                            ('Poultry & Eggs', 'Poultry & Eggs'),
                                                            ('Power Utilities', 'Power Utilities'),
                                                            ('Printing & Publishing', 'Printing & Publishing'),
                                                            ('Professional Sports', 'Professional Sports'),
                                                            ('Public Sector Unions', 'Public Sector Unions'),
                                                            ('Publishing & Printing', 'Publishing & Printing'),
                                                            ('Real Estate', 'Real Estate'),
                                                            ('Record Companies/Singers', 'Record Companies/Singers'),
                                                            ('Recorded Music & Music Production',
                                                             'Recorded Music & Music Production'),
                                                            ('Recreation / Live Entertainment',
                                                             'Recreation / Live Entertainment'),
                                                            ('Religious Organizations/Clergy',
                                                             'Religious Organizations/Clergy'),
                                                            ('Residential Construction', 'Residential Construction'),
                                                            ('Restaurants & Drinking Establishments',
                                                             'Restaurants & Drinking Establishments'),
                                                            ('Retail Sales', 'Retail Sales'),
                                                            ('Savings & Loans', 'Savings & Loans'),
                                                            ('Schools/Education', 'Schools/Education'),
                                                            ('Sea Transport', 'Sea Transport'),
                                                            ('Securities & Investment', 'Securities & Investment'),
                                                            ('Special Trade Contractors', 'Special Trade Contractors'),
                                                            ('Sports, Professional', 'Sports, Professional'),
                                                            ('Steel Production', 'Steel Production'),
                                                            ('Stock Brokers/Investment Industry',
                                                             'Stock Brokers/Investment Industry'),
                                                            ('Student Loan Companies', 'Student Loan Companies'),
                                                            ('Sugar Cane & Sugar Beets', 'Sugar Cane & Sugar Beets'),
                                                            ('Teachers Unions', 'Teachers Unions'),
                                                            ('Teachers/Education', 'Teachers/Education'),
                                                            ('Telecom Services & Equipment',
                                                             'Telecom Services & Equipment'),
                                                            ('Telephone Utilities', 'Telephone Utilities'),
                                                            ('Textiles', 'Textiles'),
                                                            ('Timber & Logging', 'Timber & Logging'),
                                                            ('Paper Mills', 'Paper Mills'),
                                                            ('Tobacco', 'Tobacco'),
                                                            ('Transportation', 'Transportation'),
                                                            ('Transportation Unions', 'Transportation Unions'),
                                                            ('Trash Collection/Waste Management',
                                                             'Trash Collection/Waste Management'),
                                                            ('Trucking', 'Trucking'),
                                                            ('Unions', 'Unions'),
                                                            ('Venture Capital', 'Venture Capital'),
                                                            ('Waste Management', 'Waste Management'),
                                                            ('Occupational Therapy Assistant',
                                                             'Occupational Therapy Assistant'),
                                                            ('Orderly Attendant', 'Orderly Attendant'),
                                                            ('Pharmacy Clerk', 'Pharmacy Clerk'),
                                                            ('Physical Therapist Assistant',
                                                             'Physical Therapist Assistant'),
                                                            ('Physician Aide', 'Physician Aide'),
                                                            ('Physician Assistant', 'Physician Assistant'),
                                                            ('Psychiatric Aide', 'Psychiatric Aide'),
                                                            ('Radiation Therapist', 'Radiation Therapist'),
                                                            ('Recreational Therapist', 'Recreational Therapist'),
                                                            ('Regional Kidney Smart Educator',
                                                             'Regional Kidney Smart Educator'),
                                                            ('Technical Healthcare / Medical Roles',
                                                             'Technical Healthcare / Medical Roles'),
                                                            ('Athletic Trainer', 'Athletic Trainer'),
                                                            ('Certified Medical Assistant',
                                                             'Certified Medical Assistant'),
                                                            ('Certified Nurse Assistant', 'Certified Nurse Assistant'),
                                                            ('Certified Nursing Assistant',
                                                             'Certified Nursing Assistant'),
                                                            ('Clinical Liaison', 'Clinical Liaison'),
                                                            ('Clinical Nurse Manager', 'Clinical Nurse Manager'),
                                                            ('Clinical Research Associate',
                                                             'Clinical Research Associate'),
                                                            ('Clinical Research Coordinator',
                                                             'Clinical Research Coordinator'),
                                                            ('Clinical Reviewer', 'Clinical Reviewer'),
                                                            ('Clinical Specialist', 'Clinical Specialist'),
                                                            ('Dental Assistant', 'Dental Assistant'),
                                                            ('Dental Hygienist', 'Dental Hygienist'),
                                                            ('Dietitian', 'Dietitian'),
                                                            ('Exercise Physiologist', 'Exercise Physiologist'),
                                                            ('Health Educator', 'Health Educator'),
                                                            ('Home Health Aide', 'Home Health Aide'),
                                                            ('Hospice Aide', 'Hospice Aide'),
                                                            ('Massage Therapist', 'Massage Therapist'),
                                                            ('Nurse Aide', 'Nurse Aide'),
                                                            ('Nurse Clinical Educator', 'Nurse Clinical Educator'),
                                                            ('Nurse Consultant', 'Nurse Consultant'),
                                                            ('Nurse Informatics Analyst', 'Nurse Informatics Analyst'),
                                                            ('Nurse Manager', 'Nurse Manager'),
                                                            ('Nurse Paralegal', 'Nurse Paralegal'),
                                                            ('Nutritionist', 'Nutritionist'),
                                                            ('Occupational Therapy Assistant',
                                                             'Occupational Therapy Assistant'),
                                                            ('Orderly Attendant', 'Orderly Attendant'),
                                                            ('Pharmacy Clerk', 'Pharmacy Clerk'),
                                                            ('Physical Therapist Assistant',
                                                             'Physical Therapist Assistant'),
                                                            ('Physician Aide', 'Physician Aide'),
                                                            ('Physician Assistant', 'Physician Assistant'),
                                                            ('Psychiatric Aide', 'Psychiatric Aide'),
                                                            ('Radiation Therapist', 'Radiation Therapist'),
                                                            ('Recreational Therapist', 'Recreational Therapist'),
                                                            ('Regional Kidney Smart Educator',
                                                             'Regional Kidney Smart Educator')])
    org_website = StringField('Website', [Length(max=255)])
    org_city = StringField('City', [Length(max=255)])
    org_state = StringField('State', [Length(max=50)])
    org_country = SelectField(u'Select Country', choices=[

        ('Afganistan', 'Afghanistan'),
        ('Albania', 'Albania'),
        ('Algeria', 'Algeria'),
        ('American Samoa', 'American Samoa'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Anguilla', 'Anguilla'),
        ('Antigua & Barbuda', 'Antigua & Barbuda'),
        ('Argentina', 'Argentina'),
        ('Armenia', 'Armenia'),
        ('Aruba', 'Aruba'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('Bahamas', 'Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bermuda', 'Bermuda'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('Bonaire', 'Bonaire'),
        ('Bosnia & Herzegovina', 'Bosnia & Herzegovina'),
        ('Botswana', 'Botswana'),
        ('Brazil', 'Brazil'),
        ('British Indian Ocean Ter', 'British Indian Ocean Ter'),
        ('Brunei', 'Brunei'),
        ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'),
        ('Burundi', 'Burundi'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('Canary Islands', 'Canary Islands'),
        ('Cape Verde', 'Cape Verde'),
        ('Cayman Islands', 'Cayman Islands'),
        ('Central African Republic', 'Central African Republic'),
        ('Chad', 'Chad'),
        ('Channel Islands', 'Channel Islands'),
        ('Chile', 'Chile'),
        ('China', 'China'),
        ('Christmas Island', 'Christmas Island'),
        ('Cocos Island', 'Cocos Island'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo', 'Congo'),
        ('Cook Islands', 'Cook Islands'),
        ('Costa Rica', 'Costa Rica'),
        ('Cote DIvoire', 'Cote DIvoire'),
        ('Croatia', 'Croatia'),
        ('Cuba', 'Cuba'),
        ('Curaco', 'Curacao'),
        ('Cyprus', 'Cyprus'),
        ('Czech Republic', 'Czech Republic'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica', 'Dominica'),
        ('Dominican Republic', 'Dominican Republic'),
        ('East Timor', 'East Timor'),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'),
        ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Ethiopia', 'Ethiopia'),
        ('Falkland Islands', 'Falkland Islands'),
        ('Faroe Islands', 'Faroe Islands'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('French Guiana', 'French Guiana'),
        ('French Polynesia', 'French Polynesia'),
        ('French Southern Ter', 'French Southern Ter'),
        ('Gabon', 'Gabon'),
        ('Gambia', 'Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Ghana', 'Ghana'),
        ('Gibraltar', 'Gibraltar'),
        ('Great Britain', 'Great Britain'),
        ('Greece', 'Greece'),
        ('Greenland', 'Greenland'),
        ('Grenada', 'Grenada'),
        ('Guadeloupe', 'Guadeloupe'),
        ('Guam', 'Guam'),
        ('Guatemala', 'Guatemala'),
        ('Guinea', 'Guinea'),
        ('Guyana', 'Guyana'),
        ('Haiti', 'Haiti'),
        ('Hawaii', 'Hawaii'),
        ('Honduras', 'Honduras'),
        ('Hong Kong', 'Hong Kong'),
        ('Hungary', 'Hungary'),
        ('Iceland', 'Iceland'),
        ('Indonesia', 'Indonesia'),
        ('India', 'India'),
        ('Iran', 'Iran'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('Isle of Man', 'Isle of Man'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ('Korea North', 'Korea North'),
        ('Korea Sout', 'Korea South'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Laos', 'Laos'),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('Libya', 'Libya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Macau', 'Macau'),
        ('Macedonia', 'Macedonia'),
        ('Madagascar', 'Madagascar'),
        ('Malaysia', 'Malaysia'),
        ('Malawi', 'Malawi'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marshall Islands', 'Marshall Islands'),
        ('Martinique', 'Martinique'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mayotte', 'Mayotte'),
        ('Mexico', 'Mexico'),
        ('Midway Islands', 'Midway Islands'),
        ('Moldova', 'Moldova'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montserrat', 'Montserrat'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar', 'Myanmar'),
        ('Nambia', 'Nambia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherland Antilles', 'Netherland Antilles'),
        ('Netherlands', 'Netherlands (Holland, Europe)'),
        ('Nevis', 'Nevis'),
        ('New Caledonia', 'New Caledonia'),
        ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Niue', 'Niue'),
        ('Norfolk Island', 'Norfolk Island'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Pakistan', 'Pakistan'),
        ('Palau Island', 'Palau Island'),
        ('Palestine', 'Palestine'),
        ('Panama', 'Panama'),
        ('Papua New Guinea', 'Papua New Guinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Phillipines', 'Philippines'),
        ('Pitcairn Island', 'Pitcairn Island'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Puerto Rico', 'Puerto Rico'),
        ('Qatar', 'Qatar'),
        ('Republic of Montenegro', 'Republic of Montenegro'),
        ('Republic of Serbia', 'Republic of Serbia'),
        ('Reunion', 'Reunion'),
        ('Romania', 'Romania'),
        ('Russia', 'Russia'),
        ('Rwanda', 'Rwanda'),
        ('St Barthelemy', 'St Barthelemy'),
        ('St Eustatius', 'St Eustatius'),
        ('St Helena', 'St Helena'),
        ('St Kitts-Nevis', 'St Kitts-Nevis'),
        ('St Lucia', 'St Lucia'),
        ('St Maarten', 'St Maarten'),
        ('St Pierre & Miquelon', 'St Pierre & Miquelon'),
        ('St Vincent & Grenadines', 'St Vincent & Grenadines'),
        ('Saipan', 'Saipan'),
        ('Samoa', 'Samoa'),
        ('Samoa American', 'Samoa American'),
        ('San Marino', 'San Marino'),
        ('Sao Tome & Principe', 'Sao Tome & Principe'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Senegal', 'Senegal'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Singapore', 'Singapore'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Suriname', 'Suriname'),
        ('Swaziland', 'Swaziland'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Syria', 'Syria'),
        ('Tahiti', 'Tahiti'),
        ('Taiwan', 'Taiwan'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania', 'Tanzania'),
        ('Thailand', 'Thailand'),
        ('Togo', 'Togo'),
        ('Tokelau', 'Tokelau'),
        ('Tonga', 'Tonga'),
        ('Trinidad & Tobago', 'Trinidad & Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Turks & Caicos Is', 'Turks & Caicos Is'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('United Kingdom', 'United Kingdom'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Erimates', 'United Arab Emirates'),
        ('United States of America', 'United States of America'),
        ('Uraguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Vatican City State', 'Vatican City State'),
        ('Venezuela', 'Venezuela'),
        ('Vietnam', 'Vietnam'),
        ('Virgin Islands (Brit)', 'Virgin Islands (Brit)'),
        ('Virgin Islands (USA)', 'Virgin Islands (USA)'),
        ('Wake Island', 'Wake Island'),
        ('Wallis & Futana Is', 'Wallis & Futana Is'),
        ('Yemen', 'Yemen'),
        ('Zaire', 'Zaire'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe')])
    org_website = StringField('www.example.com', [Length(max=255)])
    org_description = TextAreaField('Description', [Required()])
    submit = SubmitField('Submit')


