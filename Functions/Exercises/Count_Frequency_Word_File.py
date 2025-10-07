def count_word_frequency(filepath):
    word_count={}
    with open(filepath,'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?')
                word_count[word] = word_count.get(word,0) + 1

    return word_count


print(count_word_frequency(filepath='Functions/Exercises/sample.txt'))





