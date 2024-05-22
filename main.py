import psycopg2

conn = psycopg2.connect(database = 'finalproject1', user = 'postgres', password = 'kiflin24', host='localhost', port = 5432)

cur = conn.cursor()

# # select dokter
def read_data_dokter(cur):
    query = "SELECT * FROM dokter"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
# cur.close()
conn.close
# query = "SELECT * FROM dokter"
# cur.execute(query)
# data = cur.fetchall()
# for i in data:
#     print(i)
# cur.close()
# conn.close

# insert data
total_input = int(input(f"Mau menambahkan berapa data? "))

for i in range(total_input):
    id_dokter = input(f"Masukkan no id dokter: ")
    nama_dokter = input(f"Masukkan nama dokter: ")
    alamat = input(f"Masukkan alamat: ")
    no_telepon = input (f"Masukkan no telepon: ")
    query = f"INSERT INTO dokter(id_dokter, nama_dokter, alamat, no_telepon) VALUES (%s, %s, %s, %s)"
    cur.execute(query, (id_dokter, nama_dokter, alamat, no_telepon))
    
conn.commit()

# read_data(cur)
# cur.close()
# conn.close()

# update
# query = f"UPDATE dokter SET di_dokter = %s, nama_dokter = %s, alamat = %s, no_telepon = %s "
# # read_data_dokter(cur)

# # read semua data dokter
query_select = "SELECT * FROM dokter"
cur.execute(query_select)
data1 = cur.fetchall()
for i in data1:
    print(i)

# # read data dokter yang dipilih
# id_dokter = input('Masukkan id dokter yang ingin di update: ')
# show_query = "SELECT * FROM dokter WHERE id_dokter = %s"
# cur.execute(show_query, (id_dokter))
# data2 = cur.fetchone()

# if data2:
#     print("f")
#     print(f'id dokter{data2[0]}')
#     print(f'nama dokter{data2[1]}')
#     print(f'alamat{data2[2]}')
#     print(f'no telepon{data2[3]}')

#update
# id_dokter = input(f"Masukkan no id dokter: ")
# nama_dokter = input(f"Masukkan nama dokter: ")
# alamat = input(f"Masukkan alamat: ")
# no_telepon = input (f"Masukkan no telepon: ")