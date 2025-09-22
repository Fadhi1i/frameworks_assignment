import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load the dataset
@st.cache_data
@st.cache_data
def load_data():
    return pd.read_csv("metadata.csv", low_memory=False, nrows=5000)  # only first 5k rows

df = load_data()

# --- Title & description ---
st.title("CORD-19 Metadata Explorer")
st.write("Explore COVID-19 research papers from the CORD-19 dataset.")

# --- Show a sample of the data ---
st.subheader("Sample Data")
st.dataframe(df.head(20))

# --- Interactive filters ---
st.subheader("Filters")
year = st.slider("Select Publication Year", 2010, 2025, 2020)
filtered = df[df['publish_time'].str.contains(str(year), na=False)]

st.write(f"Number of papers in {year}: {len(filtered)}")

# --- Visualization 1: Publications over time ---
st.subheader("Publications Over Time")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
yearly_counts = df['publish_time'].dt.year.value_counts().sort_index()

fig, ax = plt.subplots()
yearly_counts.plot(kind='bar', ax=ax)
ax.set_title("Number of Publications per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# --- Visualization 2: Word Cloud from Titles ---
st.subheader("Word Cloud of Paper Titles")
text = " ".join(df['title'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
