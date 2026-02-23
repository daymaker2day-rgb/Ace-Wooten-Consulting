#!/usr/bin/env python3
"""
SOVEREIGN QUANTUM SAFETY SYSTEM
Launcher script - Run this to start everything
"""

import os
import sys
import subprocess
import time

def main():
    print("=" * 60)
    print("SOVEREIGN QUANTUM SAFETY SYSTEM")
    print("Launching complete system...")
    print("=" * 60)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        sys.exit(1)
    
    # Install dependencies if needed
    print("\n📦 Checking dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except:
        print("⚠️  Could not install dependencies automatically")
        print("   Run: pip install -r requirements.txt")
    
    # Run the system
    print("\n🚀 Starting system...")
    import importlib.util
    spec = importlib.util.spec_from_file_location("sovereign_quantum_system", "sovereign_quantum_system.py")
    sq_system = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sq_system)
    
    # Run demo
    bridge = sq_system.run_demo()
    
    # Start server
    if sq_system.HAS_FLASK:
        print("\n🌐 Starting Flask server...")
        print("   Listening on http://localhost:5000")
        print("   Press Ctrl+C to stop\n")
        sq_system.app.run(host='0.0.0.0', port=5000, debug=False)
    else:
        print("\n❌ Flask not installed - cannot start server")
        print("   Install with: pip install flask flask-cors")
        sys.exit(1)

if __name__ == "__main__":
    main()