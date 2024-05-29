import psycopg2
from prettytable import PrettyTable
import time


def connect_db():
    try:
        conn = psycopg2.connect(database='finalproject1', user='postgres', password='kiflin24', host='localhost', port=5432)
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def admin_login():
    conn = connect_db()
    if not conn:
        return False
    cur = conn.cursor()
    
    try:
        nama_admin = input("Masukkan username admin: ")
        id_admin = input("Masukkan password admin: ")

        query = "SELECT * FROM admin WHERE nama_admin = %s AND id_admin = %s"
        cur.execute(query, (nama_admin, id_admin))
        admin = cur.fetchone()
        
        if admin:
            print("Login berhasil.")
            return True
        else:
            print("Username atau password salah.")
            return False
    except Exception as e:
        print(f"Error during login: {e}")
        return False
    finally:
        cur.close()
        conn.close()
        

def patient_register():
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()
    
    try:
        nama_pasien = input("Masukkan nama pasien: ")
        tanggal_lahir = input("Masukkan tanggal lahir (YYYY-MM-DD): ")
        alamat = input("Masukkan alamat: ")
        no_telepon = input("Masukkan no telepon: ")
        id_pasien = input("Masukkan ID pasien: ")

        query = "INSERT INTO pasien (id_pasien, nama_pasien, tanggal_lahir, alamat, no_telepon) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(query, (id_pasien, nama_pasien, tanggal_lahir, alamat, no_telepon))
        conn.commit()
        print("Registrasi pasien berhasil.")

    except Exception as e:
        print(f"Error while registering patient: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
        

def patient_login():
    conn = connect_db()
    if not conn:
        return False
    cur = conn.cursor()
    
    try:
        nama_pasien = input("Masukkan nama pasien: ")
        id_pasien = input("Masukkan ID pasien: ")

        query = "SELECT * FROM pasien WHERE nama_pasien = %s AND id_pasien = %s"
        cur.execute(query, (nama_pasien, id_pasien))
        patient = cur.fetchone()
        
        if patient:
            print("Login berhasil.")
            return True
        else:
            print("Nama pasien atau ID pasien salah.")
            return False
    except Exception as e:
        print(f"Error during login: {e}")
        return False
    finally:
        cur.close()
        conn.close()
        

def choose_option_admin():
    print('(1) Kelola Data Dokter\n(2) Kelola Data Pasien\n(3) Kelola Data Obat')
    choose = input("Pilih Opsi: ")
    
    if choose == "1":
        choose_option_dokter()
    elif choose == "2":
        choose_option_pasien()
    elif choose == "3":
        choose_option_obat()
    else:
        print("Opsi tidak valid. Silakan coba lagi.")


def choose_option_dokter():
    while True:
        print('(1) Menambahkan data dokter\n(2) Melihat data dokter\n(3) Update data dokter\n(4) Menghapus data dokter\n(5) Kembali ke Menu Utama')
        choose = input("Pilih Opsi: ")
        
        if choose == "1":
            tambah_data_dokter()
        elif choose == "2":
            read_data_dokter()
        elif choose == "3":
            update_data_dokter()
        elif choose == "4":
            hapus_data_dokter()
        elif choose == "5":
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")
            

def choose_option_pasien():
    while True:
        print('(1) Menambahkan data pasien\n(2) Melihat data pasien\n(3) Update data pasien\n(4) Menghapus data pasien\n(5) Kembali ke menu utama')
        choose = input("Pilih Opsi: ")
        
        if choose == "1":
            tambah_data_pasien()
        elif choose == "2":
            read_data_pasien()
        elif choose == "3":
            update_data_pasien()
        elif choose == "4":
            hapus_data_pasien()
        elif choose == "5" :
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")
            
            
def choose_option_obat():
    while True:
        print('(1) Menambahkan data obat\n(2) Melihat data obat\n(3) Update data obat\n(4) Menghapus data obat\n(5) Kembali ke menu utama')
        choose = input("Pilih Opsi: ")
        
        if choose == "1":
            tambah_data_obat()
        elif choose == "2":
            read_data_obat()
        elif choose == "3":
            update_data_obat()
        elif choose == "4":
            hapus_data_obat()
        elif choose == "5":
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

def choose_option_patient():
    print('(1) Melihat data dokter')
    choose = input("Pilih Opsi: ")
    
    if choose == "1":
        read_data_dokter()
    else:
        print("Opsi tidak valid. Silakan coba lagi.")
        

def tambah_data_dokter():
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()
    
    try:
        data_dokter = "SELECT * FROM dokter"
        cur.execute(data_dokter)
        dokter = cur.fetchall()
        
        table = PrettyTable()
        table.field_names = ["ID Dokter", "Nama Dokter", "Alamat", "No Telepon"]
        for row in dokter:
            table.add_row(row)
        
        print(table)

        total_input = int(input("Mau menambahkan berapa data? "))
        for i in range(total_input):
            id_dokter = input("Masukkan no id dokter: ")
            nama_dokter = input("Masukkan nama dokter: ")
            alamat = input("Masukkan alamat: ")
            no_telepon = input("Masukkan no telepon: ")
            query = "INSERT INTO dokter(id_dokter, nama_dokter, alamat, no_telepon) VALUES (%s, %s, %s, %s)"
            cur.execute(query, (id_dokter, nama_dokter, alamat, no_telepon))
        
        conn.commit()
        print("Data dokter berhasil ditambahkan.")
    except Exception as e:
        print(f"Error while inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
        

def read_data_dokter():
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()
    
    try:
        lihat_data = "SELECT * FROM dokter"
        cur.execute(lihat_data)
        data = cur.fetchall()
        
        table = PrettyTable()
        table.field_names = ["ID Dokter", "Nama Dokter", "Alamat", "No Telepon"]
        for row in data:
            table.add_row(row)
        
        print(table)
    except Exception as e:
        print(f"Error while reading data: {e}")
    finally:
        cur.close()
        conn.close()
        

def update_data_dokter():
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()
    
    try:
        query_select = "SELECT * FROM dokter"
        cur.execute(query_select)
        data1 = cur.fetchall()
        
        table = PrettyTable()
        table.field_names = ["ID Dokter", "Nama Dokter", "Alamat", "No Telepon"]
        for row in data1:
            table.add_row(row)
        
        print(table)

        id_dokter = input('Masukkan ID dokter yang ingin di-update: ')
        show_query = "SELECT * FROM dokter WHERE id_dokter = %s"
        cur.execute(show_query, (id_dokter,))
        data2 = cur.fetchone()

        if data2:
            table_single = PrettyTable()
            table_single.field_names = ["ID Dokter", "Nama Dokter", "Alamat", "No Telepon"]
            table_single.add_row(data2)
            print(table_single)

            nama_dokter = input(f"Masukkan nama dokter (lama: {data2[1]}): ")
            alamat = input(f"Masukkan alamat (lama: {data2[2]}): ")
            no_telepon = input(f"Masukkan no telepon (lama: {data2[3]}): ")

            update_query = "UPDATE dokter SET nama_dokter = %s, alamat = %s, no_telepon = %s WHERE id_dokter = %s"
            cur.execute(update_query, (nama_dokter, alamat, no_telepon, id_dokter))
            conn.commit()
            print("Data dokter berhasil diupdate.")
        else:
            print("Data dokter tidak ditemukan.")
    except Exception as e:
        print(f"Error while updating data: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
        

def hapus_data_dokter():
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()

    try:
        id_dokter = input('Masukkan id dokter yang ingin dihapus: ')
        delete_query = "DELETE FROM dokter WHERE id_dokter = %s"
        cur.execute(delete_query, (id_dokter,))
        conn.commit()
        print(f"Data dokter dengan id {id_dokter} telah dihapus.")
    except Exception as e:
        print(f"Error while deleting data: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
        

def tambah_data_pasien():
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()
    
    try:
        data_pasien = "SELECT * FROM pasien"
        cur.execute(data_pasien)
        pasien = cur.fetchall()
        for row in pasien:
            print(row)
        
        total_input = int(input(f"Mau menambahkan berapa data? "))
        for i in range(total_input):
            id_pasien = input(f"Masukkan no id pasien: ")
            nama_pasien = input(f"Masukkan nama pasien: ")
            tanggal_lahir = input(f"Masukkan tanggal lahir (YYYY-MM-DD): ")
            alamat = input(f"Masukkan alamat: ")
            no_telepon = input(f"Masukkan no telepon: ")
            query = "INSERT INTO pasien(id_pasien, nama_pasien, tanggal_lahir, alamat, no_telepon) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(query, (id_pasien, nama_pasien, tanggal_lahir, alamat, no_telepon))
        
        conn.commit()
        print("Data pasien berhasil ditambahkan.")
    except Exception as e:
        print(f"Error while inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
        

def read_data_pasien():
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()
    
    try:
        lihat_data = "SELECT * FROM pasien"
        cur.execute(lihat_data)
        data = cur.fetchall()
        
        table = PrettyTable()
        table.field_names = ["ID Pasien", "Nama Pasien", "Tanggal Lahir", "Alamat", "No Telepon"]
        for row in data:
            # Format tanggal lahir menjadi YYYY-MM-DD
            formatted_row = list(row)
            formatted_row[2] = formatted_row[2].strftime('%Y-%m-%d')
            table.add_row(formatted_row)
        
        print(table)
    except Exception as e:
        print(f"Error while reading data: {e}")
    finally:
        cur.close()
        conn.close()
        

def update_data_pasien():
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()
    
    try:
        query_select = "SELECT * FROM pasien"
        cur.execute(query_select)
        data1 = cur.fetchall()
        table = PrettyTable()
        table.field_names = ["ID Pasein", "Nama Pasien", "Alamat", "Tanggal Lahir", "No Telepon"]
        for row in data1:
            table.add_row(row)
        
        print(table)
    

        id_pasien = input('Masukkan id pasien yang ingin di-update: ')
        show_query = "SELECT * FROM pasien WHERE id_pasien = %s"
        cur.execute(show_query, (id_pasien,))
        data2 = cur.fetchone()

        if data2:
            table_single = PrettyTable()
            table_single.field_names = ["ID Pasein", "Nama Pasien", "Alamat", "Tanggal Lahir", "No Telepon"]
            table_single.add_row(data2)
            print(table_single)
            
            print(f'id pasien: {data2[0]}')
            print(f'nama pasien: {data2[1]}')
            print(f'tanggal lahir: {data2[2]}')
            print(f'alamat: {data2[3]}')
            print(f'no telepon: {data2[4]}')

            nama_pasien = input(f"Masukkan nama pasien (lama: {data2[1]}): ")
            tanggal_lahir = input(f"Masukkan tanggal lahir (lama: {data2[2]}): ")
            alamat = input(f"Masukkan alamat (lama: {data2[3]}): ")
            no_telepon = input(f"Masukkan no telepon (lama: {data2[4]}): ")

            update_query = "UPDATE pasien SET nama_pasien = %s, tanggal_lahir = %s, alamat = %s, no_telepon = %s WHERE id_pasien = %s"
            cur.execute(update_query, (nama_pasien, tanggal_lahir, alamat, no_telepon, id_pasien))
            conn.commit()
            print("Data pasien berhasil diupdate.")
        else:
            print("Data pasien tidak ditemukan.")
    except Exception as e:
        print(f"Error while updating data: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
        

def hapus_data_pasien():
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()

    try:
        # Tampilkan semua pasien agar user bisa memverifikasi ID
        query_select = "SELECT * FROM pasien"
        cur.execute(query_select)
        data = cur.fetchall()
        
        table = PrettyTable()
        table.field_names = ["ID Pasien", "Nama Pasien", "Tanggal Lahir", "Alamat", "No Telepon"]
        for row in data:
            table.add_row(row)
        
        print(table)
        
        id_pasien = input('Masukkan id pasien yang ingin dihapus: ')

        # Cek apakah pasien dengan ID tersebut ada
        check_query = "SELECT * FROM pasien WHERE id_pasien = %s"
        cur.execute(check_query, (id_pasien,))
        patient = cur.fetchone()

        if patient:
            delete_query = "DELETE FROM pasien WHERE id_pasien = %s"
            cur.execute(delete_query, (id_pasien,))
            conn.commit()
            print(f"Data pasien dengan id {id_pasien} telah dihapus.")
        else:
            print(f"Pasien dengan id {id_pasien} tidak ditemukan.")
    except Exception as e:
        print(f"Error while deleting data: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def tambah_data_obat():
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()
    
    try:
        # Tampilkan jenis obat yang tersedia
        data_jenis_obat = "SELECT * FROM obat"
        cur.execute(data_jenis_obat)
        jenis_obat = cur.fetchall()

        jenis_table = PrettyTable()
        jenis_table.field_names = ["ID Obat", "Nama Obat", "Harga", "ID Jenis Obat"]
        for row in jenis_obat:
            jenis_table.add_row(row)
        
        print(jenis_table)

        total_input = int(input("Mau menambahkan berapa data? "))
        for i in range(total_input):
            id_obat = input("Masukkan ID obat: ")
            nama_obat = input("Masukkan nama obat: ")
            harga = float(input("Masukkan harga: "))
            jenis_obat_id_jenisobat = int(input("Masukkan ID jenis obat: "))

            # Sesuaikan nama kolom sesuai dengan struktur tabel di database
            query = "INSERT INTO obat (id_obat, nama_obat, harga, jenis_obat_id) VALUES (%s, %s, %s, %s)"
            cur.execute(query, (id_obat, nama_obat, harga, jenis_obat_id_jenisobat))
        
        conn.commit()
        print("Data obat berhasil ditambahkan.")
    except Exception as e:
        print(f"Error while inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
        

def read_data_obat():
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()
    
    try:
        lihat_data = "SELECT o.id_obat, o.nama_obat, o.harga, j.id_jenisobat FROM obat o JOIN jenis_obat j ON o.jenis_obat_id_jenisobat = j.id_jenisobat"
        cur.execute(lihat_data)
        data = cur.fetchall()

        table = PrettyTable()
        table.field_names = ["ID Obat", "Nama Obat", "Harga", "Jenis Obat"]
        for row in data:
            table.add_row(row)
        
        print(table)
    except Exception as e:
        print(f"Error while reading data: {e}")
    finally:
        cur.close()
        conn.close()
        

def update_data_obat():
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()
    
    try:
        lihat_data = "SELECT o.id_obat, o.nama_obat, o.harga, j.id_jenisobat FROM obat o JOIN jenis_obat j ON o.jenis_obat_id_jenisobat = j.id_jenisobat"
        cur.execute(lihat_data)
        data = cur.fetchall()

        table = PrettyTable()
        table.field_names = ["ID Obat", "Nama Obat", "Harga", "Jenis Obat ID"]
        for row in data:
            table.add_row(row)
        
        print(table)

        id_obat = input('Masukkan ID obat yang ingin di-update: ')
        show_query = "SELECT * FROM obat WHERE id_obat = %s"
        cur.execute(show_query, (id_obat,))
        data2 = cur.fetchone()

        if data2:
            table_single = PrettyTable()
            table_single.field_names = ["ID Obat", "Nama Obat", "Harga", "Jenis Obat ID"]
            table_single.add_row(data2)
            print(table_single)

            nama_obat = input(f"Masukkan nama obat (lama: {data2[1]}): ")
            harga = float(input(f"Masukkan harga (lama: {data2[2]}): "))
            jenis_obat_id_jenisobat = int(input(f"Masukkan ID jenis obat (lama: {data2[3]}): "))

            update_query = "UPDATE obat SET nama_obat = %s, harga = %s, jenis_obat_id_jenisobat = %s WHERE id_obat = %s"
            cur.execute(update_query, (nama_obat, harga, jenis_obat_id_jenisobat, id_obat))
            conn.commit()
            print("Data obat berhasil diupdate.")
        else:
            print("Data obat tidak ditemukan.")
    except Exception as e:
        print(f"Error while updating data: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def hapus_data_obat():
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()

    try:
        id_obat = input('Masukkan id obat yang ingin dihapus: ')
        delete_query = "DELETE FROM obat WHERE id_obat = %s"
        cur.execute(delete_query, (id_obat,))
        conn.commit()
        print(f"Data obat dengan id {id_obat} telah dihapus.")
    except Exception as e:
        print(f"Error while deleting data: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def main():
    while True:
        print('(1) Login Admin\n(2) Registrasi Pasien\n(3) Login Pasien\n(4) Keluar')
        choice = input("Pilih Opsi: ")
        
        if choice == "1":
            if admin_login():
                choose_option_admin()
        elif choice == "2":
            patient_register()
        elif choice == "3":
            if patient_login():
                choose_option_patient()
        elif choice == "4":
            print("Terima kasih! Sampai jumpa lagi.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
