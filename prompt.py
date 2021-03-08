def prompt(message):
    response = ''
    while response != 'y' and response != 'n':
        print(message)
        response = input()
    return response

print(prompt("Are you sure (y/n)? "))
