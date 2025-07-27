import random
answers = ["✅ Yes, definitely", "❌ Absolutely not", "🤷‍♀️ Ask again later", "⚠️ The signs say no... but who really knows?", "💭 It’s possible, but not likely", "🔥 Yes — but it will cost you", "⏳ Too soon to tell. Be patient", "👀 Only if you are brave enough", "💔 Do not do it. You will regret it", "🌕 Yes — but only under the next full moon" ]


print("🔮 Welcome to the Magic 8-Ball!")
print("Ask me any yes/no question... if you dare")
print(" ")

while True:
    input("Your question: ")
    print("")
    print(f"🧠 The Oracle says... {random.choice(answers)}\n")

    continue_prompt = input("Do you want to ask another question? (yes/no): ").strip().lower()
    print("")

    if continue_prompt != "yes":
        print("Thanks for consulting the Magic 8-Ball. See you next time! 🔮")
        break