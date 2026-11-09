import streamlit as st

st.set_page_config(page_title="متجري الاكتروني",page_icon="🏪")

st.title("🏪متجري اﻻكتروني الاحترافي")
st.write("مرحبا بك! تصفح منتجاتنا المميزة وقم بالشراء مباشرة:")
st.markodown("---")

#المنتج الاول
st.header("📱هاتف ذكي حديت")
st.image("https://unsplash.com", width=300)
st.write("✨ مواصفات رائعة، كاميرا حترافية، وبطارية تدوم طويلا.")
st.subheader("💰 السعر: 1500 ريال")
if st.button("🛒 شراء الهاتف الذكي"):
  st.success("🎉 تهانينا! تم تسجيل طلبك لشراء الهاتف بنجاح!")
