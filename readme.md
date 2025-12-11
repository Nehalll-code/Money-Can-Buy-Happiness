<p align="center">
  <img src="https://dummyimage.com/1400x350/6c5ce7/ffffff&text=📊+Money+Can+Buy+Happiness+(Data+Says+So)+💸" alt="Project Banner">
</p>

# 🌍 **Money Can Buy Happiness**
### *A data-driven exploration of the relationship between income and life satisfaction*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Linear%20Regression-Completed-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Happiness%20Explained-~60%25-green?style=for-the-badge" />
</p>

---

# 📌 **Overview**

Does money buy happiness?  
This project uses real-world data from **Our World In Data** to examine whether countries with higher GDP per capita tend to report higher levels of happiness.

Using linear regression (and a surprisingly decent R²), we explore:

- How strongly income correlates with life satisfaction  
- Whether log-income better explains the relationship  
- What the data says… and what it doesn’t  

**Conclusion:**  
Money doesn’t guarantee happiness — but statistically, it helps.

---

# 🚀 **Features**

- Cleaned and preprocessed GDP–Happiness dataset  
- Linear & log-linear regression models  
- Visualizations (scatter plot + regression line)  
- R² evaluation and interpretation  
- Lightweight, reproducible Python workflow  

---

# 📁 **Data Source**

The dataset used in this project is from **Our World In Data**, specifically the *GDP vs Happiness* data.

- 🌍 Source: https://ourworldindata.org/grapher/gdp-vs-happiness  
- 📄 License: CC-BY (free to use with attribution)  
- 📝 Variables included:
  - Happiness score (0–10 scale)  
  - GDP per capita (PPP, constant international $)  
  - Country metadata (region, code, year)  

A cleaned version of the dataset is placed in `./data/` for reproducibility.

---

# 🧠 **Key Insights**

- Countries with higher GDP per capita **tend to be happier**  
- Simple linear regression gives **R² ≈ 0.6**  
- Log-transforming GDP improves realism  
- Happiness depends on many factors beyond income  

---

# 🔧 **Installation**

Clone the repository:

bash
git clone https://github.com/<your-username>/money-can-buy-happiness.git
cd money-can-buy-happiness
Run the script:

bash
Copy code
python script.py
📊 Outputs
📈 Scatter plot of GDP vs Happiness

➖ Regression line overlay

📉 R² score printed in console

🤖 A statistically informed answer to: “Can money buy happiness?”

📝 Example Interpretation
“Our model suggests that GDP explains roughly 60% of cross-country variation in reported happiness. While income is a significant predictor, other social and cultural factors play meaningful roles.”

TL;DR:

✔ Yes, money makes people happier

✖ No, it doesn’t fix everything

😌 But let’s be honest — it helps

So if you're sad, consider increasing your GDP per capita.
(Or talk to a therapist. Or both.)

🪪 License
Released under the MIT License — feel free to use, modify, and build upon the project.
