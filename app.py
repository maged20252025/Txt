
import streamlit as st
import os

st.set_page_config(page_title="📂 استخراج أسماء الملفات", layout="centered")
st.title("📂 استخراج أسماء ملفات Word وPDF")

uploaded_files = st.file_uploader("📤 ارفع ملفات Word أو PDF", type=["pdf", "docx", "doc"], accept_multiple_files=True)

if uploaded_files:
    st.success(f"✅ تم رفع {len(uploaded_files)} ملف.")
    
    # استخراج الأسماء بدون الامتداد
    filenames = [os.path.splitext(file.name)[0] for file in uploaded_files]

    # عرض الأسماء
    st.markdown("### 🧾 أسماء الملفات:")
    for name in filenames:
        st.write(f"📄 {name}")
    
    # إعداد محتوى الملف النصي
    txt_content = "\n".join(filenames)
    
    # زر التحميل
    st.download_button(
        label="📥 تحميل الأسماء كملف نصي",
        data=txt_content,
        file_name="file_names.txt",
        mime="text/plain"
    )
else:
    st.info("📎 الرجاء رفع ملفات Word أو PDF.")
