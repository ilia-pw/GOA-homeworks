# 2) დაწერეთ პროგრამა, სადაც თავდაპირველად მომხმარებელს შემოატანინებთ ანგარიშის პაროლს, შემდეგ 
# შეეკითხეთ რომ გაიმეოროს იქამდე,
# სანამ არ დაემთხვევა შეყვანილი პაროლი.

# 3) შექმენით Number guess game:

# ცვლადში შეინახეთ სასურველი რიცხვი. მომხმარებელს Input-ის მეშვეობით შეეკითხეთ ეცადოს რიცხვის გამოცნობა,
# ვერ გამოცნობის შემთხვევა გამოუტანეთ "Try again" და იქამდე გამოუტანეთ Input ველი სანამ არ გამოიცნობს რიცხვს.
# წარმატებით გამოცნობის შემთხვევაში გამოუტანეთ "You guessed the number sucessfully!".

# num = 5

# num_1=(int(input("gues the number")))
# while num_1 != num:
#     num_1 = (int(input("try agein: ")))
# print("correct answer")
    
    

# 4) შექმენით სია, სადაც შეინახავთ თქვენს საყვარელ ცხოველებს. გამოიტანეთ სიიდან პირველი და ბოლო ელემენტი
# და ერთ ხაზზე დაბეჭდეთ.
# animals = ["ძაღლი","კატა","კოალა","ცხენი"]
# print(animals[0:4:3])

# 5) შექმენით სია და მასში შეინახეთ თქვენი საყვარელი ფერები (მინიმუმ 5). გამოიყენეთ უარყოფითი ინდექსინგი 
# (Negative Indexing) იმისთვის, რომ გამოიტანოთ სიის მესამე ელემენტი.
# color = ["blue","black","white","brown","gray"]
# print(color[-3])

# ----------
# HARD LEVEL:

# შექმენით სახელების სია და მასში დაამატეთ 3 სახელი, თუმცა სამივე სახელი უნდა იყოს მომხმარებლის მიერ შემოტანილი. დაბეჭდეთ სიის მნიშვნელობა.

names = ["ilia","nika","vano"]
name = (names.append(input("Enter your name: ")))
name = (names.append(input("Enter your name: ")))
name = (names.append(input("Enter your name: ")))
print(names)


