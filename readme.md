# 🌱 Python Frameworks Assignment

This project is part of a Python assignment exploring frameworks for **data analysis and visualization**.  
It demonstrates working with **Jupyter Notebooks** for analysis and a **Streamlit app** for interactive visualization.

---

## 📌 Project Purpose

The main goal of this project is to:

- Practice using **Pandas** for data loading and exploration.
- Build **visualizations** with Matplotlib/Seaborn.
- Create a simple **Streamlit app** with interactive widgets.
- Learn how to manage large datasets in GitHub-friendly ways.

---

## 📂 Project Structure

frameworks_assignment/
│
├── notebooks/
│ ├── 01_data_loading.ipynb # Load and inspect dataset
│ ├── 02_visualization.ipynb # Create visualizations
│
├── app.py # Streamlit app
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Ignore large files like CSVs

yaml
Copy code

---

## 📊 Dataset

The dataset (`metadata.csv`) is about **[briefly describe what your dataset contains]**.  
It is too large (>100 MB) to store directly on GitHub.

👉 Download it here: [Download metadata.csv](https://drive.google.com/file/d/1Yvy8MeXmUHEply-68B_fzWLx8jFjKuTN/view?usp=sharing)

After downloading, place it in the project’s root folder:

frameworks_assignment/
│
├── metadata.csv
├── app.py
└── ...

yaml
Copy code

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/frameworks_assignment.git
cd frameworks_assignment
Create a virtual environment (recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
Install requirements:

bash
Copy code
pip install -r requirements.txt
📒 Jupyter Notebook Usage
Launch Jupyter:

bash
Copy code
jupyter notebook
Open the notebooks in the notebooks/ folder and run cells step by step.

🚀 Running the Streamlit App
Run the following command:

bash
Copy code
python -m streamlit run app.py
Then open your browser at http://localhost:8501 to view the app.

The app includes:

A title and description.

Interactive widgets (slider, dropdown).

Visualizations.

A data sample preview.

✅ Requirements
All dependencies are listed in requirements.txt, including:

pandas

numpy

matplotlib

seaborn

streamlit

📌 Notes
The dataset is cached in the app for faster loading.

Large files are excluded from GitHub using .gitignore.


✨ Author
Fadhili
Python Frameworks Assignment – 2025


---










```
