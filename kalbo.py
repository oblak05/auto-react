import requests
import json

def get_user_input():
    link = input("Enter the Facebook post link: ")
    quantity = int(input("Enter the number of reactions (up to 10,000): "))
    reaction_type = input("Enter the reaction type (like, love, haha, wow, sad, angry): ")
    token = input("Enter your Facebook token: ")
    return link, quantity, reaction_type, token

def send_reaction(link, reaction_type, token):
    url = f"https://graph.facebook.com/v12.0/{link}/reactions"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "type": reaction_type
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 200

def main():
    link, quantity, reaction_type, token = get_user_input()
    
    for _ in range(quantity):
        success = send_reaction(link, reaction_type, token)
        if success:
            print("Reaction sent successfully!")
        else:
            print("Failed to send reaction. Check your token or link.")

if __name__ == "__main__":
    main()
