print("Welcome to the Anti-Racist Project.")
print("This Is a Platform to Make the World a Better Place for Everyone.")
# Function to Check the Racism
def check(racist_text):
    # The List of Dictionary Where the Key Indicates the Type and Values are the words to flag.
    toxic_words = {
        "toxic": ["jerk", "pervert", "pathetic", "don't deserve", "hate"],
        "racist": ["nigga", "gypped", "uppity", "peanut gallery", "black", "dark"],
        "vulgar": ["fuck", "shit", "asshole", "cunt", "motherfucker", "ass"],
        "body shaming": ["fat", "slim", "overweight", "underweight"]
    }
    found = False
    text_lower = racist_text.lower()
    # logic of finding and printing the type of words with reccomendation
    for key, value in toxic_words.items():
        for word in value:
            words_in_input = text_lower.split() 
            if word in words_in_input:
                found = True
                print(f"The statement contains '{word}' and the verdict is '{key}'.")
                if key == "toxic":
                    print("The language used was inappropriate.")
                elif key == "racist":
                    print("The statement was racist.")
                elif key == "vulgar":
                    print("The statement was vulgar.")
                else:
                    print("Body shaming is wrong and harmful.")
    # if no racist or Inappropriate word is found then
    if not found:
        print("No toxic or racist language was detected.")
# The variable that inputs the sentence
racist_text = input("Enter the message to validate: ")
print("The engine is starting to analyse.")
check(racist_text)