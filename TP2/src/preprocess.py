'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    my_df = my_df.groupby(['Act', 'Player']).size().reset_index()
    my_df = my_df.rename(columns={0: 'LineCount'})
    my_df['LinePercent'] = my_df.groupby('Act')['LineCount'].transform(lambda x: 100 * x / x.sum())#.round(3)
    return my_df


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    top_players = my_df.groupby('Player')['LineCount'].sum().nlargest(5).index
    my_df['Player'] = my_df['Player'].apply(lambda x: x if x in top_players else 'Other')
    my_df = my_df.groupby(['Act', 'Player'])['LineCount'].sum().reset_index()
    my_df['LinePercent'] = my_df.groupby('Act')['LineCount'].transform(lambda x: 100 * x / x.sum())#.round(3)
    return my_df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    my_df['Player'] = my_df['Player'].str.title()
    return my_df
