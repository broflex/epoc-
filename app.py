#!/usr/bin/bash
# -*- coding: utf-8 -*-


from flask import Flask, jsonify
from spotify import get_mood_levels

app = Flask(__name__)

'''
Return mood levels:
{
    moods: {
        happy: x,
        sad: x,
        focused: x
    }
}
'''
@app.route("/api/v1.0/mood_levels", methods=['GET'])
def mood_levels():
    return jsonify({'moods': get_mood_levels()})



@app.route("/api/v1.0/test", methods=['GET'])
def test():
    return "Hello World!"



if __name__ == '__main__':
    app.run(debug=True)