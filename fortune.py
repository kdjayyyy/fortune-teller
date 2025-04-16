# v.1.0 objectives -> including the basic emotions

def main():
   """Main function for the Fortune Teller program."""
   # Display welcome message with personal identifiers
   print("🔮 Welcome to Kinjal Das's Fortune Teller (21JE0473) 🔮")
    
   # Get user's mood input
   mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()
    
   # Generate fortune based on mood
   if mood == "happy":
      print("✨ Your fortune: Great things await you, Kinjal! Keep smiling. ✨")
   elif mood == "sad":
      print("✨ Your fortune: Better days are coming dear Kinjal. This too shall pass. ✨")
   elif mood == "neutral":
      print("✨ Your fortune: Balance is good. New opportunities await you. ✨")
   else:
      print("I'm not sure how to interpret that mood. Try happy, sad, or neutral.")

if __name__ == "__main__":
   main()