# Ace Wooten Consulting – ZER01NE 67 Project

This repository contains two distinct parts:

- **`backend/`**: private logic and Flask API. This directory should be treated like a separate project and can be kept private or deployed to a secure platform. It is *not* served by GitHub Pages.
- **`docs/`**: static dashboard and marketing site. GitHub Pages publishes the contents of this folder at `https://daymaker2day-rgb.github.io/Ace-Wooten-Consulting/`.

## Workflow

- Develop backend code under `backend/`; run it locally with `python backend/run.py`.
- The frontend in `docs/` calls the backend via HTTP. When you update the frontend, commit and push; GitHub Actions will automatically build and deploy the site.

## Privacy and Deployment

Only the files under `docs/` are visible on the Pages site. All logic, API routes, environment variables, and secrets live in the backend, which you can choose not to publish publicly. For production you can deploy the backend to a service such as:

- **Supabase (Edge Functions)**
- **Vercel (Serverless Functions)**
- **Heroku, AWS, Azure, DigitalOcean, etc.**

This separation keeps your Stripe keys and other sensitive code hidden while still allowing the UI to remain public.
