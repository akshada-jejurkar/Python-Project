# 🌈 Akshada's Daily Mood Tracker (Core Python Project)

from datetime import datetime

MOOD_FILE = "mood_log.txt"

def log_today_mood():
    today = datetime.now().strftime("%Y-%m-%d")
    mood = input("💬 How are you feeling today (Happy, Sad, Anxious, Excited, etc.)? ")
    note = input("📝 Any notes you'd like to add? (optional): ")

    with open(MOOD_FILE, "a") as file:
        file.write(f"{today} | Mood: {mood} | Note: {note}\n")

    print("✅ Mood logged successfully!\n")

def view_mood_history():
    print("\n📖 Your Mood History:\n")
    try:
        with open(MOOD_FILE, "r") as file:
            logs = file.readlines()
            if logs:
                for log in logs:
                    print(log.strip())
            else:
                print("⚠️ No entries found.")
    except FileNotFoundError:
        print("⚠️ No mood log file found. Start by logging today's mood.\n")

def main():
    print("🌈 Welcome to Akshada's Daily Mood Tracker")
    print("Track how you feel and reflect on your emotions.\n")

    while True:
        print("🔹 Menu:")
        print("1. Log Today's Mood")
        print("2. View Mood History")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            log_today_mood()
        elif choice == "2":
            view_mood_history()
        elif choice == "3":
            print("👋 Take care! Come back tomorrow to log your mood.")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
