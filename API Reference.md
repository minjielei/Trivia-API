# Trivia API Reference

## Getting Started
* Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default local location `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration
* Authentication: This version of the application does not require authentication or API keys.

## Error Handling
Errors are returned as JSON objects in the following format
```python
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
```

The following error types are returned by the API when requests fail:
* 404: Resource not found
* 422: Not Processible

## Endpoints
**GET /categories**
* General:
    - Returns a list of categories, success value, and total number of categories
* Sample: `curl http://127.0.0.1:5000/categories`
```python
{
    "categories": [
        {
            "id": 1,
            "type": "Science"
        },
        {
            "id": 2,
            "type": "Art"
        },
        {
            "id": 3,
            "type": "Geography"
        },
        {
            "id": 4,
            "type": "History"
        },
        {
            "id": 5,
            "type": "Entertainment"
        },
        {
            "id": 6,
            "type": "Sports"
        }
    ],
    "success": True,
    "total_categories": 6
}
```

**GET /questions**
* General:
    - Return a list of questions, success value, and total number of questions
    - Results are paginated in groups of 10. Include a request argument to choose page number, start from 1
* Sample: `curl http://127.0.0.1:5000/questions`
```python
{
    "questions": [
        {
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
            "answer": "Apollo 13",
            "difficulty": 4,
            "category": 5
        },
        {
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
            "answer": "Tom Cruise",
            "difficulty": 4,
            "category": 5
        },
        {
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
            "answer": "Maya Angelou",
            "difficulty": 2,
            "category": 4
        },
        {
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
            "answer": "Edward Scissorhands",
            "difficulty": 3,
            "category": 5
        },
        {
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?",
            "answer": "Muhammad Ali",
            "difficulty": 1,
            "category": 4
        },
        {
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?",
            "answer": "Brazil",
            "difficulty": 3,
            "category": 6
        },
        {
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?",
            "answer": "Uruguay",
            "difficulty": 4,
            "category": 6
        },
        {
            "id": 12,
            "question": "Who invented Peanut Butter?",
            "answer": "George Washington Carver",
            "difficulty": 2,
            "category": 4
        },
        {
            "id": 13,
            "question": "What is the largest lake in Africa?",
            "answer": "Lake Victoria",
            "difficulty": 2,
            "category": 3
        },
        {
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?",
            "answer": "The Palace of Versailles",
            "difficulty": 3,
            "category": 3
        }
    ],
    "success": True,
    "total_questions": 19
}
```

**DELETE /questions/{question_id}**
* General:
    - Delete the question of the given id if it exists. Returns the id of the deleted book, success value, total questions, and question list based on current page number to update the frontend
* Sample: `curl -X DELETE http://127.0.0.1:5000/questions/9`
```python
{
    "deleted_question": 9,
    "success": True,
    "total_questions": 18,
    "questions": [
        {
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
            "answer": "Apollo 13",
            "difficulty": 4,
            "category": 5
        },
        {
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
            "answer": "Tom Cruise",
            "difficulty": 4,
            "category": 5
        },
        {
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
            "answer": "Maya Angelou",
            "difficulty": 2,
            "category": 4
        },
        {
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
            "answer": "Edward Scissorhands",
            "difficulty": 3,
            "category": 5
        },
        {
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?",
            "answer": "Brazil",
            "difficulty": 3,
            "category": 6
        },
        {
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?",
            "answer": "Uruguay",
            "difficulty": 4,
            "category": 6
        },
        {
            "id": 12,
            "question": "Who invented Peanut Butter?",
            "answer": "George Washington Carver",
            "difficulty": 2,
            "category": 4
        },
        {
            "id": 13,
            "question": "What is the largest lake in Africa?",
            "answer": "Lake Victoria",
            "difficulty": 2,
            "category": 3
        },
        {
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?",
            "answer": "The Palace of Versailles",
            "difficulty": 3,
            "category": 3
        },
        {
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?",
            "answer": "Agra",
            "difficulty": 2,
            "category": 3
        }
    ]
}
```

**POST /questions**
* General:
    - Create a new question using the submitted question, answer, difficulty and category. Return the id of the created question, success value, total questions, and question list based on current page number to update the frontend.
* Sample: `curl http://127.0.0.1:5000/questions?page=2 -X POST -H "Content-Type: application/json" -d '{"question": "what is the lightest massive particle?", "answer": "neutrino", "difficulty": "2", "category": "1"}'`
```python
{
    "questio_id": 24,
    "success": True,
    "total_questions": 20,
    "question": [
        {
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?",
            "answer": "Agra",
            "difficulty": 2,
            "category": 3
        },
        {
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?",
            "answer": "Escher",
            "difficulty": 1,
            "category": 2
        },
        {
            "id": 17,
            "question": "La Giaconda is better known as what?",
            "answer": "Mona Lisa",
            "difficulty": 3,
            "category": 2
        },
        {
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?",
            "answer": "One",
            "difficulty": 4,
            "category": 2
        },
        {
            "id": 19,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?",
            "answer": "Jackson Pollock",
            "difficulty": 2,
            "category": 2
        },
        {
            "id": 20,
            "question": "What is the heaviest organ in the human body?",
            "answer": "The Liver",
            "difficulty": 4,
            "category": 1
        },
        {
            "id": 21,
            "question": "Who discovered penicillin?",
            "answer": "Alexander Fleming",
            "difficulty": 3,
            "category": 1
        },
        {
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?",
            "answer": "Blood",
            "difficulty": 4,
            "category": 1
        },
        {
            "id": 23,
            "question": "Which dung beetle was worshipped by the ancient Egyptians?",
            "answer": "Scarab",
            "difficulty": 4,
            "category": 4
        },
        {
            "id": 24,
            "question": "what is the lightest massive particle?",
            "answer": "neutrino",
            "difficulty": 2,
            "category": 1
        }
    ]
}
```
* General: 
    - Search for questions that contain a given search term. Return search term, success value, a list of questions that contain the search term, and total such questions
* Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"search": "Mirrors"}'`
```python
{
    "search_term": "Mirrors",
    "success": True,
    "questions": [
        {
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?",
            "answer": "The Palace of Versailles",
            "difficulty": 3,
            "category": 3
        }
    ],
    "total_questions": 1
}
```

**POST /categories/{category_id}/quesitons**
* General:
    - Get questions from the category with the given id. Return category, success value, questions list, and total questions in that category
* Sample: `curl -X POST http://127.0.0.1:5000/categories/1/questions`
```python
{
    "category": "Science",
    "success": True,
    "questions": [
        {
            {
            "id": 20,
            "question": "What is the heaviest organ in the human body?",
            "answer": "The Liver",
            "difficulty": 4,
            "category": 1
            },
            {
                "id": 21,
                "question": "Who discovered penicillin?",
                "answer": "Alexander Fleming",
                "difficulty": 3,
                "category": 1
            },
            {
                "id": 22,
                "question": "Hematology is a branch of medicine involving the study of what?",
                "answer": "Blood",
                "difficulty": 4,
                "category": 1
            }
        }
    ],
    "total_questions": 3
}
```
