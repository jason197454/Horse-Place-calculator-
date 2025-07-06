
import streamlit as st
from fractions import Fraction

# Title
st.title("Horse Racing Place Probability & Profit Calculator (Fractional Odds)")

# User inputs
fraction_input = st.text_input("Enter Fractional Odds (e.g., 5/2, 1/1, 7/4):", value="2/1")
stake = st.number_input("Enter Stake (£):", min_value=0.0, step=1.0, value=10.0)

# Convert fractional odds to decimal odds
try:
    frac = Fraction(fraction_input)
    odds = float(frac) + 1
except (ValueError, ZeroDivisionError):
    st.error("Please enter valid fractional odds like 5/2 or 1/1")
    st.stop()

# Estimate place probability based on decimal odds
if odds < 1.31:
    place_prob = 96
elif odds < 1.51:
    place_prob = 93.5
elif odds < 1.81:
    place_prob = 90
elif odds < 2.01:
    place_prob = 86
elif odds < 2.51:
    place_prob = 81
elif odds < 3.01:
    place_prob = 75
elif odds < 4.01:
    place_prob = 68.5
elif odds < 6.01:
    place_prob = 61.5
elif odds < 9.01:
    place_prob = 54
elif odds < 13.01:
    place_prob = 46
else:
    place_prob = 37

# Place odds calculation (1/5th of SP)
place_odds = round((odds - 1) / 5 + 1, 2)

# Profit or Loss calculations
profit_if_placed = stake * (place_odds - 1)
loss_if_unplaced = -stake

# Display results
st.markdown(f"**Entered Odds:** {fraction_input} (Decimal: {odds:.2f})")
st.markdown(f"**Estimated Place Probability:** {place_prob}%")
st.markdown(f"**Place Odds:** {place_odds} (approx)")
st.markdown(f"**Profit if Placed:** £{profit_if_placed:.2f}")
st.markdown(f"**Loss if Unplaced:** £{loss_if_unplaced:.2f}")
