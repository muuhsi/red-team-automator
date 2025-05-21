import os
import openai

def generate_red_team_advice(task_description):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    prompt = f"""
    You are a red team assistant. For the given task, provide relevant commands, techniques, or tools to use.

    Task: {task_description}

    Reply with concise and practical suggestions.
    """
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None
    )
    
    advice = response.choices[0].text.strip()
    return advice

def main():
    print("=== Red Team Task Automator ===")
    task = input("Enter red team task or scenario: ")
    advice = generate_red_team_advice(task)
    print("\nSuggested commands/techniques:\n")
    print(advice)

if __name__ == "__main__":
    main()
