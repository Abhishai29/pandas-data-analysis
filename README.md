# Pandas Data Analysis Practice

This repository contains scripts demonstrating foundational data manipulation and exploratory data analysis (EDA) using Python. It includes practice with basic Pandas operations and a visual analysis of the classic Titanic dataset.

## Features and Topics Covered
### Data Manipulation (analysis.py):
- Creating and modifying Series and Dataframes.
- Data selection and filtering using .loc and conditional logic.
- Data aggregation and grouping (groupby, mean, max, min).

### Exploratory Data Analysis (data_real_cvs.py):
- Loading real-world datasets (Titanic).
- Inspecting data structures (.head(), .info(), .describe()).
- Handling categorical data and generating value counts.

### Data Visualization:

- Pie charts for demographic distribution.
- Bar charts (sns.countplot) for survival rates by class and gender.
- Histograms for age distributions.
- Boxplots to analyze age variations across passenger classes.

<br>
<br>
  <p align="center">
  <img width="48%" alt="Figure_1" src="https://github.com/user-attachments/assets/014e604b-b666-4f97-b17f-cc0abe6a7860" />
    &nbsp; &nbsp;
  <img width="48%" alt="Figure_2" src="https://github.com/user-attachments/assets/1877736f-31d7-4dfd-993a-0bcdc9208f3a" />
  </p>
<br>


## Tech Stack Used

- Python
- Pandas (Data manipulation)
- Seaborn (Advanced visualization)
- Matplotlib (Base plotting)

## Prerequisites and Installation

To run these scripts, you will need Python installed along with the required libraries. You can install them using pip:

- pip install pandas seaborn matplotlib

## How to Run

To execute the basic Pandas analysis:
- python analysis.py

To run the Titanic dataset EDA and generate the visualizations:
- python data_real_cvs.py
  
(Note: When running data_real_cvs.py, close each plot window to generate the next one.)
