"""Canonical unit-conversion helpers for engineering calculations.

These helpers provide fixed target units commonly used in chemical-engineering
modelling and simulation.  Conversion factors remain defined by PyCUC's
existing conversion engine and reference registry; this module only fixes the
target unit for convenience and consistency.
"""

from .app import convert_from_to, from_to


# Base and general engineering quantities

def to_K(value: float, from_unit: str) -> float:
    """Convert an absolute temperature to kelvin (K)."""
    return convert_from_to(value, from_unit, "K")


def to_Pa(value: float, from_unit: str) -> float:
    """Convert pressure to pascal (Pa)."""
    return from_to(value, from_unit, "Pa")


def to_m(value: float, from_unit: str) -> float:
    """Convert length to metre (m)."""
    return from_to(value, from_unit, "m")


def to_m2(value: float, from_unit: str) -> float:
    """Convert area to square metre (m^2)."""
    return from_to(value, from_unit, "m^2")


def to_m3(value: float, from_unit: str) -> float:
    """Convert volume to cubic metre (m^3)."""
    return from_to(value, from_unit, "m^3")


def to_kg(value: float, from_unit: str) -> float:
    """Convert mass to kilogram (kg)."""
    return from_to(value, from_unit, "kg")


def to_mol(value: float, from_unit: str) -> float:
    """Convert amount of substance to mole (mol)."""
    return from_to(value, from_unit, "mol")


def to_s(value: float, from_unit: str) -> float:
    """Convert time to second (s)."""
    return from_to(value, from_unit, "s")


def to_J(value: float, from_unit: str) -> float:
    """Convert energy to joule (J)."""
    return from_to(value, from_unit, "J")


def to_W(value: float, from_unit: str) -> float:
    """Convert power to watt (W)."""
    return from_to(value, from_unit, "W")


# Composition, density, and amount-based quantities

def to_kg_per_m3(value: float, from_unit: str) -> float:
    """Convert mass density or mass concentration to kg/m^3."""
    return from_to(value, from_unit, "kg/m^3")


def to_mol_per_m3(value: float, from_unit: str) -> float:
    """Convert molar density or molar concentration to mol/m^3."""
    return from_to(value, from_unit, "mol/m^3")


def to_mol_per_kg(value: float, from_unit: str) -> float:
    """Convert molality or amount-per-mass quantity to mol/kg."""
    return from_to(value, from_unit, "mol/kg")


def to_kg_per_mol(value: float, from_unit: str) -> float:
    """Convert molar mass to kg/mol."""
    return from_to(value, from_unit, "kg/mol")


def to_m3_per_mol(value: float, from_unit: str) -> float:
    """Convert molar volume to m^3/mol."""
    return from_to(value, from_unit, "m^3/mol")


def to_m3_per_kg(value: float, from_unit: str) -> float:
    """Convert specific volume to m^3/kg."""
    return from_to(value, from_unit, "m^3/kg")


# Process-flow quantities

def to_kg_per_s(value: float, from_unit: str) -> float:
    """Convert mass flow rate to kg/s."""
    return from_to(value, from_unit, "kg/s")


def to_mol_per_s(value: float, from_unit: str) -> float:
    """Convert molar flow rate to mol/s."""
    return from_to(value, from_unit, "mol/s")


def to_m3_per_s(value: float, from_unit: str) -> float:
    """Convert volumetric flow rate to m^3/s."""
    return from_to(value, from_unit, "m^3/s")


def to_m_per_s(value: float, from_unit: str) -> float:
    """Convert velocity to m/s."""
    return from_to(value, from_unit, "m/s")


# Thermodynamic quantities

def to_J_per_mol(value: float, from_unit: str) -> float:
    """Convert molar energy, enthalpy, or Gibbs energy to J/mol."""
    return from_to(value, from_unit, "J/mol")


def to_J_per_kg(value: float, from_unit: str) -> float:
    """Convert specific energy or enthalpy to J/kg."""
    return from_to(value, from_unit, "J/kg")


def to_J_per_mol_K(value: float, from_unit: str) -> float:
    """Convert molar heat capacity or entropy to J/(mol.K)."""
    return from_to(value, from_unit, "J/(mol.K)")


def to_J_per_kg_K(value: float, from_unit: str) -> float:
    """Convert specific heat capacity or entropy to J/(kg.K)."""
    return from_to(value, from_unit, "J/(kg.K)")


# Transport quantities

def to_Pa_s(value: float, from_unit: str) -> float:
    """Convert dynamic viscosity to Pa.s."""
    return from_to(value, from_unit, "Pa.s")


def to_m2_per_s(value: float, from_unit: str) -> float:
    """Convert diffusivity or kinematic viscosity to m^2/s."""
    return from_to(value, from_unit, "m^2/s")


def to_W_per_m_K(value: float, from_unit: str) -> float:
    """Convert thermal conductivity to W/(m.K)."""
    return from_to(value, from_unit, "W/(m.K)")


def to_W_per_m2_K(value: float, from_unit: str) -> float:
    """Convert heat-transfer coefficient to W/(m^2.K)."""
    return from_to(value, from_unit, "W/(m^2.K)")


# Flux, reaction, and membrane quantities

def to_mol_per_m2_s(value: float, from_unit: str) -> float:
    """Convert molar flux or surface reaction rate to mol/(m^2.s)."""
    return from_to(value, from_unit, "mol/(m^2.s)")


def to_kg_per_m2_s(value: float, from_unit: str) -> float:
    """Convert mass flux to kg/(m^2.s)."""
    return from_to(value, from_unit, "kg/(m^2.s)")


def to_mol_per_m3_s(value: float, from_unit: str) -> float:
    """Convert volumetric reaction rate to mol/(m^3.s)."""
    return from_to(value, from_unit, "mol/(m^3.s)")


def to_mol_per_m2_s_Pa(value: float, from_unit: str) -> float:
    """Convert gas permeance to mol/(m^2.s.Pa)."""
    return from_to(value, from_unit, "mol/(m^2.s.Pa)")


__all__ = [
    "to_K",
    "to_Pa",
    "to_m",
    "to_m2",
    "to_m3",
    "to_kg",
    "to_mol",
    "to_s",
    "to_J",
    "to_W",
    "to_kg_per_m3",
    "to_mol_per_m3",
    "to_mol_per_kg",
    "to_kg_per_mol",
    "to_m3_per_mol",
    "to_m3_per_kg",
    "to_kg_per_s",
    "to_mol_per_s",
    "to_m3_per_s",
    "to_m_per_s",
    "to_J_per_mol",
    "to_J_per_kg",
    "to_J_per_mol_K",
    "to_J_per_kg_K",
    "to_Pa_s",
    "to_m2_per_s",
    "to_W_per_m_K",
    "to_W_per_m2_K",
    "to_mol_per_m2_s",
    "to_kg_per_m2_s",
    "to_mol_per_m3_s",
    "to_mol_per_m2_s_Pa",
]
