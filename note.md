1. 如果你想在数据库中定义个自增字段，先看看这里：
SQLAlchemy will automatically set the first Integer PK column that's not marked as a FK as auto_increment=True
sqlalchemy会自动将第一个不是外键的主键设置为自增字段。

2. 对于ms sql server 无法远程连接数据库的情况，要确保以下几点：
  * 可以通过sql身份验证登陆数据库
  * 在计算机管理 --> 服务和应用程序 --> SQL Server配置管理器 --> SQLEXPRESS的协议 中，把 TCP/IP更改为已启用
  * 双击上一个步骤中的 TCP/IP，打开 TCP/IP属性，点 IP地址选项卡，找到 127.0.0.1，更该 TCP端口为 1433，IPALL的TCP端口也改为1433.TCP动态端口留空。
  * 在系统服务中，确保 SQL Server Browser正在运行。

3. 对于创建了登陆名还是无法远程通过或者通过ms sql server managment stdio 的sql 身份验证登陆，需要尝试一下方法：
服务器上右键，点击停止，再启动。这样mssqlserver服务会关闭再开启，然后就可以通过sql身份验证登陆了

4. 对象转换成字典可以参考如下形式
  ```
  def chat2dict(chat):
      return {
          'nickname': chat.nickname,
          'content': chat.content,
          'timestamp': str(chat.timestamp)
      }
  ```

5. 要以json格式返回数据时，可以这样
  ```
  import json
  json_data = json.dumps({'a':'A','b':'B'})
  resp = Response(json_data, status=200, mimetype='application/json')
  resp.headers['Access-Control-Allow-Origin'] = '*' # 这里是自定义response headers
  return resp
  ```
  也可以这样
  ```
  from flask import jsonify
  return jsonify(result = result)
  ```
  但后一种方法无法定制response请求。

6. 用 sqlalchemy 时，可以很方便的用同样的代码操作各种不同的数据，只需要修改链接字符串即可。
比如mssql的：
  ```
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://sa:lishenzhi1214@localhost:1433/chatroom?charset=utf8'
  ```
比如mysql的：
  ```
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lishenzhi1214@localhost:3306/chatroom?charset=utf8'
  ```
其他的各种操作如增删改查，只需要操作orm提供的接口即可，由orm代我们和数据库通信。

7. sqlalchemy 针对不同数据库的各种特性支持不足，会出一些问题。
我碰到的一个最主要的问题就是字符编码的问题。我需要数据库以unicode存储，可是通过sqlamchemy建立的字段不一定是你想要的，比如你想要nvarchar,但是sqlalchemy会给你定义成varchar，这个貌似不能很轻易的定制。这时，就需要进入数据库自行修改部分属性。
这个问题还是比较致命的，因为在mysql 中，如果我想修改数据库的字符集类型，可以通过status命令查看，通过其他的语句修改，但是在sql server中，没有这些选项，必须设置字段类型为n开头的才行。

8. 当使用 Flask-SQLAlchemy时，我是这样初始化数据库并且建表的。
  ```
  from flask import Flask
  from flask.ext.sqlalchemy import SQLAlchemy

  app = Flask(__name__)

  # 定义数据库连接字段，最后的charset参数可以不要。默认的端口号可以不要。
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://sa:lishenzhi1214@localhost:1433/chatroom?charset=utf8'
  #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lishenzhi1214@localhost:3306/chatroom?charset=utf8'

  db = SQLAlchemy(app)

  # 建立数据模型
  class Chat(db.Model):
      id = db.Column(db.Integer, primary_key = True)
      # SQLAlchemy will automatically set the first Integer PK column that's not marked as a FK as auto_increment=True
      nickname = db.Column(db.String(20))
      content = db.Column(db.Text)
      timestamp = db.Column(db.DateTime)

      def __repr__(self):
          return '<Chat %r>' % (self.nickname)

  # 自动创建表结构
  db.create_all()
  ```
  先在数据库中建立一个新的数据库，只需要名称即可。
  接着将以上代码放在一个脚本文件中，执行即可。
  接着我手动在数据库中修改的部分内容，因为这是mssql。。。无语。

9.
