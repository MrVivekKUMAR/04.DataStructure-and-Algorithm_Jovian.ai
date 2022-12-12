def queryCards(cards,query):
    minPosition = 0
    maxPosition = len(cards)-1

    while True:
        midPostion = (maxPosition + minPosition)//2
        if cards[midPostion] == query:
             return midPostion
        elif (cards[midPostion] < query):
            maxPosition = midPostion -1
        else:
            minPosition = midPostion +1




cards = [32,29,28,14,13,19,9,7,5,3,1]
query1 = 29
query2 = 3

print(queryCards(cards,query1))
print(queryCards(cards,query2))

