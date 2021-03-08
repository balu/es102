def greet(name, age, gender):
    if gender == 'M' and age < 18:
        title = 'Master'
    elif gender == 'M':
        title = 'Mr.'
    else:
        title = 'Ms.'
    return f"Hello {title} {name}"

print(greet(name='Wayne', gender='M', age=16))
print(greet(name='Joe', gender='M', age=30))
print(greet(name='Barbie', gender='F', age=18))
