import streamlit as st
import requests
import joblib
import pandas as pd

# load model
model = joblib.load('xgbmodel.pkl')

st.title("Prediksi Tingkat Obesitas")
st.write("Masukkan data gaya hidup untuk mengetahui tingkat risiko obesitas.")

# Form input
with st.form("form"):
    gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
    age = st.number_input("Usia", min_value=1, max_value=100, value=25)
    height = st.number_input("Tinggi (meter)", min_value=1.0, max_value=2.5, value=1.7)
    weight = st.number_input("Berat (kg)", min_value=30.0, max_value=200.0, value=70.0)
    history = st.selectbox("Riwayat keluarga obesitas", ["yes", "no"])
    favc = st.selectbox("Sering makan makanan berkalori tinggi?", ["yes", "no"])
    fcvc = st.slider("Frekuensi makan sayur (1-3)", 1.0, 3.0, 2.0)
    ncp = st.slider("Jumlah makan utama per hari", 1.0, 4.0, 3.0)
    caec = st.selectbox("Makan di luar jam makan utama", ["No", "Sometimes", "Frequently", "Always"])
    smoke = st.selectbox("Merokok", ["yes", "no"])
    ch2o = st.slider("Asupan air harian (1-3)", 1.0, 3.0, 2.0)
    scc = st.selectbox("Pantau asupan kalori?", ["yes", "no"])
    faf = st.slider("Frekuensi olahraga (0-3)", 0.0, 3.0, 1.0)
    tue = st.slider("Waktu dengan teknologi (0-3)", 0.0, 3.0, 1.0)
    calc = st.selectbox("Konsumsi alkohol", ["no", "Sometimes", "Frequently", "Always"])
    mtrans = st.selectbox("Moda transportasi", ["Public_Transportation", "Walking", "Motorbike", "Bike", "Automobile"])

    submitted = st.form_submit_button("PREDIKSI")

if submitted:
    # Format data sesuai format backend
    input_data = {
        "Age": age,
        "Height": height,
        "Weight": weight,
        "FCVC": fcvc,
        "NCP": ncp,
        "CAEC": caec,
        "CH2O": ch2o,
        "FAF": faf,
        "TUE": tue
    }

    input_df = pd.DataFrame([input_data])

    #catcols = ['Gender', 'family_history_with_overweight', 'FAVC', 'CAEC',
    #       'SMOKE', 'SCC', 'CALC', 'MTRANS']
    #for col in catcols:
     #   input_df[col] = input_df[col].astype('category')


    pred = model.predict(input_df)[0]

    st.subheader("Hasil Prediksi:")
    st.success(f"Tingkat obesitas: {pred}")

    if pred == 1:
        st.success("APPROVE")
    else:
        st.error("REJECTED")
