def word_frequency(words):
    """Returns frequency of each word given a list of words.

        >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
    """
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency

a=word_frequency("jjkkkll")
print a


print "\n**********Reading FILE*************"
def read_words(filename):
    return open(filename).read().split()
    
b=read_words('a1.py')    
print b

print"\n\n\n*************dISPLAY ITEMS IN DICTIONARY**************"
def main(filename):
    frequency = word_frequency(read_words(filename))
    for word, count in frequency.items():
        print word, count

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
    
    
print"\n\n\n****DISPLAY ITEMS IN DICTIONARY IN REVERSE ORDER OF VALUES*****"   
def main(filename):
    frequency = word_frequency(read_words(filename))
    s=sorted(frequency.items(),key=lambda x: (-x[1],x[0]))
    print s
    
if __name__ == "__main__":
    import sys
    main(sys.argv[1])
    
