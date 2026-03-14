import os
import sys

# Make the parent folder importable so `src` (sibling folder) can be imported.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.predict import predict_score

st.title("🏏 CricketIQ ML")

runs = st.number_input("Current Runs", 0, 200)
balls = st.number_input("Balls Faced", 1, 120)

if st.button("Predict Final Score"):

    pred = predict_score(runs, balls)

    st.success(f"Predicted Final Score: {int(pred)}")