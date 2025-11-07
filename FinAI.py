import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json
import os

DATA_FILE = "expenses.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = []
