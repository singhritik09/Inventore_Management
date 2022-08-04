for p in Employee.objects.raw('SELECT * FROM employee'):
    print(p)