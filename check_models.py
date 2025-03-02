import google.generativeai as genai

# Set your Google API Key
genai.configure(api_key="AIzaSyDyjl8neHCv1IoOd1GdpSs2o8pgAR_3Hg8")

# List available models
models = genai.list_models()

# Print available models
print("Available Gemini Models:")
for model in models:
    print(model.name)
