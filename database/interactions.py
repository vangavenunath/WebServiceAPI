import fdb, json
from utils import DateTimeEncoder


class DatabaseInteractions:
    def get_connection(self):
        con = fdb.connect(dsn='localhost:C:\\Users\\Laddu\\PycharmProjects\\WebService\\data\\OSTENDO.FDB',
                          user='SYSDBA',
                          password='masterkey')
        return con

    def get_employees(self, employee_name):
        con = self.get_connection()
        cur = con.cursor()
        query = "SELECT FIRST 5 EMPLOYEENAME FROM EMPLOYEE_VIEW WHERE EMPLOYEENAME LIKE '%" + employee_name + "%'"
        emp_result_set = cur.execute(query).fetchall()
        employees = [''.join(i) for i in emp_result_set]
        json_employees = json.dumps(employees, cls=DateTimeEncoder)
        return json_employees

    def get_tasks(self, task_name):
        con = self.get_connection()
        cur = con.cursor()
        tasks_result_set = cur.execute(
            "SELECT TASKNAME FROM TASKNAMES WHERE TASKNAME LIKE '%" + task_name + "%'").fetchall()
        tasks = [''.join(i) for i in tasks_result_set]
        json_tasks = json.dumps(tasks, cls=DateTimeEncoder)
        con.close()
        return json_tasks

    def get_clock_in_out_status(self, employee_name):
        con = self.get_connection()
        cur = con.cursor()
        status_result_set = cur.execute(
            "SELECT 1 FROM WEB_TIMESHEETLINES WHERE EMPLOYEENAME = '" + employee_name + "' AND DAYENDTIME IS NULL").fetchall()
        status = [i[0] for i in status_result_set]
        con.close()
        if 1 in status:
            return "True"
        else:
            return "False"

    def get_tasks_by_employee_name(self, employee_name):
        con = self.get_connection()
        cur = con.cursor()
        res = cur.execute("""
        SELECT DATEWORKED, TASKORSTEPNAME, DAYSTARTTIME, DAYENDTIME, HOURSWORKED, REFERENCEDESCRIPTION FROM WEB_TIMESHEETLINES
        WHERE EMPLOYEENAME = '""" + employee_name + """'""")
        results = res.fetchall()
        data = json.dumps(results, cls=DateTimeEncoder)
        return data

    def insert_employee_tasks(self, employee_name, task_name):
        con = self.get_connection()
        cur = con.cursor()
        # request.json.get('description',"")
        query = "INSERT INTO WEB_TIMESHEETLINES SELECT cast('Now' as date),'" + '' + "','" + \
                employee_name + "','" + task_name + "',cast('Now' as TIMESTAMP),NULL,0,0,0,cast('Now' as TIMESTAMP),cast('Now' as TIMESTAMP) from rdb$database"
        cur.execute(query)
        con.commit()
        return "Success"

    def update_employee_tasks(self, employee_name):
        con = self.get_connection()
        cur = con.cursor()
        cur.callproc("UPDATE_TASK", (employee_name,))
        con.commit()
        return "Success"

    def update_employee_clockinout(self, employee_name):
        con = self.get_connection()
        cur = con.cursor()
        cur.callproc("UPDATE_EMPLOYEE_CLOCKINOUT", (employee_name,))
        con.commit()
        return "Success"

    def get_employee_clock_in_out_status(self, employee_name):
        con = self.get_connection()
        cur = con.cursor()
        status_result_set = cur.execute(
            "SELECT 1 FROM WEB_EMPLOYEE_CLOCKINOUT WHERE EMPLOYEENAME = '" + employee_name + "' AND DAYENDTIME IS NULL").fetchall()
        status = [i[0] for i in status_result_set]
        print(status)
        con.close()
        if 1 in status:
            return "True"
        else:
            return "False"

    def insert_employee_clockin(self, employee_name):
        con = self.get_connection()
        cur = con.cursor()
        # request.json.get('description',"")
        query = "INSERT INTO WEB_EMPLOYEE_CLOCKINOUT \
         SELECT '"+employee_name + "', cast('Now' as TIMESTAMP),NULL,0, cast('Now' as TIMESTAMP),cast('Now' as TIMESTAMP) from rdb$database"
        cur.execute(query)
        con.commit()
        return "Success"

if __name__ == '__main__':
    dbobj = DatabaseInteractions()
    results = dbobj.get_employees('')
    if "Jili Ren" in results:
        print("TESTING")
    jsondata = dbobj.get_tasks_by_employee_name("Venkataprasad Kola").replace("null","")
    print(jsondata)
