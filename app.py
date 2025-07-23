import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

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

# Perform Linear Regression
x = df_exercise['Production Volume (Units)']
y = df_exercise['Total Overhead Costs (£)']

slope, intercept, r_value, p_value, std_err = linregress(x, y)

st.subheader("Regression Analysis Results:")
st.write(f"The calculated linear regression equation is: **Y = {intercept:.2f} + {slope:.2f}X**")
st.write(f"Where Y is Total Overhead Costs and X is Production Volume (Units).")
st.write(f"This means for every unit increase in production, overhead costs increase by £{slope:.2f}.")
st.write(f"The fixed overhead cost (when production is 0) is estimated at £{intercept:.2f}.")

# Prediction for 1400 units
predicted_cost_1400 = intercept + slope * 1400
st.write(f"**Prediction:** Based on this model, for 1,400 units, the estimated total overhead cost would be £{predicted_cost_1400:.2f}.")


# Plotting the regression line
st.subheader("Regression Line Graph:")
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x, y, color='blue', label='Actual Data Points')
ax.plot(x, intercept + slope * x, color='red', label=f'Regression Line: Y = {intercept:.2f} + {slope:.2f}X')
ax.set_xlabel('Production Volume (Units)')
ax.set_ylabel('Total Overhead Costs (£)')
ax.set_title('Production Volume vs. Total Overhead Costs with Regression Line')
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()
st.pyplot(fig) # Display the plot in Streamlit

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
    """
)
st.markdown("---")

# --- Significance of Correlation Section ---
st.header("Significance of Correlation and Its Calculation")
st.write(
    "While linear regression helps us find a relationship, **correlation** tells us about the strength "
    "and direction of that linear relationship."
)

st.subheader("The Correlation Coefficient ($r$)")
st.write(
    "The **Pearson product-moment correlation coefficient ($r$)** measures the strength and direction "
    "of a linear relationship between two variables. Its value always ranges between -1 and +1."
)
st.markdown(
    """
    * **$r = +1$**: Perfect positive linear correlation. As one variable increases, the other increases proportionally.
    * **$r = -1$**: Perfect negative linear correlation. As one variable increases, the other decreases proportionally.
    * **$r = 0$**: No linear correlation. There's no consistent linear relationship between the variables.
    * **Values between -1 and +1**: Indicate varying degrees of positive or negative linear correlation (e.g., +0.8 is strong positive, -0.3 is weak negative).
    """
)
st.write(f"For our exercise, the correlation coefficient (r) is: **{r_value:.4f}**")

st.subheader("How $r$ is Calculated:")
st.write(
    "The formula for the Pearson correlation coefficient is complex, involving the covariance "
    "of the two variables divided by the product of their standard deviations. It can be expressed as:"
)
st.latex(r"""
r = \frac{n(\sum xy) - (\sum x)(\sum y)}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}}
""")
st.write(
    "Where:"
    "\n* $n$: Number of data pairs."
    "\n* $\sum xy$: Sum of the product of each x and y pair."
    "\n* $\sum x$: Sum of all x values."
    "\n* $\sum y$: Sum of all y values."
    "\n* $\sum x^2$: Sum of the squares of each x value."
    "\n* $\sum y^2$: Sum of the squares of each y value."
)
st.write(
    "*(Note: Software like Python's `scipy.stats.linregress` or spreadsheet programs handle this calculation automatically.)*"
)


st.subheader("The Coefficient of Determination ($r^2$)")
st.write(
    "The **coefficient of determination ($r^2$)** is the square of the correlation coefficient ($r^2 = r \times r$). "
    "It is even more significant from a predictive standpoint."
)
st.markdown(
    """
    * **Interpretation:** $r^2$ represents the proportion (or percentage) of the total variation in the dependent variable (y) that can be explained by the independent variable (x) through the linear regression model.
    * For example, if $r^2 = 0.81$, it means that 81% of the variation in the dependent variable can be explained by the variation in the independent variable. The remaining 19% is due to other unmeasured factors or random variation.
    * A higher $r^2$ value (closer to 1) indicates that the regression model is a better fit for the data and provides more reliable predictions.
    """
)
st.write(f"For our exercise, the coefficient of determination (r²) is: **{r_value**2:.4f}**")
st.write(f"This means approximately {r_value**2 * 100:.2f}% of the variation in Total Overhead Costs can be explained by the Production Volume.")


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
