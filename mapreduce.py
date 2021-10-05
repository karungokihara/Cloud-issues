def find_longest_string(list_of_strings):
    longest_string = None
    longest_string_len = 0 
    for s in list_of_strings:
        if len(s) > longest_string_len:
            longest_string_len = len(s)
            longest_string = s
    return longest_string
  
list_of_strings = ['abc', 'python', 'dima']
%time max_length = print(find_longest_string(list_of_strings))

large_list_of_strings = list_of_strings*100000000
%time max_length = max(large_list_of_strings, key=len)

%%time
# step 1:
list_of_string_lens = [len(s) for s in list_of_strings]
list_of_string_lens = zip(list_of_strings, list_of_string_lens)
#step 2:
max_len = max(list_of_string_lens, key=lambda t: t[1])
print(max_len)

mapper = len
def reducer(p, c):
    if p[1] > c[1]:
        return p
    return c
 



#step 1
mapped = map(mapper, list_of_strings)
mapped = zip(list_of_strings, mapped)
#step 2:
reduced = reduce(reducer, mapped)
print(reduced)
