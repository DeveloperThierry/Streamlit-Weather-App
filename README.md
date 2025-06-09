## 📺 Video Demonstration

Watch the full demo video on YouTube here:
🎥 **[https://youtu.be/G6Y-0hBpHT0](https://youtu.be/G6Y-0hBpHT0)**

[![Watch the demo video](https://img.youtube.com/vi/G6Y-0hBpHT0/0.jpg)](https://youtu.be/G6Y-0hBpHT0)

# 🛠️ Setup Instructions – My Streamlit Weather Dashboard

This guide will help you install and run the **Streamlit-based real-time weather dashboard**. It provides interactive forecasts, maps, visualizations, and UI customization.

---

## 📦 Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- `pip` (Python package manager)

---

## 🔧 Installation Steps

1.  **Clone the Repository**

    ```bash
    git clone [https://github.com/yourusername/streamlit-weather-app.git](https://github.com/yourusername/streamlit-weather-app.git)
    cd streamlit-weather-app
    ```

2.  **(Optional) Create a Virtual Environment**

    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

    > Or install packages manually if no `requirements.txt`:

    ```bash
    pip install streamlit pandas numpy requests
    ```

4.  **Set Up Streamlit Secrets**

    Instead of a `.env` file, you will use Streamlit's secrets management.

    Create a file named `.streamlit/secrets.toml` in the root of your project (you might need to create the `.streamlit` directory).

    Add your API key to this file:

    ```toml
    API_KEY = "your_openweathermap_api_key"
    ```

    Make sure your Streamlit application (`app.py`) includes the following to access the secret:

    ```python
    import streamlit as st

    API_KEY = st.secrets["API_KEY"]
    ```

---

## 📂 Project Structure

streamlit-weather-app/
├── app.py                       # Main Streamlit application
├── .streamlit/
│   └── secrets.toml             # Secure API key storage
├── requirements.txt             # Dependencies list
└── README.md                    # This file


---

## 🚀 Running the App

Use this command in the terminal:

```bash
streamlit run app.py
```

Your default browser will open at [http://localhost:8501](http://localhost:8501)

---

## 🎨 Features

- 🌤️ Search real-time weather by city
- 🌡️ View basic and advanced weather metrics
- 📊 Line and bar charts for temperature and other metrics
- 🗺️ Interactive map showing selected city's coordinates
- 🎛️ UI widgets: text input, sliders, buttons, checkboxes, radio
- 🎨 Custom text color picker
- ✅ User feedback boxes for success, warnings, and errors

---

## ✅ Notes

- OpenWeatherMap API is required.
- App supports 1–5 day forecast simulation.
- Custom color settings affect text only, for better visual accessibility.

---

## 🔗 Repository

[GitHub Repo: developerthierry/streamlit-weather-app](https://github.com/DeveloperThierry/Streamlit-Weather-App?tab=readme-ov-file)

---

## 📄 License

This project is provided for educational use under the MIT License.

---

## 🙋 Author

**Thierry Laguerre**  
GitHub: [@developerthierry](https://github.com/developerthierry)
