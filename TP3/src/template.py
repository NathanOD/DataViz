'''
    Contains the template to use in the data visualization.
'''
import plotly.graph_objects as go
import plotly.io as pio


THEME = {
    'background_color': '#ffffff',
    'font_family': 'Roboto',
    'accent_font_family': 'Roboto Slab',
    'dark_color': '#2A2B2E',
    'pale_color': '#DFD9E2',
    'line_chart_color': 'black',
    'label_font_size': 14,
    'label_background_color': '#ffffff',
    'colorscale': 'Bluyl'
}



def create_custom_theme():
    '''
        Adds a new layout template to pio's templates.

        The template sets the font color and
        font to the values defined above in
        the THEME dictionary, using the dark
        color.

        The plot background and paper background
        are the background color defined
        above in the THEME dictionary.

        Also, sets the hover label to have a
        background color and font size
        as defined for the label in the THEME dictionary.
        The hover label's font color is the same
        as the theme's overall font color. The hover mode
        is set to 'closest'.

        Sets the line chart's line color to the one
        designated in the THEME dictionary. Also sets
        the color scale to be used by the heatmap
        to the one in the THEME dictionary.

        Specifies the x-axis ticks are tilted 45
        degrees to the right.
    '''
    # TODO : Generate template described above
    template = go.layout.Template(
        layout=
        {
            'font': {
                'family': THEME['font_family'],
            },
            'plot_bgcolor': THEME['background_color'],
            'paper_bgcolor': THEME['background_color'],
            'hoverlabel': {
                'bgcolor': THEME['label_background_color'],
                'font': {
                    'size': THEME['label_font_size'],
                }
            },
            'hovermode': 'closest',
            'colorway': [THEME['line_chart_color']],
            # add colorscale
            'colorscale': {
                'sequential': THEME['colorscale']
            },
            'xaxis': {
                'tickangle': 45
            }
        }
    )
    pio.templates['custom_template'] = template


def set_default_theme():
    '''
        Sets the default theme to be a combination of the
        'plotly_white' theme and our custom theme.
    '''
    # TODO : Set default theme
    pio.templates.default = 'plotly_white+custom_template'
