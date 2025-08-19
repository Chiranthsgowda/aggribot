import google.generativeai as genai
from src.config import GOOGLE_API_KEY

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Model configuration (tunable settings)
generation_config = {
    "temperature": 0.5,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 4096,
}

# Create model with config
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=generation_config,
)


def get_gemini_response(prompt: str) -> str:
    """
    Sends a text prompt to Gemini and returns the response.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip() if response and response.text else "No response received."
    except Exception as e:
        return f"Error: {str(e)}"
