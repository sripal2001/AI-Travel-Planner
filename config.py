import google.generativeai as genai

# Set your Google Gemini API Key
genai.configure(api_key="AIzaSyDyjl8neHCv1IoOd1GdpSs2o8pgAR_3Hg8")

def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro-001")  # Correct model name
    response = model.generate_content(prompt)
    return response.text
