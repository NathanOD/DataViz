'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover


def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        The opacity of the map background color should be 0.2.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace

    '''
    # TODO : Draw the map base
    fig.add_choroplethmapbox(
        geojson=montreal_data,
        locations=locations,
        z=z_vals,
        colorscale=colorscale,
        showscale=False,
        marker_opacity=0.2,
        featureidkey="properties.NOM",
        hovertemplate=hover.map_base_hover_template(),
    )
    return fig


def add_scatter_traces(fig, street_df):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        The marker size should be 20.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter trace

    '''
    # TODO : Add the scatter markers to the map base
    streets = px.scatter_mapbox(
        data_frame=street_df,
        lat='properties.LATITUDE',
        lon='properties.LONGITUDE',
        color="properties.TYPE_SITE_INTERVENTION",
        custom_data = ["properties.NOM_PROJET", "properties.OBJECTIF_THEMATIQUE", "properties.MODE_IMPLANTATION"],
    )
    streets.update_traces(marker=dict(size=20))
    [trace.update({"hovertemplate": hover.map_marker_hover_template(trace["legendgroup"])}) for trace in streets["data"]]
    fig.add_traces(streets["data"])
    return fig
