birthYear = int(input("Enter your birth year: "))

if birthYear >= 1900:
    chineseAnimals = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]
    i = (birthYear - 1900) % 12
    zodiacAnimal = chineseAnimals[i]
    print(f"Your Chinese zodiac animal is: {zodiacAnimal}")
else:
    print("Invalid Year, it should not be earlier than 1900")