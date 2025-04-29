import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_number = int(request.form.get('user_number'))

    try:
        conn = mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'localhost'),  # docker MySQL server address
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', 'yourpassword'),
        database=os.environ.get('DB_NAME', 'test')
                                       )

        cursor = conn.cursor()
        cursor.callproc('sp_get_country_code', [user_number])

        result1, result2 = None, None  # define variables

        for res in cursor.stored_results():
            row = res.fetchone()
            if row:
                result1, result2 = row[0], row[1]

        cursor.close()
        conn.close()

        return render_template('result.html', result1=result1, result2=result2)

    except Exception as e:  # <-- Fixed this line
        return f'Error: {e}'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

