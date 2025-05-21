# 📊 Dashboard for Supermarket Sales 

This is an interactive dashboard built with [Streamlit](https://streamlit.io/) for visualizing supermarket sales data.  
It uses **pandas** for data manipulation and **plotly** for rich, interactive visualizations.

![alt text](https://github.com/lucianomap/dashboard-for-supermarket-sales/blob/0fde4e9b9a641b2eaa5e68fac59627522b4bce55/images/example.png)

---

## 🚀 Demo

Use the sidebar to select a month and explore sales insights by:

- 📅 **Date** – Total profit per day  
- 🛒 **Product Line** – Profit per product type  
- 🏙️ **City** – Total profit by city  
- 💳 **Payment Method** – Profit distribution by payment type  
- ⭐ **Rating** – Customer ratings per city

---

## 📁 Dataset

The dashboard uses the `supermarket_sales.csv` file as an example to run the script.

---

## 🛠️ Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/lucianomap/dashboard-for-supermarket-sales.git
    cd supermarket-sales-dashboard
    ```

2. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**

    ```bash
    streamlit run dashboard.py
    ```

> ✅ Make sure the `supermarket_sales.csv` file is in the same directory as `dashboard.py`.


---

## 📌 Notes

- The `Date` column is converted to datetime format and filtered by month.
- Visualizations are dynamically updated based on the selected month.
- Layout uses multiple columns for simultaneous charts in a wide format.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
