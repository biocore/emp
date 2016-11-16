def empo3_to_color(category):
    #definitions copies from Amnon
    color=['DarkGoldenRod','yellow','sandybrown','tan','saddlebrown','MediumSpringGreen','lawngreen','darkgreen','red','lightsalmon','tomato','black','dimgrey','lightgrey','navy','royalblue','PaleTurquoise','lightskyblue','violet','fuchsia']
    env_mat_list=['Animal surface','Animal corpus','Animal secretion','Animal proximal gut','Animal distal gut','Plant surface','Plant corpus','Plant rhizosphere','Soil (non-saline)','Sediment (non-saline)','Sediment (saline)','Surface (non-saline)','Surface (saline)','Aerosol (non-saline)','Water (non-saline)','Water (saline)','Intertidal (saline)','Hypersaline (saline)','Sterile water blank','Mock community']
    
    dict_colors = dict(zip(env_mat_list, color))
    if category in dict_colors:
        return dict_colors[category]
    else:
        raise Exception('No color defined for category "'+category+'".')