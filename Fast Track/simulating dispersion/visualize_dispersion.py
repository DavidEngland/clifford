def visualize_dispersion(particle_positions, x_grid, y_grid):
    """Create visualizations of the dispersion results"""
    
    # Prepare figure
    fig = plt.figure(figsize=(15, 10))
    
    # 1. Particle positions at different times
    display_hours = [0, 6, 12, 18, 23]
    
    for i, hour in enumerate(display_hours):
        hour_idx = min(int(hour / dt), len(particle_positions) - 1)
        
        # Get particle positions at this time
        positions = particle_positions[hour_idx]
        x = [p[0] for p in positions]
        y = [p[1] for p in positions]
        z = [p[2] for p in positions]
        
        # Extract hour of day
        hour_of_day = positions[0][4]
        is_daytime = (hour_of_day >= 6) and (hour_of_day < 18)
        
        # Plot
        ax = fig.add_subplot(2, 3, i+1, projection='3d')
        scatter = ax.scatter(x, y, z, c=z, cmap='viridis', alpha=0.7)
        ax.set_title(f"Hour {hour:.1f} ({hour_of_day:.1f}h - {'Day' if is_daytime else 'Night'})")
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_zlabel('Z (m)')
        
        # Add mixing height plane
        stability = calculate_stability_parameters(hour_of_day)
        mixing_height = stability['mixing_height']
        ax.plot_surface(
            x_grid[:5, :5], y_grid[:5, :5], 
            np.ones((5, 5)) * mixing_height,
            alpha=0.2, color='red'
        )
    
    # 2. Concentration contours (horizontal slice)
    ax = fig.add_subplot(2, 3, 6)
    
    # Create concentration grid from final positions
    final_positions = particle_positions[-1]
    x_final = [p[0] for p in final_positions]
    y_final = [p[1] for p in final_positions]
    
    # Create 2D histogram (concentration)
    hist, xedges, yedges = np.histogram2d(
        x_final, y_final,
        bins=[20, 20],
        range=[[0, domain_size[0]], [0, domain_size[1]]]
    )
    
    # Plot concentration contours
    extent = [0, domain_size[0], 0, domain_size[1]]
    contour = ax.contourf(hist.T, extent=extent, cmap='plasma')
    ax.set_title('Final Concentration')
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    plt.colorbar(contour, ax=ax, label='Particle count')
    
    plt.tight_layout()
    return fig