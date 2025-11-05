
with open('input') as f:
    lines = f.readlines()
    max = 0
    seats = []
    for i in lines:
        i = i.rstrip()
        print(i)
        rowstr = i[0: 7]
        columnstr = i[7:]
        row = int(rowstr.replace('F','0').replace('B','1'), 2)
        column = int(columnstr.replace('L','0').replace('R','1'), 2)
        seat_id = (row*8)+column
        seats.append(seat_id)

    print(len(seats))
        
    for i in range(0, 127):
        for j in range(0, 7):
            s_id = (i * 8) + j
            
            if s_id in seats:
                print(f'Row {i}, Column {j}: OCCUPIED')
            else:
                print(f'Row {i}, Column {j}: AVAILABLE, ID: {s_id}')