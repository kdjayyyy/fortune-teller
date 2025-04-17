import random

def main():
   # Personal information - REPLACE WITH YOUR ACTUAL INFO
   NAME = "Kinjal Das"  # Replace with your full name
   ADMISSION_NUMBER = "21JE0473"  # Replace with your actual admission number

   # Display welcome message with personal identifiers
   print(f"🔮 Welcome to {NAME}'s Fortune Teller ({ADMISSION_NUMBER}) 🔮")

   # Get user's mood input
   mood = input("How are you feeling today? : ").strip().lower()

   # Fortune messages for each mood
   happy_fortunes = [
      f"✨ Your fortune: Great things await you, {NAME}! Keep smiling. ✨",
      "✨ Your fortune: Your positive energy will bring wonderful opportunities today! ✨",
      "✨ Your fortune: Success is on your horizon. Your happiness is well-deserved! ✨"
   ]

   sad_fortunes = [
      "✨ Your fortune: Better days are coming. This too shall pass. ✨",
      "✨ Your fortune: Every cloud has a silver lining. Yours is coming soon! ✨",
      f"✨ Your fortune: {NAME}, remember that tough times never last, but tough people do! ✨"
   ]

   neutral_fortunes = [
      "✨ Your fortune: Balance is good. New opportunities await you. ✨",
      "✨ Your fortune: Your calm demeanor will help you make the right choices today. ✨",
      "✨ Your fortune: A steady mind leads to steady progress. Stay balanced! ✨"
   ]

   stressed_fortunes = [
      "✨ Your fortune: Take a deep breath. The universe has a plan for you. ✨",
      f"✨ Your fortune: {NAME}, stress is temporary but your strength is permanent. ✨",
      "✨ Your fortune: Soon you'll find clarity and peace. Trust the journey. ✨"
   ]
      
   anxious_fortunes = [
      "✨ Your fortune: The worries of today are preparing you for tomorrow's success. ✨",
      f"✨ Your fortune: {NAME}, your anxiety shows you care deeply. Channel it into positive action. ✨",
      "✨ Your fortune: Focus on what you can control, and let go of what you cannot. Relief awaits. ✨"
   ]
   
   hopeful_fortunes = [
      f"✨ Your fortune: Your optimism will be rewarded, {NAME}. Keep believing! ✨",
      "✨ Your fortune: Hope is the seed from which great achievements grow. Nurture it. ✨",
      "✨ Your fortune: The universe responds to your positive expectations. Good things are coming. ✨"
   ]

   # Generate fortune based on mood
   if mood == "happy":
      print(random.choice(happy_fortunes))
   elif mood == "sad":
      print(random.choice(sad_fortunes))
   elif mood == "neutral":
      print(random.choice(neutral_fortunes))
   elif mood == "stressed":
      print(random.choice(stressed_fortunes))
   elif mood == "anxious":
      print(random.choice(anxious_fortunes))
   elif mood == "hopeful":
      print(random.choice(hopeful_fortunes))
   else:
      print("I'm not sure how to interpret that mood!")

if __name__ == "__main__":
   main()