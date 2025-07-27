# TransBorderFreight_Data_Analysis

This project aims to answer some business questions for a multinational logistics and supply chain company operating across North America (U.S., Canada, and Mexico) through the use of data visualization. It includes data engineering; data wrangling, data visualization; documentation and actionable insights for all stakeholders.

## Business Problem Statement

<b><i>How can our logistics company leverage detailed trade data on transportation modes, freight costs, commodity values, and regional trade flows to optimize network efficiency, improve pricing strategies, and target high-growth markets across North America?</i></b>

## Business Questions

1. Which transportation modes are most frequently used for freight movement, and how has this changed over time?

2. What is the relationship between the Value of Goods, Freight Charges, and Ship Weight for both exported and imported Goods?

3. Which Exported and Imported Goods have the highest Total Value?

4. How have the Total Annual Freight Charges for Exports and Imports changed over time?

5. How has the Total Annual Value of Goods for Exports and Imports changed over time?

6. How does the Total Annual Value of Exported and Imported Goods compare with each province/state in the peak year 2022?

7. What is the Trade Volume of Exports and Imports between all the US States and Mexico/Canada?


## Dataset Description

This dataset supports comprehensive analysis of cross-border trade patterns—particularly between the U.S., Mexico, and Canada—by value, weight, transport method, location, time, and commodity type.

`TRDTYPE` : Trade Type Code (1-Exports, 2-Imports) (numeric)

`USASTATE` : U.S. State Code (categorical)

`DEPE` Port/District Code (categorical): 

`DISAGMOT` : Mode of Transportation Code (categorical)

`MEXSTATE` : Mexican State Code (categorical)

`CANPROV` : Canadian Province Code (categorical)

`COUNTRY` : Country Code 

`VALUE` : Value of Goods ($) (numeric)

`SHIPWT` : Shipping Weight (kg) (numeric)

`FREIGHT_CHARGES` : Freight Charges ($) (numeric)

`DF` : Domestic/Foreign Code (categorical)

`CONTCODE` : Container Code (categorical)

`MONTH` : Month of Freight  (categorical)

`YEAR` : Year of Freight (categorical)

`COMMODITY2` : Commodity Classification Code (categorical)


<b>Available datasets:</b>

combined_data.csv: (obtained by following the steps in the getting started section)

<b>Link</b>: https://azubiafrica-my.sharepoint.com/personal/emmanuel_agyen_azubiafrica_org/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Femmanuel%5Fagyen%5Fazubiafrica%5Forg%2FDocuments%2FTMP%2Fdata%2Ezip&parent=%2Fpersonal%2Femmanuel%5Fagyen%5Fazubiafrica%5Forg%2FDocuments%2FTMP&ga=1


###  Dataset Preview

| TRDTYPE | USASTATE | DP | DISAGMOT | MEXSTATE | CANPROV | COUNTRY | VALUE | SHIPWT | FREIGHT_CHARGES | DF | CONTCODE | MONTH | YEAR | COMMODITY2 |
| :-------| :--------| :-------| :--------| :-------| :--------| :-------| :--------| :-------| :--------| :-------| :--------| :-------| :--------| :--------|
| 1.0 | AK | 07XX | 3.0 | NaN | XA | 1220.0 | 3302.0 | 378.0 | 125.0 | 1.0 | X | 1.0| 2020.0 | NaN | 
| 1.0 | AK | 20XX | 3.0 | NaN | XA | 1220.0 | 133362.0 | 137.0 | 1563.0 | 1.0 | X | 1.0| 2020.0 | NaN | 
| 1.0 | AK | 20XX | 3.0 | NaN | XA | 1220.0 | 49960.0 | 66.0 | 2631.0 | 2.0 | X | 1.0| 2020.0 | NaN | 


### Report

<b>Link</b>: https://docs.google.com/document/d/1yDkwOwi_v78rCYLmJMtw3I3owRPqjcnrrw03gr_1quA/edit?usp=sharing

### Slide Deck

<b>Link</b>: https://docs.google.com/presentation/d/1BWXuYa3HvlIqdAXSgqcKUMXeAK54MSQO2DHd85itybk/edit?usp=sharing

## Approach and Methodology

### Dataset Engineering Pipeline

The dataset was provided as a ZIP file containing multiple CSV and Excel files with consistent structure. To process this efficiently, a Python-based data pipeline was built with the following steps:

1. Extract all nested zip files
2. Collect all data files into one folder
3. Combine them into a single unified CSV file 

Useful for handling complex, multi-layered datasets commonly received from external sources.

### Dataset Cleaning and Processing 

After combining, the data was cleaned and preprocessed:

* Removed unnecessary columns

* Verified and standardized key fields like Trade Type and Month

* Ensured data types were consistent (using `pandas` and `numpy`)

### Dataset Visualization

Finally, visualizations were created using `matplotlib` and `seaborn` to explore trends over time and relationships in the data. Charts included line plots, bar charts, area charts, and correlation heatmaps.

This streamlined pipeline ensures the data is clean, consistent, and ready for analysis.

---

## Project Key Findings

<b>Dominant Transportation Mode:</b> Truck is the primary mode for both exports and imports, but its usage is declining. Explore alternative modes like rail.

<b>High-Value Commodities:</b> Mineral fuels and oils are the most valuable imports, requiring optimized logistics.

<b>Regional Focus (Canada):</b> Prioritize Ontario, Quebec, and Alberta for exports; Ontario, Quebec, and British Columbia for imports.

<b>Regional Focus (Mexico):</b> Focus on Mexico City, Nuevo León, and Chihuahua for exports.

<b>U.S. State Contributions (To Canada):</b> California, Texas, and Illinois are key exporters.

<b>U.S. State Contributions (To Mexico):</b> Texas, California, and Illinois lead in imports.

<b>Declining Trends:</b> Investigate the decline in total freight volume and how that relates to the decline in freight charges and total trade values post-2022 to stabilize future growth.

---

### Folder Structure (After Setup)

project/

├── .gitignore

├── LICENSE

├── requirements.txt ← Required Packages

├── data.zip ← Input: main compressed dataset

├── extracted/ ← Temp: all contents extracted here

├── csv_files/ ← Output: collected CSV/Excel files

├── combined_data.csv ← Final output: merged dataset

├── extract_zips.py ← Step 1: Unpack nested zips

├── move_excel_files.py ← Step 2: Gather data files

├── combine_csv_files.py ← Step 3: Merge into one file

├── main.ipynb ← Data Notebook

└── README.md

## Getting Started:

### How to Run: Step-by-Step

#### Step 1: Clone this Remote Repository

```bash
`git clone https://github.com/02sagoe/TransBorderFreight_Data_Analysis `
```

#### Step 2: Change the Working Directory

```bash
`cd `TransBorderFreight_Data_Analysis`
```

#### Step 3: Ensure `data.zip` File is Downloaded into this Directory (IMPORTANT)


#### Step 4: Create a New Virtual Environment

```bash
virtualenv venv
```

#### Step 5: Activate your Virtual Environment

```bash
venv\scripts\activate
```

#### Step 6: Install the Required Packages using

```bash
pip install -r requirements.txt
```

#### Step 7: Extract All Nested ZIP Files

Run the extraction script to unpack `data.zip` and any inner `.zip` files recursively.

```bash
python extract_zips.py
```

Creates an extracted/ directory with full unpacked structure. 
Handles multiple levels of nesting.

#### Step 8: Move All CSV Files into one folder

Run the directory moving script to move all `.csv` and any inner `.csv` files recursively.

```bash
python move_excel_files.py
```

Creates a driectory and stores all CSV files in there 
Handles multiple levels of nesting.

#### Step 9: Concatenates all CSV Files into one huge CSV File

Run the concatenation script to combine all `.csv` into one final `.csv` files recursively.

```bash
python combine_csv_files.py
```

Creates a CSV file by combining all the other CSV files together

#### Step 10: Open Notebook File and Interact with Cells in Order

* Use this notebook: python `main.ipynb`


### Questions?

If you have any questions about the implementation, want to improve the model, or need help deploying it, feel free to reach out!

Email: kbwsagoe@gmail.com

LinkedIn: https://www.linkedin.com/in/kbsagoe/