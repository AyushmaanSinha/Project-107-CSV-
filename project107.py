import csv
import pandas as pd
import plotly.express as px

data = pd.read_csv("Python/data.csv")
studentID = data.groupby(["student_id","level"], as_index = False)["attempt"].mean()
fig = px.scatter(studentID, x = "student_id", y = "level", color = "attempt", size = "attempt")
fig.show()