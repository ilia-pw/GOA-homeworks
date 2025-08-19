# 2) კომენტარის სახით ახსენით რატომ ვიყენებთ Slicing-ს Python-ში.
# სლაისინგის დახმარებით ჩვენ ვიღებთ რაიმე სტრინგს ან ინტეჯერს სიიდან

# 3) შექმენით რიცხვების სია, სადაც შენახული გექნებათ 10 რიცხვი. Slicing-ის მეშვეობით გამოიტანეთ ამ სიის პირველი ხუთი რიცხვი და გამოიტანეთ 
# ტერმინალში.
num = [1,2,3,4,5,6,7,8,9,10]
print(num[0:5])

# 4) ცვლადში შეინახეთ სიტყვა "Goal-Oriented Academy".
# გამოიყენეთ Slicing რათა აქედან დაბეჭდოთ მხოლოდ სიტყვა "Academy".
name = "Goal-Oriented Academy "
print(name[-8:-1])

# 5) ცვლადში შეინახეთ სიტყვა "Goal-Oriented Academy".
# გამოიყენეთ Slicing რათა აქედან დაბეჭდოთ მხოლოდ სიტყვა "Oriented".
nam ="Goal-Oriented Academy"
print(nam[5:13])

# 6) ცვლადში შეინახეთ თქვენი გვარი. ინდექსინგის საშუალებით გამოიტანეთ თქვენი გვარის პირველი, ბოლო და შუა ასოები.
num1 = ("belqania")
print(num1[0])
print(num1[-1])
print(num1[3])

# 7) შექმენით სია colors = ["Black", "Yellow", "Blue", "Purple", "Orange"]
# სიიდან გამოიტანეთ მხოლოდ Yellow და Black.
colors = ["Black", "Yellow", "Blue", "Purple", "Orange"]
print(colors[0])
print(colors[1])

# 8) შეინახეთ ცვლადში "Hello, World!". Slicing-ის საშუალებით ამ სტრინგიდან  ამოიღეთ ცალკე სიტყვა "Hello" და ცალკე სიტყვა "World!". შეინახეთ ისინი
#  ცვლადებში და გამოიტანეთ ეკრანზე.
num2 = "Hello, World!"
print(num2[0:5])
print(num2[7:13])
