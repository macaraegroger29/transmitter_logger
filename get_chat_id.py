import requests
import json

BOT_TOKEN = "8561232630:AAE9MmFmcpp5G_SOdlsFqQwfPwOywjeKW-E"
url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

print("Checking for messages to your bot...")
print("IMPORTANT: You must send a message to your bot on Telegram FIRST.")

try:
    response = requests.get(url)
    data = response.json()
    
    if data.get("ok"):
        results = data.get("result", [])
        if not results:
            print("\n❌ No messages found.")
            print("Please open Telegram, find your bot, and send it a message (like 'Hello'). Then run this script again.")
        else:
            # Get the chat ID from the last message
            last_message = results[-1]
            chat_id = last_message.get("message", {}).get("chat", {}).get("id")
            first_name = last_message.get("message", {}).get("from", {}).get("first_name")
            
            print(f"\n✅ SUCCESS!")
            print(f"User: {first_name}")
            print(f"Your CHAT_ID is: {chat_id}")
            print("\nCopy this number and paste it into transmitter_logger.py")
    else:
        print(f"\n❌ Telegram Error: {data.get('description')}")

except Exception as e:
    print(f"\n❌ Error: {e}")
