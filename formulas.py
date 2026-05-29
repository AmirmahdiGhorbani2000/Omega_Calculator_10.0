# =============================================================================
# Omega Calculator 10.0 - Module 6: Physics Formulas Library
# Author: Amirmahdi Ghorbani
# =============================================================================
# This module provides a comprehensive collection of physics formulas
# organized by subfield. It serves as the computational backend for the
# physics section of the Omega Calculator application.
#
# Subfields Covered (69 formulas total):
#   1. Kinematics (10): motion in 1D/2D, projectile motion, free fall
#   2. Dynamics (9): forces, friction, momentum, impulse, Hooke's law
#   3. Work, Energy & Power (9): KE, PE, work-energy theorem, efficiency
#   4. Fluid Mechanics (6): density, pressure, buoyancy, Bernoulli
#   5. Electricity & Magnetism (13): Ohm's law, power, resistors, Coulomb
#   6. Heat & Thermodynamics (10): calorimetry, expansion, ideal gas, engines
#   7. Light & Optics (7): wave speed, refraction, Snell's law, lenses
#   8. Modern Physics (7): relativity (E=mc², time dilation), quantum (photons)
#
# Unit Conventions:
#   - Angles: Input in DEGREES (converted to radians internally via math.radians)
#   - Default values: g = 9.8 m/s², c = 3×10⁸ m/s, h = 6.626×10⁻³⁴ J·s
#   - All other parameters in standard SI units unless otherwise noted
#
# Dependencies:
#   - math (standard library): Mathematical functions and constants
#
# Last Modified: 2026-05-29
# Version: 10.0 (Modular Edition)
# =============================================================================

import math


class PhysicsFormulas:
    """
    A comprehensive library of physics formulas spanning classical mechanics
    through modern physics (relativity and quantum mechanics).

    All methods are static and stateless. Each formula accepts the required
    physical parameters and returns the computed result in standard SI units.
    Angles are accepted in degrees for user convenience and converted to
    radians internally using math.radians().
    """

    # =========================================================================
    # KINEMATICS - The study of motion without regard to its causes
    # =========================================================================

    @staticmethod
    def velocity_final_1(v0, a, t):
        """
        Calculates final velocity under constant acceleration.
        Formula: v = v₀ + at
        This is the first kinematic equation for constant acceleration.
        """
        return v0 + a * t

    @staticmethod
    def position_2(x0, v0, a, t):
        """
        Calculates position under constant acceleration.
        Formula: x = x₀ + v₀t + ½at²
        """
        return x0 + v0 * t + 0.5 * a * t ** 2

    @staticmethod
    def velocity_final_3(v0, a, dx):
        """
        Calculates final velocity without time (time-independent).
        Formula: v² = v₀² + 2aΔx → v = √(v₀² + 2aΔx)
        """
        return math.sqrt(v0 ** 2 + 2 * a * dx)

    @staticmethod
    def velocity_average(dx, dt):
        """
        Calculates average velocity over a time interval.
        Formula: v_avg = Δx / Δt
        """
        return dx / dt

    @staticmethod
    def acceleration_average(dv, dt):
        """
        Calculates average acceleration over a time interval.
        Formula: a_avg = Δv / Δt
        """
        return dv / dt

    @staticmethod
    def free_fall_velocity(t, g=9.8):
        """
        Calculates velocity during free fall from rest.
        Formula: v = gt (assuming initial velocity v₀ = 0)
        """
        return g * t

    @staticmethod
    def free_fall_height(t, g=9.8):
        """
        Calculates distance fallen during free fall from rest.
        Formula: h = ½gt²
        """
        return 0.5 * g * t ** 2

    @staticmethod
    def projectile_range(v0, theta_deg, g=9.8):
        """
        Calculates the horizontal range of a projectile.
        Formula: R = v₀² sin(2θ) / g
        Assumes launch and landing at same elevation, no air resistance.
        Maximum range occurs at θ = 45°.
        """
        theta_rad = math.radians(theta_deg)
        return (v0 ** 2 * math.sin(2 * theta_rad)) / g

    @staticmethod
    def projectile_max_height(v0, theta_deg, g=9.8):
        """
        Calculates the maximum height of a projectile.
        Formula: H = v₀² sin²(θ) / (2g)
        """
        theta_rad = math.radians(theta_deg)
        return (v0 ** 2 * math.sin(theta_rad) ** 2) / (2 * g)

    @staticmethod
    def projectile_time_of_flight(v0, theta_deg, g=9.8):
        """
        Calculates total time of flight for a projectile.
        Formula: T = 2v₀ sin(θ) / g
        Assumes launch and landing at same elevation.
        """
        theta_rad = math.radians(theta_deg)
        return 2 * v0 * math.sin(theta_rad) / g

    # =========================================================================
    # DYNAMICS - The study of forces and their effects on motion
    # =========================================================================

    @staticmethod
    def force_newton(m, a):
        """
        Calculates net force using Newton's second law.
        Formula: F = ma
        """
        return m * a

    @staticmethod
    def weight(m, g=9.8):
        """
        Calculates the weight of an object near Earth's surface.
        Formula: w = mg
        """
        return m * g

    @staticmethod
    def normal_incline(m, theta_deg, g=9.8):
        """
        Calculates the normal force on an inclined plane.
        Formula: N = mg cos(θ)
        The normal force is perpendicular to the surface.
        """
        theta_rad = math.radians(theta_deg)
        return m * g * math.cos(theta_rad)

    @staticmethod
    def friction_kinetic(mu_k, N):
        """
        Calculates kinetic (sliding) friction force.
        Formula: f_k = μₖ·N
        Kinetic friction opposes relative motion of surfaces.
        """
        return mu_k * N

    @staticmethod
    def friction_static_max(mu_s, N):
        """
        Calculates the maximum static friction force.
        Formula: f_s,max = μₛ·N
        Static friction prevents motion up to this maximum.
        """
        return mu_s * N

    @staticmethod
    def net_force_1d(forces):
        """
        Calculates the net force in one dimension.
        Formula: F_net = ΣFᵢ (sum of all forces along a single axis)
        """
        return sum(forces)

    @staticmethod
    def momentum(m, v):
        """
        Calculates linear momentum.
        Formula: p = mv
        Momentum is conserved in isolated systems.
        """
        return m * v

    @staticmethod
    def impulse(force, dt):
        """
        Calculates impulse (change in momentum).
        Formula: J = F·Δt = Δp
        """
        return force * dt

    @staticmethod
    def hooke_law(k, x):
        """
        Calculates the restoring force of an ideal spring.
        Formula: F = -kx
        Negative sign indicates force opposes displacement.
        """
        return -k * x

    # =========================================================================
    # WORK, ENERGY & POWER
    # =========================================================================

    @staticmethod
    def work(force, distance, theta_deg=0):
        """
        Calculates work done by a constant force.
        Formula: W = Fd cos(θ)
        Only the force component parallel to displacement does work.
        """
        theta_rad = math.radians(theta_deg)
        return force * distance * math.cos(theta_rad)

    @staticmethod
    def kinetic_energy(m, v):
        """
        Calculates kinetic energy of a moving object.
        Formula: KE = ½mv²
        """
        return 0.5 * m * v ** 2

    @staticmethod
    def potential_energy_gravity(m, h, g=9.8):
        """
        Calculates gravitational potential energy.
        Formula: PE = mgh (relative to a reference height)
        """
        return m * g * h

    @staticmethod
    def potential_energy_spring(k, x):
        """
        Calculates elastic potential energy stored in a spring.
        Formula: PE = ½kx²
        """
        return 0.5 * k * x ** 2

    @staticmethod
    def work_energy_theorem(ke_initial, ke_final):
        """
        Calculates net work from the change in kinetic energy.
        Formula: W_net = ΔKE = KE_final - KE_initial
        """
        return ke_final - ke_initial

    @staticmethod
    def mechanical_energy(ke, pe):
        """
        Calculates total mechanical energy.
        Formula: E = KE + PE
        Conserved in the absence of non-conservative forces.
        """
        return ke + pe

    @staticmethod
    def power_average(work_done, time):
        """
        Calculates average power.
        Formula: P_avg = W / t (rate of doing work)
        """
        return work_done / time

    @staticmethod
    def power_instantaneous(force, velocity, theta_deg=0):
        """
        Calculates instantaneous power.
        Formula: P = Fv cos(θ)
        """
        theta_rad = math.radians(theta_deg)
        return force * velocity * math.cos(theta_rad)

    @staticmethod
    def efficiency(work_out, work_in):
        """
        Calculates efficiency as a percentage.
        Formula: η = (W_out / W_in) × 100%
        """
        return (work_out / work_in) * 100

    # =========================================================================
    # FLUID MECHANICS
    # =========================================================================

    @staticmethod
    def density(m, v):
        """
        Calculates density of a substance.
        Formula: ρ = m / V (mass per unit volume)
        """
        return m / v

    @staticmethod
    def pressure(force, area):
        """
        Calculates pressure on a surface.
        Formula: P = F / A (force per unit area, in Pascals)
        """
        return force / area

    @staticmethod
    def pressure_depth(p0, rho, h, g=9.8):
        """
        Calculates pressure at a given depth in a fluid.
        Formula: P = P₀ + ρgh
        Pressure increases linearly with depth.
        """
        return p0 + rho * g * h

    @staticmethod
    def buoyant_force(rho_fluid, volume_submerged, g=9.8):
        """
        Calculates the buoyant force (Archimedes' principle).
        Formula: F_b = ρ_fluid · V_sub · g
        Equals the weight of fluid displaced.
        """
        return rho_fluid * volume_submerged * g

    @staticmethod
    def bernoulli_simple(p1, v1, h1, v2, h2, rho, g=9.8):
        """
        Applies Bernoulli's principle along a streamline.
        Formula: P₂ = P₁ + ½ρ(v₁² - v₂²) + ρg(h₁ - h₂)
        Expresses conservation of energy in flowing fluids.
        """
        p2 = p1 + 0.5 * rho * (v1 ** 2 - v2 ** 2) + rho * g * (h1 - h2)
        return p2

    @staticmethod
    def continuity_equation(a1, v1, a2):
        """
        Calculates velocity using the continuity equation.
        Formula: A₁v₁ = A₂v₂ → v₂ = A₁v₁ / A₂
        Expresses conservation of mass in incompressible flow.
        """
        return (a1 * v1) / a2

    # =========================================================================
    # ELECTRICITY & MAGNETISM
    # =========================================================================

    @staticmethod
    def ohms_law_voltage(current, resistance):
        """
        Calculates voltage using Ohm's law.
        Formula: V = IR
        """
        return current * resistance

    @staticmethod
    def ohms_law_current(voltage, resistance):
        """
        Calculates current using Ohm's law.
        Formula: I = V / R
        """
        return voltage / resistance

    @staticmethod
    def ohms_law_resistance(voltage, current):
        """
        Calculates resistance using Ohm's law.
        Formula: R = V / I
        """
        return voltage / current

    @staticmethod
    def electric_power_vi(voltage, current):
        """
        Calculates electric power from voltage and current.
        Formula: P = VI
        """
        return voltage * current

    @staticmethod
    def electric_power_i2r(current, resistance):
        """
        Calculates electric power (Joule heating) from current.
        Formula: P = I²R
        """
        return current ** 2 * resistance

    @staticmethod
    def electric_power_v2r(voltage, resistance):
        """
        Calculates electric power from voltage and resistance.
        Formula: P = V² / R
        """
        return voltage ** 2 / resistance

    @staticmethod
    def resistors_series(resistors):
        """
        Calculates equivalent resistance for series connection.
        Formula: R_total = R₁ + R₂ + R₃ + ...
        """
        return sum(resistors)

    @staticmethod
    def resistors_parallel(resistors):
        """
        Calculates equivalent resistance for parallel connection.
        Formula: 1/R_total = 1/R₁ + 1/R₂ + 1/R₃ + ...
        """
        return 1 / sum(1 / r for r in resistors)

    @staticmethod
    def voltage_energy(energy, charge):
        """
        Calculates voltage from energy and charge.
        Formula: V = W / q (potential difference)
        """
        return energy / charge

    @staticmethod
    def current_rate(charge, time):
        """
        Calculates electric current from charge flow.
        Formula: I = Δq / Δt
        """
        return charge / time

    @staticmethod
    def coulomb_law(q1, q2, r, k=8.99e9):
        """
        Calculates electrostatic force between two point charges.
        Formula: F = k·q₁·q₂ / r²
        k = 1/(4πε₀) ≈ 8.99 × 10⁹ N·m²/C²
        """
        return k * q1 * q2 / (r ** 2)

    @staticmethod
    def electric_field(force, charge):
        """
        Calculates electric field strength.
        Formula: E = F / q (force per unit charge)
        """
        return force / charge

    @staticmethod
    def electric_field_parallel_plate(voltage, distance):
        """
        Calculates uniform electric field between parallel plates.
        Formula: E = V / d
        """
        return voltage / distance

    # =========================================================================
    # HEAT & THERMODYNAMICS
    # =========================================================================

    @staticmethod
    def heat_sensible(m, c, delta_t):
        """
        Calculates sensible heat (temperature change, no phase change).
        Formula: Q = mcΔT
        """
        return m * c * delta_t

    @staticmethod
    def heat_latent_fusion(m, L_f):
        """
        Calculates latent heat of fusion (melting/freezing).
        Formula: Q = m·L_f
        """
        return m * L_f

    @staticmethod
    def heat_latent_vaporization(m, L_v):
        """
        Calculates latent heat of vaporization (boiling/condensation).
        Formula: Q = m·L_v
        """
        return m * L_v

    @staticmethod
    def thermal_expansion_linear(L0, alpha, delta_t):
        """
        Calculates linear thermal expansion/contraction.
        Formula: ΔL = α·L₀·ΔT
        """
        return alpha * L0 * delta_t

    @staticmethod
    def thermal_expansion_area(A0, beta, delta_t):
        """
        Calculates area thermal expansion/contraction.
        Formula: ΔA = β·A₀·ΔT (for isotropic materials, β ≈ 2α)
        """
        return beta * A0 * delta_t

    @staticmethod
    def thermal_expansion_volume(V0, gamma, delta_t):
        """
        Calculates volume thermal expansion/contraction.
        Formula: ΔV = γ·V₀·ΔT (for isotropic materials, γ ≈ 3α)
        """
        return gamma * V0 * delta_t

    @staticmethod
    def ideal_gas_law_pressure(n, r, t, v):
        """
        Calculates pressure using the ideal gas law.
        Formula: P = nRT / V
        """
        return n * r * t / v

    @staticmethod
    def ideal_gas_law_volume(n, r, t, p):
        """
        Calculates volume using the ideal gas law.
        Formula: V = nRT / P
        """
        return n * r * t / p

    @staticmethod
    def first_law_thermodynamics(q, w):
        """
        Calculates change in internal energy (First Law).
        Formula: ΔU = Q - W (heat added minus work done BY system)
        """
        return q - w

    @staticmethod
    def heat_engine_efficiency(q_h, q_c):
        """
        Calculates the efficiency of a heat engine.
        Formula: η = 1 - (Q_c / Q_h)
        Q_h = heat from hot reservoir, Q_c = heat to cold reservoir.
        """
        return 1 - (q_c / q_h)

    # =========================================================================
    # LIGHT & OPTICS
    # =========================================================================

    @staticmethod
    def wave_speed(frequency, wavelength):
        """
        Calculates wave speed.
        Formula: c = fλ (applies to all waves: sound, light, etc.)
        """
        return frequency * wavelength

    @staticmethod
    def refractive_index(c, v):
        """
        Calculates the refractive index of a medium.
        Formula: n = c / v (ratio of speed in vacuum to speed in medium)
        """
        return c / v

    @staticmethod
    def snells_law_angle2(n1, theta1_deg, n2):
        """
        Calculates refraction angle using Snell's law.
        Formula: θ₂ = arcsin(n₁ sin(θ₁) / n₂)
        Returns angle in degrees.
        """
        theta1_rad = math.radians(theta1_deg)
        sin_theta2 = n1 * math.sin(theta1_rad) / n2
        return math.degrees(math.asin(sin_theta2))

    @staticmethod
    def lens_maker_equation(focal_length, p, q):
        """
        Calculates focal length using the thin lens equation.
        Formula: 1/f = 1/p + 1/q → f = 1/(1/p + 1/q)
        p = object distance, q = image distance.
        """
        return 1 / ((1 / p) + (1 / q))

    @staticmethod
    def magnification(p, q):
        """
        Calculates lateral magnification of a lens.
        Formula: M = -q / p
        Negative M means inverted image, |M|>1 means enlarged.
        """
        return -q / p

    @staticmethod
    def lens_power(focal_length_m):
        """
        Calculates optical power of a lens in diopters.
        Formula: P = 1/f (converging lenses: +, diverging: -)
        """
        return 1 / focal_length_m

    @staticmethod
    def critical_angle(n1, n2):
        """
        Calculates critical angle for total internal reflection.
        Formula: θ_c = arcsin(n₂ / n₁)
        Requires n₁ > n₂. Returns angle in degrees.
        """
        return math.degrees(math.asin(n2 / n1))

    # =========================================================================
    # MODERN PHYSICS - Relativity and Quantum Mechanics
    # =========================================================================

    @staticmethod
    def mass_energy_equivalence(m, c=3e8):
        """
        Calculates rest energy using Einstein's equation.
        Formula: E = mc²
        """
        return m * c ** 2

    @staticmethod
    def photon_energy(frequency, h=6.626e-34):
        """
        Calculates photon energy from frequency.
        Formula: E = hf
        """
        return h * frequency

    @staticmethod
    def photon_energy_wavelength(wavelength, h=6.626e-34, c=3e8):
        """
        Calculates photon energy from wavelength.
        Formula: E = hc / λ
        """
        return h * c / wavelength

    @staticmethod
    def de_broglie_wavelength(m, v, h=6.626e-34):
        """
        Calculates the de Broglie wavelength of a particle.
        Formula: λ = h / (mv)
        All matter exhibits wave-particle duality.
        """
        return h / (m * v)

    @staticmethod
    def lorentz_factor(v, c=3e8):
        """
        Calculates the Lorentz factor for special relativity.
        Formula: γ = 1 / √(1 - v²/c²)
        γ ≥ 1, approaches infinity as v → c.
        """
        return 1 / math.sqrt(1 - (v ** 2 / c ** 2))

    @staticmethod
    def time_dilation(dt0, v, c=3e8):
        """
        Calculates relativistic time dilation.
        Formula: Δt = γ·Δt₀
        Moving clocks run slower (Δt > Δt₀).
        """
        gamma = PhysicsFormulas.lorentz_factor(v, c)
        return gamma * dt0

    @staticmethod
    def length_contraction(L0, v, c=3e8):
        """
        Calculates relativistic length contraction.
        Formula: L = L₀ / γ
        Moving objects appear shorter along direction of motion.
        """
        gamma = PhysicsFormulas.lorentz_factor(v, c)
        return L0 / gamma