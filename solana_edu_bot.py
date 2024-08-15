#!/usr/bin/env python3

import os
import json
from termcolor import colored
import pytgpt.phind as phind
from typing import List, Dict

# Initialize LLM interaction
bot = phind.PHIND()

# Constants
CONFIG_FILE = "solana_bot_config.json"
HISTORY_FILE = "conversation_history.json"

def load_config() -> Dict:
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"api_key": "", "model": "gpt-3.5-turbo"}

def save_config(config: Dict):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def load_history() -> List[Dict]:
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history: List[Dict]):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)

def print_header(text: str):
    print(colored("=" * len(text), "green"))
    print(colored(text, "yellow"))
    print(colored("=" * len(text), "green"))

def get_bot_response(prompt: str) -> str:
    config = load_config()
    return bot.chat(prompt, model=config["model"])

def explain_concept():
    print_header("Explain a Solana Concept")
    concept = input(colored("Enter the Solana concept you'd like to learn about: ", "cyan"))
    prompt = f"Explain the concept of {concept} in Solana in simple terms. Include its importance and practical applications."
    explanation = get_bot_response(prompt)
    print(colored("Explanation:", "blue"))
    print(explanation)
    return {"type": "explanation", "concept": concept, "explanation": explanation}

def generate_code():
    print_header("Generate Solana Code")
    task = input(colored("What code would you like to generate (e.g., a basic smart contract, a token transfer script)? ", "cyan"))
    prompt = f"""Generate a {task} in Rust for the Solana blockchain. Include the following:
    1. A brief explanation of what the code does
    2. The complete code snippet
    3. Instructions on how to compile and deploy the code
    4. Any necessary dependencies or setup required"""
    response = get_bot_response(prompt)
    print(colored("Generated Code and Instructions:", "blue"))
    print(response)
    return {"type": "code_generation", "task": task, "response": response}

def interactive_learning():
    print_header("Interactive Learning")
    topic = input(colored("What would you like to learn interactively (e.g., how to deploy a DApp on Solana)? ", "cyan"))
    prompt = f"""Provide a step-by-step interactive guide on {topic} for the Solana blockchain. For each step:
    1. Explain what needs to be done
    2. Provide any necessary code snippets
    3. Explain the purpose of each step
    4. Include checkpoints to ensure understanding before moving to the next step"""
    guide = get_bot_response(prompt)
    print(colored("Interactive Guide:", "blue"))
    print(guide)
    return {"type": "interactive_learning", "topic": topic, "guide": guide}

def solana_market_analysis():
    print_header("Solana Market Analysis")
    aspect = input(colored("What aspect of the Solana market would you like to analyze (e.g., price trends, adoption rates, competitor comparison)? ", "cyan"))
    prompt = f"""Provide a detailed analysis of {aspect} in the Solana market. Include:
    1. Current state and recent trends
    2. Factors influencing the {aspect}
    3. Potential future scenarios
    4. Implications for developers and investors"""
    analysis = get_bot_response(prompt)
    print(colored("Market Analysis:", "blue"))
    print(analysis)
    return {"type": "market_analysis", "aspect": aspect, "analysis": analysis}

def debug_solana_code():
    print_header("Debug Solana Code")
    code = input(colored("Paste your Solana code here (press Enter twice when done):\n", "cyan"))
    issue = input(colored("Describe the issue you're encountering: ", "cyan"))
    prompt = f"""Debug the following Solana code:

    {code}

    Issue: {issue}

    Provide:
    1. Identification of potential problems
    2. Suggested fixes
    3. Explanation of why these issues might be occurring
    4. Best practices to avoid similar issues in the future"""
    debug_response = get_bot_response(prompt)
    print(colored("Debugging Suggestions:", "blue"))
    print(debug_response)
    return {"type": "debugging", "code": code, "issue": issue, "suggestions": debug_response}

def main():
    history = load_history()
    while True:
        print_header("Advanced Solana Education & Simulation Bot")
        print(colored("1. Explain a Solana Concept", "yellow"))
        print(colored("2. Generate Solana Code", "yellow"))
        print(colored("3. Interactive Learning", "yellow"))
        print(colored("4. Solana Market Analysis", "yellow"))
        print(colored("5. Debug Solana Code", "yellow"))
        print(colored("6. View Conversation History", "yellow"))
        print(colored("7. Configure Bot", "yellow"))
        print(colored("8. Exit", "yellow"))
        
        choice = input(colored("Choose an option: ", "cyan"))
        
        if choice == '1':
            result = explain_concept()
        elif choice == '2':
            result = generate_code()
        elif choice == '3':
            result = interactive_learning()
        elif choice == '4':
            result = solana_market_analysis()
        elif choice == '5':
            result = debug_solana_code()
        elif choice == '6':
            print_header("Conversation History")
            for i, item in enumerate(history, 1):
                print(f"{i}. {item['type'].capitalize()}: {item.get('concept') or item.get('task') or item.get('topic') or item.get('aspect')}")
            continue
        elif choice == '7':
            config = load_config()
            config["api_key"] = input(colored("Enter your API key (press Enter to keep current): ", "cyan")) or config["api_key"]
            config["model"] = input(colored("Enter preferred model (e.g., gpt-3.5-turbo, gpt-4): ", "cyan")) or config["model"]
            save_config(config)
            print(colored("Configuration updated.", "green"))
            continue
        elif choice == '8':
            print(colored("Goodbye!", "green"))
            break
        else:
            print(colored("Invalid choice, please try again.", "red"))
            continue
        
        history.append(result)
        save_history(history)

if __name__ == "__main__":
    main()
