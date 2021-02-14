# Imports
import pandas as pd
import requests

def download_laureates(n=10000):
    """
    Get data from Nobel Prize laureates using the API of nobelprize.org.

    :param int n: number of consecutive connections to the API.
    :return: list, list of Nobel Prize laureates in dict format.
    """
    # Initialize list of laureates
    laureates = []

    # Check all possible urls
    for i in range(n):
        # Set the url
        url = "https://api.nobelprize.org/2.0/laureate/{}".format(i)

        # Get data in json
        r = requests.get(url)
        data = r.json()

        # Check if empty
        if len(data) != 0:
            # Save data from the laureate
            laureates.append(data[0])
        else:
            pass

    return laureates


def get_nobelPrizes_info(laureates):
    """
    Get data from Nobel Prizes from the data of the laureates.

    :param list laureates: list of Nobel Prize laureates in dict format
    :return: pd.DataFrame, dataframe with data from the prizes.
    """
    # Initialize the dataframe
    df = pd.DataFrame(columns=['Name',
                               'Gender',
                               'Birth date',
                               'Birth city',
                               'Birth country',
                               'Prize year',
                               'Prize category',
                               'Prize portion',
                               'Prize motivation',
                               'Prize amount',
                               'Prize amount adjusted',
                               'Affiliation institution',
                               'Affiliation city',
                               'Affiliation country'
                               ]
                      )

    # Loop over the laureates to collect the info
    for laureate in laureates:
        # Initialize data
        name = None
        gender = None
        birth_date = None
        birth_city = None
        birth_country = None
        price_year = None
        price_category = None
        price_portion = None
        price_motivation = None
        price_amount = None
        prize_amount_adj = None
        affiliation_name = None
        affiliation_city = None
        affiliations_country = None

        # Check if it is a person or an organization and collect info
        if laureate.get('knownName'):
            # Name and gender
            name = laureate.get('knownName').get('en')
            gender = laureate.get('gender')

            # Birth info
            if laureate.get('birth'):
                birth_date = laureate.get('birth').get('date')
                if laureate.get('birth').get('place').get('cityNow'):
                    birth_city = laureate.get('birth').get('place').get('cityNow').get('en')
                if laureate.get('birth').get('place').get('countryNow'):
                    birth_country = laureate.get('birth').get('place').get('countryNow').get('en')

        elif laureate.get('orgName'):
            # Name and gender
            name = laureate.get('orgName').get('en')
            gender = 'organization'

            # Birth info
            if laureate.get('founded'):
                birth_date = laureate.get('founded').get('date')
                if laureate.get('founded').get('place').get('cityNow'):
                    birth_city = laureate.get('founded').get('place').get('cityNow').get('en')
                if laureate.get('founded').get('place').get('countryNow'):
                    birth_country = laureate.get('founded').get('place').get('countryNow').get('en')

        # Loop over the prizes of the laureate to collect the info
        for nobelPrize in laureate['nobelPrizes']:
            # Prize info
            prize_year = nobelPrize.get('awardYear')
            prize_category = nobelPrize.get('category').get('en')
            prize_portion = nobelPrize.get('portion')
            prize_motivation = nobelPrize.get('motivation').get('en')
            prize_amount = nobelPrize.get('prizeAmount')
            prize_amount_adj = nobelPrize.get('prizeAmountAdjusted')

            # Affiliation info
            if nobelPrize.get('affiliations'):
                affiliation_name = nobelPrize.get('affiliations')[0].get('nameNow').get('en')
                if nobelPrize.get('affiliations')[0].get('cityNow'):
                    affiliation_city = nobelPrize.get('affiliations')[0].get('cityNow').get('en')
                if nobelPrize.get('affiliations')[0].get('countryNow'):
                    affiliation_country = nobelPrize.get('affiliations')[0].get('countryNow').get('en')

            # Save info
            df = df.append({'Name': name,
                            'Gender': gender,
                            'Birth date': birth_date,
                            'Birth city': birth_city,
                            'Birth country': birth_country,
                            'Prize year': prize_year,
                            'Prize category': prize_category,
                            'Prize portion': prize_portion,
                            'Prize motivation': prize_motivation,
                            'Prize amount': prize_amount,
                            'Prize amount adjusted': prize_amount_adj,
                            'Affiliation institution': affiliation_name,
                            'Affiliation city': affiliation_city,
                            'Affiliation country': affiliation_country
                            }, ignore_index=True)

    return df

# Download and save data
laureates = download_laureates()
nobelPrizes = get_nobelPrizes_info(laureates)
nobelPrizes.to_csv('../data/nobelPrizes.csv', index=False)
