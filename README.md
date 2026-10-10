# MLB Ticket Price Tracker

A Python and SQL data engineering project designed to collect, store, and analyze MLB ticket prices throughout the 2027 season.

## Project Overview

MLB ticket prices can fluctuate depending on the opponent, day of the week, and proximity to game day. This project aims to build a historical ticket-price dataset to investigate these trends and help identify potentially advantageous times to purchase tickets.

The system combines official MLB schedule data with planned ticket-price observations, using an ETL pipeline and a relational database to support future analysis and visualization.

## Tech Stack

- **Python:** API integration, data transformation, and database ingestion
- **Pandas:** Data cleaning and tabular processing
- **SQLite / SQL:** Relational storage, querying, and data validation
- **Requests:** HTTP requests to the MLB Stats API
- **Git / GitHub:** Version control and project documentation
- **Streamlit (planned):** Interactive analytics dashboard

## Current Progress

### Phase 1 — MLB Schedule ETL Pipeline (Completed)

Implemented an ETL pipeline that:

1. Extracts the 2027 MLB regular-season schedule from the MLB Stats API.
2. Preserves the original API response as JSON.
3. Transforms nested game records into a structured CSV dataset.
4. Validates game identifiers and checks for missing or duplicate records.
5. Loads the processed schedule into a SQLite relational database.
6. Executes SQL queries to verify data completeness and retrieve team schedules.

**Validation results:**

| Metric | Result |
|---|---|
| Regular-season games | 2,430 |
| Unique MLB teams | 30 |
| Duplicate game IDs | 0 |
| Boston Red Sox home games | 81 |

### Phase 2 — Ticket Price Collection (Planned)

- Identify and integrate an accessible ticket-pricing data source.
- Collect timestamped ticket-price observations.
- Store historical price snapshots linked to MLB game IDs.
- Implement duplicate prevention and repeatable ingestion.

### Phase 3 — SQL Analytics (Planned)

- Analyze ticket prices by team and opponent.
- Compare weekday and weekend prices.
- Measure price changes leading up to game day.
- Identify trends in listed ticket prices.

### Phase 4 — Dashboard and Automation (Planned)

- Build an interactive Streamlit dashboard.
- Visualize historical ticket-price trends.
- Automate data collection and validation.
- Add automated tests and CI workflows.

## Data Sources

- **MLB Stats API:** 2027 MLB schedule and game metadata.
- **Ticket pricing:** Source to be determined and validated.

## Project Status

**In development — Schedule ETL pipeline completed.**

The project currently processes MLB schedule data. Ticket-price collection, historical pricing analysis, and dashboard functionality are not yet implemented.
