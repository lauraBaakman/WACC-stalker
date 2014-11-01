""" Test Data. """
import random

from faker import Factory

from models import Stalker, Search, Victim


def populate(connection, numStalkers=50, numVictims=20, numSearches=70):
    """ . """
    relationship_statuses = [
        u'Single',
        u'In a relationship',
        u'Widowed',
        u'Engaged',
        u'Married',
        u'In an open relationship',
        u"It's complicated",
        u'Separated',
        u'Divorced'
    ]
    genders = [u'female', u'male']
    country_codes = [
        u'AD', u'AE', u'AF', u'AG', u'AI', u'AL', u'AM', u'AO', u'AQ',
        u'AR', u'AS', u'AT', u'AU', u'AW', u'AX', u'AZ', u'BA', u'BB',
        u'BD', u'BE', u'BF', u'BG', u'BH', u'BI', u'BJ', u'BL', u'BM',
        u'BN', u'BO', u'BQ', u'BR', u'BS', u'BT', u'BV', u'BW', u'BY',
        u'ci', u'BZ', u'CA', u'CC', u'CD', u'CF', u'CG', u'CH', u'CI',
        u'CK', u'CL', u'CM', u'CN', u'CO', u'CR', u'CU', u'CV', u'CW',
        u'CX', u'CY', u'CZ', u'DE', u'DJ', u'DK', u'DM', u'DO', u'DZ',
        u'EC', u'EE', u'EG', u'EH', u'ER', u'ES', u'ET', u'FI', u'FJ',
        u'FK', u'FM', u'FO', u'FR', u'GA', u'GB', u'ci', u'GD', u'GE',
        u'GF', u'GG', u'GH', u'GI', u'GL', u'GM', u'GN', u'GP', u'GQ',
        u'GR', u'GS', u'GT', u'GU', u'GW', u'GY', u'HK', u'HM', u'HN',
        u'HR', u'HT', u'HU', u'ID', u'IE', u'IL', u'IM', u'IN', u'IO',
        u'IQ', u'IR', u'IS', u'IT', u'JE', u'JM', u'JO', u'JP', u'KE',
        u'KG', u'KH', u'KI', u'KM', u'KN', u'KP', u'KR', u'KW', u'KY',
        u'KZ', u'LA', u'LB', u'LC', u'LI', u'LK', u'LR', u'LS', u'LT',
        u'LU', u'LV', u'LY', u'MA', u'MC', u'MD', u'ME', u'MF', u'MG',
        u'MH', u'MK', u'ML', u'MM', u'MN', u'MO', u'MP', u'MQ', u'MR',
        u'MS', u'MT', u'MU', u'MV', u'MW', u'MX', u'MY', u'MZ', u'NA',
        u'NC', u'NE', u'NF', u'NG', u'NI', u'NL', u'NO', u'NP', u'NR',
        u'NU', u'NZ', u'OM', u'PA', u'PE', u'PF', u'PG', u'PH', u'PK',
        u'PL', u'PM', u'PN', u'PR', u'PS', u'PT', u'PW', u'PY', u'QA',
        u'RE', u'RO', u'RS', u'RU', u'RW', u'SA', u'SB', u'SC', u'SD',
        u'SE', u'SG', u'SH', u'SI', u'SJ', u'SK', u'SL', u'SM', u'SN',
        u'SO', u'SR', u'SS', u'ST', u'SV', u'SX', u'SY', u'SZ', u'TC',
        u'TD', u'TF', u'TG', u'TH', u'TJ', u'TK', u'TL', u'TM', u'TN',
        u'TO', u'TR', u'TT', u'TV', u'TW', u'ci', u'TZ', u'UA', u'ci',
        u'UG', u'UM', u'US', u'UY', u'UZ', u'VA', u'VC', u'VE', u'VG',
        u'VI', u'VN', u'VU', u'WF', u'WS', u'YE', u'YT', u'ZA', u'ZM',
        u'ZR'
    ]
    industries = [
        u'Accounting',
        u'Airlines/Aviation',
        u'Alternative Dispute Resolution',
        u'Alternative Medicine',
        u'Animation',
        u'Apparel and Fashion',
        u'Architecture and Planning',
        u'Arts and Crafts',
        u'Automotive',
        u'Aviation and Aerospace',
        u'Banking',
        u'Biotechnology',
        u'Broadcast Media',
        u'Building Materials',
        u'Business Supplies and Equipment',
        u'Capital Markets',
        u'Chemicals',
        u'Civic and Social Organization',
        u'Civil Engineering',
        u'Commercial Real Estate',
        u'Computer and Network Security',
        u'Computer Games',
        u'Computer Hardware',
        u'Computer Networking',
        u'Computer Software',
        u'Construction',
        u'Consumer Electronics',
        u'Consumer Goods',
        u'Consumer Services',
        u'Cosmetics',
        u'Dairy',
        u'Defense and Space',
        u'Design',
        u'Education Management',
        u'E-Learning',
        u'Electrical/Electronic Manufacturing',
        u'Entertainment',
        u'Environmental Services',
        u'Events Services',
        u'Executive Office',
        u'Facilities Services',
        u'Farming',
        u'Financial Services',
        u'Fine Art',
        u'Fishery',
        u'Food and Beverages',
        u'Food Production',
        u'Fund-Raising',
        u'Furniture',
        u'Gambling and Casinos',
        u'Glass, Ceramics and Concrete',
        u'Government Administration',
        u'Government Relations',
        u'Graphic Design',
        u'Health, Wellness and Fitness',
        u'Higher Education',
        u'Hospital and Health Care',
        u'Hospitality',
        u'Human Resources',
        u'Import and Export',
        u'Individual and Family Services',
        u'Industrial Automation',
        u'Information Services',
        u'Information Technology and Services',
        u'Insurance',
        u'International Affairs',
        u'International Trade and Development',
        u'Internet',
        u'Investment Banking',
        u'Investment Management',
        u'Judiciary',
        u'Law Enforcement',
        u'Law Practice',
        u'Legal Services',
        u'Legislative Office',
        u'Leisure, Travel and Tourism',
        u'Libraries',
        u'Logistics and Supply Chain',
        u'Luxury Goods and Jewelry',
        u'Machinery',
        u'Management Consulting',
        u'Maritime',
        u'Market Research',
        u'Marketing and Advertising',
        u'Mechanical or Industrial Engineering',
        u'Media Production',
        u'Medical Devices',
        u'Medical Practice',
        u'Mental Health Care',
        u'Military',
        u'Mining and Metals',
        u'Motion Pictures and Film',
        u'Museums and Institutions',
        u'Music',
        u'Nanotechnology',
        u'Newspapers',
        u'Non-Profit Organization Management',
        u'Oil and Energy',
        u'Online Media',
        u'Outsourcing/Offshoring',
        u'Package/Freight Delivery',
        u'Packaging and Containers',
        u'Paper and Forest Products',
        u'Performing Arts',
        u'Pharmaceuticals',
        u'Philanthropy',
        u'Photography',
        u'Plastics',
        u'Political Organization',
        u'Primary/Secondary Education',
        u'Printing',
        u'Professional Training and Coaching',
        u'Program Development',
        u'Public Policy',
        u'Public Relations and Communications',
        u'Public Safety',
        u'Publishing',
        u'Railroad Manufacture',
        u'Ranching',
        u'Real Estate',
        u'Recreational Facilities and Services',
        u'Religious Institutions',
        u'Renewables and Environment',
        u'Research',
        u'Restaurants',
        u'Retail',
        u'Security and Investigations',
        u'Semiconductors',
        u'Shipbuilding',
        u'Sporting Goods',
        u'Sports',
        u'Staffing and Recruiting',
        u'Supermarkets',
        u'Telecommunications',
        u'Textiles',
        u'Think Tanks',
        u'Tobacco',
        u'Translation and Localization',
        u'Transportation/Trucking/Railroad',
        u'Utilities',
        u'Venture Capital and Private Equity',
        u'Veterinary',
        u'Warehousing',
        u'Wholesale',
        u'Wine and Spirits',
        u'Wireless',
        u'Writing and Editing'
    ]

    # Create stalkers
    fake = Factory.create()
    for i in range(0, numStalkers):
        stalker = connection.Stalker()

        # TODO: Use hash
        stalker.stalker_id = unicode('stalker_facebook' + repr(i))

        stalker.relationship_status = relationship_statuses[
            random.randrange(0, len(relationship_statuses))
        ]

        # TODO: Naar zelfde format als frontend gaan
        stalker.birthdate = unicode(fake.date(pattern="%Y-%m-%d"))

        stalker.gender = genders[random.randrange(0, len(genders))]

        # TODO: Use hash
        stalker.linkedIn_id = unicode('stalker_linked' + repr(i))

        stalker.industry = industries[
            random.randrange(0, len(industries) - 1)
        ]
        stalker.save()

    for i in range(0, numVictims):
        victim = connection.Victim()

        victim.victim_id = unicode('victim' + repr(i))
        victim.save()

    for i in range(0, numVictims):
        victim = unicode('victim' + repr(i))
        search = connection.Search()

        search.stalker_id = unicode(
            'stalker_facebook' + repr(random.randrange(0, numStalkers))
        )
        search.location['lat'] = float(fake.latitude())
        search.location['long'] = float(fake.longitude())
        search.location['country_code'] = country_codes[
            random.randrange(0, len(country_codes) - 1)
        ]
        search.victim_id = victim
        search.save()

    for i in range(numVictims, numSearches):
        search = connection.Search()

        search.stalker_id = unicode(
            'stalker_facebook' + repr(random.randrange(0, numStalkers))
        )
        search.location['lat'] = float(fake.latitude())
        search.location['long'] = float(fake.longitude())
        search.location['country_code'] = country_codes[
            random.randrange(0, len(country_codes) - 1)
        ]
        search.save()


def clear(connection):
    """ Clear database. """
    connection.wacc.drop_collection('stalkers')
    connection.wacc.drop_collection('searches')
    connection.wacc.drop_collection('victims')

if __name__ == '__main__':
    import database as db
    db.init()
    db.connection.register([Stalker, Search, Victim])
    clear(db.connection)
    populate(db.connection)
