print("swagat aapka deviyon aur sajanoo\nTo Kaun Banega Crorepati mein")
user_input1 = input("Enter your name:")
print(f"Hamare saamne hai {user_input1} ji\n Toh chaliye hum Khel ka subhaarmbh karte hai")
rules = """
Aapke screen par ek, ek karke prashn puche jayenge uska aapko sahi jawab dena hai 
phele prashn se 14 prashn hai es khel mein jawab aako A/B/C/D mein he dena hai
"""

print(rules)

levels = ["₹5000", "₹10,000", "₹20,000", "₹40,000", "₹80,000", "₹1,60,000", "₹3,20,000", "₹6,40,000", "₹1,250,000",
          "₹2,500,000", "₹50,00,000", "₹1crore", "₹3crore", "₹7crore"]

questions = [
    "1. Current Railway Minister of India is",
    "2. What does not grow on a tree according to a popular Hindi saying?",
    "3. Which city is known as the Pink City in India?",
    "4. Who wrote India's National Anthem?",
    "5. How many religions are there in India?",
    "6. When is the National Hindi Diwas celebrated?",
    "7. How many states are there in India?",
    "8. Where is India Gate located?",
    "9. Who wrote Vande Mataram?",
    "10. Which one of the following places is famous for the Great Vishnu Temple?",
    "11. The largest Buddhist Monastery in India is located at",
    "12. Which of the following musical instruments is NOT of foreign origin?",
    "13. Who among the following was killed during 'Operation Bluestar' of 1984?",
    "14. Which former Indian President died as a result of a road accident?"
]

options = [
    ["A.Mamta Banarjee", "B.Ram Vilash", "C.Ashwini Vaishnaw", "D.Piyush Goyal"],
    ["A.Money", "B.Flowers", "C.Leaves", "D.Fruits"],
    ["A.Bangalore", "B.Mysore", "C.Jaipur", "D.Kochi"],
    ["A.Rabindranath Tagore", "B.Lal Bahadur Shastri", "C.Chetan Bhagat", "D.RK Narayan"],
    ["A.6", "B.7", "C.8", "D.9"],
    ["A.13 September", "B.14 September", "C.14 July", "D.15 August"],
    ["A.28", "B.29", "C.31", "D.30"],
    ["A.Agra", "B.Punjab", "C.Mumbai", "D.New Delhi"],
    ["A.Sarat Chandra Chattopadhyay", "B.Rabindranath Tagore", "C.Bankim Chandra Chatterjee",
     "D.Ishwar Chandra Vidyasagar"],
    ["A.Bordubar, Indonesia", "B.Bamiyan, Afghanistan", "C.Panja Sahib, Pakistan", "D.Ankorvat, Cambodia"],
    ["A.Sarnath, Uttar Pradesh", "B.Tawang, Arunachal Pradesh", "C.Dharmashala, Himachal Pradesh", "D.Gangtok, Sikkim"],
    ["A.Tabla", "B.Flute", "C.Sitar", "D.Violin"],
    ["A.Baba Santa Singh", "B.Haji Mastan", "C.Jarnail Singh Bhindrawale", "D.Homi Jehangir Bhabha"],
    ["A.Rajendra Prasad", "B.Faqruddin Ali Ahmed", "C.Giani Zail Singh", "D.R.Venkatraman"]
]

answers = ["C","A", "C", "A", "A", "B", "A", "D", "C", "D", "B", "B", "C", "C"]

total_winning = 0

for i in range(len(levels)):
    print(f"Aapke screen par {levels[i]} ka prashn")
    print(questions[i])
    for option in options[i]:
        print(option)
    user_input2 = input("Enter your answer (A/B/C/D):")
    if user_input2 == answers[i]:
        print("Correct answer")
        total_winning = levels[i]
    else:
        print("Wrong answer")
        print("Game over")
        break
    if user_input2.lower() == "quit":
        print("Game over")
        break

print(f"You won {total_winning} money")
