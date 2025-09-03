class Particle:
    def __init__(self, x, y, z, release_time):
        # Position
        self.x = x
        self.y = y
        self.z = z

        # Metadata
        self.release_time = release_time
        self.age = 0  # Time since release in hours
    
    def update_position(self, u, v, stability, dt):
        """Update particle position based on wind and diffusion"""
        
        # Convert dt from hours to seconds
        dt_seconds = dt * 3600
        
        # Advection component (deterministic)
        dx_advection = u * dt_seconds
        dy_advection = v * dt_seconds
        
        # Diffusion component (random)
        # Uses stability parameters to determine diffusion strength
        sigma_h = 10 * stability['sigma_h_factor'] * np.sqrt(dt_seconds)
        sigma_z = 5 * stability['sigma_z_factor'] * np.sqrt(dt_seconds)
        
        dx_diffusion = np.random.normal(0, sigma_h)
        dy_diffusion = np.random.normal(0, sigma_h)
        dz_diffusion = np.random.normal(0, sigma_z)

        # Update position
        self.x += dx_advection + dx_diffusion
        self.y += dy_advection + dy_diffusion
        self.z += dz_diffusion

        # Boundary conditions
        # Reflection at ground
        if self.z < 0:
            self.z = -self.z

        # Reflection at mixing height
        if self.z > stability['mixing_height']:
            self.z = 2 * stability['mixing_height'] - self.z

        # Update age
        self.age += dt