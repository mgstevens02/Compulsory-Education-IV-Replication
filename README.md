Hello! This repository replicates part of the study "Does Compulsory School Attendance Affect Schooling and Earnings?"

The data is split into 3 separate cohorts by birth year: 1930-1939, 1940-1949, and 1950-1959.

Due to GitHub file size restrictions the 1940-1949 and 1950-1959 data is split into two files. The data needed to replicate Figures II and III is located in the "base_data" files. 
To independently replicate the IV for the 1940-1949 and 1959 age groups, use the "extra_data" files which contain the data needed for the model's covariates.

The main part of the replication is the IV Analysis that aims to replicate the data in Table V of the paper. 
The 1930-1939 data is used for this table and all necessary data is in the same file.

This replication includes 4 separate TSLS models and 4 separate OLS models. Each model uses a different mixture of covariates.

The code to run in VSC is labeled "Compulsory_Education_IV_Replication_VSC.py"

The empirical example from Colab has been imported as well and can be found in the file titled "Compulsory_Education_IV_Replication.ipynb"

The actual Colab version of the empirical example can be found using this link: https://colab.research.google.com/drive/1-G-qiAaJQEkk2DXXVH1nr3GsIpduhUa5?usp=sharing

