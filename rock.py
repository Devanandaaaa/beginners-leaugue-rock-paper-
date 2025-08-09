import random


choices = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️",
    "lizard": "🦎",
    "spock": "🖖"
}

# Rules 
rules = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

print("🎮 Rock Paper Scissors Lizard Spock 🎮")
print("Choices: rock 🪨, paper 📄, scissors ✂️, lizard 🦎, spock 🖖")

#  choice
player_choice = input("Enter your choice: ").strip().lower()
if player_choice not in choices:
    print("❌ Invalid choice! Please run again.")
    exit()

# Computer choice
computer_choice = random.choice(list(choices.keys()))

# Show choices
print(f"\nYou chose: {choices[player_choice]} ({player_choice})")
print(f"Computer chose: {choices[computer_choice]} ({computer_choice})\n")

# winner
if player_choice == computer_choice:
    print("🤝 It's a tie!")
elif computer_choice in rules[player_choice]:
    print("✅ You win!")
else:
    print("💀 You lose!")
