import pandas as pd
import joblib
import warnings
from sklearn.exceptions import InconsistentVersionWarning

warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

model = joblib.load("movie-success-predictor.joblib")
columns = joblib.load("columns.joblib")


print("\n       Movie Success Predictor\n")


data = {
    "Released_Year": [int(input("Released Year: "))],
    "Certificate": [input("Certificate: ").strip()],
    "Runtime": [int(input("Runtime: "))],
    "Genre": [input("Genre: ").strip()],
    "IMDB_Rating": [float(input("IMDB Rating: "))],
    "Meta_score": [int(input("Meta_score: "))],
    "No_of_Votes": [int(input("No_of_Votes: "))]
}

df = pd.DataFrame(data)

df = pd.get_dummies(df)

df = df.reindex(columns=columns, fill_value=0)



prediction = model.predict(df)

print("\nPredicted Domain:", prediction[0])