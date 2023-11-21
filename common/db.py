import pymysql

'''
打开远端MySQL数据库连接
获取数据库中weixin用户信息
'''
class Db():
    db = ""  # 数据库
    user = 'VAJ_木子'
    def mysql_conn(self):
        global db
        try:
            # 打开数据库连接
            db = pymysql.connect(
                host="mysql.sqlpub.com",
                user="muzi123890",
                password="e7aa9fea95977f7a",
                database="test_muzi_api",
                charset="utf8"
            )
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            # SQL 查询数据库中的某一张表
            # sql = 'select a.openid from weixin_user_test a where user = ""'
            sql = 'select a.openid from weixin_user_test a where user = "'+Db.user+'"'
            # 执行sql语句
            cursor.execute(sql)
            # fetchall():接收全部的返回结果行.
            # alldata = cursor.fetchall()
            # return alldata
            # fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
            onedate = cursor.fetchone()
            return onedate[0]
        except:
            # Rollback in case there is any error
            db.rollback()
        finally:
            db.close()