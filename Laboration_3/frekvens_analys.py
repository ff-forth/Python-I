def list_to_dict(word_list,key):
    """Funktionen gör en list till en dictionary
    nyckel = ord och värde = antal uppkommande gånger på ordet
    parameter : list och string
    returvärde : dict
    """
    lower_dict = {}
    for word in word_list:
        if key == "lower":
            word = word.lower()
        if word not in lower_dict:
            lower_dict[word] = 1
        else:
            lower_dict[word] += 1
    return lower_dict

def frequency(file_name):
    """Funktionen analyserar en text fil till en dictionary
    nyckel = ord och värde = antal uppkommande gånger på ordet
    parameter : fil
    returvärde : dict
    """
    file = open(file_name, 'r')
    string = file.read()
    file.close()
    word_list = string.split()
    lower_dict = list_to_dict(word_list,"lower")
    word_dict = list_to_dict(word_list,"None")
    return_dict = {}
    for key in word_dict:
        k_lower = key.lower()
        if k_lower in lower_dict:
            return_dict[key] = lower_dict[k_lower]
            del lower_dict[k_lower]
    return_dict
    return return_dict

def most_frequent(freq_dict):
    """
    Funktionen returnera 10 första ord i topplistan
    parameter : dict
    returvärde: dict
    """
    tup_list = []
    for item in freq_dict:
        tup = (freq_dict.get(item),item)
        tup_list.append(tup)
    tup_list.sort()
    tup_list.reverse()
    return_dict = {}
    if len(tup_list) > 10:
        for item in tup_list[:10]:
            return_dict[item[1]] = item[0]
        return return_dict
    else:
        for item in tup_list:
            return_dict[item[1]] = item[0]
        return return_dict

def word_count(freq_dict):
    """
    Funktionen räkknar antal total ord i en fil
    parameter : dict
    returvärde: int
    """
    word = 0
    for item in freq_dict:
        word += int(freq_dict.get(item))
    return word

def unique_words(freq_dict):
    """
    Funktionen räknar antal ord i en fil
    parameter : dict
    returvärde: int
    """
    result = len(freq_dict)
    return result
    
def mean_frequency(freq_dict):
    """
    Funktionen räknar medelvärde
    parameter : dict
    returvärde: float
    """
    freq_dict = most_frequent(freq_dict)
    word = word_count(freq_dict)
    sum_words = len(freq_dict)
    mean = word/sum_words
    return round(mean,2)

def median_frequency(freq_dict):
    """
    Funktionen räknar median
    parameter : dict
    returvärde: float
    """
    freq_dict = most_frequent(freq_dict)
    items = len(freq_dict)
    index = 0
    if items%2 == 1:
        for item in freq_dict:
            index += 1
            pos = items//2+items%2
            if index == pos:
                return freq_dict[item]
    else:
        sum = 0
        for item in freq_dict:
            index += 1
            pos = items//2
            if index == pos or index == pos+1:
                sum += freq_dict[item]
        return sum/2

def closest_word(freq_dict,rate):
    """
    Funktionen identifiera närmaste ord till raten
    parameter : dict och float
    returvärde: string
    """
    differ = rate
    for items in freq_dict.keys():
        words = int(freq_dict[items])
        new_differ = abs(words-rate)
        if new_differ < differ:
            differ = new_differ
            item = items
    return item

def main():
    print( "\nVälkommen till 'Frekvensanalys'\n")
    file_name = input("Vilken fil vill du undersöka?\n")
    freq_dict = frequency(file_name)
    most_freq = most_frequent(freq_dict)
    sum_words = word_count(freq_dict)
    uniq_words = unique_words(freq_dict)
    print("\nFilen innehåller\n"+
            f"Antal ord: {sum_words}\n"+
            f"Antal unika ord: {uniq_words}\n"+
            f"\nHär är de {len(most_freq)} vanligaste orden i filen fallande ordning.\n")
    
    print("Ord\tAntal förekommaster")
    print("----------------------------")
    for item in most_freq.keys():
        print(f"{item}\t\t{most_freq.get(item)}")
    
    freq_mean = mean_frequency(freq_dict)
    freq_median = median_frequency(freq_dict)
    closest = closest_word(freq_dict,freq_mean)
    print("\nAv ordet i topp-listan är\n"+
            f"Frekvens-medelvärde = {freq_mean}\n"+
            f"Frekvens-median = {freq_median}\n"+
            f"\nOrdet '{closest}' har frekvensen som ligger närmst medelvärdet.\n")

if __name__ == "__main__":
    main()
