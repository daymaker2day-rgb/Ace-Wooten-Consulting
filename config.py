"""
SOVEREIGN QUANTUM SAFETY SYSTEM
Configuration file - Set your API keys here
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Master configuration for the entire system"""
    
    # ===== SYSTEM INFO =====
    SYSTEM_NAME = "ZER01NE 67"
    VERSION = "2.0"
    ZER01NE_POINTS = 47
    SAFETY_POINTS = 20
    TOTAL_POINTS = 67
    
    # ===== GENESIS CONSTANTS (from 47-point matrix) =====
    GENESIS_TIMESTAMP = "2026-02-20T23:52:44Z"
    GRID_MAP_TIMESTAMP = "2026-02-20T23:56:18Z"
    GLOBAL_GENESIS_TIMESTAMP = "2026-02-20T23:59:59Z"
    HARDWARE_ID = "4C4C4544-0048-4210-8053-B4C04F354D33"
    
    # Revenue
    BOT_TOLL = 0.50       # EGVT per bot interaction
    HUMAN_HANDSHAKE = 0.05  # EGVT per human handshake
    
    # ===== YOUR 20-LOGIC CONSTANTS =====
    SAFETY_THRESHOLD = 0.999  # 99.9% certainty before alert
    POOL_ALARM_RADIUS_M = 30.0
    WATER_SURFACE_TEMP_DELTA = 2.0
    
    # ===== API KEYS (set in .env file) =====
    NASA_API_KEY = os.getenv('NASA_API_KEY', 'DEMO_KEY')
    NOAA_TOKEN = os.getenv('NOAA_TOKEN', None)
    NOAA_API_URL = os.getenv('NOAA_API_URL', 'https://www.ncdc.noaa.gov/cdo-web/api/v2')
    USGS_TOKEN = os.getenv('USGS_TOKEN', None)
    USGS_API_URL = os.getenv('USGS_API_URL', 'https://waterservices.usgs.gov/nwis/qw')
    
    # AZ Government Registries (real portals, not APIs)
    AZ_REGISTRY_PORTAL = os.getenv('AZ_REGISTRY_PORTAL', 'https://dcs.az.gov/public-records')
    AZ_FINGERPRINT_PORTAL = os.getenv('AZ_FINGERPRINT_PORTAL', 'https://dps.az.gov/services/fingerprint-clearance')
    AZ_OLR_PORTAL = os.getenv('AZ_OLR_PORTAL', 'https://olr.az.gov/licensing-lookup')
    
    # Webhooks for insurance partners (no public APIs available)
    STATE_FARM_WEBHOOK = os.getenv('STATE_FARM_WEBHOOK', 'https://YOUR_DOMAIN/webhooks/state-farm')
    ALLSTATE_WEBHOOK = os.getenv('ALLSTATE_WEBHOOK', 'https://YOUR_DOMAIN/webhooks/allstate')
    
    # ===== SERVER CONFIG =====
    PORT = int(os.getenv('PORT', 5000))
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    HOST = os.getenv('HOST', '0.0.0.0')
    
    # ===== SECURITY =====
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-in-production')
    ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', None)
    JWT_SECRET = os.getenv('JWT_SECRET', 'change-this-in-production')
    
    # ===== DATABASE =====
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
    REDIS_DB = int(os.getenv('REDIS_DB', 0))
    
    # ===== EARTH CONSTANTS =====
    EARTH_RADIUS_M = 6371000.0
    EARTH_RADIUS_KM = 6371.0
    SPEED_OF_LIGHT = 299792458.0
    STANDARD_GRAVITY = 9.80665
    SEA_LEVEL_PRESSURE = 1013.25
    EARTH_OMEGA = 7.292115e-5  # rad/s
    G_CONSTANT = 6.67430e-11
    EARTH_MASS = 5.9722e24
    ROYAL_CUBIT = 0.5236  # meters
    SOVEREIGN_DEPTH = 1.0472  # meters (2 × royal cubit)
    MAX_LEGAL_DEPTH_M = 1.5
    
    # Euler pole for North America
    EPP_NORTH_AMERICA = {
        "lat": 48.7,
        "lon": -104.0,
        "rate_rad_yr": 0.00000021,
    }
    
    THERMAL_COEFFICIENTS = {
        "concrete": 12e-6,
        "steel": 17e-6,
        "aluminum": 23e-6,
        "copper": 16.5e-6,
        "glass": 8.5e-6,
        "wood": 5e-6,
    }
    
    # ===== PHYSICS CONSTANTS (47-Point Matrix) =====
    BOLTZMANN_K = 1.380649e-23  # J/K
    PLANCK_H = 6.62607015e-34  # J·s
    VACUUM_PERMITTIVITY = 8.854187817e-12  # F/m
    VACUUM_PERMEABILITY = 1.2566370614e-6  # H/m
    WATER_REFRACTIVE_INDEX = 1.33
    AIR_REFRACTIVE_INDEX = 1.000293
    SOIL_CONDUCTIVITY_AVG = 0.01  # S/m
    RHO_WATER = 1000.0  # kg/m³
    RHO_CRUST = 2700.0  # kg/m³
    SHEAR_MODULUS_CRUST = 30e9  # Pa
    
    # ===== RF CONSTANTS (900 MHz) =====
    FREQ_900MHZ = 900e6  # Hz
    WAVELENGTH_900MHZ = 299792458.0 / FREQ_900MHZ  # ~0.333 m
    POOL_ALARM_RADIUS_M = 4828.0  # 3 miles in meters
    POOL_THERMAL_DELTA_C = 2.0  # °C difference for pool detection
    
    # ===== AVIATION & SPATIAL =====
    FAA_UNCONTROLLED_CEILING_M = 121.92  # 400 ft in meters
    EYE_LEVEL_M = 1.676  # 5.5 ft average standing height
    
    # ===== LUNAR & SOLAR =====
    SYNODIC_MONTH = 29.530589  # days (phase cycle)
    LUNAR_PERIOD_DAYS = 27.321661  # sidereal month
    
    # ===== REVENUE (Wooten Consulting EIN 12-271978) =====
    ISSUER_EIN = "12-271978"
    OPS_RECV_HUMAN = 0.05  # USD per human session
    OPS_RECV_BOT = 1.50  # USD per bot/API call
    OPS_RECV_QUANTUM = 10.00  # USD per quantum-tier call