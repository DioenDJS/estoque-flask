from src.main.server.server import app
from dotenv import load_dotenv
import os

load_dotenv()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv("API_PORT"), debug=True)
