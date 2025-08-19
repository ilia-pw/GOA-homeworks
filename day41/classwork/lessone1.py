# <!-- 1) კომენტარის სახით ახსენით რას აკეთებს len(), append(), insert() და pop() ფუნქციები
# len ფუნქცია თვლის რამდენი ასოა სტრინგში ან რამდენი სტრინგია სიაში
# append() შეგვიძლია ჩავსვათ რაიმე სთრინგი სიაში
#  insert() ინსერტით შეგვიძლია სტრინგი ნებისმიერ ინდექსზე დავსვათ
#  pop() პოპით შეგვიძლია რაიმე სტრინგი სიიდან ამოვიღოთ

# 2) შექმენით სია და შეინახეთ  5 სახელი. მომხმარებელს შემოატანინეთ სახელი და დაამატეთ ამ სიაში.
#  ბოლოს, დაბეჭდეთ ამ სიის სიგრძე და სიის განახლებული ვერსია.


# 3) შექმენით სია: fruits = ["Melon", "Orange", "Cantaloupe", "Watermelon", "Kiwi"]
# ამოაგდეთ სიიდან ბოლო ელემენტი და მესამე ინდექსზე ჩასვით "Pomegranate". -->


names = ["ilia","vano","lika","giorgi","qeti"]
names.append("nino")
print(len(names))


fruits = ["Melon", "Orange", "Cantaloupe", "Watermelon", "Kiwi"]
fruits.insert(3,"Pomegranate")
fruits.pop(-1)
print(fruits)