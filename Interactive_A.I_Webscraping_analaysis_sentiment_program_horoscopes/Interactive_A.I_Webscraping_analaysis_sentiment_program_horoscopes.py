import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Function to fetch horoscope text from SunSigns.com
def fetch_horoscope(sign):
    url = f"https://www.sunsigns.com/horoscopes/daily/{sign}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the element containing the horoscope text
    horoscope_text = soup.find('div', class_='horoscope-content').get_text(strip=True)
    return horoscope_text

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

# Function to handle user questions
def ask_horoscope():
    while True:
        user_input = input("Ask me about a horoscope or type 'exit' to quit: ").strip().lower()
        if user_input == 'exit':
            print("Goodbye!")
            break
        
        # Extract zodiac sign from user input
        zodiac_signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 
                        'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']

        # Match input with a zodiac sign
        for sign in zodiac_signs:
            if sign in user_input:
                horoscope = fetch_horoscope(sign)
                sentiment = analyze_sentiment(horoscope)
                print(f"\n{sign.capitalize()} Horoscope: {horoscope}")
                print(f"Sentiment Polarity: {sentiment}\n")
                break
        else:
            print("Sorry, I didn't recognize that zodiac sign. Please try again.")

# Start the AI program
if __name__ == "__main__":
    ask_horoscope()
