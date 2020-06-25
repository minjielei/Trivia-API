import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
  page = request.args.get('page', 1, type=int)
  start = (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE
  questions = [question.format() for question in selection]

  return questions[start:end]

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  # Set up CORS, allow * for origins
  CORS(app, resources={'/': {'origins': '*'}})
  # Use the after_request decorator to set Access-Control-Allow
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authentication,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE,OPTIONS')
    return response

  # Create an endpoint to handle GET requests for all available categories.
  @app.route('/categories')
  def get_categories():
    selection = Category.query.order_by(Category.id).all()
    categories = {category.id: category.type for category in selection}
    if len(categories) == 0:
      abort(404)

    return jsonify({
        'success': True,
        'categories': categories,
        'total_categories': len(categories)
      })

  '''
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions).  
  '''
  @app.route('/questions')
  def get_questions():
    selection = Question.query.order_by(Question.id).all()
    questions = paginate_questions(request, selection)
    categories = Category.query.order_by(Category.id).all()

    if len(questions) == 0:
      abort(404)

    return jsonify({
        'success': True,
        'questions': questions,
        'total_questions': len(selection),
        'categories': {category.id: category.type for category in categories},
        'current_category': None
      })


  # Create an endpoint to DELETE question using a question ID. 
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id==question_id).one_or_none()
      if question is None:
        abort(404)

      question.delete()
      selection = Question.query.order_by(Question.id).all()
      questions = paginate_questions(request, selection)

      return jsonify({
        'success': True,
        'deleted': question_id,
        'questions': questions,
        'total_questions': len(selection)
      })
    except:
      abort(422)

  '''
  Create an endpoint to POST a new question, or to get questions based on a search term
  '''
  @app.route('/questions', methods=['POST'])
  def create_question():
    body = request.get_json()

    new_question = body.get('question', None)
    new_answer = body.get('answer', None)
    new_difficulty = body.get('difficulty', None)
    new_category = body.get('category', None)
    search = body.get('searchTerm', None)

    try:
      if search:
        selection = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search)))
        questions = paginate_questions(request, selection)

        return jsonify({
          'success': True,
          'questions': questions,
          'total_questions': len(selection.all()),
          'current_category': None
        })

      else:
        question = Question(question=new_question, answer=new_answer, difficulty=new_difficulty, category=new_category)
        question.insert()
        selection = Question.query.order_by(Question.id).all()
        questions = paginate_questions(request, selection)

        return jsonify({
          'success': True,
          'created': new_question,
          'questions': questions,
          'total_questions': len(selection)
        })

    except:
      abort(422)

  '''
  Create a GET endpoint to get questions based on category. 
  '''
  @app.route('/categories/<int:category_id>/questions')
  def get_questions_by_category(category_id):
    try:
      selection = Question.query.order_by(Question.id).filter(Question.category==category_id).all()
      questions = paginate_questions(request, selection)

      if len(questions) == 0:
        abort(404)

      return jsonify({
            'success': True,
            'questions': questions,
            'total_questions': len(selection),
            'current_category': category_id
          })

    except:
      abort(422)

  '''
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def play_quiz():
      try:
          body = request.get_json()

          if 'quiz_category' not in body or 'previous_questions' not in body:
              abort(422)

          category = body.get('quiz_category')
          previous_questions = body.get('previous_questions')

          if category['type'] == 'click':
              available_questions = Question.query.filter(Question.id.notin_((previous_questions))).all()
          else:
              available_questions = Question.query.filter_by(category=category['id']).filter(Question.id.notin_((previous_questions))).all()

          new_question = available_questions[random.randrange(0, len(available_questions))].format() if len(available_questions) > 0 else None

          return jsonify({
              'success': True,
              'question': new_question
          })

      except:
          abort(422)

  # Create error handlers for all expected errors including 404 and 422. 
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': "resource not found"
      }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422
  
  return app

    