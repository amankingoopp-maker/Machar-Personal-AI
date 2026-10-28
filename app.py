

# Machar Personal AI
# Basic Hindi/Hinglish assistant

def get_reply(message):
    text = message.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey", "नमस्ते"]):
        return "Namaste! Main Machar Personal AI hoon. Bataiye, main aapki kya madad kar sakta hoon?"

    if any(word in text for word in ["नाम", "name"]):
        return "Mera naam Machar Personal AI hai."

    if any(word in text for word in ["कैसे हो", "kaise ho"]):
        return "Main bilkul theek hoon! Aap kaise hain?"

    if any(word in text for word in ["समय", "time"]):
        return "Mujhe abhi live time jaanne ke liye phone ki clock dekhni hogi."

    if any(word in text for word in ["धन्यवाद", "thanks", "thank you"]):
        return "Aapka swagat hai!"

    return (
        "Main Machar Personal AI hoon. "
        "Abhi mera offline AI model connect nahi hua hai. "
        "Aap apna sawaal doosre tareeke se pooch sakte hain."
    )


if __name__ == "__main__":
    while True:
        try:
            message = input("Aap: ")
            if message.lower().strip() in ["exit", "quit", "band"]:
                break
            print("Machar AI:", get_reply(message))
        except (EOFError, KeyboardInterrupt):
            break
