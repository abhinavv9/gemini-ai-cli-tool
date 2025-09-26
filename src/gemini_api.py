# src/gemini_api.py

import os
import google.generativeai as genai

# Configure the generative AI client with your API key
API_KEY = os.getenv('GOOGLE_API_KEY')

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable not set.")

genai.configure(api_key=API_KEY)

def generate_content_from_gemini(prompt: str, model_name: str = "gemini-1.5-flash") -> str:
    """
    Sends a prompt to the specified Gemini model and returns the generated content.

    Args:
        prompt: The text prompt to send to the AI.
        model_name: The name of the Gemini model to use (default is 'gemini-1.5-flash').

    Returns:
        The generated text content from the AI.

    Raises:
        Exception: If there's an error during the API call.
    """
    try:
        # Initialize the generative model
        model = genai.GenerativeModel(model_name)

        # Generate content
        response = model.generate_content(prompt)

        # Extract and return the text from the response
        if response and response.text:
            return response.text
        else:
            return "No content generated."

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error generating content."

if __name__ == '__main__':
    # Example usage when running this script directly
    sample_prompt = "Tell me a short, funny story about a robot learning to cook."
    print(f"Sending prompt: '{sample_prompt}' to Gemini...")
    generated_text = generate_content_from_gemini(sample_prompt)
    print("\nGenerated Response:")
    print(generated_text)
