import os

from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 5001))  # Default to port 5000
    app.run(host='0.0.0.0', port=port)
