import streamlit as st;

st.title("Dataset")
st.text("You can Download Dataset from Each model described below from Here ")
st.link_button("DataSet 1", "https://github.com/MohamedAliHabib/Brain-Tumor-Detection/tree/master/augmented%20data")
st.link_button("DataSet 2", "https://www.kaggle.com/datasets/salikhussaini49/brain-image-clean")

st.title("Model")
st.text("You can see our implemented Model from clicking Here ")
st.link_button("Model 1", "https://github.com/Pratikparvat/BE_Project_stage-1")
st.link_button("Model 2", "https://www.kaggle.com/code/pratikparvat/brain-tumor-prediction-be-project")


st.title("Project Report")
st.text("You can Download Project Report from Button Here ")

with open("Stage1_Report_2023_24.pdf", "rb") as f:
        pdf_bytes = f.read()
st.download_button(
    label="Download PDF",
    data=pdf_bytes,
    file_name="Report.pdf",
    mime="application/pdf"
)
