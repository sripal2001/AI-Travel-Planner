import streamlit as st
from itinerary import generate_itinerary
from weather import get_weather
from pdf_generator import save_itinerary_to_pdf

# Streamlit UI Setup
st.set_page_config(page_title="AI Travel Planner", page_icon="🌍", layout="wide")

st.sidebar.title("🌍 AI Travel Planner")
st.sidebar.write("Plan your perfect trip with AI!")

# User Inputs
st.sidebar.subheader("✈️ Travel Details")

source = st.sidebar.text_input("🏠 Source Location:", placeholder="Enter your departure city")
destination = st.sidebar.text_input("📍 Destination:", placeholder="Enter your destination")
travel_date = st.sidebar.date_input("📅 Travel Date:")
days = st.sidebar.slider("📆 Number of Days:", min_value=1, max_value=30, value=5)
passengers = st.sidebar.number_input("👥 Number of Passengers:", min_value=1, value=1)

travel_time = st.sidebar.selectbox("⏰ Preferred Travel Time:", ["Anytime", "Morning", "Afternoon", "Evening", "Night"])

st.sidebar.subheader("🚗 Select Preferred Travel Modes")
travel_modes = st.sidebar.multiselect(
    "Choose Travel Modes:",
    ["Flight", "Train", "Bus", "Car"],
    default=["Flight"]
)

priority = st.sidebar.radio("🔄 Priority:", ["Cheapest", "Fastest", "Best Balance"])

interests = st.sidebar.text_area("🎯 Interests:", placeholder="E.g., Adventure, Museums, Beaches")
budget = st.sidebar.selectbox("💰 Budget Level:", ["Low", "Medium", "High"])

if st.sidebar.button("🚀 Generate Itinerary"):
    if source and destination and days and interests:
        with st.spinner("Generating your AI-powered itinerary..."):
            itinerary = generate_itinerary(destination, days, interests, budget)
            weather = get_weather(destination)
        
        st.subheader("🗺️ Your AI-Generated Itinerary")
        st.markdown(itinerary)

        st.subheader("🌤️ Weather Forecast")
        st.write(weather)

        # Download Itinerary as PDF
        pdf_filename = "travel_itinerary.pdf"
        save_itinerary_to_pdf(itinerary, pdf_filename)
        with open(pdf_filename, "rb") as pdf_file:
            st.download_button(label="📥 Download Itinerary as PDF", data=pdf_file, file_name=pdf_filename)

    else:
        st.sidebar.error("⚠️ Please fill all fields before generating your itinerary.")
