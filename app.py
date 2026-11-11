
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

# ==========================================
# 🤖 أولاً: شات بوت المساعد الافتراضي الذكي
# ==========================================
st.markdown("---")
st.subheader("🤖 Assistente Virtuale - Ago Italy")
st.write("Hai domande sui nostri prodotti o sulla spedizione? Chiedi pure al nostro assistente!")

# تهيئة ذاكرة المحادثة في المتصفح لكي لا تختفي الرسائل عند التحديث
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Ciao! Sono l'assistente virtuale di Ago Italy. Come posso aiutarti oggi? Posso darti informazioni sui nostri prodotti in Vera Pelle o sul pagamento alla consegna!"}
    ]

# عرض الرسائل السابقة للمستخدم
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# استقبال سؤال الزبون والرد عليه تلقائياً بقواعد ذكية
if user_input := st.chat_input("Scrivi qui la tua domanda... (es. Avete il pagamento alla consegna?)"):
    # عرض سؤال المستخدم فوراً
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # تحويل النص إلى حروف صغيرة لتسهيل البحث عن الكلمات المفتاحية
    query = user_input.lower()
    
    # تحديد الرد الذكي بناءً على السؤال باللغة الإيطالية
    if "consegna" in query or "contrassegno" in query or "pagare alla consegna" in query:
        reply = "Sì, assolutamente! Offriamo il servizio di **Pagamento alla Consegna (Contrassegno)** in tutta Italia senza costi aggiuntivi nascosti. Paghi direttamente al corriere quando ricevi la borsa a casa tua! 📦"
    elif "pelle" in query or "materiale" in query or "qualità" in query:
        reply = "Tutti i nostri Cancel prodotti sono realizzati in **Vera Pelle (100% Genuine Leather) e fatti in ...**. Garantiamo la massima qualità e durata nel tempo per ogni borsa! 🇮🇹👜"
    elif "spedizione" in query or "tempo" in query or "tempi" in query:
        reply = "La spedizione in Italia è veloce e tracciabile via corriere espresso (BRT/SDA). Di lavoro impiega **24-48 ore** lavorative per arrivare a casa tua. 🚚"
    elif "prezzo" in query or "costo" in query or "quanto costa" in query:
        reply = "I prezzi delle nostre borse in Vera Pelle variano, ma la nostra fascia media è intorno agli **80 euro**, offrendo un rapporto qualità-prezzo imbattibile per il vero Made in Italy! 💶"
    else:
        reply = "Grazie per la domanda! Siamo felici del tuo interesse per **Ago Italy**. Per questa richiesta specifica o per ordinare, puoi contattarci direttamente alla nostra email: **tnfelmakoudi799@gmail.com** o scriverci su WhatsApp! ✉️"

    # عرض رد الروبوت وحفظه في الذاكرة
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)


# ==========================================
# ⚖️ ثانياً: البيانات القانونية الإلزامية في الأسفل (Footer)
# ==========================================
st.markdown("---") 
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 14px;'>
        <strong>Ago Italy</strong><br>
        Sede Legale: Borgomanero (NO), Italia<br>
        Partita IVA: 02845350038<br>
        Email: tnfelmakoudi799@gmail.com
    </div>
    """, 
    unsafe_allow_html=True
)
