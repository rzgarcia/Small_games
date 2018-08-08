"""Complete the most_frequent() function below so that it returns the most frequently occurring word in a given *string*.
If there is a tie for the most common word, return only one result, the first (tied) word in alphabetical order."""

def most_frequent(s):
    """Return the most frequently occuring word in s."""
    # HINT: Use the built-in split() function to transform the string s into an
    #       array
    words = s.split(' ')

    # HINT: Sort the new array by using the built-in sorted() function or
    #       .sort() list method
    words.sort()


    # HINT: Iterate through the array and count each occurance of every word
    #       using the .count() list method
    dict1 = dict((x,words.count(x)) for x in words)

    # HINT: Find the number of times the most common word appears using max()
    # HINT: Locate the index of the most frequently seen word
    # HINT: Return the most frequent word. Remember that if there is a tie,
    #       return the first (tied) word in alphabetical order.
    result = [x for x, y in dict1.items() if y == max(dict1.values())]
 
    # extract the first string one.
    return result[0]

def test_run():
    #Output: ['cat']
    print(most_frequent("cat bat mat cat bat cat")) 

    #Output: ['butter']
    print(most_frequent("betty bought a bit of butter but the butter was bitter")) 

    #Output: ['dddd']
    print(most_frequent('a bb bb ccc ccc ccc dddd dddd dddd dddd'))

    #['down', 'falling']
    print(most_frequent('london bridge is falling down falling down falling down london bridge is falling down my fair lady'))

if __name__ == '__main__':
    test_run()