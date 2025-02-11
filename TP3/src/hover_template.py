'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    template = (
        '<b style="font-family: {label_font}"">Neighborhood : </b>'
        '{neighborhood}<br>'

        '<b style="font-family: {label_font}"">Year : </b>'
        '{year}<br>'

        '<b style="font-family: {label_font}"">Trees planted : </b>'
        '{trees}<br>'

        '<extra></extra>'
    ).format(label_font="Roboto Slab", neighborhood="%{y}", year="%{x}", trees="%{z}")
    return template

def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    template = (
        '<b style="font-family: {label_font}"">Date : </b>'
        '{date}<br>'

        '<b style="font-family: {label_font}"">Trees : </b>'
        '{trees}<br>'

        '<extra></extra>'
    ).format(label_font="Roboto Slab", date="%{x}", trees="%{y}")
    return template