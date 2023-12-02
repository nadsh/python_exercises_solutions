# Important things
# * You can add "special characters" to string. Examples of special characters:
#   \n  new line character
#   \t  tab character
#   \0  NULL terminator
X = float(input("Wikipedia MB consumption: "))
Y = float(input("Memes MB consumption: "))
money_for_wikipedia = X * 0.1 # dollars
money_for_memes = Y * 0.05 # dollars
total_consumption = money_for_wikipedia + money_for_memes

if total_consumption > 100:
    print("Too much consumption")

if money_for_wikipedia < money_for_memes:
    print("WOW MANY MEMES\nSUCH LOL")