# Examples for PyInquirer

1. [Home Page](https://github.com/CITGuru/PyInquirer)
2. [Helpful site](https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df)

## 1. Hello World

Basic example:

```python
from __future__ import print_function, unicode_literals
from PyInquirer import prompt
"""pprint print data structures in a beautiful way"""
from pprint import pprint

"""The question for users"""
questions = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'What\'s your first name',
     }
]

"""Create objects for answers"""
answers = prompt(questions)
"""print the answer we got, the dictionary look data can be used for future use"""
pprint(answers)
```

**Output:**

```bash
pipenv run python hello.py
? What's your first name  Sheldon
{'first_name': 'Sheldon'}
```

## 2. Interactive

```python
from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

"""Style for pretty interface"""
style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

"""question set up"""
questions = [
    {
        'type': 'checkbox',
        'message': 'Select toppings',
        'name': 'toppings',
        'choices': [
            Separator('= The Meats ='),
            {
                'name': 'Ham'
            },
            {
                'name': 'Ground Meat'
            },
            {
                'name': 'Bacon'
            },
            Separator('= The Cheeses ='),
            {
                'name': 'Mozzarella',
                'checked': True
            },
            {
                'name': 'Cheddar'
            },
            {
                'name': 'Parmesan'
            },
            Separator('= The usual ='),
            {
                'name': 'Mushroom'
            },
            {
                'name': 'Tomato'
            },
            {
                'name': 'Pepperoni'
            },
            Separator('= The extras ='),
            {
                'name': 'Pineapple'
            },
            {
                'name': 'Olives',
                'disabled': 'out of stock'
            },
            {
                'name': 'Extra cheese'
            }
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

answers = prompt(questions, style=style)
pprint(answers)
```

**Outputs:**

![Interface](img/interactive.png)

![After selection](img/result.png)

## 3. Summary

Let's see the data type of answer:

If we run `type(answers)`, we get `<class 'dict'>`.

So, one possible approach is that we provide possible options for user to choose.
And we use the dictionary for later access. If we do end up need to get user
password, we can hash it first, then use the match method.
