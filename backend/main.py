from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuration
app.config['DEBUG'] = os.getenv('DEBUG', False)
app.config['ENV'] = os.getenv('FLASK_ENV', 'development')

# Register blueprints
from app.api.routes import api_bp

app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/', methods=['GET'])
def health_check():
    return {
        'status': 'ok',
        'message': 'Focus Enhancement System API'
    }, 200

@app.errorhandler(404)
def not_found(error):
    return {
        'error': 'Not Found',
        'message': 'The requested endpoint does not exist'
    }, 404

@app.errorhandler(500)
def internal_error(error):
    return {
        'error': 'Internal Server Error',
        'message': 'An error occurred while processing your request'
    }, 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
