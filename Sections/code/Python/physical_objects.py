from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple, ClassVar, Set, Union
import numpy as np
from datetime import datetime, timedelta

# Type definitions for physical object properties
class OrbitalParameters(TypedDict, total=False):
    semi_major_axis: float  # meters
    eccentricity: float
    inclination: float  # radians
    longitude_ascending_node: float  # radians
    argument_periapsis: float  # radians
    mean_anomaly: float  # radians
    period: float  # seconds

# Enumerations for physical object properties
class ObjectType(Enum):
    STAR = auto()
    PLANET = auto()
    MOON = auto()
    ASTEROID = auto()
    COMET = auto()
    DUST_PARTICLE = auto()
    GAS_CLOUD = auto()
    BLACK_HOLE = auto()
    SPACECRAFT = auto()
    CUSTOM = auto()
    
    def __str__(self) -> str:
        return self.name.replace('_', ' ').capitalize()

class CompositionType(Enum):
    ROCKY = auto()
    GASEOUS = auto()
    ICY = auto()
    METALLIC = auto()
    ORGANIC = auto()
    MIXED = auto()
    PLASMA = auto()
    UNKNOWN = auto()
    
    def __str__(self) -> str:
        return self.name.capitalize()

class SystemType(Enum):
    SOLAR_SYSTEM = auto()
    BINARY_SYSTEM = auto()
    MULTI_STAR_SYSTEM = auto()
    PLANETARY_SYSTEM = auto()
    SATELLITE_SYSTEM = auto()
    ASTEROID_BELT = auto()
    GALAXY = auto()
    CUSTOM = auto()
    
    def __str__(self) -> str:
        return self.name.replace('_', ' ').capitalize()

@dataclass
class Vector3D:
    """A 3D vector class for position, velocity, and other physical quantities."""
    
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    
    def __add__(self, other: 'Vector3D') -> 'Vector3D':
        """Add two vectors."""
        return Vector3D(
            x=self.x + other.x,
            y=self.y + other.y,
            z=self.z + other.z
        )
    
    def __sub__(self, other: 'Vector3D') -> 'Vector3D':
        """Subtract two vectors."""
        return Vector3D(
            x=self.x - other.x,
            y=self.y - other.y,
            z=self.z - other.z
        )
    
    def __mul__(self, scalar: float) -> 'Vector3D':
        """Multiply vector by scalar."""
        return Vector3D(
            x=self.x * scalar,
            y=self.y * scalar,
            z=self.z * scalar
        )
    
    def __rmul__(self, scalar: float) -> 'Vector3D':
        """Multiply scalar by vector (right multiplication)."""
        return self * scalar
    
    def __truediv__(self, scalar: float) -> 'Vector3D':
        """Divide vector by scalar."""
        if scalar == 0:
            raise ValueError("Cannot divide vector by zero")
        return Vector3D(
            x=self.x / scalar,
            y=self.y / scalar,
            z=self.z / scalar
        )
    
    def dot(self, other: 'Vector3D') -> float:
        """Calculate the dot product with another vector."""
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other: 'Vector3D') -> 'Vector3D':
        """Calculate the cross product with another vector."""
        return Vector3D(
            x=self.y * other.z - self.z * other.y,
            y=self.z * other.x - self.x * other.z,
            z=self.x * other.y - self.y * other.x
        )
    
    def magnitude(self) -> float:
        """Calculate the magnitude (length) of the vector."""
        return np.sqrt(self.dot(self))
    
    def normalized(self) -> 'Vector3D':
        """Return a normalized version of the vector (unit length)."""
        mag = self.magnitude()
        if mag == 0:
            return Vector3D()
        return self / mag
    
    def to_dict(self) -> Dict[str, float]:
        """Convert vector to dictionary format."""
        return {"x": self.x, "y": self.y, "z": self.z}
    
    def to_numpy(self) -> np.ndarray:
        """Convert vector to numpy array."""
        return np.array([self.x, self.y, self.z])
    
    @classmethod
    def from_dict(cls, d: Dict[str, float]) -> 'Vector3D':
        """Create vector from dictionary."""
        return cls(x=d.get("x", 0.0), y=d.get("y", 0.0), z=d.get("z", 0.0))
    
    @classmethod
    def from_numpy(cls, arr: np.ndarray) -> 'Vector3D':
        """Create vector from numpy array."""
        if len(arr) != 3:
            raise ValueError("Array must have exactly 3 elements")
        return cls(x=float(arr[0]), y=float(arr[1]), z=float(arr[2]))

@dataclass
class PhysicalObject:
    """Base class for all physical objects in space or atmosphere."""
    
    name: str
    mass_kg: float
    object_type: ObjectType
    composition: CompositionType = CompositionType.UNKNOWN
    radius_m: float = 0.0
    temperature_k: float = 0.0
    position: Vector3D = field(default_factory=Vector3D)
    velocity: Vector3D = field(default_factory=Vector3D)
    properties: Dict[str, Any] = field(default_factory=dict)
    
    # Class constants
    GRAVITATIONAL_CONSTANT: ClassVar[float] = 6.67430e-11  # m^3 kg^-1 s^-2
    
    def __post_init__(self) -> None:
        """Initialize default properties if not provided."""
        if self.mass_kg <= 0:
            raise ValueError(f"Mass must be positive: {self.mass_kg}")
        
        if self.radius_m < 0:
            raise ValueError(f"Radius cannot be negative: {self.radius_m}")
        
        # Convert dict positions to Vector3D if needed
        if isinstance(self.position, dict):
            self.position = Vector3D.from_dict(self.position)
        if isinstance(self.velocity, dict):
            self.velocity = Vector3D.from_dict(self.velocity)
        
        # Calculate volume and density if radius is provided
        if self.radius_m > 0:
            self.properties["volume_m3"] = (4/3) * np.pi * (self.radius_m ** 3)
            self.properties["density_kg_m3"] = self.mass_kg / self.properties["volume_m3"]
    
    def __repr__(self) -> str:
        """Return a string representation of the physical object."""
        return f"{self.name} ({self.object_type})"
    
    def __eq__(self, other) -> bool:
        """Compare two physical objects for equality."""
        if not isinstance(other, PhysicalObject):
            return False
        return (self.name == other.name and 
                self.object_type == other.object_type and
                self.mass_kg == other.mass_kg)
    
    def __hash__(self) -> int:
        """Generate a hash for using objects in sets and as dict keys."""
        return hash((self.name, self.object_type, self.mass_kg))
    
    @property
    def volume(self) -> float:
        """Return the volume of the object in cubic meters."""
        if "volume_m3" not in self.properties and self.radius_m > 0:
            self.properties["volume_m3"] = (4/3) * np.pi * (self.radius_m ** 3)
        return self.properties.get("volume_m3", 0.0)
    
    @property
    def density(self) -> float:
        """Return the density of the object in kg/m³."""
        if "density_kg_m3" not in self.properties and self.volume > 0:
            self.properties["density_kg_m3"] = self.mass_kg / self.volume
        return self.properties.get("density_kg_m3", 0.0)
    
    @property
    def surface_gravity(self) -> float:
        """Return the surface gravity in m/s²."""
        if self.radius_m > 0:
            return self.GRAVITATIONAL_CONSTANT * self.mass_kg / (self.radius_m ** 2)
        return 0.0
    
    @property
    def escape_velocity(self) -> float:
        """Return the escape velocity in m/s."""
        if self.radius_m > 0:
            return np.sqrt(2 * self.GRAVITATIONAL_CONSTANT * self.mass_kg / self.radius_m)
        return 0.0
    
    @property
    def position_vector(self) -> np.ndarray:
        """Return the position as a numpy array."""
        return self.position.to_numpy()
    
    @property
    def velocity_vector(self) -> np.ndarray:
        """Return the velocity as a numpy array."""
        return self.velocity.to_numpy()
    
    @property
    def kinetic_energy(self) -> float:
        """Return the kinetic energy in joules."""
        velocity_magnitude = self.velocity.magnitude()
        return 0.5 * self.mass_kg * (velocity_magnitude ** 2)
    
    def distance_to(self, other: 'PhysicalObject') -> float:
        """Calculate the distance to another object in meters."""
        return (self.position - other.position).magnitude()
    
    def gravitational_force_with(self, other: 'PhysicalObject') -> Vector3D:
        """Calculate the gravitational force vector with another object in newtons."""
        r_vector = other.position - self.position
        distance = r_vector.magnitude()
        
        if distance == 0:
            return Vector3D()
        
        # Calculate the gravitational force magnitude
        force_magnitude = (self.GRAVITATIONAL_CONSTANT * self.mass_kg * other.mass_kg) / (distance ** 2)
        
        # Calculate the force vector (direction from this object to the other)
        direction = r_vector.normalized()
        return direction * force_magnitude
    
    def update_position(self, time_step: float) -> None:
        """Update position based on velocity and time step (in seconds)."""
        self.position = self.position + (self.velocity * time_step)
    
    def update_velocity(self, acceleration: Union[Vector3D, np.ndarray], time_step: float) -> None:
        """Update velocity based on acceleration and time step (in seconds)."""
        if isinstance(acceleration, np.ndarray):
            acceleration = Vector3D.from_numpy(acceleration)
        self.velocity = self.velocity + (acceleration * time_step)


@dataclass
class CelestialBody(PhysicalObject):
    """Class for astronomical objects like planets, stars, and moons."""
    
    orbital_parameters: Dict[str, float] = field(default_factory=dict)
    rotation_period_s: float = 0.0  # Rotation period in seconds
    axial_tilt_rad: float = 0.0  # Axial tilt in radians
    
    def __post_init__(self) -> None:
        """Initialize celestial-body-specific properties."""
        super().__post_init__()
        
        # Calculate orbital period if not provided but semi-major axis is
        if ("period" not in self.orbital_parameters and 
            "semi_major_axis" in self.orbital_parameters and 
            "parent_mass" in self.properties):
            parent_mass = self.properties["parent_mass"]
            semi_major_axis = self.orbital_parameters["semi_major_axis"]
            # Kepler's third law: T² = (4π²/G(M+m)) * a³
            # For most cases M >> m, so we can approximate with just M
            period_squared = (4 * (np.pi ** 2) / (self.GRAVITATIONAL_CONSTANT * parent_mass)) * (semi_major_axis ** 3)
            self.orbital_parameters["period"] = np.sqrt(period_squared)
    
    @property
    def rotation_rate(self) -> float:
        """Return the rotation rate in radians per second."""
        if self.rotation_period_s > 0:
            return 2 * np.pi / self.rotation_period_s
        return 0.0
    
    @property
    def orbital_period(self) -> float:
        """Return the orbital period in seconds."""
        return self.orbital_parameters.get("period", 0.0)
    
    @property
    def orbital_speed(self) -> float:
        """Return the average orbital speed in m/s."""
        if "semi_major_axis" in self.orbital_parameters and self.orbital_period > 0:
            # Approximation for circular orbit
            circumference = 2 * np.pi * self.orbital_parameters["semi_major_axis"]
            return circumference / self.orbital_period
        return 0.0
    
    def calculate_position_at_time(self, time: datetime) -> Vector3D:
        """
        Calculate the position at a specific time using orbital parameters.
        This is a simplified model for approximate positions.
        """
        if not self.orbital_parameters:
            return self.position
        
        # Extract orbital elements
        a = self.orbital_parameters.get("semi_major_axis", 0)
        e = self.orbital_parameters.get("eccentricity", 0)
        i = self.orbital_parameters.get("inclination", 0)
        Ω = self.orbital_parameters.get("longitude_ascending_node", 0)
        ω = self.orbital_parameters.get("argument_periapsis", 0)
        M0 = self.orbital_parameters.get("mean_anomaly", 0)
        period = self.orbital_parameters.get("period", 0)
        
        if a == 0 or period == 0:
            return self.position
        
        # Calculate time since epoch
        if "epoch" in self.properties:
            epoch = self.properties["epoch"]
            dt = (time - epoch).total_seconds()
        else:
            dt = 0
        
        # Calculate mean anomaly at the given time
        n = 2 * np.pi / period  # Mean motion
        M = (M0 + n * dt) % (2 * np.pi)
        
        # Solve Kepler's equation (simple approximation)
        E = M
        for _ in range(10):  # Iterative solution
            E = M + e * np.sin(E)
        
        # Calculate true anomaly
        ν = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E/2), np.sqrt(1 - e) * np.cos(E/2))
        
        # Calculate distance from focus
        r = a * (1 - e * np.cos(E))
        
        # Position in orbital plane
        x_orbit = r * np.cos(ν)
        y_orbit = r * np.sin(ν)
        z_orbit = 0
        
        # Rotation to reference plane (simplified)
        x = (np.cos(ω) * np.cos(Ω) - np.sin(ω) * np.cos(i) * np.sin(Ω)) * x_orbit + \
            (-np.sin(ω) * np.cos(Ω) - np.cos(ω) * np.cos(i) * np.sin(Ω)) * y_orbit
        y = (np.cos(ω) * np.sin(Ω) + np.sin(ω) * np.cos(i) * np.cos(Ω)) * x_orbit + \
            (-np.sin(ω) * np.sin(Ω) + np.cos(ω) * np.cos(i) * np.cos(Ω)) * y_orbit
        z = np.sin(ω) * np.sin(i) * x_orbit + np.cos(ω) * np.sin(i) * y_orbit
        
        return Vector3D(x=x, y=y, z=z)


@dataclass
class Planet(CelestialBody):
    """Class for planets."""
    
    has_atmosphere: bool = False
    has_magnetic_field: bool = False
    
    def __post_init__(self) -> None:
        """Initialize planet-specific properties."""
        if not self.object_type == ObjectType.PLANET:
            self.object_type = ObjectType.PLANET
            
        super().__post_init__()
        
        # Add planet-specific properties
        self.properties["has_atmosphere"] = self.has_atmosphere
        self.properties["has_magnetic_field"] = self.has_magnetic_field


@dataclass
class Star(CelestialBody):
    """Class for stars."""
    
    luminosity_watts: float = 0.0
    spectral_type: str = ""
    
    def __post_init__(self) -> None:
        """Initialize star-specific properties."""
        if not self.object_type == ObjectType.STAR:
            self.object_type = ObjectType.STAR
            
        super().__post_init__()
        
        # Add star-specific properties
        self.properties["luminosity_watts"] = self.luminosity_watts
        self.properties["spectral_type"] = self.spectral_type
        
        # Calculate habitable zone (simplified)
        if self.luminosity_watts > 0:
            # Inner and outer edges of habitable zone in AU (simplified)
            l_rel = self.luminosity_watts / 3.828e26  # Relative to Sun
            self.properties["habitable_zone_inner_au"] = 0.75 * np.sqrt(l_rel)
            self.properties["habitable_zone_outer_au"] = 1.8 * np.sqrt(l_rel)
    
    @property
    def habitable_zone(self) -> Tuple[float, float]:
        """Return the inner and outer radius of the habitable zone in meters."""
        inner_au = self.properties.get("habitable_zone_inner_au", 0)
        outer_au = self.properties.get("habitable_zone_outer_au", 0)
        au_to_m = 1.496e11  # 1 AU in meters
        return (inner_au * au_to_m, outer_au * au_to_m)


@dataclass
class Comet(CelestialBody):
    """Class for comets."""
    
    nucleus_radius_m: float = 0.0
    coma_radius_m: float = 0.0
    tail_length_m: float = 0.0
    
    def __post_init__(self) -> None:
        """Initialize comet-specific properties."""
        if not self.object_type == ObjectType.COMET:
            self.object_type = ObjectType.COMET
        
        # Use nucleus radius as the main radius
        if self.radius_m == 0 and self.nucleus_radius_m > 0:
            self.radius_m = self.nucleus_radius_m
            
        super().__post_init__()
        
        # Add comet-specific properties
        self.properties["nucleus_radius_m"] = self.nucleus_radius_m
        self.properties["coma_radius_m"] = self.coma_radius_m
        self.properties["tail_length_m"] = self.tail_length_m
    
    def calculate_tail_direction(self, star_position: np.ndarray) -> np.ndarray:
        """Calculate the direction of the comet's tail (away from the star)."""
        direction_to_star = star_position - self.position_vector
        distance = np.linalg.norm(direction_to_star)
        
        if distance == 0:
            return np.array([0.0, 0.0, 0.0])
        
        # Tail points away from the star
        return -direction_to_star / distance
    
    def update_tail(self, star_position: np.ndarray, distance_to_star: float) -> None:
        """Update tail length and coma radius based on distance to star."""
        # Simplified model: tail grows as comet approaches star
        if distance_to_star > 0:
            # AU in meters
            au = 1.496e11
            
            # Tail is longer when closer to star (inverse relationship)
            # Maximum at perihelion, minimal at aphelion
            base_tail = self.properties.get("base_tail_length_m", self.tail_length_m)
            self.tail_length_m = base_tail * (5 * au / distance_to_star)
            
            # Coma also grows when closer
            base_coma = self.properties.get("base_coma_radius_m", self.coma_radius_m)
            self.coma_radius_m = base_coma * (2 * au / distance_to_star)
            
            # Update properties
            self.properties["tail_length_m"] = self.tail_length_m
            self.properties["coma_radius_m"] = self.coma_radius_m


@dataclass
class DustParticle(PhysicalObject):
    """Class for dust particles."""
    
    diameter_m: float = 0.0
    
    def __post_init__(self) -> None:
        """Initialize dust-specific properties."""
        if not self.object_type == ObjectType.DUST_PARTICLE:
            self.object_type = ObjectType.DUST_PARTICLE
        
        # Set radius from diameter if provided
        if self.radius_m == 0 and self.diameter_m > 0:
            self.radius_m = self.diameter_m / 2
            
        super().__post_init__()
        
        # Add dust-specific properties
        self.properties["aerodynamic_drag_coefficient"] = 0.47  # Default sphere
    
    def calculate_terminal_velocity(self, fluid_density: float, gravity: float) -> float:
        """
        Calculate terminal velocity in a fluid (e.g., air) in m/s.
        
        Args:
            fluid_density: Density of the fluid (kg/m³)
            gravity: Gravitational acceleration (m/s²)
        
        Returns:
            Terminal velocity in m/s
        """
        if self.radius_m <= 0 or self.density <= 0:
            return 0.0
        
        # Stokes' law for small particles
        if self.radius_m < 1e-4:  # 0.1 mm
            # v = (2/9) * (ρₚ - ρf) * g * r² / μ
            # Assuming air viscosity μ = 1.8e-5 Pa·s
            viscosity = 1.8e-5
            return (2/9) * ((self.density - fluid_density) * gravity * (self.radius_m ** 2)) / viscosity
        else:
            # For larger particles, use drag equation
            # v = sqrt(2 * m * g / (ρf * A * Cd))
            drag_coef = self.properties.get("aerodynamic_drag_coefficient", 0.47)
            cross_section = np.pi * (self.radius_m ** 2)
            return np.sqrt((2 * self.mass_kg * gravity) / (fluid_density * cross_section * drag_coef))


class PhysicalObjectFactory:
    """Factory class for creating common physical objects."""
    
    @staticmethod
    def create_solar_system() -> List[CelestialBody]:
        """Create a simplified model of our solar system."""
        # Sun
        sun = Star(
            name="Sun",
            mass_kg=1.989e30,
            object_type=ObjectType.STAR,
            composition=CompositionType.PLASMA,
            radius_m=6.957e8,
            temperature_k=5778,
            luminosity_watts=3.828e26,
            spectral_type="G2V"
        )
        
        # Mercury
        mercury = Planet(
            name="Mercury",
            mass_kg=3.3011e23,
            object_type=ObjectType.PLANET,
            composition=CompositionType.ROCKY,
            radius_m=2.4397e6,
            temperature_k=440,
            orbital_parameters={
                "semi_major_axis": 5.791e10,
                "eccentricity": 0.2056,
                "inclination": np.radians(7.005),
                "period": 7.60052e6
            },
            rotation_period_s=5.067e6,
            properties={"parent_mass": 1.989e30}
        )
        
        # Venus
        venus = Planet(
            name="Venus",
            mass_kg=4.8675e24,
            object_type=ObjectType.PLANET,
            composition=CompositionType.ROCKY,
            radius_m=6.0518e6,
            temperature_k=737,
            has_atmosphere=True,
            orbital_parameters={
                "semi_major_axis": 1.082e11,
                "eccentricity": 0.0067,
                "inclination": np.radians(3.39),
                "period": 1.9414e7
            },
            rotation_period_s=-2.0995e6,  # Negative for retrograde rotation
            properties={"parent_mass": 1.989e30}
        )
        
        # Earth
        earth = Planet(
            name="Earth",
            mass_kg=5.9724e24,
            object_type=ObjectType.PLANET,
            composition=CompositionType.ROCKY,
            radius_m=6.371e6,
            temperature_k=288,
            has_atmosphere=True,
            has_magnetic_field=True,
            orbital_parameters={
                "semi_major_axis": 1.496e11,
                "eccentricity": 0.0167,
                "inclination": np.radians(0.0),
                "period": 3.1558e7
            },
            rotation_period_s=8.6164e4,
            axial_tilt_rad=np.radians(23.44),
            properties={"parent_mass": 1.989e30}
        )
        
        # Mars
        mars = Planet(
            name="Mars",
            mass_kg=6.4171e23,
            object_type=ObjectType.PLANET,
            composition=CompositionType.ROCKY,
            radius_m=3.3895e6,
            temperature_k=210,
            has_atmosphere=True,
            orbital_parameters={
                "semi_major_axis": 2.279e11,
                "eccentricity": 0.0935,
                "inclination": np.radians(1.85),
                "period": 5.9355e7
            },
            rotation_period_s=8.8643e4,
            axial_tilt_rad=np.radians(25.19),
            properties={"parent_mass": 1.989e30}
        )
        
        # Jupiter
        jupiter = Planet(
            name="Jupiter",
            mass_kg=1.8982e27,
            object_type=ObjectType.PLANET,
            composition=CompositionType.GASEOUS,
            radius_m=6.9911e7,
            temperature_k=165,
            has_atmosphere=True,
            has_magnetic_field=True,
            orbital_parameters={
                "semi_major_axis": 7.786e11,
                "eccentricity": 0.0489,
                "inclination": np.radians(1.31),
                "period": 3.7402e8
            },
            rotation_period_s=3.573e4,
            axial_tilt_rad=np.radians(3.13),
            properties={"parent_mass": 1.989e30}
        )
        
        # Return all bodies
        return [sun, mercury, venus, earth, mars, jupiter]
    
    @staticmethod
    def create_halley_comet() -> Comet:
        """Create a model of Halley's Comet."""
        return Comet(
            name="Halley's Comet",
            mass_kg=2.2e14,
            object_type=ObjectType.COMET,
            composition=CompositionType.ICY,
            nucleus_radius_m=5.5e3,
            coma_radius_m=1e5,
            tail_length_m=1e8,
            orbital_parameters={
                "semi_major_axis": 2.667e12,
                "eccentricity": 0.967,
                "inclination": np.radians(162.3),
                "period": 2.375e9
            },
            rotation_period_s=2.2 * 24 * 3600,  # 2.2 days
            properties={
                "parent_mass": 1.989e30,
                "base_tail_length_m": 1e8,
                "base_coma_radius_m": 1e5
            }
        )
    
    @staticmethod
    def create_dust_particle(diameter_microns: float, density_kg_m3: float) -> DustParticle:
        """Create a dust particle with specified diameter in microns."""
        diameter_m = diameter_microns * 1e-6
        volume = (4/3) * np.pi * ((diameter_m/2) ** 3)
        mass_kg = volume * density_kg_m3
        
        return DustParticle(
            name=f"Dust-{diameter_microns}μm",
            mass_kg=mass_kg,
            object_type=ObjectType.DUST_PARTICLE,
            composition=CompositionType.MIXED,
            diameter_m=diameter_m,
            properties={"density_kg_m3": density_kg_m3}
        )


class PhysicalSystem:
    """Class to represent a system of physical objects (e.g., solar system)."""
    
    def __init__(self, name: str, system_type: SystemType, central_object: Optional[PhysicalObject] = None):
        """
        Initialize a physical system.
        
        Args:
            name: Name of the system
            system_type: Type of system
            central_object: Central object of the system (e.g., star)
        """
        self.name = name
        self.system_type = system_type
        self.central_object = central_object
        self.objects: List[PhysicalObject] = []
        
        if central_object:
            self.objects.append(central_object)
    
    def add_object(self, obj: PhysicalObject) -> None:
        """Add an object to the system."""
        if obj not in self.objects:
            self.objects.append(obj)
    
    def remove_object(self, obj: PhysicalObject) -> None:
        """Remove an object from the system."""
        if obj in self.objects:
            self.objects.remove(obj)
    
    def get_object_by_name(self, name: str) -> Optional[PhysicalObject]:
        """Find an object by name."""
        for obj in self.objects:
            if obj.name.lower() == name.lower():
                return obj
        return None
    
    def get_objects_by_type(self, object_type: ObjectType) -> List[PhysicalObject]:
        """Get all objects of a specific type."""
        return [obj for obj in self.objects if obj.object_type == object_type]
    
    def calculate_center_of_mass(self) -> Vector3D:
        """Calculate the center of mass of the system."""
        total_mass = sum(obj.mass_kg for obj in self.objects)
        
        if total_mass == 0:
            return Vector3D()
        
        weighted_sum = Vector3D()
        for obj in self.objects:
            weighted_sum = weighted_sum + (obj.position * obj.mass_kg)
            
        return weighted_sum / total_mass
    
    def calculate_total_energy(self) -> Dict[str, float]:
        """Calculate the total energy of the system (kinetic, potential, total)."""
        kinetic_energy = sum(obj.kinetic_energy for obj in self.objects)
        
        # Calculate gravitational potential energy
        potential_energy = 0.0
        for i, obj1 in enumerate(self.objects):
            for j, obj2 in enumerate(self.objects):
                if i < j:  # Avoid double counting
                    distance = obj1.distance_to(obj2)
                    if distance > 0:
                        potential_energy -= (PhysicalObject.GRAVITATIONAL_CONSTANT * 
                                           obj1.mass_kg * obj2.mass_kg / distance)
        
        return {
            "kinetic": kinetic_energy,
            "potential": potential_energy,
            "total": kinetic_energy + potential_energy
        }
    
    def simulate_step(self, time_step: float) -> None:
        """
        Simulate one time step (in seconds) of the system's evolution.
        
        Uses a simple Euler integration method. For more accurate simulations,
        consider using Runge-Kutta or symplectic integrators.
        """
        # Calculate accelerations for each object
        accelerations = [Vector3D() for _ in self.objects]
        
        # Calculate gravitational forces between all pairs of objects
        for i, obj1 in enumerate(self.objects):
            for j, obj2 in enumerate(self.objects):
                if i != j:
                    force = obj1.gravitational_force_with(obj2)
                    accelerations[i] = accelerations[i] + (force / obj1.mass_kg)
        
        # Update velocities based on accelerations
        for i, obj in enumerate(self.objects):
            obj.update_velocity(accelerations[i], time_step)
        
        # Update positions based on velocities
        for obj in self.objects:
            obj.update_position(time_step)
            
        # Update comet tails if applicable
        if self.central_object and self.central_object.object_type == ObjectType.STAR:
            for obj in self.objects:
                if obj.object_type == ObjectType.COMET and isinstance(obj, Comet):
                    distance = obj.distance_to(self.central_object)
                    obj.update_tail(self.central_object.position_vector, distance)


# Example usage
if __name__ == "__main__":
    # Create a solar system
    solar_system_objects = PhysicalObjectFactory.create_solar_system()
    sun = solar_system_objects[0]
    
    solar_system = PhysicalSystem(
        name="Solar System",
        system_type=SystemType.SOLAR_SYSTEM,
        central_object=sun
    )
    
    # Add planets
    for obj in solar_system_objects[1:]:
        solar_system.add_object(obj)
    
    # Add Halley's comet
    halley = PhysicalObjectFactory.create_halley_comet()
    solar_system.add_object(halley)
    
    # Create dust particles of different sizes
    dust_10 = PhysicalObjectFactory.create_dust_particle(10.0, 2500.0)  # 10 micron, density 2500 kg/m³
    dust_50 = PhysicalObjectFactory.create_dust_particle(50.0, 2500.0)  # 50 micron, density 2500 kg/m³
    
    # Calculate terminal velocity on Earth
    earth = solar_system.get_object_by_name("Earth")
    if earth:
        earth_gravity = earth.surface_gravity
        air_density = 1.225  # kg/m³ at sea level
        
        v_10 = dust_10.calculate_terminal_velocity(air_density, earth_gravity)
        v_50 = dust_50.calculate_terminal_velocity(air_density, earth_gravity)
        
        print(f"=== Physical Objects Demonstration ===")
        print(f"\nSolar System objects:")
        for obj in solar_system.objects:
            if obj.object_type in [ObjectType.STAR, ObjectType.PLANET]:
                print(f"  {obj.name}: mass={obj.mass_kg:.2e} kg, radius={obj.radius_m:.2e} m")
        
        print(f"\nHalley's Comet details:")
        print(f"  Nucleus radius: {halley.nucleus_radius_m:.2e} m")
        print(f"  Orbital period: {halley.orbital_period/(365.25*24*3600):.2f} years")
        print(f"  Eccentricity: {halley.orbital_parameters['eccentricity']:.3f}")
        
        print(f"\nDust particle behavior in Earth's atmosphere:")
        print(f"  10μm dust terminal velocity: {v_10:.2f} m/s")
        print(f"  50μm dust terminal velocity: {v_50:.2f} m/s")
        
        # Get Earth's habitable zone from Sun
        habitable_zone = sun.habitable_zone
        print(f"\nSun's habitable zone:")
        print(f"  Inner boundary: {habitable_zone[0]/1.496e11:.2f} AU")
        print(f"  Outer boundary: {habitable_zone[1]/1.496e11:.2f} AU")
        print(f"  Earth's orbit: {earth.orbital_parameters['semi_major_axis']/1.496e11:.2f} AU")
