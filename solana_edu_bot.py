#!/usr/bin/env python3
import os
from termcolor import colored
import pytgpt.phind as phind

# Initialize LLM interaction
bot = phind.PHIND()

def print_header(text):
    print(colored("=" * len(text), "green"))
    print(colored(text, "yellow"))
    print(colored("=" * len(text), "green"))

def explain_concept():
    print_header("Explain a Solana Concept")
    concept = input(colored("Enter the Solana concept you'd like to learn about: ", "cyan"))
    prompt = f"Explain the concept of {concept} in Solana in simple terms."
    explanation = bot.chat(prompt)
    print(colored("Explanation:", "blue"))
    print(explanation)

def generate_code():
    print_header("Generate Solana Code")
    task = input(colored("What code would you like to generate (e.g., a basic smart contract, a token transfer script)? ", "cyan"))
    prompt = f"Generate a {task} in Rust for the Solana blockchain."
    code_snippet = bot.chat(prompt)
    print(colored("Generated Code:", "blue"))
    print(code_snippet)

def interactive_learning():
    print_header("Interactive Learning")
    topic = input(colored("What would you like to learn interactively (e.g., how to deploy a DApp on Solana)? ", "cyan"))
    prompt = f"Provide a step-by-step interactive guide on {topic} for the Solana blockchain."
    guide = bot.chat(prompt)
    print(colored("Interactive Guide:", "blue"))
    print(guide)

def main():
    while True:
        print_header("Solana Education & Simulation Bot")
        print(colored("1. Explain a Solana Concept", "yellow"))
        print(colored("2. Generate Solana Code", "yellow"))
        print(colored("3. Interactive Learning", "yellow"))
        print(colored("4. Exit", "yellow"))

        choice = input(colored("Choose an option: ", "cyan"))

        if choice == '1':
            explain_concept()
        elif choice == '2':
            generate_code()
        elif choice == '3':
            interactive_learning()
        elif choice == '4':
            print(colored("Goodbye!", "green"))
            break
        else:
            print(colored("Invalid choice, please try again.", "red"))

if __name__ == "__main__":
    main()
