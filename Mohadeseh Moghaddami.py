#professor's name:Mrs. Haniyeh Yazdian
#Student's name:Mrs.Mohadeseh Moghaddami
#Course name: programming language laboratory

#Program description:
#Write a program that will count the total number of words and the number of letters in a variable named: 
#(num_k) and (num_h). 
#Then place the character "r" instead of "p". 
#Print the number of sentences


sentence='Python is a very useful programming language'
num_h=sentence.split()
num_k=len(sentence)
print(len(num_h))>>>>>>>   #7
print(num_k)>>>>>>>   #44
print(sentence.replace('p','r') )>>>>>  #rython is a very useful rrogramming language

sentence='Python is a very useful programming language.Python is a very practical programming language. Python is a popular language. This language is used to create many apps'
print(sentence.count('.'))>>>>> #3

