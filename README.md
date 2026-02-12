# 🚘 AutoEconomix

AutoEconomix is a Machine Learning web application that predicts the price of used vehicles based on various features such as brand, model, fuel type, kilometers driven, city, and vehicle age.

This project demonstrates end-to-end ML engineering — from data preprocessing and model training to building a deployable web interface using Streamlit.

---

## 📌 Features

- 🚗 Used Car Price Prediction
- 🧠 Random Forest Regressor Model
- 🔄 Automated Preprocessing Pipeline (OneHotEncoder + StandardScaler)
- 🎛 Interactive Web UI using Streamlit
- 💾 Saved Model with Joblib
- 📂 Clean Project Structure

---

## 🧠 Machine Learning Approach

### Data Processing
- Extracted `brand` and `model` from `car_name`
- Converted `year_of_manufacture` into `age`
- Handled categorical features using OneHotEncoder
- Scaled numeric features using StandardScaler

### Model Used
- RandomForestRegressor (Scikit-learn)
- Pipeline used to combine preprocessing and model training
- Model serialized using Joblib

---

## 🗂 Project Structure

Good. Now we make this look like a serious project — not a casual upload.

Copy everything below and replace your entire README.md with this:

# 🚘 AutoEconomix

AutoEconomix is a Machine Learning web application that predicts the price of used vehicles based on various features such as brand, model, fuel type, kilometers driven, city, and vehicle age.

This project demonstrates end-to-end ML engineering — from data preprocessing and model training to building a deployable web interface using Streamlit.

---

## 📌 Features

- 🚗 Used Car Price Prediction
- 🧠 Random Forest Regressor Model
- 🔄 Automated Preprocessing Pipeline (OneHotEncoder + StandardScaler)
- 🎛 Interactive Web UI using Streamlit
- 💾 Saved Model with Joblib
- 📂 Clean Project Structure

---

## 🧠 Machine Learning Approach

### Data Processing
- Extracted `brand` and `model` from `car_name`
- Converted `year_of_manufacture` into `age`
- Handled categorical features using OneHotEncoder
- Scaled numeric features using StandardScaler

### Model Used
- RandomForestRegressor (Scikit-learn)
- Pipeline used to combine preprocessing and model training
- Model serialized using Joblib

---

## 🗂 Project Structure



AutoEconomix/
│
├── data/
│ ├── cars.csv
│ └── bikes.csv
│
├── model/
│ └── CarRandomForestRegressor.pkl
│
├── notebooks/
│ ├── car.ipynb
│ └── bike.ipynb
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md


---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

git clone https://github.com/YOUR_USERNAME/AutoEconomix.git

cd AutoEconomix


### 2️⃣ Create Virtual Environment (Recommended)

python -m venv venv
venv\Scripts\activate (Windows)


### 3️⃣ Install Dependencies

pip install -r requirements.txt


### 4️⃣ Run the Streamlit App


The application will open in your browser.

---

## 📊 Input Features (Car Model)

- Brand
- Model
- Kilometers Driven
- Fuel Type
- City
- Age (calculated from year of manufacture)

---

## 🔮 Example Prediction Flow

1. User selects car brand and model
2. User enters kms driven and age
3. Model pipeline preprocesses input
4. Random Forest predicts price
5. Estimated price displayed instantly

---

## 📦 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Git

---

## 📈 Future Improvements

- Add Bike Price Prediction (Unified Vehicle Selector)
- Deploy to Streamlit Cloud
- Add Model Evaluation Metrics Display
- Improve UI Styling
- Add Feature Importance Visualization

---

## 👨‍💻 Author

**Aayush Pardeshi**  
PG-DAC | MCA Graduate | Software Developer  
Passionate about Machine Learning and Full Stack Development

---

## 📜 License

This project is for educational and portfolio purposes.
