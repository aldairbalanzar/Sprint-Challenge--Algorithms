'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
     #init variable  with count to start at 0 since there have been no instances of "th"
    #check length
    #if len(word) < 2, return count (should be 0)
    #if len(word) > 2, proceed with checking the word for "th"
    #check first two indexes if they equal "th"
        #if current two indexes include "th"(['t', 'h']), increase count by 1
        #if not, return the funcion again only this time with the first two indexes of word sliced off
    count = 0
    if len(word) < 2:
        return count
    else:
        if word[:2] == 'th':
            count += 1
    return count + count_th(word[1:])

print(count_th('thth'))
