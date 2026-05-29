# =============================================================================
# Omega Calculator 10.0 - Module 5: Physical Constants
# Author: Amirmahdi Ghorbani
# =============================================================================
# This module provides a comprehensive collection of fundamental physical
# constants used throughout the physics section of Omega Calculator.
#
# Constants are organized by field:
#   - Gravitational: g (Earth surface gravity), G (universal constant)
#   - Electromagnetic: c (speed of light), e (elementary charge),
#     ε₀ (vacuum permittivity), μ₀ (vacuum permeability)
#   - Quantum: h (Planck), ħ (reduced Planck)
#   - Thermodynamic: k_B (Boltzmann), R (gas constant), σ (Stefan-Boltzmann)
#   - Atomic/Nuclear: m_e (electron mass), m_p (proton mass),
#     N_A (Avogadro), R_∞ (Rydberg), μ_B (Bohr magneton), a₀ (Bohr radius)
#
# Each constant is exposed as a static method returning a float value
# in standard SI units. All values are hardcoded for offline availability.
#
# Dependencies:
#   - math (standard library): Used only for μ₀ = 4π × 10⁻⁷
#
# Last Modified: 2026-05-29
# Version: 10.0 (Modular Edition)
# =============================================================================

import math


class PhysicalConstants:
    """
    A repository of fundamental physical constants in SI units.

    Each constant is exposed as a static method for consistent, semantic
    access throughout the application. Constants are returned as float
    values in standard SI units (meters, kilograms, seconds, etc.).
    """

    # =========================================================================
    # GRAVITATIONAL CONSTANTS
    # =========================================================================

    @staticmethod
    def constant_g():
        """
        Standard gravitational acceleration at Earth's surface.

        Value: 9.8 m/s²
        This approximate value is suitable for educational calculations
        and most practical problems. The actual local value varies with
        latitude (9.78 at equator to 9.83 at poles) and altitude.

        Returns:
            float: 9.8 (meters per second squared)
        """
        return 9.8

    @staticmethod
    def constant_G():
        """
        Newton's universal gravitational constant.

        Value: 6.674 × 10⁻¹¹ N·m²/kg²
        Appears in F = G·m₁·m₂ / r². This fundamental constant quantifies
        the strength of gravitational interaction between masses.

        Returns:
            float: 6.674e-11 (N·m²/kg²)
        """
        return 6.674e-11

    # =========================================================================
    # ELECTROMAGNETIC CONSTANTS
    # =========================================================================

    @staticmethod
    def constant_c():
        """
        Speed of light in vacuum (exact defined value).

        Value: 3.0 × 10⁸ m/s
        Since 1983, this is the exact defined value used to define the
        meter. It is the universal speed limit for information and matter.

        Returns:
            float: 300000000.0 (m/s)
        """
        return 3e8

    @staticmethod
    def constant_e():
        """
        Elementary electric charge (magnitude of proton/electron charge).

        Value: 1.6 × 10⁻¹⁹ C
        All observed electric charges are integer multiples of this
        fundamental charge. Electrons carry -e, protons carry +e.

        Returns:
            float: 1.6e-19 (Coulombs)
        """
        return 1.6e-19

    @staticmethod
    def constant_epsilon0():
        """
        Vacuum permittivity (electric constant).

        Value: 8.85 × 10⁻¹² C²/N·m²
        Appears in Coulomb's law and Maxwell's equations. Related to
        the speed of light by c² = 1/(ε₀μ₀).

        Returns:
            float: 8.85e-12 (C²/N·m²)
        """
        return 8.85e-12

    @staticmethod
    def constant_mu0():
        """
        Vacuum permeability (magnetic constant).

        Value: 4π × 10⁻⁷ N/A²
        This is the exact defined value (prior to 2019 SI redefinition).
        Appears in Ampère's law and Biot-Savart law for magnetic fields.

        Returns:
            float: 4π × 10⁻⁷ ≈ 1.2566... × 10⁻⁶ (N/A²)
        """
        return 4 * math.pi * 1e-7

    # =========================================================================
    # QUANTUM MECHANICAL CONSTANTS
    # =========================================================================

    @staticmethod
    def constant_h():
        """
        Planck's constant - the fundamental quantum of action.

        Value: 6.626 × 10⁻³⁴ J·s
        Relates photon energy to frequency: E = hf. Sets the scale at
        which quantum effects become significant in physical systems.

        Returns:
            float: 6.626e-34 (Joule-seconds)
        """
        return 6.626e-34

    @staticmethod
    def constant_hbar():
        """
        Reduced Planck's constant (h-bar).

        Value: 1.054 × 10⁻³⁴ J·s
        Defined as h/(2π). Appears frequently in quantum mechanics:
        Schrödinger equation, commutation relations, and the Heisenberg
        uncertainty principle (Δx·Δp ≥ ħ/2).

        Returns:
            float: 1.054e-34 (Joule-seconds)
        """
        return 1.054e-34

    # =========================================================================
    # THERMODYNAMIC CONSTANTS
    # =========================================================================

    @staticmethod
    def constant_k_B():
        """
        Boltzmann's constant - bridges temperature and energy.

        Value: 1.38 × 10⁻²³ J/K
        Relates the average kinetic energy of particles in an ideal gas
        to temperature: KE_avg = (3/2)k_B·T. Converts between Kelvin
        and Joules at the microscopic scale.

        Returns:
            float: 1.38e-23 (J/K)
        """
        return 1.38e-23

    @staticmethod
    def constant_R():
        """
        Universal (molar) gas constant.

        Value: 8.314 J/(mol·K)
        Appears in the ideal gas law: PV = nRT. Related to Boltzmann's
        constant by R = N_A·k_B (Avogadro's number times Boltzmann).

        Returns:
            float: 8.314 (J/mol·K)
        """
        return 8.314

    @staticmethod
    def constant_sigma():
        """
        Stefan-Boltzmann constant for black-body radiation.

        Value: 5.67 × 10⁻⁸ W/m²·K⁴
        Appears in the Stefan-Boltzmann law: P/A = σ·T⁴, where P/A is
        the total power radiated per unit surface area of a black body.

        Returns:
            float: 5.67e-08 (W/m²·K⁴)
        """
        return 5.67e-8

    # =========================================================================
    # ATOMIC AND NUCLEAR CONSTANTS
    # =========================================================================

    @staticmethod
    def constant_m_e():
        """
        Electron rest mass.

        Value: 9.11 × 10⁻³¹ kg
        Approximately 1/1836 of the proton mass. Appears in calculations
        of atomic energy levels, Bohr radius, Compton wavelength, and
        electron microscopy.

        Returns:
            float: 9.11e-31 (kg)
        """
        return 9.11e-31

    @staticmethod
    def constant_m_p():
        """
        Proton rest mass.

        Value: 1.67 × 10⁻²⁷ kg
        Together with neutrons, protons constitute the vast majority of
        ordinary (baryonic) matter's mass in the universe.

        Returns:
            float: 1.67e-27 (kg)
        """
        return 1.67e-27

    @staticmethod
    def constant_N_A():
        """
        Avogadro's number.

        Value: 6.022 × 10²³ mol⁻¹
        The number of constituent particles (atoms, molecules, ions) in
        one mole of a substance. Links the atomic mass unit to grams.

        Returns:
            float: 6.022e23 (particles per mole)
        """
        return 6.022e23

    @staticmethod
    def constant_Rydberg():
        """
        Rydberg constant (for infinite nuclear mass).

        Value: 1.097 × 10⁷ m⁻¹
        Appears in the Rydberg formula for spectral lines of hydrogen:
        1/λ = R_∞·(1/n₁² - 1/n₂²). For real atoms, a reduced mass
        correction is needed for precise calculations.

        Returns:
            float: 10970000.0 (per meter)
        """
        return 1.097e7

    @staticmethod
    def constant_mu_B():
        """
        Bohr magneton - natural unit of electron magnetic moment.

        Value: 9.274 × 10⁻²⁴ J/T
        Defined as μ_B = eħ/(2m_e). Appears in the Zeeman effect
        (splitting of spectral lines in magnetic fields) and in
        calculations of paramagnetic susceptibility.

        Returns:
            float: 9.274e-24 (J/T)
        """
        return 9.274e-24

    @staticmethod
    def constant_a0():
        """
        Bohr radius - characteristic size of the hydrogen atom.

        Value: 5.29 × 10⁻¹¹ m
        The most probable distance between the proton and electron in
        a hydrogen atom in its ground state. Defines the atomic scale.

        Returns:
            float: 5.29e-11 (meters)
        """
        return 5.29e-11