import os
from dotenv import load_dotenv
from openai import OpenAI

# Load your API key from the .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def generate_red_team_advice(task):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # You can change to "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are an expert red team analyst."},
            {"role": "user", "content": f"Provide red team techniques and tools for: {task}"}
        ]
    )
    return response.choices[0].message.content.strip()

def main():
    print("\n=== Red Team Task Automator ===")
    task = input("Enter red team task or scenario: ")
    print("\nGenerating red team advice...\n")
    advice = generate_red_team_advice(task)
    print("💡 Advice:\n")
    print(advice)

if __name__ == "__main__":
    main()

