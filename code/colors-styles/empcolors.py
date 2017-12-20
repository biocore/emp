def get_empo_cat_color(empocat=None, returndict=False):
    """returns standard empo colors for EMP figures
    input:
    empocat- empo category name (string)
    returndict-  the user needs the dictionary mapping category to color (boolean)
    
    output: either a color for passed empocat or the dictionay if returndict=True"""
    
    # hex codes for matplotlib colors are described here:
    # https://github.com/matplotlib/matplotlib/blob/cf83cd5642506ef808853648b9eb409f8dbd6ff3/lib/matplotlib/_color_data.py

    empo_cat_color={'EMP sample': '#929591', # 'grey'
                    'Host-associated': '#fb9a99',
                    'Free-living': '#e31a1c',
                    'Animal': '#b2df8a',
                    'Plant': '#33a02c',
                    'Non-saline': '#a6cee3',
                    'Saline': '#1f78b4',
                    'Aerosol (non-saline)': '#d3d3d3', # 'lightgrey'
                    'Animal corpus': '#ffff00', # 'yellow'
                    'Animal distal gut': '#8b4513', # 'saddlebrown'
                    'Animal proximal gut': '#d2b48c', # 'tan'
                    'Animal secretion': '#f4a460', # 'sandybrown'
                    'Animal surface': '#b8860b', # 'darkgoldenrod'
                    'Hypersaline (saline)': '#87cefa', # 'lightskyblue'
                    'Intertidal (saline)': '#afeeee', # 'paleturquoise'
                    'Mock community': '#ff00ff', # 'fuchsia'
                    'Plant corpus': '#7cfc00', # 'lawngreen'
                    'Plant rhizosphere': '#006400', # 'darkgreen'
                    'Plant surface': '#00fa9a', # 'mediumspringgreen'
                    'Sediment (non-saline)': '#ffa07a', # 'lightsalmon'
                    'Sediment (saline)': '#ff6347', # 'tomato'
                    'Soil (non-saline)': '#ff0000', # 'red'
                    'Sterile water blank': '#ee82ee', # 'violet'
                    'Surface (non-saline)': '#000000', # 'black'
                    'Surface (saline)': '#696969', # 'dimgrey'
                    'Water (non-saline)': '#000080', # 'navy'
                    'Water (saline)': '#4169e1' # 'royalblue'
                    }
    
    if returndict==True:
        return empo_cat_color
    else:
        return empo_cat_color[empocat]
