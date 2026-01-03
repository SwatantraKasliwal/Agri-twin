def fertilizer_advisory(soil_moisture, heat_stress, crop_stage):
    """
    Rule based fertilizer recommendation system.
    This operates alongside RL irrigation control.
    """

    if heat_stress > 0.6:
        return{
            "fertilizer": "None",
            "reason": "High heat stress — fertilization paused to prevent crop damage"
        }
    
    if soil_moisture < 0.35:
        return{
            "fertilizer": "None",
            "reason": "Soil too dry — fertilization delayed until moisture improves"
        }
    
    if crop_stage < 0.3:
        return{
            "fertilizer": "Nitrogen-rich",
            "reason": "Early growth stage — nitrogen supports vegetative growth"
        }
    
    if crop_stage < 0.7:
        return{
            "fertilizer": "Balanced NPK",
            "reason": "Mid growth stage — balanced nutrients for biomass and roots"
        }
    
    else:
        return{
            "fertilizer": "Low Nitrogen / Potassium-rich",
            "reason": "Late growth stage — reduced nitrogen to support maturation"
        }
    


