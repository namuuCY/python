import io, os

input2 = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

employees = set([])

for _ in range(int(input2())):
    employee, enter_or_leave = input2().split()
    if enter_or_leave == b'enter':
        employees.add(employee)
    else:
        employees.discard(employee)

os.write(1, b"\n".join(sorted(employees, reverse=True)))
 