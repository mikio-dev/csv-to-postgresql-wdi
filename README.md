# 🌍 CSV to PostgreSQL: World Bank WDI Project

This project automates the ingestion of **World Bank's World Development Indicators (WDI)** data into a PostgreSQL database, then visualises population trends in a Streamlit dashboard.

- 🔄 Scheduled ETL pipeline using GitHub Actions
- 📥 Ingests CSV data from [GitHub (datasets/population)](https://github.com/datasets/population)
- 🗄 Loads into PostgreSQL (e.g., Supabase, Render, Neon)
- 📊 Visualised with [Streamlit](https://streamlit.io/)
- ☁️ Fully free stack, suitable for public portfolio projects

✅ Technologies Used

- Python 3.12
- Pandas
- SQLAlchemy
- Streamlit
- GitHub Actions
- PostgreSQL (Supabase-compatible)

## 🔍 Data Source

We use a simplified subset of the WDI dataset:

- 📥 **Source**: [`datasets/population`](https://github.com/datasets/population)
- 📄 Format: CSV
- 📈 Fields: `Country Name`, `Country Code`, `Year`, `Value` (Population estimate)
- 🕒 Frequency: Annual

---

## ⚙️ Project Architecture

```mermaid
graph TD
    A["Scheduled Trigger (GitHub Actions)"] --> B["ETL Script (Python)"]
    C["Source CSV (GitHub)"] --> B
    B --> D[Transform with Pandas]
    D --> E["PostgreSQL (Cloud DB)"]
    E --> F[Streamlit App]
```

## Setup Guide

1. Clone the Repository

   ```
   git clone https://github.com/mikio-dev/csv-to-postgresql-wdi.git
   cd csv-to-postgresql-wdi
   ```

2. Provision the PostgreSQL Database

   Use a free PostgreSQL provider, for example:

   - [Supabase](https://supabase.io/)
   - [Render PostgreSQL](https://render.com/docs/databases)
   - [Neon](https://neon.com/)

   Create a new database and copy the connection string:

   ```
   postgresql://USER:PASSWORD@HOST:PORT/DB_NAME
   ```

3. Add GitHub Secret

   Go to GitHub → Settings → Secrets → Actions → New Repository Secret

   - Name: DATABASE_URL
   - Value: postgresql://...

4. Set Up GitHub Actions

   - The pipeline is pre-configured to run daily at 2am UTC
   - You can trigger it manually via GitHub → Actions → Run workflow

5. Deploy Streamlit App (Free)

   Option A: Streamlit Community Cloud

   1. Go to [streamlit.io/cloud](streamlit.io/cloud)
   2. Click “New app”
   3. Connect your GitHub repo
   4. Select:

   - Branch: main
   - App file: streamlit_app/app.py

   5. Add a secrets.toml via Streamlit UI:

   ```
   DATABASE_URL = "postgresql://USER:PASSWORD@HOST:PORT/DB"
   ```

   Option B: Run Locally

   ```
   pip install -r requirements.txt
   streamlit run streamlit_app/app.py
   ```

📊 Example Dashboard

A sample dashboard on Streamlit Community Cloud can be accessed here:
https://wqu3efnkrlqes9wfgmqefc.streamlit.app/

![Dashboard screenshot](./images/dashboard_screenshot.png)

It lets users:

- Choose a country
- View population trends over time
