from flask import Flask, render_template
from impala.dbapi import connect


app = Flask(__name__)

@app.route("/")
def main():
    # CONNECTION TO DATABASE
    conn = connect(host='your hive db host Ip/hostname', port=10000, auth_mechanism='PLAIN', user='xxx', password='xxx',
                   database='xxx')
    c = conn.cursor()

    # QUERIES
    query_1 = """
      SELECT *
      FROM your_table
    """
    query_2 = """
        SELECT *
        FROM your_table_2 a
        where to_date(timestamp) = current_date
        group by x
    """

    # EXECUTE QUERIES

    # EXE TOTAL
    c.execute(query_1)
    result_1 = c.fetchall()

    # EXE TOTAL PER REGION
    c.execute(query_2)
    result_2 = c.fetchall()
    fields = ['field_1', 'field_2', 'field_3']
    # CONVERT DATA tuple TO dictionary	
    total_per_region = [dict(zip(fields, d)) for d in reg]

    # RETURN VALUES TO TEMPLATE
    return render_template('index.html', result1=result_1, result2=result_2)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
