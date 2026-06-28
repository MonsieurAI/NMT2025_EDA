# NMT 2025 in Figures: Exploratory Data Analysis

An exploratory data analysis (EDA) of the 2025 Ukrainian National Multi-Subject Test (NMT). This project investigates performance disparities, subject correlations, and educational stratification among high school graduates using official open data.

## Overview
The goal of this analysis is to uncover the structural characteristics of the 2025 NMT results. By analyzing the raw testing data, this project explores how geography, educational institution type, and subject selection impact overall student performance.

## Key Insights
*   **The Math Ceiling Effect:** The mathematics exam distribution is highly right-skewed with an unnatural spike at the absolute maximum score (32 points). This indicates a lack of variance required to accurately differentiate between top-tier performers.
*   **Academic Stratification:** Participant performance varies drastically by institution type. Specialized schools and Lyceums significantly outperform vocational schools and pre-higher educational institutions, establishing a clear national baseline.
*   **The Physics/Math Prerequisite:** Joint distribution analysis (hexbin) shows that high mathematical proficiency acts as a prerequisite for success in physics, whereas the reverse is not true.

*(Note: See `notebooks/03_visualizations.ipynb` for the full visual breakdown and correlation matrices).*

## Project Structure
```text
nmt2025/
│
├── data/                   # Raw and processed CSV datasets
├── notebooks/              # Jupyter notebooks for execution
│   ├── 01_data_cleaning.ipynb
│   ├── 02_data_tables.ipynb
│   └── 03_visualizations.ipynb
├── outputs/                # Generated SVG visualizations
├── src/                    # Reusable Python modules
│   ├── __init__.py
│   └── load_data.py
├── .gitignore              
├── Dockerfile              # Container environment configuration
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## Tech Stack
*   **Python 3.11**
*   **Pandas & NumPy:** Data cleaning, manipulation, and binning
*   **Seaborn & Matplotlib:** Statistical data visualization
*   **Docker:** Containerized, reproducible execution environment

## How to Run (via Docker)
To ensure full reproducibility, this project is configured to run inside a Docker container with a volume mount.

**1. Clone the repository:**
```bash
git clone [https://github.com/MonsieurAI/nmt2025.git](https://github.com/MonsieurAI/nmt2025.git)
cd nmt2025
```

**2. Build the Docker image:**
```bash
docker build -t nmt-analysis .
```

**3. Run the container:**
```bash
docker run -p 8888:8888 --name nmt-container -v "${PWD}:/app" nmt-analysis
```

**4. Access the notebooks:** 
Open the provided `http://127.0.0.1:8888/tree` link in your browser to access and run the notebooks.