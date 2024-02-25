#%%

"""""
**IMPORTING DATA INTO COLAB ENVIRONMENT**
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib


# Function to replace Google Colab's drive.mount and direct file access
def download_data(url):
    return pd.read_csv(url)

# Adjustment for data loading
data_urls = {
    "1980_30_39_all_data": "https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/main/1980_30_39_all_data.csv",
    "1980_40_49_base_data": "https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/main/1980_40_49_base_data.csv",
    "1980_40_49_extra_data": "https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/main/1980_40_49_extra_data.csv",
    "1980_50_59_base_data": "https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/main/1980_50_59_base_data.csv"
}

# Downloading data
datasets = {name: download_data(url) for name, url in data_urls.items()}

# Adjusted analysis example 
df = datasets["1980_30_39_all_data"]
#%%
"""## **SECTION I: SEASON OF BIRTH, COMPULSORY SCHOOLING, AND YEARS OF EDUCATION**

**REPLICATING FIGURE I: YEARS OF EDUCATION AND SEASON OF BIRTH 1980 CENSUS YEARS 1930-1939**
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
url = 'https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/cb1cddf3b7ed8b127357f5aea2caf64b97b5ef7b/1980_30_39_all_data.csv'
df = pd.read_csv(url)

# Calculate the average years of education for each birth quarter of each year
grouped = df.groupby(['BIRTHYR', 'BIRTHQTR'])['YRSED'].mean().reset_index()

# Creating a continuous index to represent each unique (year, quarter) combination
grouped['YearQuarterIndex'] = grouped['BIRTHYR'] + (grouped['BIRTHQTR'] - 1) / 4

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(grouped['YearQuarterIndex'], grouped['YRSED'], '-o', label='Average Years of Education')

# Annotating each point with the quarter of birth, ensuring no decimals are included
for idx, row in grouped.iterrows():
    quarter_annotation = f'Q{int(row["BIRTHQTR"])}'  # Convert to integer to remove decimal
    plt.annotate(quarter_annotation, (row['YearQuarterIndex'], row['YRSED']), textcoords="offset points", xytext=(0,5), ha='center')

plt.xlabel('Year and Quarter')
plt.ylabel('Average Years of Education')
plt.title('Average Years of Education by Birth Quarter and Year')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
plt.show()

#%%

"""**REPLICATING FIGURE II: YEARS OF EDUCATION AND SEASON OF BIRTH 1980 CENSUS YEARS 1940-1949**"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
url = 'https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/cb1cddf3b7ed8b127357f5aea2caf64b97b5ef7b/1980_40_49_base_data.csv'
df = pd.read_csv(url)

# Calculate the average years of education for each birth quarter of each year
grouped = df.groupby(['BIRTHYR', 'BIRTHQTR'])['YRSED'].mean().reset_index()

# Creating a continuous index to represent each unique (year, quarter) combination
grouped['YearQuarterIndex'] = grouped['BIRTHYR'] + (grouped['BIRTHQTR'] - 1) / 4

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(grouped['YearQuarterIndex'], grouped['YRSED'], '-o', label='Average Years of Education')

# Annotating each point with the quarter of birth, ensuring no decimals are included
for idx, row in grouped.iterrows():
    quarter_annotation = f'Q{int(row["BIRTHQTR"])}'  # Convert to integer to remove decimal
    plt.annotate(quarter_annotation, (row['YearQuarterIndex'], row['YRSED']), textcoords="offset points", xytext=(0,5), ha='center')

plt.xlabel('Year and Quarter')
plt.ylabel('Average Years of Education')
plt.title('Average Years of Education by Birth Quarter and Year')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

#%%

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
url = 'https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/cb1cddf3b7ed8b127357f5aea2caf64b97b5ef7b/1980_50_59_base_data.csv'
df = pd.read_csv(url)

# Calculate the average years of education for each birth quarter of each year
grouped = df.groupby(['BIRTHYR', 'BIRTHQTR'])['YRSED'].mean().reset_index()

# Creating a continuous index to represent each unique (year, quarter) combination
grouped['YearQuarterIndex'] = grouped['BIRTHYR'] + (grouped['BIRTHQTR'] - 1) / 4

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(grouped['YearQuarterIndex'], grouped['YRSED'], '-o', label='Average Years of Education')

# Annotating each point with the quarter of birth, ensuring no decimals are included
for idx, row in grouped.iterrows():
    quarter_annotation = f'Q{int(row["BIRTHQTR"])}'  # Convert to integer to remove decimal
    plt.annotate(quarter_annotation, (row['YearQuarterIndex'], row['YRSED']), textcoords="offset points", xytext=(0,5), ha='center')

plt.xlabel('Year and Quarter')
plt.ylabel('Average Years of Education')
plt.title('Average Years of Education by Birth Quarter and Year')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
plt.show()


#%%

"""## **SECTION II: ESTIMATING THE RETURN TO EDUCATION**

**REPLICATING TABLE III PANEL B: WALD ESTIMATES FOR 1980 CENSUS MEN BORN 1930-1939**
"""""

import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/cb1cddf3b7ed8b127357f5aea2caf64b97b5ef7b/1980_30_39_all_data.csv'

# Load data from the provided URL
df = pd.read_csv(url)

# Drop rows with missing values
df.dropna(subset=['BIRTHQTR', 'WEEKERN', 'YRSED'], inplace=True)

# Calculate means for men born in the first quarter and men born in the last three quarters
first_quarter = df[df['BIRTHQTR'] == 1]
last_three_quarters = df[df['BIRTHQTR'].isin([2, 3, 4])]

# Calculate means
mean_ln_earnings_fq = np.log(first_quarter['WEEKERN']).mean()
mean_ln_earnings_l3q = np.log(last_three_quarters['WEEKERN']).mean()
mean_education_fq = first_quarter['YRSED'].mean()
mean_education_l3q = last_three_quarters['YRSED'].mean()

# Calculate differences
difference_ln_earnings = mean_ln_earnings_fq - mean_ln_earnings_l3q
difference_education = mean_education_fq - mean_education_l3q

# Calculate Wald estimate
wald_estimate = difference_ln_earnings / difference_education

# Calculate bivariate regression of log weekly earnings on years of education
y = np.log(df['WEEKERN'])
X = df['YRSED']
X = sm.add_constant(X)  # Add constant term to the predictor
model = sm.OLS(y, X).fit()
difference_ln_weekly_wage = mean_ln_earnings_fq - mean_ln_earnings_l3q
difference_YRSED = mean_education_fq - mean_education_l3q
ols_estimate = model.params['YRSED']

# Create a DataFrame for the results
results = pd.DataFrame({
    'Statistic': ['ln Weekly Wage', 'Education', 'Wald Estimate', 'OLS Estimate'],
    'First Quarter': [mean_ln_earnings_fq, mean_education_fq, '-', '-'],
    'Last Three Quarters': [mean_ln_earnings_l3q, mean_education_l3q, '-', '-'],
    'Difference': [difference_ln_weekly_wage, difference_YRSED, wald_estimate, ols_estimate]
})

# Print or display the results DataFrame
print(results)

#%%
""""

*OLS*
"""
#%%

import pandas as pd
import numpy as np
import statsmodels as sm
import statsmodels.api as sm

# Load the dataset
url = 'https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/cb1cddf3b7ed8b127357f5aea2caf64b97b5ef7b/1980_30_39_all_data.csv'
df = pd.read_csv(url)

df.dropna(inplace=True)

# Get the coefficients
coefficients = model.params
# Create birth year dummies
for year in range(1930, 1940):
    df[f'BirthYearDummy_{year}'] = (df['BIRTHYR'] == year).astype(int)

# Define the dependent variable (Y) and the independent variables (X)
Y = np.log(df['WEEKERN'])  # Natural logarithm of WEEKERN
independent_vars = ['YRSED'] + [f'BirthYearDummy_{year}' for year in range(1930, 1940)]
X = df[independent_vars]

# Add constant term to the independent variables
X = sm.add_constant(X)

# Fit OLS regression model
ols_model = sm.OLS(Y, X).fit()

# Extract YRS ED coefficient and standard error
YRSED_coef_ols_1 = round(ols_model.params['YRSED'], 4)
YRSED_std_err_ols_1 = round(ols_model.bse['YRSED'], 4)

"""*TSLS*"""
#%%

import pandas as pd
import statsmodels.api as sm

import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the dataset
url = 'https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/cb1cddf3b7ed8b127357f5aea2caf64b97b5ef7b/1980_30_39_all_data.csv'
df = pd.read_csv(url)

df.dropna(inplace=True)



# First stage: Regress YRSED on BIRTHQTR and a constant (with instrumental variable)
endog_first_stage = df['YRSED']
exog_first_stage = sm.add_constant(df['BIRTHQTR'])
instrument_first_stage = sm.add_constant(df['BIRTHQTR'])  # Instrumental variable
first_stage_model = sm.OLS(endog_first_stage, exog_first_stage).fit(cov_type='HC0')  # Use robust standard errors

# Predict YRSED using the fitted first-stage model
df['YRSED_predicted'] = first_stage_model.predict()


# Second stage: Regress natural logarithm of WEEKERN on the predicted YRSED from the first stage

# Create birth year dummies
for year in range(1930, 1940):
    df[f'BirthYearDummy_{year}'] = (df['BIRTHYR'] == year).astype(int)

covariate_columns = ['YRSED_predicted'] + [f'BirthYearDummy_{year}' for year in range(1930, 1940)]

# Select the explanatory variables for the second stage
exog_second_stage = sm.add_constant(df[covariate_columns])
endog_second_stage = np.log(df['WEEKERN'])  # Natural logarithm of WEEKERN

second_stage_model = sm.OLS(endog_second_stage, exog_second_stage).fit(cov_type='HC0')  # Use robust standard errors

# Extract YRS ED coefficient and standard error from the second stage

YRSED_coef_second_stage_1 = round(second_stage_model.params['YRSED_predicted'], 4)
YRSED_std_err_second_stage_1 = round(second_stage_model.bse['YRSED_predicted'], 4)

# Create DataFrame
data = {
    'OLS': [YRSED_coef_ols_1, YRSED_std_err_ols_1,"-","-","-","-","-","-","-","-","-","-"],
    'TSLS': [YRSED_coef_second_stage_1, YRSED_std_err_second_stage_1, "-","-","-","-","-","-","-","-","-","-"]
}
index = ['Years of Education', '', 'AGE', '','AGESQR', '', 'Married (1= married)', '', 'Race (1= black)', '', 'Place of Work (1= center city)', '']
df_1_output = pd.DataFrame(data, index=index)

# Display DataFrame
print(df_1_output)

"""**OLS AND TSLS #2**

Adding independent variables 'AGE' and 'AGE SQUARED' to OLS and TSLS.

*OLS*
"""
#%%

import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the dataset
url = 'https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/cb1cddf3b7ed8b127357f5aea2caf64b97b5ef7b/1980_30_39_all_data.csv'
df = pd.read_csv(url)

df.dropna(inplace=True)


# Create birth year dummies
for year in range(1930, 1940):
    df[f'BirthYearDummy_{year}'] = (df['BIRTHYR'] == year).astype(int)

# Define the dependent variable (Y) and the independent variables (X)
Y = np.log(df['WEEKERN'])  # Natural logarithm of WEEKERN
independent_vars = ['YRSED'] + [f'BirthYearDummy_{year}' for year in range(1930, 1940)]+['AGE']+['AGESQR']
X = df[independent_vars]

# Add constant term to the independent variables
X = sm.add_constant(X)

# Fit OLS regression model
ols_model = sm.OLS(Y, X).fit()

# Extract YRS ED coefficient and standard error
YRSED_coef_ols_2 = round(ols_model.params['YRSED'], 4)
YRSED_std_err_ols_2 = round(ols_model.bse['YRSED'], 4)

# Extract coefficients and standard errors for AGE and AGESQR
age_coef = round(ols_model.params['AGE'], 4)
age_std_err = round(ols_model.bse['AGE'], 4)

agesqr_coef = round(ols_model.params['AGESQR'], 4)
agesqr_std_err = round(ols_model.bse['AGESQR'], 4)

"""*TSLS*"""
#%%

import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the dataset
url = 'https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/cb1cddf3b7ed8b127357f5aea2caf64b97b5ef7b/1980_30_39_all_data.csv'
df = pd.read_csv(url)

df.dropna(inplace=True)

# First stage: Regress YRSED on BIRTHQTR and a constant (with instrumental variable)
endog_first_stage = df['YRSED']
exog_first_stage = sm.add_constant(df[['BIRTHQTR']])
instrument_first_stage = sm.add_constant(df['BIRTHQTR'])  # Instrumental variable
first_stage_model = sm.OLS(endog_first_stage, exog_first_stage).fit(cov_type='HC0')  # Use robust standard errors

# Predict YRSED using the fitted first-stage model
df['YRSED_predicted'] = first_stage_model.predict()


# Second stage: Regress natural logarithm of WEEKERN on the predicted YRSED from the first stage

# Create birth year dummies
for year in range(1930, 1940):
    df[f'BirthYearDummy_{year}'] = (df['BIRTHYR'] == year).astype(int)

covariate_columns = ['YRSED_predicted', 'AGE', 'AGESQR'] + [f'BirthYearDummy_{year}' for year in range(1930, 1940)]
endog_second_stage = np.log(df['WEEKERN'])  # Natural logarithm of WEEKERN
exog_second_stage = sm.add_constant(df[covariate_columns])
second_stage_model = sm.OLS(endog_second_stage, exog_second_stage).fit(cov_type='HC0')  # Use robust standard errors

# Extract YRS ED coefficient and standard error from the second stage
YRSED_coef_second_stage_2 = round(second_stage_model.params['YRSED_predicted'], 4)
YRSED_std_err_second_stage_2 = round(second_stage_model.bse['YRSED_predicted'], 4)


# Extract coefficients and standard errors for AGE and AGESQR from the second stage model
age_coef_second_stage = round(second_stage_model.params['AGE'], 4)
age_std_err_second_stage = round(second_stage_model.bse['AGE'], 4)

agesqr_coef_second_stage = round(second_stage_model.params['AGESQR'], 4)
agesqr_std_err_second_stage = round(second_stage_model.bse['AGESQR'], 4)

# Create DataFrame
data = {
    'OLS': [YRSED_coef_ols_2, YRSED_std_err_ols_2, age_coef, age_std_err, agesqr_coef, agesqr_std_err, "-","-","-","-","-","-"],
    'TSLS': [YRSED_coef_second_stage_2, (YRSED_std_err_second_stage_2), age_coef_second_stage, (age_std_err_second_stage), agesqr_coef_second_stage, (agesqr_std_err_second_stage),"-","-","-","-","-","-"]
}
index = ['Years of Education', '', 'AGE', '','AGESQR', '', 'Married (1= married)', '', 'Race (1= black)', '', 'Place of Work (1= center city)', '']
df_2_output = pd.DataFrame(data, index=index)

# Display DataFrame
print(df_2_output)

"""**OLS AND TSLS #3**

Adding independent variables 'MARST' and 'PWTYPE' and 'RACE'

*OLS*
"""
#%%

import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the dataset
url = 'https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/cb1cddf3b7ed8b127357f5aea2caf64b97b5ef7b/1980_30_39_all_data.csv'
df = pd.read_csv(url)

df.dropna(inplace=True)

# Create birth year dummies
for year in range(1930, 1940):
    df[f'BirthYearDummy_{year}'] = (df['BIRTHYR'] == year).astype(int)

# Create MARST_dummy
df['MARST_dummy'] = (df['MARST'] == 1).astype(int)

# Create Race_dummy
df['Race_dummy'] = (df['RACE'] == 2).astype(int)

# Create PWTYPE_dummy
df['PWTYPE_dummy'] = df['PWTYPE'].isin([1, 2, 3]).astype(int)

# Define the dependent variable (Y) and the independent variables (X)
Y = np.log(df['WEEKERN'])  # Natural logarithm of WEEKERN
independent_vars = ['YRSED'] + [f'BirthYearDummy_{year}' for year in range(1930, 1940)] + ['MARST_dummy', 'Race_dummy', 'PWTYPE_dummy']
X = df[independent_vars]

# Add constant term to the independent variables
X = sm.add_constant(X)

# Fit OLS regression model
ols_model = sm.OLS(Y, X).fit()

# Extract YRS ED coefficient and standard error
YRSED_coef_ols_3 = round(ols_model.params['YRSED'], 4)
YRSED_std_err_ols_3 = round(ols_model.bse['YRSED'], 4)


# Extract coefficients and standard errors
coefficients = ols_model.params
standard_errors = ols_model.bse

# Extract coefficients and standard errors for the dummy variables
MARST_dummy_coef_ols_1 = round(ols_model.params['MARST_dummy'], 4)
MARST_dummy_std_err_ols_1 = round(ols_model.bse['MARST_dummy'], 4)

Race_dummy_coef_ols_1 = round(ols_model.params['Race_dummy'], 4)
Race_dummy_std_err_ols_1 = round(ols_model.bse['Race_dummy'], 4)

PWTYPE_dummy_coef_ols_1 = round(ols_model.params['PWTYPE_dummy'], 4)
PWTYPE_dummy_std_err_ols_1 = round(ols_model.bse['PWTYPE_dummy'], 4)

"""*TSLS*"""
#%%

import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the dataset
url = 'https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/cb1cddf3b7ed8b127357f5aea2caf64b97b5ef7b/1980_30_39_all_data.csv'
df = pd.read_csv(url)

df.dropna(inplace=True)

# Create birth year dummies
for year in range(1930, 1940):
    df[f'BirthYearDummy_{year}'] = (df['BIRTHYR'] == year).astype(int)

# Create MARST_dummy variable
df['MARST_dummy'] = (df['MARST'] == 1).astype(int)

# Create Race_dummy variable
df['Race_dummy'] = (df['RACE'] == 2).astype(int)

# Create PWTYPE_dummy variable
df['PWTYPE_dummy'] = (df['PWTYPE'].isin([1, 2, 3])).astype(int)

# Create region dummies
df['MW_dummy'] = (df['REGION2'] == 'MW').astype(int)
df['South_dummy'] = (df['REGION2'] == 'South').astype(int)
df['NE_dummy'] = (df['REGION2'] == 'NE').astype(int)
df['West_dummy'] = (df['REGION2'] == 'West').astype(int)

# First stage: Regress YRSED on BIRTHQTR and a constant (with instrumental variable)
endog_first_stage = df['YRSED']
exog_first_stage = sm.add_constant(df['BIRTHQTR'])
instrument_first_stage = sm.add_constant(df['BIRTHQTR'])  # Instrumental variable
first_stage_model = sm.OLS(endog_first_stage, exog_first_stage).fit(cov_type='HC0')  # Use robust standard errors

# Predict YRSED using the fitted first-stage model
df['YRSED_predicted'] = first_stage_model.predict()

# Second stage: Regress natural logarithm of WEEKERN on the predicted YRSED from the first stage

covariate_columns = ['YRSED_predicted', 'MARST_dummy', 'Race_dummy', 'PWTYPE_dummy', 'MW_dummy', 'South_dummy', 'NE_dummy', 'West_dummy'] + [f'BirthYearDummy_{year}' for year in range(1930, 1940)]

# Ensure all specified columns are present in df
# This is a safety check; remove or adjust columns as necessary based on your actual DataFrame
missing_columns = [col for col in covariate_columns if col not in df.columns]
if missing_columns:
    raise ValueError(f"Missing columns: {missing_columns}")

# Select the explanatory variables for the second stage
exog_second_stage = sm.add_constant(df[covariate_columns])
endog_second_stage = np.log(df['WEEKERN'])  # Natural logarithm of WEEKERN

second_stage_model = sm.OLS(endog_second_stage, exog_second_stage).fit(cov_type='HC0')  # Use robust standard errors

# Extract YRS ED coefficient and standard error from the second stage
YRSED_coef_second_stage_3 = round(second_stage_model.params['YRSED_predicted'], 4)
YRSED_std_err_second_stage_3 = round(second_stage_model.bse['YRSED_predicted'], 4)


# Extract coefficients and standard errors for the dummy variables
MARST_dummy_coef_1 = round(second_stage_model.params['MARST_dummy'], 4)
MARST_dummy_std_err_1 = round(second_stage_model.bse['MARST_dummy'], 4)

Race_dummy_coef_1 = round(second_stage_model.params['Race_dummy'], 4)
Race_dummy_std_err_1 = round(second_stage_model.bse['Race_dummy'], 4)

PWTYPE_dummy_coef_1 = round(second_stage_model.params['PWTYPE_dummy'], 4)
PWTYPE_dummy_std_err_1 = round(second_stage_model.bse['PWTYPE_dummy'], 4)

# Create DataFrame
data = {
    'OLS': [YRSED_coef_ols_3, YRSED_std_err_ols_3, "-", "-","-","-",MARST_dummy_coef_ols_1, MARST_dummy_std_err_ols_1, Race_dummy_coef_ols_1, Race_dummy_std_err_ols_1, PWTYPE_dummy_coef_ols_1, PWTYPE_dummy_std_err_ols_1],
    'TSLS': [YRSED_coef_second_stage_3, YRSED_std_err_second_stage_3, "-", "-","-","-",MARST_dummy_coef_1, MARST_dummy_std_err_1, Race_dummy_coef_1, Race_dummy_std_err_1,PWTYPE_dummy_coef_1,PWTYPE_dummy_std_err_1 ]
}
index = ['Years of Education', '', 'AGE', '','AGESQR', '', 'Married (1= married)', '', 'Race (1= black)', '', 'Place of Work (1= center city)', '']
df_3_output = pd.DataFrame(data, index=index)

# Display DataFrame
print(df_3_output)

"""**OLS AND TSLS #4**

Adding independent variables 'AGE', 'AGESQR', 'MARST' and 'PWTYPE' and 'RACE'

*OLS*
"""
#%%

import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the dataset
url = 'https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/cb1cddf3b7ed8b127357f5aea2caf64b97b5ef7b/1980_30_39_all_data.csv'
df = pd.read_csv(url)

df.dropna(inplace=True)

# Create birth year dummies
for year in range(1930, 1940):
    df[f'BirthYearDummy_{year}'] = (df['BIRTHYR'] == year).astype(int)

# Create MARST_dummy
df['MARST_dummy'] = (df['MARST'] == 1).astype(int)

# Create Race_dummy
df['Race_dummy'] = (df['RACE'] == 2).astype(int)

# Create PWTYPE_dummy
df['PWTYPE_dummy'] = df['PWTYPE'].isin([1, 2, 3]).astype(int)

# Define the dependent variable (Y) and the independent variables (X)
Y = np.log(df['WEEKERN'])  # Natural logarithm of WEEKERN
independent_vars = ['YRSED'] + [f'BirthYearDummy_{year}' for year in range(1930, 1940)] + ['MARST_dummy', 'Race_dummy', 'PWTYPE_dummy']+['AGE']+['AGESQR']
X = df[independent_vars]

# Add constant term to the independent variables
X = sm.add_constant(X)

# Fit OLS regression model
ols_model = sm.OLS(Y, X).fit()


# Extract YRS ED coefficient and standard error
YRSED_coef_ols_4 = round(ols_model.params['YRSED'], 4)
YRSED_std_err_ols_4 = round(ols_model.bse['YRSED'], 4)


# Extract coefficients and standard errors for AGE and AGESQR
age_coef_2 = round(ols_model.params['AGE'], 4)
age_std_err_2 = round(ols_model.bse['AGE'], 4)

agesqr_coef_2 = round(ols_model.params['AGESQR'], 4)
agesqr_std_err_2= round(ols_model.bse['AGESQR'], 4)

# Extract coefficients and standard errors
coefficients = ols_model.params
standard_errors = ols_model.bse

# Extract coefficients and standard errors for the dummy variables
MARST_dummy_coef_ols_2 = round(ols_model.params['MARST_dummy'], 4)
MARST_dummy_std_err_ols_2 = round(ols_model.bse['MARST_dummy'], 4)

Race_dummy_coef_ols_2 = round(ols_model.params['Race_dummy'], 4)
Race_dummy_std_err_ols_2 = round(ols_model.bse['Race_dummy'], 4)

PWTYPE_dummy_coef_ols_2 = round(ols_model.params['PWTYPE_dummy'], 4)
PWTYPE_dummy_std_err_ols_2 = round(ols_model.bse['PWTYPE_dummy'], 4)

"""*TSLS*"""
#%%

import pandas as pd
import numpy as np
import statsmodels as sm
import statsmodels.api as sm

# Load the dataset
url = 'https://raw.githubusercontent.com/mgstevens02/Compulsory-Education-IV-Replication/cb1cddf3b7ed8b127357f5aea2caf64b97b5ef7b/1980_30_39_all_data.csv'
df = pd.read_csv(url)

df.dropna(inplace=True)

# Create birth year dummies
for year in range(1930, 1940):
    df[f'BirthYearDummy_{year}'] = (df['BIRTHYR'] == year).astype(int)

# Create MARST_dummy variable
df['MARST_dummy'] = (df['MARST'] == 1).astype(int)

# Create Race_dummy variable
df['Race_dummy'] = (df['RACE'] == 2).astype(int)

# Create PWTYPE_dummy variable
df['PWTYPE_dummy'] = (df['PWTYPE'].isin([1, 2, 3])).astype(int)

# Create region dummies
df['MW_dummy'] = (df['REGION2'] == 'MW').astype(int)
df['South_dummy'] = (df['REGION2'] == 'South').astype(int)
df['NE_dummy'] = (df['REGION2'] == 'NE').astype(int)
df['West_dummy'] = (df['REGION2'] == 'West').astype(int)

# First stage: Regress YRSED on BIRTHQTR and a constant (with instrumental variable)
endog_first_stage = df['YRSED']
exog_first_stage = sm.add_constant(df['BIRTHQTR'])
instrument_first_stage = sm.add_constant(df['BIRTHQTR'])  # Instrumental variable
first_stage_model = sm.OLS(endog_first_stage, exog_first_stage).fit(cov_type='HC0')  # Use robust standard errors

# Predict YRSED using the fitted first-stage model
df['YRSED_predicted'] = first_stage_model.predict()


# Second stage: Regress natural logarithm of WEEKERN on the predicted YRSED from the first stage,

# Construct the list of explanatory variable names for the second stage
covariate_columns = ['YRSED_predicted', 'MARST_dummy', 'Race_dummy', 'PWTYPE_dummy', 'MW_dummy', 'South_dummy', 'NE_dummy', 'West_dummy', 'AGE', 'AGESQR'] + [f'BirthYearDummy_{year}' for year in range(1930, 1940)]

# Ensure all specified columns are present in df
# This is a safety check; remove or adjust columns as necessary based on your actual DataFrame
missing_columns = [col for col in covariate_columns if col not in df.columns]
if missing_columns:
    raise ValueError(f"Missing columns: {missing_columns}")

# Select the explanatory variables for the second stage
exog_second_stage = sm.add_constant(df[covariate_columns])

endog_second_stage = np.log(df['WEEKERN'])  # Natural logarithm of WEEKERN
second_stage_model = sm.OLS(endog_second_stage, exog_second_stage).fit(cov_type='HC0')  # Use robust standard errors


# Extract YRS ED coefficient and standard error from the second stage
YRSED_coef_second_stage_4 = round(second_stage_model.params['YRSED_predicted'], 4)
YRSED_std_err_second_stage_4 = round(second_stage_model.bse['YRSED_predicted'], 4)


# Extract coefficients and standard errors for AGE and AGESQR from the second stage model
age_coef_second_stage_2 = round(second_stage_model.params['AGE'], 4)
age_std_err_second_stage_2 = round(second_stage_model.bse['AGE'], 4)

agesqr_coef_second_stage_2 = round(second_stage_model.params['AGESQR'], 6)
agesqr_std_err_second_stage_2 = round(second_stage_model.bse['AGESQR'], 4)


# Extract coefficients and standard errors for the dummy variables
MARST_dummy_coef_2 = round(second_stage_model.params['MARST_dummy'], 4)
MARST_dummy_std_err_2 = round(second_stage_model.bse['MARST_dummy'], 4)

Race_dummy_coef_2 = round(second_stage_model.params['Race_dummy'], 4)
Race_dummy_std_err_2 = round(second_stage_model.bse['Race_dummy'], 4)

PWTYPE_dummy_coef_2 = round(second_stage_model.params['PWTYPE_dummy'], 4)
PWTYPE_dummy_std_err_2 = round(second_stage_model.bse['PWTYPE_dummy'], 4)

# Create DataFrame
data = {
    'OLS': [YRSED_coef_ols_4, YRSED_std_err_ols_4, age_coef_2, age_std_err_2, agesqr_coef_2,agesqr_std_err_2, MARST_dummy_coef_ols_2, MARST_dummy_std_err_ols_2, Race_dummy_coef_ols_2, Race_dummy_std_err_ols_2, PWTYPE_dummy_coef_ols_2, PWTYPE_dummy_std_err_ols_2],
    'TSLS': [YRSED_coef_second_stage_4, YRSED_std_err_second_stage_4, age_coef_second_stage_2, age_std_err_second_stage_2, agesqr_coef_second_stage_2,agesqr_std_err_second_stage_2,MARST_dummy_coef_2, MARST_dummy_std_err_2, Race_dummy_coef_2, Race_dummy_std_err_2,PWTYPE_dummy_coef_2,PWTYPE_dummy_std_err_2 ]
}
index = ['Years of Education', '', 'AGE', '','AGESQR', '', 'Married (1= married)', '', 'Race (1= black)', '', 'Place of Work (1= center city)', '']
df_4_output = pd.DataFrame(data, index=index)

# Display DataFrame
print(df_4_output)

"""## **TABLE V COMBINED RESULTS**"""
#%%

import pandas as pd

# Assuming df_1_output, df_2_output, df_3_output, and df_4_output are your dataframes

# Rename the "OLS" and "TSLS" columns for each dataframe
df_1_output.rename(columns={'OLS': 'OLS (1)', 'TSLS': 'TSLS (1)'}, inplace=True)
df_2_output.rename(columns={'OLS': 'OLS (2)', 'TSLS': 'TSLS (2)'}, inplace=True)
df_3_output.rename(columns={'OLS': 'OLS (3)', 'TSLS': 'TSLS (3)'}, inplace=True)
df_4_output.rename(columns={'OLS': 'OLS (4)', 'TSLS': 'TSLS (4)'}, inplace=True)

# Reset the index of each dataframe
df_1_output.reset_index(drop=True, inplace=True)
df_2_output.reset_index(drop=True, inplace=True)
df_3_output.reset_index(drop=True, inplace=True)
df_4_output.reset_index(drop=True, inplace=True)

# Concatenate the dataframes along the rows axis (axis=1)
combined_df = pd.concat([df_1_output, df_2_output, df_3_output, df_4_output], axis=1)

# Add appropriate row names
row_names = ['Years of Education', '', 'AGE', '', 'AGESQR', '', 'Married (1= married)', '', 'Race (1= black)', '', 'Place of Work (1= center city)', '']
combined_df.index = row_names[:len(combined_df.index)]

# Print the combined dataframe
print(combined_df)
