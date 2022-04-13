import json
import sqlite3
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

# db_connect = create_engine('sqlite:///chinook.db')

def get_connection():
    return sqlite3.connect("chinook.db")


app = Flask(__name__)
api = Api(app)


class Employees(Resource):
    post_fields = [
        "Address", "BirthDate",
        "City", "Country",
        "Email",
        "Fax", "FirstName",
        "HireDate", "LastName",
        "Phone", "PostalCode",
        "ReportsTo", "State", "Title"
    ]

    def get(self):
        conn = db_connect.connect()
        # This line performs query and returns json result
        query = conn.execute("select * from employees")
        conn.close()
        return {'employees': [i[0] for i in query.cursor.fetchall()]}

    def post(self):
        """
        Method for create new user in database
        """
        data_obj = json.loads(request.data)
        conn = get_connection()

        post_template = """insert into employees """
        data_obj_keys = ', '.join(data_obj.keys())
        data_obj_values = ', '.join(map(lambda x: "\'{}\'".format(str(x)), data_obj.values()))
        post_query = post_template + f'({data_obj_keys})' + f' values ({data_obj_values})' + ' returning FirstName'

        try:
            cursor = conn.cursor()
            query = cursor.execute(post_query)
        except Exception as e:
            conn.rollback()
            return jsonify({'data': f'User {first_name} {last_name} already in DB'})

        first_name = data_obj.get('FirstName')
        last_name = data_obj.get('LastName')
        return jsonify({'data': f'User {first_name} {last_name} was created'})



class Tracks(Resource):
    def get(self):
        conn = get_connection()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple(query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)


class Employees_Name(Resource):
    def get(self, employee_id):
        """
        Method that Get user from database by id
        :param: employee_id (int)
        """
        conn = get_connection()

        try:
            cursor = conn.cursor()
            query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        except Exception as e:
            conn.rollback()
            return jsonify({'data' : 'Server error occured'})

        description = [item[0] for item in query.description]
        employee_info = query.fetchall()
        result = {'data': [dict(zip(description, *employee_info))]}
        return jsonify(result)

    def delete(self, employee_id):
        """
        Method that removed user from database by id
        :param: employee_id (int)
        """
        if False:
            conn = db_connect.connect()
            query = conn.execute("delete from employees where EmployeeId =%d "  %int(employee_id))
            conn.close()
            result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify({'data': 'delete was called with employee_id={}'.format(employee_id)})


# add URI paths for our API
api.add_resource(Employees, '/employees')
api.add_resource(Tracks, '/tracks')
api.add_resource(Employees_Name, '/employees/<employee_id>')


if __name__ == '__main__':
     app.run(port='5002')
