""" Test Data. """
import random

from faker import Factory

from models import Stalker, Search, Victim


def populate(connection, numStalkers=500, numVictims=200, numSearches=700):
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
        u'ALA', u'AFG', u'ALB', u'DZA', u'ASM', u'AND', u'AGO', u'AIA',
        u'ATA', u'ATG', u'ARG', u'ARM', u'ABW', u'AUS', u'AUT', u'AZE',
        u'BHS', u'BHR', u'BGD', u'BRB', u'BLR', u'BEL', u'BLZ', u'BEN',
        u'BMU', u'BTN', u'BOL', u'BIH', u'BWA', u'BVT', u'BRA', u'IOT',
        u'BRN', u'BGR', u'BFA', u'BDI', u'KHM', u'CMR', u'CAN', u'CPV',
        u'CYM', u'CAF', u'TCD', u'CHL', u'CHN', u'CXR', u'CCK', u'COL',
        u'COM', u'COD', u'COG', u'COK', u'CRI', u'CIV', u'HRV', u'CUB',
        u'CYP', u'CZE', u'DNK', u'DJI', u'DMA', u'DOM', u'ECU', u'EGY',
        u'SLV', u'GNQ', u'ERI', u'EST', u'ETH', u'FLK', u'FRO', u'FJI',
        u'FIN', u'FRA', u'GUF', u'PYF', u'ATF', u'GAB', u'GMB', u'GEO',
        u'DEU', u'GHA', u'GIB', u'GRC', u'GRL', u'GRD', u'GLP', u'GUM',
        u'GTM', u'GIN', u'GNB', u'GUY', u'HTI', u'HMD', u'HND', u'HKG',
        u'HUN', u'ISL', u'IND', u'IDN', u'IRN', u'IRQ', u'IRL', u'ISR',
        u'ITA', u'JAM', u'JPN', u'JOR', u'KAZ', u'KEN', u'KIR', u'PRK',
        u'KOR', u'KWT', u'KGZ', u'LAO', u'LVA', u'LBN', u'LSO', u'LBR',
        u'LBY', u'LIE', u'LTU', u'LUX', u'MAC', u'MKD', u'MDG', u'MWI',
        u'MYS', u'MDV', u'MLI', u'MLT', u'MHL', u'MTQ', u'MRT', u'MUS',
        u'MYT', u'MEX', u'FSM', u'MDA', u'MCO', u'MNG', u'MSR', u'MAR',
        u'MOZ', u'MMR', u'NAM', u'NRU', u'NPL', u'NLD', u'ANT', u'NCL',
        u'NZL', u'NIC', u'NER', u'NGA', u'NIU', u'NFK', u'MNP', u'NOR',
        u'OMN', u'PAK', u'PLW', u'PSE', u'PAN', u'PNG', u'PRY', u'PER',
        u'PHL', u'PCN', u'POL', u'PRT', u'PRI', u'QAT', u'REU', u'ROU',
        u'RUS', u'RWA', u'SHN', u'KNA', u'LCA', u'SPM', u'VCT', u'WSM',
        u'SMR', u'STP', u'SAU', u'SEN', u'SCG', u'SYC', u'SLE', u'SGP',
        u'SVK', u'SVN', u'SLB', u'SOM', u'ZAF', u'SGS', u'ESP', u'LKA',
        u'SDN', u'SUR', u'SJM', u'SWZ', u'SWE', u'CHE', u'SYR', u'TWN',
        u'TJK', u'TZA', u'THA', u'TLS', u'TGO', u'TKL', u'TON', u'TTO',
        u'TUN', u'TUR', u'TKM', u'TCA', u'TUV', u'UGA', u'UKR', u'ARE',
        u'GBR', u'USA', u'UMI', u'URY', u'UZB', u'VUT', u'VAT', u'VEN',
        u'VNM', u'VGB', u'VIR', u'WLF', u'ESH', u'YEM', u'ZMB', u'ZWE'
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


def generate(connection, num_stalkers=500, num_victims=200, num_searches=700):
    """ Generate test data. """
    clear(connection)
    populate(connection, num_stalkers, num_victims, num_searches)


if __name__ == '__main__':
    import database as db
    db.init()
    db.connection.register([Stalker, Search, Victim])
    clear(db.connection)
    populate(db.connection)
