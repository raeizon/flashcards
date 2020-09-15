from random import randint
import random

answer_list = []

global our_chords
our_chords = ['maj73rdstringroot', 'maj74thstringroot','maj75thstringroot', 'maj76thstringroot' ]

global our_chords_dictionary
our_chords_dictionary = {
'maj73rdstringroot':'Maj7 3rd String Root',
'maj74thstringroot':'Maj7 4th String Root',
'maj75thstringroot':'Maj7 5th String Root',
'maj76thstringroot':'Maj7 6th String Root',
}

#generate a random number
global rando
rando = randint(0, len(our_chords)-1)

# print(our_chords[rando])
# print(our_chords_dictionary[our_chords[rando]])

answer = our_chords[rando]

# # add first random selection to our answer_list list
# answer_list.append(our_chords[rando])
#
#
# #remove answer from list
# our_chords.remove(our_chords[rando])
#
#
# #shuffle our original list
# random.shuffle(our_chords)
#
# #randomly select next chord
# rando = randint (0, len(our_chords)-1)
# answer_list.append(our_chords[rando])
#
# #remove 2nd answer from list
# our_chords.remove(our_chords[rando])
#
# #shuffle our original list
# random.shuffle(our_chords)
#
# #randomly select third chord
# rando = randint (0, len(our_chords)-1)
# answer_list.append(our_chords[rando])
#
# print(answer_list)
# print(answer)

count = 1

while count < 4:
    rando = randint(0, len(our_chords)-1)
    #if first selection, make it our answer
    if count == 1:
        answer = our_chords[rando]

    #add our first selection to a new list
    answer_list.append(our_chords[rando])

    #remove from old list
    our_chords.remove(our_chords[rando])

    #shuffle our original list
    random.shuffle(our_chords)


    count += 1

print(answer_list)
print(answer)
random.shuffle(answer_list)
print(answer_list)

print(our_chords_dictionary[answer])
