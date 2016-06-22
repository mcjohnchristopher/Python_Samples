line = 'From abc@xyz.com 22/11/1990'
word = line.split[]
email = word[1]
host = email.split('@')
print email
print host[1]