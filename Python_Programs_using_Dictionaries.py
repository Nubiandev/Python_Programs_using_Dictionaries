#Horoscope Program using dictionaries and if & then statements

from datetime import datetime

def get_horoscope():
    horoscope_dates = {
        "Capricorn": [(12, 22), (1, 19)],
        "Aquarius": [(1, 20), (2, 18)],
        "Pisces": [(2, 19), (3, 20)],
        "Aries": [(3, 21), (4, 19)],
        "Taurus": [(4, 20), (5, 20)],
        "Gemini": [(5, 21), (6, 20)],
        "Cancer": [(6, 21), (7, 22)],
        "Leo": [(7, 23), (8, 22)],
        "Virgo": [(8, 23), (9, 22)],
        "Libra": [(9, 23), (10, 22)],
        "Scorpio": [(10, 23), (11, 21)],
        "Sagittarius": [(11, 22), (12, 21)],
        "Capricorn": [(12, 22), (1, 19)]  # Capricorn spans December and January
    }

    while True:
        try:
            # Prompts end user to enter their birthday:
            birthday_input = input("Please enter your birthday (MM-DD): ")
            birthday = datetime.strptime(birthday_input, "%m-%d")

            # Extracts month & day 
            month = birthday.month
            day = birthday.day

            # Determines horoscope 
            for sign, ((start_month, start_day), (end_month, end_day)) in horoscope_dates.items():
                if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
                    print(f"Your horoscope sign is: {sign}")
                    return

            print("Invalid date. Please enter a valid date, and try again.")

        except ValueError:
            print("Invalid format. Please enter the date in the following format: MM-DD.")

# Calls function 
get_horoscope()
