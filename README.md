## 🚗 Automobile Dataset Analysis

This project performs exploratory data analysis on the **Kaggle Automobile Dataset**, using Python and pandas. The goal is to answer various business and technical questions related to vehicle pricing, characteristics, and distributions.

### 📁 Dataset

* **File:** `Automobile.csv`
* **Source:** [Kaggle](https://www.kaggle.com/toramky/automobile-dataset)
* **Description:** The dataset includes technical and pricing information for various car makes and models, including body style, horsepower, and price.

### 🛠️ Requirements

* Python 3.x
* pandas
* Jupyter Notebook (optional, for interactive use)
* matplotlib / seaborn (if plotting is added later)

### 📊 Analysis Performed

* Displayed the first few records of the dataset.
* Counted the total number of rows and columns.
* Calculated the average price of all cars.
* Identified the cheapest and costliest cars.
* Counted the number of cars with horsepower greater than 100.
* Found how many hatchback cars are present.
* Retrieved the top 3 most common car makes.
* Identified the make of a car purchased for \$7099.
* Listed cars priced above \$40,000.
* Listed all sedan cars priced below \$7,000.

### 📌 Sample Queries

```python
auto['price'].mean()  # Average price
auto[auto['price'] == auto['price'].max()]  # Most expensive car
auto[auto['horsepower'] > 100].count()  # Cars with HP > 100
```

### 📈 Future Improvements

* Add visualizations using seaborn/matplotlib.
* Handle missing data and clean the dataset further.
* Perform advanced statistical analysis or model training.

---
