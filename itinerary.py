from config import get_gemini_response

def generate_itinerary(destination, days, interests, budget):
    prompt = f"""
    Plan a {days}-day trip to {destination}. 
    Interests: {interests}, Budget: {budget}.
    Provide a detailed, day-wise itinerary with places to visit, activities, and food recommendations.
    """
    return get_gemini_response(prompt)
