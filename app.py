
import streamlit as st

#الاعدادات  الاساسية للصفحة باللغة ايطالية 
st.set_page_config(page_title="Ago Italy | Negozio Online", page_icon="🏪", layout="centered")

#  عنوان المتجر الرئيسي مخصص لمدينتك Buongiorno 
st.title("Ago Italy 🏪")
st.subheader("Il Tuo Negozio Online professionale a Borgomanero")
st.write("Benvenuto! Esplora i nostri prodotti esclusivi e acquista in totale sicurezza.")

st.markdown("---")

# عرض منتج تجريبي باليورو
st.subheader("Smartphone di Ultima Generazione 📱")
st.write("Specifiche eccezionali, fotocamera professionale con intelligenza artificiale e batteria a lunga durata. ✨")

# السعر الرسمي باليورو €
st.write("### **Prezzo: 399,00 €** 💰")
st.caption("Spedizione rapido e sicura in tutta Italia con fattura legale (Partita IVA.")

st.markdown(" ")

# زر الشراء التفاعلي -تم إصلاحه وحدف الحروف الزائدة
if st.button("Acquista Ora 🛒",use_container_width=True):
  st.success("Grazie per il tuo ordine! Il pagamento è sicuro e l'ordine è in fase di elaborazione.")
  st.balloons()
import streamlit as st
# اضف رقم البارتيتا إيفا وإيميلك العادي مكان الكلمة المكتوبة بالعربي 
st.markdown("---") #هدا يضع خطا فاصلا 
st.markdown(
    """
    <div style='text-align:centre; color: gray; font-size: 14px;'>
        <strong>Ago Italy</strong><br>
        Sede Legale: Borgomanero (NO) , Italia<br>
        Partita IVA: 02845350038<br>
        Email :tnfelmakoudi799@gmail.com
        </div>
        """,
        unsafe_allow_html=True
)
        
