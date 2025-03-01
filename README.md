# PROJECT-1-Machine-learning-House-Price-Prediction-Regressionn


# **🏡 Bengaluru House Price Prediction using Machine Learning**  

## 📌 **Introduction**  
Housing prices in metropolitan cities like **Bengaluru** fluctuate due to multiple factors, such as **location, availability, demand, infrastructure, and real estate trends**. Manually predicting house prices can be challenging due to **the vast number of variables affecting property costs**.  

This project aims to **predict house prices in Bengaluru** based on key features such as **location, total square footage, number of bathrooms, and BHK (Bedroom, Hall, Kitchen)**.  

The project follows a **structured machine learning pipeline** from **data collection, preprocessing, feature engineering, model selection, and evaluation**, culminating in a **Gradio-based web application** that provides **real-time price predictions** based on user inputs.  

---

## 🛠 **Steps Followed**  

---

## **📂 Step 1: Data Collection**  

### **Dataset Used:**  
- The dataset used for this project is **Bengaluru_House_Data.csv**.  
- It contains **13 columns** and **13,320 rows**, providing detailed housing attributes.  

### **Columns in Dataset:**  
| Column Name       | Description |
|-------------------|-------------|
| `area_type`      | Type of area (Super built-up, Plot, etc.) |
| `availability`   | Availability status (Ready-to-move, Launch date) |
| `location`       | Address or locality |
| `size`          | Number of bedrooms (e.g., "2 BHK") |
| `society`        | Society name (Many missing values) |
| `total_sqft`     | Total square footage (Sometimes in range format) |
| `bath`          | Number of bathrooms |
| `balcony`       | Number of balconies |
| `price`         | Price of the house (in Lakhs) |

---

## **📊 Step 2: Exploratory Data Analysis (EDA)**  

EDA helps us **understand the data distribution, check missing values, and identify trends** before applying Machine Learning models.  

### **Key Findings from EDA:**  
1. **Missing Values:**  
   - `society`, `balcony`, and `availability` had **large numbers of missing values**.  
   - `bath` had a few missing values.  
   - `size` contained some missing data.  

2. **Non-Standardized Data:**  
   - `total_sqft` contained **range values** (e.g., `"2100-3200"`) that needed conversion.  
   - `size` contained **text values** (`"3 BHK"`) instead of numbers.  

3. **Outliers Detected:**  
   - Some `total_sqft` values were **extremely high** for a low number of BHKs.  
   - Price per square foot varied **significantly within the same location**.  

---

## **🧹 Step 3: Data Cleaning & Preprocessing**  

To ensure **accurate predictions**, we cleaned and transformed the dataset.  

### **Tasks Performed:**  
✅ **Dropped Unnecessary Columns** (`area_type`, `availability`, `society`, `balcony`).  
✅ **Filled Missing Values** (`bath` with median, `size` with most frequent value).  
✅ **Extracted Numeric BHK Values** from `size` (`"3 BHK"` → `3`).  
✅ **Converted `total_sqft` to Numeric**:  
   - If in range format (e.g., `"1200-1500"`), **took the average** (`(1200+1500)/2 = 1350`).  
   - Dropped **non-numeric** values like `"34.46Sq. Meter"`.  

---

## **📏 Step 4: Feature Engineering**  

Feature engineering enhances the model's ability to learn meaningful patterns.  

### **Created Features:**  
1. **Price per Square Foot (`price_per_sqft`)**  
   \[
   price\_per\_sqft = \frac{price \times 100000}{total\_sqft}
   \]
   - Helps identify outliers based on location.  

2. **Location Simplification:**  
   - Locations with **less than 10 occurrences** grouped into `"other"`.  

---

## **📉 Step 5: Outlier Detection & Removal**  

To ensure better model accuracy, we removed extreme outliers.  

### **Outliers Identified & Removed Based on:**  
1. **Minimum Square Feet per BHK**  
   - **Removed properties where `total_sqft / bhk < 300`** (Unrealistic space).  

2. **Location-wise Price per Square Foot**  
   - Removed extreme values **beyond ±1.5 standard deviation** in price-per-sqft distribution.  

3. **BHK Price Consistency Check**  
   - Ensured that **higher BHKs are not cheaper than lower BHKs in the same area**.  

---

## **🤖 Step 6: Model Training & Evaluation**  

After data preprocessing, we trained **multiple models** and compared their performance.  

### **Train-Test Split:**  
- **80% Training Set, 20% Test Set**  
- `x = ['location', 'total_sqft', 'bath', 'bhk']`  
- `y = price`  

### **Models Used & Results:**  

| Model | R² Score |
|---------|-----------|
| **Linear Regression** | **0.82** ✅ |
| Lasso Regression | 0.78 |
| Ridge Regression | 0.80 |

🔹 **Linear Regression** performed the best! 🎯  

---

## **📁 Step 7: Model Saving & Deployment**  

### **Saving Model using Pickle:**  
- **Trained model** was saved using **Pickle (`pipe.pkl`)** to use in deployment.  

```python
import pickle
with open('pipe.pkl', 'wb') as f:
    pickle.dump(pipe, f)
```

### **Building Gradio Web App:**  
- Used **Gradio** for a simple UI.  
- Users can input: **Location, Square Footage, BHK, Bathrooms**.  
- Model **predicts house price** instantly.  

```python
import gradio as gr

def predict_price(location, total_sqft, bath, bhk):
    input_data = pd.DataFrame({'location': [location], 'total_sqft': [total_sqft], 'bath': [bath], 'bhk': [bhk]})
    prediction = pipe.predict(input_data)[0]
    return f"Predicted House Price: ₹{prediction:,.2f}"

iface = gr.Interface(fn=predict_price, inputs=["text", "number", "number", "number"], outputs="text")
iface.launch()
```

🔹 **Deployed locally using `iface.launch(share=True)`.**  

---

## **🚀 Results & Conclusion**  

### ✅ **Final Outcomes:**  
1. **Successfully built an accurate house price prediction model.**  
2. **Achieved R² score of 0.82** using **Linear Regression**.  
3. **Integrated a web-based Gradio application** for easy user interaction.  
4. **Removed outliers & improved dataset quality** for better predictions.  
5. **Model can generalize well on unseen Bengaluru house data.**  

### 📌 **Future Enhancements:**  
🚀 **Use advanced ML models** like Random Forest or XGBoost for better accuracy.  
🚀 **Deploy the model on a cloud platform** (AWS/GCP) for global accessibility.  
🚀 **Add more features like proximity to schools, hospitals, or metro stations.**  

🔹 **GitHub Repository**: [https://github.com/pawan-skecth/PROJECT-1-Machine-learning-House-Price-Prediction-Regressionn/edit/main/README.md]  

---

## 🎯 **Final Thoughts**  
This project successfully applies **Machine Learning for real-world real estate price predictions**. The **Gradio web app** makes it easy for users to **input details and get price estimates instantly**.  

📌 **Accurate, user-friendly, and easily deployable!** 🚀  

