def get_empo_cat_color(empocat=None, returndict=False):
    """returns standard empo colors for EMP figures
    input:
    empocat- empo category name (string)
    returndict-  the user needs the dictionary mapping category to color (boolean)
    
    output: either a color for passed empocat or the dictionay if returndict=True"""
    
    empo_cat_color={'EMP sample': 'white',
                    'Host-associated': '#fb9a99',
                    'Free-living': '#e31a1c',
                    'Animal': '#b2df8a',
                    'Plant': '#33a02c',
                    'Non-saline': '#a6cee3',
                    'Saline': '#1f78b4',
                    'Aerosol (non-saline)': 'lightgrey',
                    'Animal corpus': 'yellow',
                    'Animal distal gut': 'saddlebrown',
                    'Animal proximal gut': 'tan',
                    'Animal secretion': 'sandybrown',
                    'Animal surface': 'DarkGoldenRod',
                    'Hypersaline (saline)': 'lightskyblue',
                    'Intertidal (saline)': 'PaleTurquoise',
                    'Mock community': 'fuchsia',
                    'Plant corpus': 'lawngreen',
                    'Plant rhizosphere': 'darkgreen',
                    'Plant surface': 'MediumSpringGreen',
                    'Sediment (non-saline)': 'lightsalmon',
                    'Sediment (saline)': 'tomato',
                    'Soil (non-saline)': 'red',
                    'Sterile water blank': 'violet',
                    'Surface (non-saline)': 'black',
                    'Surface (saline)': 'dimgrey',
                    'Water (non-saline)': 'navy',
                    'Water (saline)': 'royalblue'}
    
    if returndict==True:
        return empo_cat_color
    else:
        return empo_cat_color[empocat]