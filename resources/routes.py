from .tasks import TaskApi, EmployeeTasksApi, TasksApi, EmployeesApi, EmployeeClockApi, EmployeeLoginLogoutApi


def initialize_routes(api):
    api.add_resource(TaskApi, '/api/v1/task/')
    api.add_resource(TasksApi, '/api/v1/tasks/<string:task_name>')
    api.add_resource(EmployeeTasksApi, '/api/v1/employee_tasks/<string:employee_name>')
    api.add_resource(EmployeesApi, '/api/v1/employees/<string:employee_name>')
    api.add_resource(EmployeeClockApi, '/api/v1/employee_clock/<string:employee_name>')
    api.add_resource(EmployeeLoginLogoutApi, '/api/v1/employee_log/<string:employee_name>')
