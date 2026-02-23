# Backend (Private Logic)

This directory contains the server-side code for the Sovereign Quantum Safety System. The frontend shown on GitHub Pages (`/docs/index.html`) is purely static and does **not** include any of the logic or secrets contained here.

## Structure

- `run.py` &ndash; launcher script; installs dependencies and starts the Flask app.
- `sovereign_quantum_system.py` &ndash; core system logic and Flask routes.
- `config.py` &ndash; configuration values, constants, and environment variable helpers.
- `env.txt` &ndash; example environment variable definitions (copy to `.env` or set in your deployment environment).
- `requirements.txt` &ndash; Python dependencies for the backend.
- `test_endpoints.bat` &ndash; Windows script for exercising the API locally.

## Local testing

1. **Create a virtual environment** (optional but recommended):
   ```powershell
   cd backend
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up configuration**. Copy `env.txt` to `.env` and edit as needed, or export the variables directly:
   ```bash
   cp env.txt .env
   # then edit .env with your real values
   ```

4. **Run the system**:
   ```bash
   python run.py
   ```
   The server will listen on `http://localhost:5000`.

5. **Use the dashboard or test scripts** to exercise endpoints. The frontend (in `../docs`) can call the local server.

## Deployment hints

Later you can deploy this backend to any hosting platform (Heroku, Vercel, Supabase Functions, AWS, etc.). Only the frontend files from `../docs` need to be published to GitHub Pages; keep this backend repository private or on a separate project to hide your logic and secrets.

For Stripe or other third‑party services, keep the secret keys in environment variables and never commit them to Git.
