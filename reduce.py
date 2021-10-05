data_chunks = chunkify(list_of_strings, number_of_chunks=30)
#step 1:
reduced_all = []
for chunk in data_chunks:
    mapped_chunk = map(mapper, chunk)
    mapped_chunk = zip(chunk, mapped_chunk)
    
    reduced_chunk = reduce(reducer, mapped_chunk)
    reduced_all.append(reduced_chunk)
    
#step 2:
reduced = reduce(reducer, reduced_all)
print(reduced)
