import streamlit as st
import pandas as pd
import numpy as np

# --- Page Configuration ---
st.set_page_config(
    page_title="ACCA Regression & Accounting Uses",
    layout="centered", # Can be "wide" or "centered"
    initial_sidebar_state="collapsed" # Can be "auto", "expanded", "collapsed"
)

# --- Title and Introduction ---
st.title("Understanding Linear Regression in Accounting")
st.markdown("---")
st.write(
    "This application explores the concept of linear regression, a powerful statistical tool "
    "for understanding relationships between variables, particularly useful in various "
    "accounting and financial contexts. It draws inspiration from ACCA's technical articles on the subject."
)

# --- ACCA Exercise Section ---
st.header("ACCA-Inspired Exercise: Cost Estimation")
st.write(
    "Imagine a manufacturing company wants to understand the relationship between its production "
    "volume and total production overhead costs. They've collected the following data for the past 6 months:"
)

# Sample Data for the exercise
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Production Volume (Units)': [1000, 1200, 900, 1500, 1100, 1300],
    'Total Overhead Costs (£)': [25000, 28000, 23000, 32000, 26000, 29000]
}
df_exercise = pd.DataFrame(data)
st.dataframe(df_exercise)

st.write(
    "**Exercise Question:** "
    "Using the principles of linear regression ($y = a + bx$), how would you estimate the "
    "total overhead costs if the company plans to produce 1,400 units next month?"
)
st.markdown(
    """
    * Identify the dependent (y) and independent (x) variables.
    * Recall the formulas for calculating 'a' (y-intercept) and 'b' (slope).
    * (You don't need to perform the calculation in this app, but consider the steps involved!)
    """
)

st.markdown("---")

# --- Further Explanation of Linear Regression ---
st.header("Further Explanation of Linear Regression")
st.write(
    "Linear regression is a statistical method used to model the relationship between a dependent "
    "variable and one or more independent variables by fitting a linear equation to observed data."
)

st.subheader("The Linear Regression Equation:")
st.latex(r"y = a + bx")
st.write(
    "Where:"
    "\n* **y:** The dependent variable (the variable you are trying to predict or explain)."
    "\n* **x:** The independent variable (the variable used to predict or explain y)."
    "\n* **a (or $b_0$):** The Y-intercept. This is the value of y when x is 0. In accounting, it often represents fixed costs."
    "\n* **b (or $b_1$):** The slope of the regression line. It represents the change in y for every one-unit change in x. In accounting, this often relates to variable costs per unit."
)

st.subheader("Key Concepts:")
st.markdown(
    """
    * **Purpose:** To predict future values of the dependent variable or to understand the strength and direction of the relationship between variables.
    * **Assumptions:** For reliable results, linear regression assumes a linear relationship, independence of observations, homoscedasticity (constant variance of residuals), and normally distributed residuals.
    * **Coefficient of Determination ($r^2$):** Often displayed alongside regression results, $r^2$ indicates the proportion of the variance in the dependent variable that can be predicted from the independent variable(s). A higher $r^2$ suggests a better fit of the model to the data.
    """
)
st.markdown("---")

# --- List of Uses Section ---
st.header("Top 10 Uses of Regression & Correlation in Accounting")
st.markdown(
    """
    Here's how regression and correlation analysis can be applied in an accounting context:

    1.  **Cost Behavior Analysis:** To understand and predict how different types of costs (e.g., variable, fixed, semi-variable) behave in relation to changes in activity levels (e.g., production units, sales volume). This is crucial for budgeting and cost control.
    2.  **Budgeting and Forecasting:** Developing more accurate budgets and financial forecasts by identifying the relationship between key financial variables (e.g., sales revenue and advertising spend, or production volume and direct materials cost).
    3.  **Variance Analysis:** Investigating the causes of variances by correlating operational factors (e.g., machine hours, labor efficiency) with cost deviations to pinpoint areas for improvement.
    4.  **Sales Forecasting:** Predicting future sales volumes and revenues based on historical data and correlated factors like marketing expenditure, economic indicators, or seasonal trends.
    5.  **Overhead Absorption Rate Calculation:** Establishing a more accurate basis for absorbing overheads by analyzing the relationship between overhead costs and relevant cost drivers (e.g., direct labor hours, machine hours).
    6.  **Break-Even Analysis:** Enhancing break-even calculations by using regression to better estimate fixed and variable cost components from mixed costs.
    7.  **Performance Evaluation:** Assessing the relationship between management actions (independent variables) and financial outcomes (dependent variables) to evaluate the effectiveness of strategies or operational changes.
    8.  **Pricing Decisions:** Analyzing the correlation between price changes and sales volume (price elasticity of demand) to inform optimal pricing strategies.
    9.  **Working Capital Management:** Forecasting working capital needs by understanding the relationship between sales levels and components like accounts receivable, inventory, and accounts payable.
    10. **Fraud Detection and Risk Assessment:** Identifying unusual patterns or anomalies in financial data by looking for deviations from expected correlations between different accounts or transactions, potentially signaling fraudulent activities or areas of higher financial risk.
    """
)
