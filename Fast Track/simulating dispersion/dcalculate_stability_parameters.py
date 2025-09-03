def calculate_stability_parameters(hour):
    """Calculate atmospheric stability parameters based on time of day"""
    
    # Determine if it's day or night (simplified)
    # Assuming sunrise at 6am and sunset at 6pm
    is_daytime = (hour >= 6) and (hour < 18)

    if is_daytime:
        # Daytime - unstable or neutral conditions
        # Higher mixing height, stronger diffusion
        mixing_height = 1000 + 500 * np.sin(np.pi * (hour - 6) / 12)  # Peaks at noon
        sigma_z_factor = 1.0  # Vertical diffusion factor (higher = more diffusion)
        sigma_h_factor = 0.8  # Horizontal diffusion factor
    else:
        # Nighttime - stable conditions
        # Lower mixing height, suppressed diffusion
        mixing_height = 300  # Shallow nighttime boundary layer
        sigma_z_factor = 0.3  # Reduced vertical diffusion
        sigma_h_factor = 0.5  # Reduced horizontal diffusion

    return {
        'mixing_height': mixing_height,
        'sigma_z_factor': sigma_z_factor,
        'sigma_h_factor': sigma_h_factor,
        'is_daytime': is_daytime
    }