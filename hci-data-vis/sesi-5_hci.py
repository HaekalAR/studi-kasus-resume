import streamlit as st
import pandas as pd

st.title("Dashboard Nilai Mahasiswa (Data Contoh)")
df = pd.DataFrame({
    "Mata Kuliah": ["ML", "IoT", "PBKK", "PPL"],
    "Rata-rata": [78, 82, 75, 88],
})
pilihan = st.multiselect("Pilih mata kuliah", df["Mata Kuliah"], default=list(df["Mata Kuliah"]))
st.bar_chart(df[df["Mata Kuliah"].isin(pilihan)].set_index("Mata Kuliah"))