
from flask import Flask, Response, jsonify, render_template,flash,redirect,session,url_for,request,g
from app import app, db
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .models import Chat
from datetime import datetime
import json

def chat2dict(chat):
    return {
        'nickname': chat.nickname,
        'content': chat.content,
        'timestamp': str(chat.timestamp)
    }


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajax/post_chat_info')
def post_chat_info():
    """
    json api
    接收一条聊天，json格式，添加到数据库，返回 True or False
    """
    nickname = request.args.get('nickname')
    content = request.args.get('content')
    timestamp = datetime.now()
    chat = Chat(nickname = nickname, content = content, timestamp = timestamp)
    db.session.add(chat)
    db.session.commit()

    json_data = json.dumps({'a':'A','b':'B'})
    resp = Response(json_data, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/ajax/get_chat_history')
def get_chat_history():
    """
    json api
    以json格式返回
    """
    chat_history = Chat.query.all()
    # chat_history = db.session.query(Chat).filter(Chat.nickname=='John')
    chat_history_list = []
    for chat in chat_history:
        chat_history_list.append(chat2dict(chat))
    data = {
        "result": chat_history_list
    }

    fake_data = {
            "result": [
                {
                  "nickname": "\u00ce\u00d2",
                  "content": "Hello world",
                  "timestamp": "2015-07-01 16:41:38.357000"
                },
                {
                  "content": "Hello world2",
                  "nickname": "John2",
                  "timestamp": "2015-07-01 16:57:44.667000"
                }
            ]
        }

    json_data = json.dumps(data)
    resp = Response(json_data, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
    """
    返回的json字符串类似下面的结构
    {
        "result": [
            {
              "nickname": "John",
              "content": "Hello world",
              "timestamp": "2015-07-01 16:41:38.357000"
            },
            {
              "content": "Hello world",
              "nickname": "John2",
              "timestamp": "2015-07-01 16:57:44.667000"
            }
        ]
    }
    """
