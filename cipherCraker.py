'''
This program asks the user for a file with text to be decrypted, reads that file, and then
decrypts the results on screen while also into a file named 'decrypted.txt' in the working directory.
I am still a novice so I added some comments/etc to help me learn as I went through this code.
'''

import random
from substitution import SimpleSubstitution as SimpleSub
import random
import re
from ngram_score import ngram_score

fitness = ngram_score('ngrams.txt') # load quadgram statistics from the file (must be in this directory)

print("\nThis program will decrypt text from a file and print it along with the key on screen and save the output to decrpted.txt\n")
print("****Remember to include the file extension & file must be in this Directory****\n")

#get input of file name from user, read it into a string to parse
str = open(raw_input("Enter your filename\n"),'r').read()
str.upper()


maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
maxscore = -99e9
parentscore,parentkey = maxscore,maxkey[:]
print "Substitution Cipher solver, you may have to wait several iterations"
print "for the correct result. Press ctrl+c to exit program."
# allows user to end program
    
i = 0
while 1:
    i = i+1
    random.shuffle(parentkey)
    deciphered = SimpleSub(parentkey).decipher(str)
    parentscore = fitness.score(deciphered)
    count = 0
    while count < 1000:
        a = random.randint(0,25)
        b = random.randint(0,25)
        child = parentkey[:]
        # swap two characters in the child
        child[a],child[b] = child[b],child[a]
        deciphered = SimpleSub(child).decipher(str)
        score = fitness.score(deciphered)
        # if the child was better, replace the parent with it
        if score > parentscore:
            parentscore = score
            parentkey = child[:]
            count = 0
        count = count+1
    #keep track of best score seen so far
    if parentscore>maxscore:
        maxscore,maxkey = parentscore,parentkey[:]
        print '\nbest score so far:',maxscore,'on iteration',i
        ss = SimpleSub(maxkey)
        print '    best key: '+''.join(maxkey)
        print '    plaintext: '+ss.decipher(str)

        fdecrypt = open("decrypted.txt", 'w')
        fdecrypt.write(ss.decipher(str))
        fdecrypt.close()
