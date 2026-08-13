import streamlit as st

st.markdown("# :red[🏋️ คำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลนํ้าหนักและส่วนสูงของคุณ เพื่อนเช็กสุขภาพเบื้องต้น")

weight = st.nimber_input("กรอกนํ้าหนักของคุณ (กิโลกรัม):", min_value=1.0, value=1.0)
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):", min_value=1.0, value=1.0)

if st.botton("คำนวณค่า BMI 🎯"):
  height_m = height_cm / 100
  bmi = weight / (height_m ** 2)

  st.write("---")
  st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

  if bmi < 18.5:
    st.warning("⚠️ คุณมีค่านํ้าหนักน้อยกว่าเกณฑ์ (ผอม)")
  elif 18.5 <= bmi < 23.0:
    st.success("🎉 คุณมีนํ้าหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)")
  elif 23.0 <= bmi < 25.0:
