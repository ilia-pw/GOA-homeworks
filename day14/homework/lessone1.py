# 2) გახსენეთ და დაწერეთ თუ რა შედეგს ვიღებს შედარების და ლოგიკური ოპერაციების გამოყენებისას.
# True,False

# 3) ჩამოწერეთ ყველა შესაძლო ლოგიკური გამოსახულება (and და or ოპერატორების გამოყენებით)
True or True
False or False
False or True

True and True
False and False
False and True
# 4)  რას გამოიტანს მოცემული კოდები?

# • False or True and True and False -- False

# • True and False or False or True -- True

# • True or True and False or True or False and True or False -- True

# 5) დაწერეთ სახლის გაგრილების სისტემის პროგრამა.
# ვთქვათ, როდესაც სახლში ტემპერატურა 30 გრადუსს ასცდება - ავტომატურად უნდა 
# ჩაირთოს გაგრილების სისტემა. იმის გასაგებად თუ რა ტემპერატურაა სახლში, მომხმარებელს იგი
#  შემოატანინეთ input() ფუნქციის მეშვეობით. (გამოიყენეთ მხოლოდ ლოგიკური ოპერატორები)
celcius = int(input("enter celcius: "))

if celcius > 30:
    print("0n")

else:
    print("off")


# HARD LVL:
# 6) დაწერეთ ოთახის გაგრილების სისტემის პროგრამა, but there’s a twist:

# ჩათვალეთ, რომ პროგრამა მხოლოდ იმ შემთხვევაში აღიქვამს ოთახის ტემპერატურას,
#  თუ იგი ფარენგეიტშია გადმოცემული. (სისტემა ჩაირთვება მაშინ, როდესაც ტემპერატურა
#  89.6 ფარენგეიტს ასცდება). 
# ერთადერთი გასათვალისწინებელი ფაქტი ის არის, 
# რომ მომხმარებელს ოთახის ტემპერატურა გრადუსებში შემოაქვს.
"ver gavige"