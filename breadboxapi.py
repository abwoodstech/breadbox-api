from flask import Flask, jsonify, request
import mysql.connector
import random
import requests
import json
import os

app = Flask(__name__)

BREAD_PASSWORD = os.getenv('BREADPW')

# Import Database
con=mysql.connector.connect(
    host='mysqlbreadbox-breadboxapi.c.aivencloud.com',
    port=24766,
    user='avnadmin',
    password=BREAD_PASSWORD,
    database='breadbox'
)



# Create Routes
@app.route('/v1/breadbox' ,methods=['GET'])
def random_bread():
    table_choice = random.choice(["Facts", "Jokes"])
    cursor = con.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {table_choice} ORDER BY RAND() LIMIT 1")
    result = cursor.fetchone()
    cursor.close()
    return jsonify({"type": table_choice.rstrip('s'), "data": result})





@app.route('/getTable' ,methods=['GET'])
def get_tables():
    cursor = con.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    cursor.close()
    con.close()
    table_names=[table[0] for table in tables]
    return jsonify({"tables":table_names}), 200


@app.route('/facts' ,methods=['GET'])
def fetch_facts():
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT * FROM facts")
    rows = cursor.fetchall()
    cursor.close()
    return jsonify(rows)

@app.route('/jokes' ,methods=['GET'])
def fetch_jokes():
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jokes")
    rows = cursor.fetchall()
    cursor.close()
    return jsonify(rows)


@app.route('/facts/<int:id>' ,methods=['GET'])
def factById(id):
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT * FROM facts WHERE id=%s", (id,))
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)

@app.route('/jokes/<int:id>' ,methods=['GET'])
def jokeById(id):
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jokes WHERE id=%s", (id,))
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)




# POST
@app.route('/addFact' ,methods=['POST'])
def add_fact():
    data = request.get_json()
    fact = data.get('Facts')

    cursor = con.cursor()
    sql_query = "INSERT INTO facts (Facts) VALUES ('%s')"
    cursor.execute(sql_query,(fact))
    con.commit()
    return jsonify({"message":"added"}), 201

@app.route('/addJoke' ,methods=['POST'])
def add_joke():
    data = request.get_json()
    fact = data.get('Jokes')

    cursor = con.cursor()
    sql_query = "INSERT INTO jokes (Jokes) VALUES ('%s')"
    cursor.execute(sql_query,(fact))
    con.commit()
    return jsonify({"message":"added"}), 201




# PUT -> Update
@app.route('/updateFacts' ,methods=['PUT'])
def update_facts():
    id = request.json.get('id')
    fact = request.json.get('Facts')
    cursor = con.cursor()
    query = "UPDATE facts SET Facts=%s WHERE id=%s"
    cursor.execute(query, (fact, id))
    con.commit()
    cursor.close()
    return jsonify({"message":"updated"}), 202

@app.route('/updateJokes' ,methods=['PUT'])
def update_jokes():
    id = request.json.get('id')
    joke = request.json.get('Jokes')
    cursor = con.cursor()
    query = "UPDATE jokes SET Jokes=%s WHERE id=%s"
    cursor.execute(query, (joke, id))
    con.commit()
    cursor.close()
    return jsonify({"message":"updated"}), 202

    


# DELETE
@app.route('/deleteFact/<int:id>' ,methods=['DELETE'])
def delete_fact(id):
    cursor = con.cursor()
    query = "DELETE FROM facts WHERE id=%s"
    cursor.execute(query,(id,))
    con.commit()
    cursor.close()
    return jsonify({"message":"deleted"})

@app.route('/deleteJoke/<int:id>' ,methods=['DELETE'])
def delete_joke(id):
    cursor = con.cursor()
    query = "DELETE FROM jokes WHERE id=%s"
    cursor.execute(query,(id,))
    con.commit()
    cursor.close()
    return jsonify({"message":"deleted"}), 203


# EXPORT TO JSON
@app.route('/export/facts', methods=['GET'])
def export_facts():
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT * FROM facts")
    facts = cursor.fetchall()
    cursor.close()
    
    with open('facts.json', 'w') as f:
        json.dump(facts, f, indent=4)
    
    return jsonify({"message": "Exported to facts.json", "count": len(facts)}), 200


@app.route('/export/jokes', methods=['GET'])
def export_jokes():
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jokes")
    jokes = cursor.fetchall()
    cursor.close()
    
    with open('jokes.json', 'w') as f:
        json.dump(jokes, f, indent=4)
    
    return jsonify({"message": "Exported to jokes.json", "count": len(jokes)}), 200


@app.route('/export/all', methods=['GET'])
def export_all():
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT * FROM facts")
    facts = cursor.fetchall()
    cursor.execute("SELECT * FROM jokes")
    jokes = cursor.fetchall()
    cursor.close()
    
    export_data = {
        "facts": facts,
        "jokes": jokes
    }
    
    with open('export.json', 'w') as f:
        json.dump(export_data, f, indent=4)
    
    return jsonify({"message": "Exported to export.json", "facts_count": len(facts), "jokes_count": len(jokes)}), 200










if __name__ == "__main__":
    print("connecting to con....")
    app.run(debug=True)
