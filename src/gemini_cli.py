#!/usr/bin/env python3

import argparse
from src.gemini_api import generate_content_from_gemini

def main():
    """
    Parses command-line arguments and interacts with the Gemini API.
    """
    parser = argparse.ArgumentParser(
        description='A CLI tool to interact with Google Gemini AI models.'
    )

    parser.add_argument(
        'prompt',
        type=str,
        help='The prompt to send to the Gemini model.'
    )

    parser.add_argument(
        '-m', '--model',
        type=str,
        default='gemini-1.5-flash',
        help='The Gemini model to use (e.g., gemini-1.5-flash, gemini-1.0-pro).'
    )

    args = parser.parse_args()

    print(f"Sending prompt to model '{args.model}':\n---\n{args.prompt}\n---")

    try:
        generated_text = generate_content_from_gemini(args.prompt, args.model)
        print("\nGemini Response:\n---")
        print(generated_text)
        print("---")
    except Exception as e:
        print(f"Error during CLI execution: {e}")

if __name__ == '__main__':
    main()
