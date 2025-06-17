# Welcome Message and Personality
def welcome_message():
    print("Hey there! I'm CryptoBuddy — your friendly crypto sidekick!")
    print("Ask me anything like:")
    print("- Which crypto is trending up?")
    print("- What’s the most sustainable coin?")
    print("- Which crypto should I buy for long-term growth?")
    print("Type 'exit' or 'bye' to quit.\n")


# Sample Crypto Data
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 0.3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 0.6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 0.8
    }
}


#  Bot Logic
def respond_to_query(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"🌱 Invest in {recommend}! It’s eco-friendly and has long-term potential!")

    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        if trending:
            print(f" These cryptos are trending up: {', '.join(trending)}")
        else:
            print(" No cryptos are trending up at the moment.")

    elif "long-term" in user_query or "growth" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 0.7:
                print(f" {coin} is trending up and has a top-tier sustainability score!")
                return
        print(" I couldn't find the perfect long-term coin right now.")

    elif "profit" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                print(f"💰 For profit potential, check out {coin}. High market cap and trending up!")
                return
        print(" No high-profit coins found at the moment.")

    else:
        print(" Sorry, I didn’t quite get that. Try asking about trending, sustainable, or long-term cryptos.")


#  Disclaimer
def disclaimer():
    print("\n DISCLAIMER: Crypto is risky — always do your own research before investing.\n")


#  Main Program
def run_chatbot():
    welcome_message()
    disclaimer()
    while True:
        user_query = input("You: ")
        if user_query.lower() in ['exit', 'bye', 'quit']:
            print("👋 Bye! Stay smart and safe with your crypto choices!")
            break
        respond_to_query(user_query)


#  Run the bot
if __name__ == "__main__":
    run_chatbot()
