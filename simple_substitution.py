import string

ciphertext = "GBSXUCGSZQGKGSQPKQKGLSKASPCGBGBKGUKGCEUKUZKGGBSQEICACGKGCEUERWKLKUPKQQGCIICUAEUVSHQKGCEUPCGBCGQOEVSHUNSUGKUZCGQSNLSHEHIEEDCUOGEPKHZGBSNKCUGSUKUASERLSKASCUGBSLKACRCACUZSSZEUSBEXHKRGSHWKLKUSQSKCHQTXKZHEUQBKZAENNSUASZFENFCUOCUEKBXGBSWKLKUSQSKNFKQQKZEHGEGBSXUCGSZQGKGSQKUZBCQAEIISKOXSZSICVSHSZGEGBSQSAHSGKHMERQGKGSKREHNKIHSLIMGEKHSASUGKNSHCAKUNSQQKOSPBCISGBCQHSLIMQGKGSZGBKGCGQSSNSZXQSISQQGEAEUGCUXSGBSSJCQGCUOZCLIENKGCAUSOEGCKGCEUQCGAEUGKCUSZUEGBHSKGEHBCUGERPKHEHKHNSZKGGKAD"
ct = list(ciphertext)
pt = list(ciphertext)
freq = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D', 'L', 'U', 'C', 'M', 'F', 'Y', 'W', 'G', 'P', 'B', 'V', 'K',
        'X', 'Q', 'J', 'Z']
ct_dict = dict.fromkeys(string.ascii_uppercase, 0)
print(ct)
for lettr in range(471):  # initializa the pt array to 0 because of overwrite bug
    pt[lettr] = '0'


def c_count():  # calculates frequency of the cipher text words
    for letter in ct:
        x = ct_dict.get(letter)
        x += 1
        ct_dict[letter] = x
    return 0


c_count()
ct_ord = sorted(ct_dict.items(), key=lambda y: y[1], reverse=True)  # generates an ordered list of tuples from dict


def crack():  # crack message
    for i, t in enumerate(ct_ord):
        for j, letter in enumerate(ct):  # using ct instead of pt because pt values got overwriten
            if letter is t[0]:
                pt[j] = freq[i]


crack()

print(pt)
print("".join(pt))
