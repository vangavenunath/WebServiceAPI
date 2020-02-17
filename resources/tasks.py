from flask import Response, request
from flask_restful import Resource
from database.interactions import DatabaseInteractions


class TaskApi(Resource):

    def put(self):
        dbobj = DatabaseInteractions()
        print("PUT method is called")
        out = dbobj.update_employee_tasks(request.json['EmployeeName'][0])
        return out, 200

    def post(self):
        dbobj = DatabaseInteractions()
        print("POST Method is called")
        print(request.json)
        out = dbobj.insert_employee_tasks(request.json['EmployeeName'][0], request.json['TaskName'][0])
        return out, 200

    def delete(self):
        print("DELETE method is called")
        print(request.json)
        return 'Success', 201

class EmployeeLoginLogoutApi(Resource):
    def put(self, employee_name):
        dbobj = DatabaseInteractions()
        print("PUT method is called")
        out = dbobj.update_employee_clockinout(employee_name)
        return out, 200

    def post(self, employee_name):
        dbobj = DatabaseInteractions()
        print("POST Method is called")
        print(request.json)
        out = dbobj.insert_employee_clockin(employee_name)
        return out, 200

    def get(self, employee_name):
        dbobj = DatabaseInteractions()
        print("GET Method is called")
        print(request.json)
        out = dbobj.get_employee_clock_in_out_status(employee_name)
        return out, 200



class EmployeeTasksApi(Resource):

    def get(self, employee_name):
        dbobj = DatabaseInteractions()
        print("EmployeeTasksApi GET method is called")
        print(employee_name)
        json_data = eval(dbobj.get_tasks_by_employee_name(employee_name).replace("null",'""'))
        return json_data, 200


class TasksApi(Resource):

    def get(self, task_name):
        dbobj = DatabaseInteractions()
        print("TasksApi GET method is called")
        tasks = eval(dbobj.get_tasks(task_name))
        return tasks, 200


class EmployeesApi(Resource):

    def get(self, employee_name):
        dbobj = DatabaseInteractions()
        print("TasksApi GET method is called")
        employees = eval(dbobj.get_employees(employee_name))
        return employees, 200

class EmployeeClockApi(Resource):

    def get(self, employee_name):
        dbobj = DatabaseInteractions()
        print("EmployeeClockApi GET method is called")
        status = dbobj.get_clock_in_out_status(employee_name)
        return status, 200