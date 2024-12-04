def vote(votes):
    max = 0
    result = 0
    for num in votes:
        if votes.count(num) > max:
            max = votes.count(num)
            result = num

    return result

if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))