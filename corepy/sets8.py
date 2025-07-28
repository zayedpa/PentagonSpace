#s1={1,2,3,[4,5,6],7}   throw an error
#print(s1)              list is not allowed inside the sets

s2={1,2,3,(4,5,6),7}    # tuples are allowed inside the sets
print(s2)

#s3={1,2,3,{4,5,6},7}  throw an error
#print(s3)             nested sets are not allowed