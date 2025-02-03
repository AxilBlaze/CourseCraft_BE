from flask import Blueprint, request, jsonify
from config import Config

bp = Blueprint('chat', __name__, url_prefix='/api/chat')

# Use DialogGPT for chat
chat_model = Config.DIALOGPT_MODEL

# Use FLAN-T5 for specific tasks
generation_model = Config.FLAN_T5_MODEL

@bp.route('/', methods=['POST'])
def chat():
    return jsonify({"message": "Chat endpoint"}), 200 