# ClimaGuard
# 🌤️ ClimaGuard: Smart Weather Monitoring & Heat Risk Intelligence for Singapore

### Databricks Smart Business Insights Challenge – Hackathon Submission

---

## 🚀 Overview

**ClimaGuard** is an end-to-end intelligent weather monitoring and alert system built on **Databricks** that provides real-time insights into Singapore’s weather conditions, forecasts heat risks, and delivers smart alerts to safeguard public health and infrastructure.

Leveraging **open government data from [Data.gov.sg](https://data.gov.sg/)** and advanced ML workflows, ClimaGuard empowers both citizens and organizations to make informed decisions based on current and emerging weather patterns.

---

## 📊 Data Sources & Pipeline

We collected and transformed real-time weather data from [Data.gov.sg](https://data.gov.sg/) including:

- 🌡️ **Air Temperature**
- 🌧️ **Rainfall**
- 💧 **Relative Humidity**
- 🧭 **Wind Direction**
- 💨 **Wind Speed**

### 🔧 Ingestion & Transformation

Using the notebook `ClimaGuard/ClimaGuard_Real_Time`, data is fetched from public APIs and ingested into Delta tables under the catalog:


      climaguard.singapore.air_temperature
      climaguard.singapore.rainfall
      climaguard.singapore.relative_humidity
      climaguard.singapore.wind_direction
      climaguard.singapore.wind_speed


Schema and ingestion logic are documented in `ClimaGuard_Catalog`.

---

## 🔁 Data Engineering Pipeline

### ✅ Merge & Feature Engineering

Notebook: `ClimaGuard/ClimaGuard/Merge_Climate_Data`

- Merges all weather datasets into a unified feature table:

      climaguard.singapore.climate_weather_features

- Features used for modeling:
- Rainfall
- Relative Humidity
- Wind Speed
- Wind Direction

---

## 🧠 ML Modeling

A custom regression model is trained using the features above to **predict air temperature**, and a **heat risk classifier** is applied to score each region as:

- 🔵 Low
- 🟡 Medium
- 🔴 High

The prediction results are stored in:

    climaguard.singapore.climate_heat_risk


Model logic and scoring are handled in the same `Merge_Climate_Data` notebook.

---

## 🔄 Orchestration: Databricks Job

A scheduled job `ClimaGuard_Job` automates the entire pipeline daily:

      ClimaGuard_Real_Time → Merge_Climate_Data → Merge_Climate_Data (ML + scoring)



Configuration and job screenshot: `ClimaGuard_Job/ClimaGuard_job.png`

---

## 📈 Dashboard & Visual Insights

We built a rich Databricks SQL Dashboard to deliver Smart Business Insights:

🔗 **Live Dashboard:**  
[Weather Situation in Singapore](https://dbc-2b551927-a689.cloud.databricks.com/dashboardsv3/01f03b11c38815db9359dfce4df4701b/published?o=2048909639413794)

### Key KPIs:

1. **Daily Trending Temperature (Last 10 Days)** – Bar Chart  
2. **Heat Risk Map Across Singapore** – Heat Map  
3. **Wind Speed vs Humidity (%)** – Line Chart  
4. **Weather Reading Table** – Tabular View  
5. **Top 5 Hottest Locations** – Geo Map

---

## 💬 Natural Language Insights with Genie

We integrated **Genie (Databricks AI Assistant)** into the dashboard to help non-technical users interact with the data using natural language.

Genie is configured to fetch insights from both dashboards and Delta tables while respecting data governance controls.

---

## 📱 ClimaGuard App – Real-Time Public Alerts

ClimaGuard isn't just a data platform — it’s a **real-time alerting application** built for **public safety**.

### Core Functions:

- Monitors live **temperature and wind conditions**
- Sends **alerts** when temperature crosses critical thresholds
- Shares **emergency contact numbers and nearby shelter info** with:
  - Schools
  - Offices
  - Public users (via phone)

---

## 🏆 Why ClimaGuard Matters

ClimaGuard addresses urgent climate resilience needs by:

- Enhancing **situational awareness** for extreme heat and wind conditions
- Supporting **data-driven decision making** across sectors
- Empowering citizens with **proactive alerts and safety recommendations**
- Leveraging **Databricks Lakehouse, MLflow, and SQL dashboards** for an end-to-end scalable solution

---

## 👥 Team

**Team Name:** DAI Team  
**Members:**  
- Ankit Kumar  
- Nilesh Mittapelli  

---

## 🔗 References

1. [https://data.gov.sg/](https://data.gov.sg/) – Singapore Government Open Data  
2. [https://api.weatherapi.com](https://api.weatherapi.com) – Supplementary Weather API for Real-Time Conditions

---
## 👥 Team

Built with ❤️ for the **Databricks Smart Business Insights Hackathon**

---






