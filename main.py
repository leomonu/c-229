import hashlib
from itertools import permutations 

def find_hash(original_hash):
    word_file = open("words.txt","r")
    word_file = list(word_file)

    anagram = "listen"
    words = anagram.count(' ')
    words += 1

    char_list = list(set(anagram))

    if ' ' in char_list:
        char_list.remove(' ')

    final_words = []

    for i in word_file:
        f=False
        temperary_word=i.replace("\n",'')
        temperary_char=list(set(temperary_word))

        for i in temperary_char:
            if i not in char_list:
                f=True
                break
        
        if f==False:
            final_words.append(temperary_word)

    print(final_words)
    print("what is analog lenght ",len(anagram))
    # print(len(final_words))

    for elem in permutations(final_words, words):
        hash_elem=elem.strip()
        hash_elem = " ".join(elem)
        print("what is lenght of hash_element ",len(hash_elem))
        if len(hash_elem)!=len(anagram):
            continue
        
        m = hashlib.md5()
        m.update(hash_elem.encode('utf-8'))
        word_hash = m.hexdigest()

        if word_hash == original_hash:
            return hash_elem

hash = '13b382e1a2f8e22535b4730d78bc8591'
# print(len(hash))
answer = find_hash(hash)
print(f"Collision!  The word corresponding to the given hash is '{answer}'")