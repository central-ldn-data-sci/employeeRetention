import pandas as pd
import pandasql as pdsql

df = pd.read_csv("employee_retention_data.csv") # pick single quotes or double quotes -> double quotes wooo

df = pdsql("SELECT employee_id")