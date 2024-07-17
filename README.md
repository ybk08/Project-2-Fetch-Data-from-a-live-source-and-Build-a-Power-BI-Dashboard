# Project-2-Fetch-Data-from-a-live-source-and-Build-a-Power-BI-Dashboard

## Project Overview
This project focuses on analyzing Walmart sales data, including data fetching, processing, and visualization. The primary goal is to provide insights into sales trends and performance across different stores and departments using Power BI.

## Technologies Used

* Python (Pandas)
* Power BI (Power Query, Data Visualization)

## Tasks Performed

* The data was fetched from a CSV file hosted on GitHub. The data was read directly into a Pandas DataFrame using Python.
* Handling Missing Values: The dataset was checked for missing values and handled appropriately.
* Remove Unnecessary Columns: Unnecessary columns were removed using Power Query in Power BI to streamline the data for visualization.

## Visualizations and Insights

### Key Metrics Overview
**Cards:** Display key metrics such as Total Sales, Total Profit, Total Quantity, and Total Customers.

### State-Level Analysis
**State Slicer:** Allows filtering of sales data by state, enabling detailed regional analysis.

### Profit Trends
**Line Chart:** Illustrates profit trends over time, highlighting seasonal patterns and trends.

### Category Profit Analysis
**Donut Chart:** Shows the distribution of profit across different categories (Furniture, Technology, and Office Supplies).

### Sales Distribution
**Map:** Displays sales distribution across states and segments (Consumer, Corporate, and Home Office).

### Segment Profit Analysis
**Pie Chart:** Illustrates profit distribution by segment, offering insights into the most profitable customer segments.

### Sub-Category Profit Insights
**Stacked Bar Chart:** Provides a detailed view of profit by sub-category.

### Detailed Sales Data
**Matrix:** Displays sales data by sub-category and segment in a grid format similar to an Excel pivot table.

## File Structure

`census_2011.xlsx`: Contains the raw data.

`census.py`: Contains the complete code for the project, organized into sections for data pipeline and analysis.

`Telangana.txt`: Contains districts after the formation of Telangana from Andhra Pradesh. 

`db_credentials.txt`: Contains Database username and password.

## Contact Information

For questions or support, please contact yashkoli995@gmail.com.
