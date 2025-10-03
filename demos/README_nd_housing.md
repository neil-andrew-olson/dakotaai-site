# Dakota AI North Dakota Real Estate Analytics Demo

## Overview
Interactive R Shiny dashboard showcasing comprehensive housing market analysis for North Dakota, with a focus on Fargo-Moorhead metro area. This demo demonstrates Dakota AI's capabilities in real estate data processing, visualization, and analytics.

## Features
- **Interactive Dashboard**: Professional Shiny interface with multiple analysis views
- **Fargo-Moorhead Focus**: Defaults to local market analysis (customizable to all ND)
- **Multiple Visualizations**: Time series trends, growth comparisons, summary statistics
- **Data Explorer**: Filterable table for in-depth data examination

## Data Sources
- Zillow Housing Value Index (ZHVI) data
- Neighborhood-level data for Fargo-Moorhead regions
- Statewide North Dakota data
- Time period: 2000-2025 (monthly granularity)

## Requirements
- R version 4.0 or higher
- Required R packages will be auto-installed:
  - shiny, shinydashboard (UI framework)
  - plotly (interactive charts)
  - DT (data tables)
  - dplyr, tidyr (data manipulation)
  - lubridate (date handling)
  - ggplot2, scales (visualization)
  - stringr (string processing)

## Installation & Setup

1. **Prerequisites**: Ensure you have R and RStudio installed

2. **File Location**: This demo expects the `Housingdata/` folder to be in the same directory as the R script

3. **Data Requirements**: Place the downloaded Zillow CSV files in the `Housingdata/` folder:
   - `Neighborhood_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv`
   - `State_zhvi_uc_sfr_tier_0.33_0.67_sm_sa_month.csv`

## Running the Demo

### Option 1: RStudio Integrated Run
1. Open `nd_housing_analytics.R` in RStudio
2. Click the "Run App" button in the top-right of the script pane
3. The Shiny app will open in your default web browser

### Option 2: Command Line
```r
# From R console:
shiny::runApp('nd_housing_analytics.R')
```

### Option 3: Source and Run
```r
# From R console:
source('nd_housing_analytics.R')
```

## Usage Guide

### Dashboard Tabs

1. **Overview**
   - Summary statistics for selected geography
   - Annual price trends by location type
   - Key metrics: total regions, average prices, growth rates

2. **Housing Trends**
   - Detailed time series charts for selected regions
   - Price progression over time with hover details
   - Statistical summary table below the chart

3. **Comparisons**
   - Normalized growth index comparison (set to 100 at start)
   - Performance comparison across different neighborhoods
   - Easy identification of outperforming markets

4. **Data Explorer**
   - Complete raw dataset with filtering capabilities
   - Sort by any column, search for specific regions
   - Export and pagination options

### Controls & Filters

- **Geography Filter**: Fargo-Moorhead Metro (default), All ND, or Custom selection
- **Date Range**: Select any time period from 2000-present
- **Custom Region Selection**: Choose specific neighborhoods or cities
- **Interactive Charts**: Hover for details, zoom, pan

## Sample Insights

When using the Fargo-Moorhead default settings, the demo reveals:
- Local market growth trends over the last 10 years
- Neighborhood-specific performance (e.g., University areas vs. suburban)
- Price volatility and stability patterns
- Comparative analysis across different property types

## Technical Details

- **Data Processing**: Converts wide-format time series to long format for analysis
- **Performance**: Handles ~100MB+ datasets with efficient filtering
- **Error Handling**: Graceful error messages if data files are missing
- **Responsive Design**: Works on desktop and tablet browsers

## Customization

To modify the demo:
- Change the `default_regions` variable for different startup defaults
- Add more statistical calculations in the server functions
- Incorporate additional chart types (e.g., heatmaps, correlations)
- Add forecasting capabilities using `forecast` package

## Dakota AI Value Proposition

This demo showcases:
- ✨ **Data Processing**: Large-scale real estate data handling
- 📊 **Analytics**: Time-series analysis and comparative studies
- 🎯 **Business Intelligence**: Actionable housing market insights
- 💡 **Custom Solutions**: Tailored analysis for local markets

## Support

For questions or customization requests, contact Dakota AI for consulting services in data analytics and real estate market analysis.

---

*Built with R Shiny • Powered by Dakota AI's expertise in real estate analytics*
