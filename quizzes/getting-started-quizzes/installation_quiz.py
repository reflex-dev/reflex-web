import reflex as rx

questions = [
    {
        "id": 0,
        "question_type": "single_choice",
        "question_body": "What is the purpose of the State class in a Reflex app?",
        "question_image": None,
        "options": [
            "To define the user interface",
            "To define variables that can change and functions that change them",
            "To define the app and add pages",
            "To import the Reflex package"
        ],
        "correct_answers": ["To define variables that can change and functions that change them"]
    },
    {
        "id": 1,
        "question_type": "multiple_choice",
        "question_body": "Which of the following are true about event handlers in Reflex?",
        "question_image": None,
        "options": [
            "They are the only way to modify state in Reflex",
            "They can be called in response to user actions",
            "They define the app's user interface",
            "They can directly update the UI"
        ],
        "correct_answers": [
            "They are the only way to modify state in Reflex",
            "They can be called in response to user actions"
        ]
    },
    {
        "id": 2,
        "question_type": "single_choice",
        "question_body": "How can components in Reflex interact with the app's state?",
        "question_image": None,
        "options": [
            "By directly modifying state variables",
            "By defining their own local state",
            "By binding event triggers to event handlers",
            "By importing the State class"
        ],
        "correct_answers": [
            "By binding event triggers to event handlers"
        ]
    }
]