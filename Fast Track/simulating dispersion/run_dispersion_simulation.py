def run_dispersion_simulation(
    duration_hours=24,
    dt=0.1,
    num_particles=1000,
    release_location=(0, 0, 10),
    grid_size=(50, 50),
    domain_size=(10000, 10000)  # 10km x 10km
):
    """Run a Lagrangian dispersion simulation"""
    
    # Initialize grid
    x_grid, y_grid = np.meshgrid(
        np.linspace(0, domain_size[0], grid_size[0]),
        np.linspace(0, domain_size[1], grid_size[1])
    )
    
    # Initialize particles (all released at t=0 for simplicity)
    particles = [
        Particle(release_location[0], release_location[1], release_location[2], 0)
        for _ in range(num_particles)
    ]
    
    # Storage for results
    particle_positions = []

    # Time loop
    current_hour = 0
    while current_hour < duration_hours:
        # Get current hour of day (0-23)
        hour_of_day = current_hour % 24
        
        # Update Eulerian weather model
        u, v = calculate_wind_field(x_grid, y_grid, hour_of_day)
        stability = calculate_stability_parameters(hour_of_day)
        
        # Interpolate wind at particle locations
        # (In a real model, you'd use proper interpolation)
        u_at_particles = u[0, 0]  # Simplified
        v_at_particles = v[0, 0]  # Simplified
        
        # Update each particle
        for particle in particles:
            particle.update_position(u_at_particles, v_at_particles, stability, dt)
        
        # Store current state
        particle_positions.append([
            (p.x, p.y, p.z, p.age, hour_of_day)
            for p in particles
        ])

        # Increment time
        current_hour += dt
    
    return particle_positions, x_grid, y_grid