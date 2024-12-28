# Earthquake Analysis Dashboard and Predictive Modeling

## Overview

This project provides a comprehensive analysis of global earthquake data from 1995 to 2023 using interactive visualizations and predictive modeling. The project is divided into two main components:

1. **Earthquake Dashboard**: A web-based interactive dashboard built with Dash and Plotly to visualize global earthquake distributions, identify high-risk zones, and analyze correlations between seismic parameters.
2. **Predictive Modeling**: Python-based scripts for exploratory data analysis (EDA), visualization, and machine learning to predict seismic impact metrics like CDI and MMI.

---

## Features

### **Earthquake Dashboard**
- **Global Map Visualization**: Interactive map showcasing global earthquake distributions with magnitudes, depths, and risk zones.
- **High-Risk Zones**: Highlighting zones prone to both high seismicity and tsunamis.
- **Correlation Analysis**: Heatmap visualization of correlations among seismic attributes like magnitude, depth, and intensity (SIG).

### **Predictive Modeling**
- Exploratory Data Analysis (EDA) using Pandas, Matplotlib, and Seaborn.
- Geospatial visualization using GeoPandas and Cartopy.
- Predictive models for seismic impact metrics (`CDI` and `MMI`) using RandomForestRegressor with hyperparameter tuning via GridSearchCV.

---

## Installation

### **Prerequisites**
- Python 3.8 or higher
- Required libraries:
  - `pandas`
  - `dash`
  - `dash-bootstrap-components`
  - `plotly`
  - `matplotlib`
  - `seaborn`
  - `geopandas`
  - `cartopy`
  - `scikit-learn`

**Usage**
Running the Dashboard
-`python dashboard.py`
Running the Predictive Model
`-python main.ipynb`


