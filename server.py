import json
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db')
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
        print('stas')
        conn = db_connect.connect()
        # This line performs query and returns json result
        query = conn.execute("select * from employees")
        return {'employees': [i[0] for i in query.cursor.fetchall()]}

    def post(self):
        """
        Method for create user in database
        """
        data_obj = json.loads(request.data)
        conn = db_connect.connect()

        post_query = """insert into employees"""
        data_obj_keys = ', '.join(data_obj.keys())
        data_obj_values = ', '.join(map(lambda x: f"'{str(x)}'", data_obj.values()))
        import pdb
        pdb.set_trace()

        post_query + f' ({data_obj_keys})' + f' values ({data_obj_values})'



        # for field_name in self.post_fields:
        #     post_query += f"{field_name}='{data_obj.get(field_name)}'"
        #
        #     if field_name == 'Title':
        #         post_query += ';'
        #     else:
        #         post_query += ', '

        # query = conn.execute(post_query)
        # sql_query = query.cursor.fetchall()
        first_name = data_obj.get('FirstName')
        last_name = data_obj.get('LastName')
        return jsonify({'data': f'User {first_name} {last_name} was created'})



class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple(query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)


class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

    def delete(self, employee_id):
        """
        Method that removed user from database by id
        :param: employee_id (int)
        """
        print('It was called "delete" method!')
        return jsonify({'data': 'delete was called with employee_id={}'.format(employee_id)})


# add URI paths for our API
api.add_resource(Employees, '/employees')
api.add_resource(Tracks, '/tracks')
api.add_resource(Employees_Name, '/employees/<employee_id>')


if __name__ == '__main__':
     app.run(port='5002')
