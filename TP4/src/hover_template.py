'''
    Provides the template for the tooltips.
'''


def get_bubble_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip
    country = "<span style='font-weight: bold'>Country</span>"
    population = "<span style='font-weight: bold'>Population</span>"
    gdp = "<span style='font-weight: bold'>GDP</span>"
    co2 = "<span style='font-weight: bold'>CO2 emissions</span>"
    return f"{country} : %{{customdata[0]}}<br>" \
           f"{population} : %{{customdata[1]}}<br>" \
           f"{gdp} : %{{x}} $ (USD)<br>" \
           f"{co2} : %{{y}} metric tonnes<br>" \
           "<extra></extra>"