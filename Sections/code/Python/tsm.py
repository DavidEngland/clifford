from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Final, TypedDict, Set, ClassVar
import numpy as np

# Type definitions for particle properties
class QuarkProperties(TypedDict, total=False):
    color: str
    flavor: str
    confined: bool

class LeptonProperties(TypedDict, total=False):
    is_neutrino: bool
    lepton_number: int

class BosonProperties(TypedDict, total=False):
    mediates: 'Force'
    range: float
    coupling_constant: float

# Enumerations for particle properties
class Spin(Enum):
    SCALAR = 0      # Higgs
    HALF = 0.5      # Fermions
    ONE = 1         # Gauge bosons
    TWO = 2         # Graviton (beyond SM)
    
    def __str__(self) -> str:
        if self == Spin.HALF:
            return "½"
        return str(self.value)

class Force(Enum):
    STRONG = auto()
    ELECTROMAGNETIC = auto()
    WEAK = auto()
    GRAVITATIONAL = auto()
    
    def __str__(self) -> str:
        return self.name.capitalize()

class ParticleType(Enum):
    QUARK = auto()
    LEPTON = auto()
    GAUGE_BOSON = auto()
    SCALAR_BOSON = auto()
    THEORETICAL = auto()
    
    def __str__(self) -> str:
        return self.name.replace('_', ' ').capitalize()

class Generation(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    NONE = 0
    
    def __str__(self) -> str:
        if self == Generation.NONE:
            return "N/A"
        return f"{self.value}ˢᵗ" if self.value == 1 else f"{self.value}ⁿᵈ" if self.value == 2 else f"{self.value}ʳᵈ"

@dataclass
class Particle:
    """Base class for all particles in the Standard Model and beyond."""
    
    name: str
    symbol: str
    mass_gev: float
    charge: float
    spin: Spin
    particle_type: ParticleType
    antiparticle: bool = False
    generation: Generation = Generation.NONE
    properties: Dict[str, Any] = field(default_factory=dict)
    
    # Class constants
    SELF_ANTIPARTICLES: ClassVar[Set[str]] = {"Photon", "Z", "Higgs", "Graviton"}
    
    def __post_init__(self) -> None:
        """Initialize default properties if not provided."""
        # Validation could be added here
        if self.mass_gev < 0:
            raise ValueError(f"Mass cannot be negative: {self.mass_gev}")
    
    def __repr__(self) -> str:
        """Return a string representation of the particle."""
        anti_prefix = "Anti-" if self.antiparticle and self.name not in self.SELF_ANTIPARTICLES else ""
        return f"{anti_prefix}{self.name}({self.symbol})"
    
    def __eq__(self, other) -> bool:
        """Compare two particles for equality."""
        if not isinstance(other, Particle):
            return False
        return (self.name == other.name and 
                self.symbol == other.symbol and 
                self.charge == other.charge and
                self.antiparticle == other.antiparticle)
    
    def __hash__(self) -> int:
        """Generate a hash for using particles in sets and as dict keys."""
        return hash((self.name, self.symbol, self.charge, self.antiparticle))
    
    @property
    def rest_energy(self) -> float:
        """Return the rest energy of the particle in GeV."""
        return self.mass_gev
    
    @property
    def is_fermion(self) -> bool:
        """Check if the particle is a fermion (half-integer spin)."""
        return self.spin == Spin.HALF
    
    @property
    def is_boson(self) -> bool:
        """Check if the particle is a boson (integer spin)."""
        return self.spin.value.is_integer()
    
    @property
    def formatted_charge(self) -> str:
        """Return the electric charge in a formatted string."""
        if self.charge == 0:
            return "0"
        if self.charge == 1:
            return "+1"
        if self.charge == -1:
            return "-1"
        if self.charge == 2/3:
            return "+2/3"
        if self.charge == -1/3:
            return "-1/3"
        return str(self.charge)
    
    def get_antiparticle(self):
        """Create the antiparticle version if it exists."""
        # Handle particles that are their own antiparticles
        if self.name in self.SELF_ANTIPARTICLES:
            return self
        
        # Create an antiparticle with inverted charge
        anti_name = f"Anti-{self.name}" if not self.antiparticle else self.name[5:]
        anti_symbol = self._get_anti_symbol()
        
        # Create a copy of properties for the antiparticle
        anti_props = self.properties.copy()
        
        return type(self)(
            name=anti_name,
            symbol=anti_symbol,
            mass_gev=self.mass_gev,
            charge=-self.charge,
            spin=self.spin,
            particle_type=self.particle_type,
            antiparticle=not self.antiparticle,
            generation=self.generation,
            properties=anti_props
        )
    
    def _get_anti_symbol(self) -> str:
        """Generate the symbol for an antiparticle."""
        # This is a simplification - proper handling would use Unicode overbar
        if self.antiparticle:
            # Converting from anti to particle
            return self.symbol.replace("̄", "")
        else:
            # Converting from particle to anti
            return f"{self.symbol}̄"
    
    def interacts_via(self, force: Force) -> bool:
        """Determine if particle interacts via the given force."""
        if force == Force.GRAVITATIONAL:
            return True  # All particles with mass interact via gravity
        
        if force == Force.ELECTROMAGNETIC:
            return self.charge != 0
            
        if force == Force.STRONG:
            return (self.particle_type == ParticleType.QUARK or 
                    (self.particle_type == ParticleType.GAUGE_BOSON and 
                     self.properties.get("mediates") == Force.STRONG))
        
        if force == Force.WEAK:
            return (self.particle_type in [ParticleType.QUARK, ParticleType.LEPTON] or
                    (self.particle_type == ParticleType.GAUGE_BOSON and
                     self.properties.get("mediates") in [Force.WEAK, Force.ELECTROMAGNETIC]))
                     
        return False


@dataclass
class Quark(Particle):
    """Specialized class for quarks with color charge."""
    
    # Additional quark-specific attributes
    color: str = "r"
    
    def __post_init__(self) -> None:
        """Initialize quark-specific properties."""
        super().__post_init__()
        # Store color in properties
        self.properties["color"] = self.color
        self.properties["confined"] = True
    
    def get_antiparticle(self):
        """Create the antiquark with opposite charge and color."""
        anti_colors = {"r": "anti-r", "g": "anti-g", "b": "anti-b", 
                      "anti-r": "r", "anti-g": "g", "anti-b": "b"}
        
        anti = Quark(
            name=f"Anti-{self.name}" if not self.antiparticle else self.name[5:],
            symbol=self._get_anti_symbol(),
            mass_gev=self.mass_gev,
            charge=-self.charge,
            spin=self.spin,
            particle_type=self.particle_type,
            antiparticle=not self.antiparticle,
            generation=self.generation,
            color=anti_colors[self.color]
        )
        return anti


@dataclass
class Lepton(Particle):
    """Specialized class for leptons."""
    
    # Additional lepton-specific attributes
    is_neutrino: bool = False
    
    def __post_init__(self) -> None:
        """Initialize lepton-specific properties."""
        super().__post_init__()
        self.properties["is_neutrino"] = self.is_neutrino
        self.properties["lepton_number"] = 1  # +1 for leptons, -1 for antileptons (set in get_antiparticle)
    
    def get_antiparticle(self):
        """Create the antilepton with opposite charge and lepton number."""
        anti = super().get_antiparticle()
        if isinstance(anti, Lepton):
            anti.properties["lepton_number"] = -1 if self.properties["lepton_number"] == 1 else 1
        return anti


@dataclass
class GaugeBoson(Particle):
    """Specialized class for gauge bosons (force carriers)."""
    
    # Additional boson-specific attributes
    mediates: Force = None
    
    def __post_init__(self) -> None:
        """Initialize boson-specific properties."""
        super().__post_init__()
        if self.mediates:
            self.properties["mediates"] = self.mediates
            
            # Set range based on force type
            if self.mediates == Force.ELECTROMAGNETIC or self.mediates == Force.GRAVITATIONAL:
                self.properties["range"] = float('inf')  # Infinite range
            elif self.mediates == Force.WEAK:
                self.properties["range"] = 1e-18  # ~10^-18 m
            elif self.mediates == Force.STRONG:
                self.properties["range"] = 1e-15  # ~10^-15 m (nuclear scale)


class ParticleFactory:
    """Factory class for creating Standard Model particles."""
    
    @staticmethod
    def create_quarks() -> List[Quark]:
        """Create all Standard Model quarks."""
        return [
            Quark("Up", "u", 0.0022, 2/3, Spin.HALF, ParticleType.QUARK, generation=Generation.FIRST),
            Quark("Down", "d", 0.0047, -1/3, Spin.HALF, ParticleType.QUARK, generation=Generation.FIRST),
            Quark("Charm", "c", 1.27, 2/3, Spin.HALF, ParticleType.QUARK, generation=Generation.SECOND),
            Quark("Strange", "s", 0.093, -1/3, Spin.HALF, ParticleType.QUARK, generation=Generation.SECOND),
            Quark("Top", "t", 172.76, 2/3, Spin.HALF, ParticleType.QUARK, generation=Generation.THIRD),
            Quark("Bottom", "b", 4.18, -1/3, Spin.HALF, ParticleType.QUARK, generation=Generation.THIRD)
        ]
    
    @staticmethod
    def create_leptons() -> List[Lepton]:
        """Create all Standard Model leptons."""
        return [
            Lepton("Electron", "e", 0.000511, -1, Spin.HALF, ParticleType.LEPTON, generation=Generation.FIRST),
            Lepton("Electron Neutrino", "νₑ", 1e-9, 0, Spin.HALF, ParticleType.LEPTON, generation=Generation.FIRST, is_neutrino=True),
            Lepton("Muon", "μ", 0.106, -1, Spin.HALF, ParticleType.LEPTON, generation=Generation.SECOND),
            Lepton("Muon Neutrino", "νᵤ", 1e-9, 0, Spin.HALF, ParticleType.LEPTON, generation=Generation.SECOND, is_neutrino=True),
            Lepton("Tau", "τ", 1.777, -1, Spin.HALF, ParticleType.LEPTON, generation=Generation.THIRD),
            Lepton("Tau Neutrino", "νᵧ", 1e-9, 0, Spin.HALF, ParticleType.LEPTON, generation=Generation.THIRD, is_neutrino=True)
        ]
    
    @staticmethod
    def create_bosons() -> List[Particle]:
        """Create all Standard Model bosons."""
        gauge_bosons = [
            GaugeBoson("Photon", "γ", 0, 0, Spin.ONE, ParticleType.GAUGE_BOSON, mediates=Force.ELECTROMAGNETIC),
            GaugeBoson("W Plus", "W⁺", 80.4, 1, Spin.ONE, ParticleType.GAUGE_BOSON, mediates=Force.WEAK),
            GaugeBoson("W Minus", "W⁻", 80.4, -1, Spin.ONE, ParticleType.GAUGE_BOSON, antiparticle=True, mediates=Force.WEAK),
            GaugeBoson("Z", "Z", 91.2, 0, Spin.ONE, ParticleType.GAUGE_BOSON, mediates=Force.WEAK),
            GaugeBoson("Gluon", "g", 0, 0, Spin.ONE, ParticleType.GAUGE_BOSON, mediates=Force.STRONG)
        ]
        
        # Higgs boson
        higgs = Particle(
            name="Higgs",
            symbol="H",
            mass_gev=125.25,
            charge=0,
            spin=Spin.SCALAR,
            particle_type=ParticleType.SCALAR_BOSON
        )
        
        return gauge_bosons + [higgs]
    
    @staticmethod
    def create_bsm_particles() -> List[Particle]:
        """Create example Beyond Standard Model particles."""
        return [
            Particle(
                name="Graviton",
                symbol="G",
                mass_gev=0,
                charge=0,
                spin=Spin.TWO,
                particle_type=ParticleType.THEORETICAL,
                properties={"mediates": Force.GRAVITATIONAL}
            ),
            Particle(
                name="Selectron",
                symbol="ẽ",
                mass_gev=500,  # Hypothetical mass
                charge=-1,
                spin=Spin.SCALAR,
                particle_type=ParticleType.THEORETICAL,
                properties={"susy_partner": "Electron"}
            )
        ]


class StandardModel:
    """Class to represent the entire Standard Model of particle physics."""
    
    def __init__(self, include_antiparticles: bool = True, include_bsm: bool = False):
        """
        Initialize the Standard Model.
        
        Args:
            include_antiparticles: Whether to include antiparticles
            include_bsm: Whether to include Beyond Standard Model particles
        """
        self.particles = []
        self._initialize_particles(include_antiparticles, include_bsm)
    
    def _initialize_particles(self, include_antiparticles: bool, include_bsm: bool) -> None:
        """Initialize all particles in the Standard Model."""
        # Use the factory to create particles
        factory = ParticleFactory()
        
        # Add Standard Model particles
        self.particles.extend(factory.create_quarks())
        self.particles.extend(factory.create_leptons())
        self.particles.extend(factory.create_bosons())
        
        # Optionally add Beyond Standard Model particles
        if include_bsm:
            self.particles.extend(factory.create_bsm_particles())
        
        # Add antiparticles if requested
        if include_antiparticles:
            # Filter particles that need antiparticles
            need_antiparticle = [p for p in self.particles if 
                                p.name not in Particle.SELF_ANTIPARTICLES and 
                                not p.antiparticle]
            
            # Create and add antiparticles
            for particle in need_antiparticle:
                self.particles.append(particle.get_antiparticle())
    
    def get_particle_by_name(self, name: str) -> Optional[Particle]:
        """
        Retrieve a particle by its name (case-insensitive).
        
        Args:
            name: The name of the particle to find
            
        Returns:
            The particle object if found, None otherwise
        """
        for particle in self.particles:
            if particle.name.lower() == name.lower():
                return particle
        return None
    
    def get_particles_by_type(self, particle_type: ParticleType) -> List[Particle]:
        """
        Get all particles of a specific type.
        
        Args:
            particle_type: The type of particles to retrieve
            
        Returns:
            A list of particles matching the specified type
        """
        return [p for p in self.particles if p.particle_type == particle_type]
    
    def get_particles_by_force(self, force: Force) -> List[Particle]:
        """
        Get all particles that interact via a specific force.
        
        Args:
            force: The force to filter by
            
        Returns:
            A list of particles that interact via the specified force
        """
        return [p for p in self.particles if p.interacts_via(force)]
    
    def print_summary(self) -> None:
        """Print a summary of all particles in the Standard Model."""
        print("=== Standard Model Summary ===")
        
        # Group particles by type for prettier output
        particle_types = {
            ParticleType.QUARK: "Quarks",
            ParticleType.LEPTON: "Leptons",
            ParticleType.GAUGE_BOSON: "Gauge Bosons",
            ParticleType.SCALAR_BOSON: "Scalar Bosons",
            ParticleType.THEORETICAL: "Theoretical Particles"
        }
        
        for p_type, title in particle_types.items():
            particles = self.get_particles_by_type(p_type)
            # Filter out antiparticles for cleaner display
            particles = [p for p in particles if not p.antiparticle]
            
            if particles:
                print(f"\n{title}:")
                for p in particles:
                    print(f"  {p.name}: charge={p.formatted_charge}, mass={p.mass_gev} GeV/c², spin={p.spin}")


# Example extension for beyond Standard Model physics
class TheoreticalParticle(Particle):
    """Class for particles beyond the Standard Model."""
    
    def __init__(self, name: str, symbol: str, mass_gev: float, charge: float, 
                 spin: Spin, properties: Dict[str, Any] = None):
        """
        Initialize a theoretical particle.
        
        Args:
            name: Particle name
            symbol: Particle symbol
            mass_gev: Mass in GeV/c²
            charge: Electric charge
            spin: Spin value
            properties: Additional properties
        """
        super().__init__(
            name=name,
            symbol=symbol,
            mass_gev=mass_gev,
            charge=charge,
            spin=spin,
            particle_type=ParticleType.THEORETICAL,
            properties=properties or {}
        )


# Example usage
if __name__ == "__main__":
    # Create the Standard Model
    sm = StandardModel(include_bsm=True)
    
    # Print a summary
    sm.print_summary()
    
    # Demonstrate the enhanced functionality
    print("\nAccessing specific particles:")
    electron = sm.get_particle_by_name("electron")
    if electron:
        print(f"Electron: {electron}")
        print(f"Is fermion: {electron.is_fermion}")
        print(f"Rest energy: {electron.rest_energy} GeV")
        
        # Get its antiparticle
        positron = electron.get_antiparticle()
        print(f"Antiparticle: {positron}")
    
    # Show particles that interact via the electromagnetic force
    print("\nParticles interacting via electromagnetic force:")
    em_particles = sm.get_particles_by_force(Force.ELECTROMAGNETIC)
    for p in em_particles[:5]:  # Show first 5 only to keep output manageable
        print(f"  {p}")