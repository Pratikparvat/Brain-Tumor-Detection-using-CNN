import streamlit as st

st.subheader("Problem Statement: ")
st.title("A Novel Framework for Brain Tumor Detection")



st.markdown("Revolutionizing medical diagnostics, our project focuses on brain tumor detection using cutting-edge Convolutional Neural Networks (CNNs). By leveraging advanced deep learning techniques, we aim to enhance early detection rates, enabling prompt intervention and improved patient outcomes. Through meticulous data collection and preprocessing, we ensure the robustness and accuracy of our model. Rigorous model training and hyperparameter tuning optimize performance, while interpretability techniques provide insights into decision-making processes. With a commitment to ethical standards and collaboration with medical professionals, our endeavor not only advances technological innovation but also prioritizes patient well-being. Together, we're pioneering a transformative approach to healthcare diagnostics.")

st.subheader("Proposed Architecture:")
st.image("images/Proposed_arch.jpeg")

st.subheader('Block Diagram')
st.image("images/flowchart.png")

st.subheader('Convnet Architecture')
st.image("images/convnet_architecture.jpg")

st.markdown("""Understanding the architecture:
Each input x (image) has a shape of (240, 240, 3) and is fed into the neural network. And, it goes through the following layers:

1. A Zero Padding layer with a pool size of (2, 2).\n
2. A convolutional layer with 32 filters, with a filter size of (7, 7) and a stride equal to 1.\n
3. A batch normalization layer to normalize pixel values to speed up computation.\n
4. A ReLU activation layer.\n
5. A Max Pooling layer with f=4 and s=4.\n
6. A Max Pooling layer with f=4 and s=4, same as before.\n
7. A flatten layer in order to flatten the 3-dimensional matrix into a one-dimensional vector.\n
8. A Dense (output unit) fully connected layer with one neuron with a sigmoid activation (since this is a binary classification task).""")