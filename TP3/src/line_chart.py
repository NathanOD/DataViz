'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import hover_template

from template import THEME


def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.

    '''
    fig = px.line()
    fig.update_layout(annotations=[dict(x=0.5, y=0.5, text="No data to display. Select a cell in the heatmap for more information.", showarrow=False)],
                      xaxis=dict(visible=False),
                      yaxis=dict(visible=False),
                      plot_bgcolor=THEME['background_color'],
                      dragmode=False)
    return fig


def add_rectangle_shape(fig):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''
    fig.add_shape(type="rect",
                  x0=0,
                  y0=0.25,
                  x1=1,
                  y1=0.75,
                  fillcolor=THEME['pale_color'],
                  layer='below',
                  line_width=0)
    return fig


def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''
    if len(line_data) == 1:
        fig = px.scatter(line_data, x='Date_Plantation', y='Count')
    else:
        fig = px.line(line_data, x='Date_Plantation', y='Count')
    
    fig.update_layout(title=f'Trees planted in {arrond} in {year}',
                      xaxis_title="",
                      yaxis_title="Trees",
                      xaxis=dict(tickformat='%d %b',
                                 
                                 tickangle=-45,
                                 showgrid=True,
                                 gridcolor=THEME['pale_color']),
                      yaxis=dict(showgrid=True,
                                 gridcolor=THEME['pale_color']),
                      plot_bgcolor=THEME['background_color'])
    fig.update_traces(hovertemplate=hover_template.get_linechart_hover_template(),
                      line_color=THEME['line_chart_color'],
                      marker_color=THEME['line_chart_color'])
    return fig