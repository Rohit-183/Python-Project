print("swaagat hai aapka deviyon aur sajanoo")
print("Kaun banega crorepati me")
name = input("Enter your Name:")
print(f"Hamare saamne hai {name} ji")
print(f"Chaliye toh {name} ji Khel ka shubhaarambh karte hai ")

levels = ["₹5000","₹10,000","₹20,000","₹40,000","₹80,000","₹1,60,000","₹3,20,000","₹6,40,000","₹1,250,000","₹2,500,000","₹50,00,000","₹1crore","₹3crore","₹7crore"]

questions = [
    "1. Current Railway Minister of India is",
    "2. Which god is also known as ‘Gauri Nandan’?",
    "3. What does not grow on tree according to a popular Hindi saying?",
    "4. Which city is known as Pink City in India?",
    "5. Who wrote India's National Anthem?",
    "6. How many religions are there in India?",
    "7. When is the National Hindi Diwas celebrated?",
    "8. How many states are there in India?",
    "9. Where in India Gate located?",
    "10. Who wrote Vande Mataram?",
    "11. Which one of the following places is famous for the Great Vishnu Temple?",
    "12. The largest Buddhist Monastery in India is located at",
    "13. Which of the following musical instruments is NOT of foreign origin?",
    "14. Who among the following was killed during 'Operation Bluestar' of 1984?",
    "15. Which former Indian President died as a result of a road accident?"

]

options = [
    ["A.Mamta Banarjee","B.Ram Vilash","C.Ashwini Vaishnaw","D.Piyush Goyal"],
    ["A.Agni","B.Indra","C.Hanuman","D.Ganesha"],
    ["A.Money","B.Flowers","C.Leaves","D.Fruits"],
    ["A.Banglore","B.Maysore","C.Jaipur","D.Kochi"],
    ["A.Rabindranath Tagore","B.Lal Bahadur Shastri","C.Chetan Bhagat","D.RK Narayan"],
    ["A.6","B.7","C.8","D.9"],
    ["A.13 September","B.14 September","C.14 July","D.15 August"],
    ["A.28","B.29","C.31","D.30"],
    ["A.Agra","B.Punjab","C.Mumbai","D.New Delhi"],
    ["A.Sarat Chandra Chattopadhyay","B.Rabindranath Tagore","C.Bankim Chandra Chatterjee","D.Ishwar Chandra Vidyasagar"],
    ["A.Bordubar,Indonesia","B.Bamiyan,Afghanistan","C.Panja Sahib,Pakistan","D.Ankorvat,Cambodia"],
    ["A.Sarnath,Uttar Pradesh","B.Tawang,Arunachal Pradesh","C.Dharmashala,Himachal Pradesh","D.Gangtok,Sikkim"],
    ["A.Tabla","B.Flute","C.Sitar","D.Violin"],
    ["A.Baba Santa Singh","B.Haji Mastan","C.Jarnail Singh Bhindrawale","D.Homi Jehangir Bhabha"],
    ["A.Rajendra Prasad","B.Faqruddin Ali Ahmed","C.Giani Zail Singh","D.R.Venkatraman"]
]

answers = ["C","D","A","C","A","A","B","A","D","C","D","B","B","C","C"]

for i in range(len(levels)):
    print(f" Aapke screen par {levels[i]} ka prashna")
    print(questions[i])
    for option in options[i]:
        print(option)
    user_answers = input("Enter your answer(A/B/C/D):")
    if user_answers == answers[i]:
        print("Correct Answers")
        total_winning = levels[i]
    else:
        print("Wrong Answers")
        print("Game Over!!!")
        break
print(f"You can take {total_winning} with you ")
