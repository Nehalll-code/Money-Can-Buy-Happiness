# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# %%
url = "https://ourworldindata.org/grapher/gdp-vs-happiness.csv"
#using colab kernel to read csv directly from url
df = pd.read_csv(url)
df.head()

# %%
df = df.dropna()

# %%
print(df.columns)


# %%
df = df.rename(columns={
    "GDP per capita, PPP (constant 2021 international $)": "gdp",
    "happiness": "happiness_score"
})
print(df.columns)

# %%
df = df.drop_duplicates()


# %%
df["log_gdp"] = np.log(df["gdp"])
df.head()

# %%
plt.scatter(df["log_gdp"], df["happiness_score"])
plt.xlabel("Log of GDP per Capita",color='red')
plt.ylabel("Happiness Score",color='red')
plt.title("GDP vs Happiness")
plt.show()

# %%
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X = df[["log_gdp"]]
y = df["happiness_score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# %%
print("β0 (intercept):", model.intercept_)
print("β1 (slope):", model.coef_[0])
print("R² score:", model.score(X, y))

# %% [markdown]
# IF B1 = POSITIVE, GDP RELATED TO HAPPINESS
# If R² is moderate (~0.3–0.5): GDP explains some happiness variation, but not all.
# if log-GDP gives higher R²: The relationship is nonlinear (diminishing returns).

# %%
plt.scatter(df["log_gdp"], df["happiness_score"])
plt.xlabel("Log of GDP per capita") 
plt.ylabel("Happiness Score")
plt.title("GDP vs Happiness with Regression Line")
# predicted line
x_line = np.linspace(df["log_gdp"].min(), df["log_gdp"].max(), 100)
y_line = model.predict(x_line.reshape(-1, 1))

plt.plot(x_line, y_line,color='red')
plt.show()

# %%



