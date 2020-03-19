from flask import jsonify

def available(email_available, username_available): 
    return jsonify({'email_available': email_available, 'username_available': username_available})