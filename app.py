from flask import Flask, request, jsonify
import pymysql
from config import DB_CONFIG

app = Flask(__name__)


def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

@app.route('/', methods=['GET'])
def main():
    return jsonify({"status": "ok"}), 200

# 创建用户
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = "INSERT INTO user (name, email) VALUES (%s, %s)"
            cursor.execute(sql, (name, email))
        conn.commit()
        return jsonify({"message": "User created successfully"}), 201
    except pymysql.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()


# 获取所有用户
@app.route('/users', methods=['GET'])
def get_all_users():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM user"
            cursor.execute(sql)
            users = cursor.fetchall()
        return jsonify(users), 200
    except pymysql.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()


# 根据 ID 获取用户
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM user WHERE id = %s"
            cursor.execute(sql, (user_id,))
            user = cursor.fetchone()
            if user:
                return jsonify(user), 200
            else:
                return jsonify({"error": "User not found"}), 404
    except pymysql.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()


# 更新用户信息
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name and not email:
        return jsonify({"error": "At least one field (name or email) is required for update"}), 400

    try:
        conn = get_db_connection()
        update_fields = []
        values = []
        if name:
            update_fields.append("name = %s")
            values.append(name)
        if email:
            update_fields.append("email = %s")
            values.append(email)
        values.append(user_id)

        update_query = ", ".join(update_fields)
        sql = f"UPDATE user SET {update_query} WHERE id = %s"

        with conn.cursor() as cursor:
            cursor.execute(sql, values)
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"message": "User updated successfully"}), 200
    except pymysql.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()


# 删除用户
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = "DELETE FROM user WHERE id = %s"
            cursor.execute(sql, (user_id,))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"message": "User deleted successfully"}), 200
    except pymysql.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)
    # 暴露 Flask 应用实例
    app = Flask(__name__)