from app import create_app
import app.models.model_bert as bert

celery, app = create_app()

if __name__ == '__main__':
    bert = bert()
    app.run(debug=True)
