import streamlit as st

#الاعدادات  الاساسية للصفحة باللغة ايطالية 
st.set_page_config(page_title="Ago Italy | Negozio Online", page_icon="🏪", layout="centered")

#  عنوان المتجر الرئيسي مخصص لمدينتك
st.title("Ago Italy 🏪")
st.subheader("Tl Tuo Negozio Online professionale a Borgomanero")
st.write("Benvenuto! Esplora i nostri prodotti esclusivi e acquista in totale sicurezza.")

st.markdown("---")

# عرض منتج تجريبي باليورو
st.subheader("Smartphone di Ultima Generazione 📱")
st.write("Specifiche eccezionali, fotocamera professionale con intelligenza artificiale e batteria a lunga durata. ✨")

# السعر الرسمي باليورو €
st.write("### **Prezzo: 399,00 €** 💰")
st.caption("Spedizione rapido e sicura in tutta Italia con fattura legale (Partita IVA.")

st.markdown(" ")

# زر الشراء التفاعلي
if st.button("Acquista Ora 🛒",use_container_width=true):
  st.success("Grazie per il tuo ordine! Il pagamento è sicuro e l'ordine è in fase di elaborazione.")
  st.balloons()
