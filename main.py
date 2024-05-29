import psycopg2
from prettytable import PrettyTable
import time
import os

def connect_db():
    try:
        conn = psycopg2.connect(database='finalproject1', user='postgres', password='kiflin24', host='localhost', port=5432)
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def admin_login():
    while True:
        os.system('clear')
        print("\033[1;36m+========================================================+")
        print("|                     LOGIN ADMIN                        |")
        print("+========================================================+\033[0m")
        conn = connect_db()
        if not conn:
            return None
        cur = conn.cursor()

        try:
            nama_admin = input("\033[1mMasukkan nama admin:\033[0m ")
            id_admin = input("\033[1mMasukkan ID admin:\033[0m ")

            query = "SELECT * FROM admin WHERE nama_admin = %s AND id_admin = %s"
            cur.execute(query, (nama_admin, id_admin))
            admin = cur.fetchone()

            if admin:
                print("\033[1mLogin berhasil.\033[0m")
                time.sleep(2)  # Tunggu 2 detik sebelum masuk ke menu admin
                return id_admin  # Mengembalikan ID admin setelah login berhasil
            else:
                print("\033[1mNama admin atau ID admin salah. Coba lagi.\033[0m")
                time.sleep(2)  # Tunggu 2 detik sebelum kembali ke tampilan login
        except Exception as e:
            print(f"\033[1mError during login:\033[1m {e}")
            time.sleep(2)  # Tunggu 2 detik sebelum kembali ke tampilan login
        finally:
            cur.close()
            conn.close()

def patient_register():
    os.system('clear')
    print("\033[1;36m+========================================================+")
    print("|                      REGISTRASI                        |")
    print("+========================================================+\033[0m")
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()
    
    try:
        nama_pasien = input("\033[1mMasukkan nama pasien: \033[0m")
        tanggal_lahir = input("\033[1mMasukkan tanggal lahir (YYYY-MM-DD): \033[0m")
        alamat = input("\033[1mMasukkan alamat: \033[0m")
        no_telepon = input("\033[1mMasukkan no telepon: \033[0m")
        id_pasien = input("\033[1mMasukkan ID pasien: \033[0m")

        query = "INSERT INTO pasien (id_pasien, nama_pasien, tanggal_lahir, alamat, no_telepon) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(query, (id_pasien, nama_pasien, tanggal_lahir, alamat, no_telepon))
        conn.commit()
        print("\033[92mRegistrasi pasien berhasil.\033[0m")

    except Exception as e:
        print(f"\033[91mError while registering patient: {e}\033[0m")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def patient_login():
    while True:
        os.system('clear')
        print("\033[1;36m+========================================================+")
        print("|                      LOGIN PASIEN                      |")
        print("+========================================================+\033[0m")
        conn = connect_db()
        if not conn:
            return None
        cur = conn.cursor()

        try:
            nama_pasien = input("\033[1mMasukkan nama pasien:\033[0m ")
            id_pasien = input("\033[1mMasukkan ID pasien:\033[0m ")

            query = "SELECT * FROM pasien WHERE nama_pasien = %s AND id_pasien = %s"
            cur.execute(query, (nama_pasien, id_pasien))
            patient = cur.fetchone()

            if patient:
                print("\033[1mLogin berhasil.\033[0m")
                return id_pasien  # Mengembalikan ID pasien setelah login berhasil
            else:
                print("\033[1mNama pasien atau ID pasien salah.\033[0m")
                time.sleep(2)  # Tunggu 2 detik sebelum kembali ke tampilan login
        except Exception as e:
            print(f"\033[1mError during login:\033[1m {e}")
            time.sleep(2)  # Tunggu 2 detik sebelum kembali ke tampilan login
        finally:
            cur.close()
            conn.close()

def choose_option_admin():
    while True:
        os.system('clear')
        print('\033[1m(1) Kelola Data Dokter\n(2) Kelola Data Pasien\n(3) Kelola Data Obat\n(4) Exit\033[0m')
        choose = input("\033[1mPilih Opsi: \033[0m")
        
        if choose == "1":
            choose_option_dokter()
        elif choose == "2":
            choose_option_pasien()
        elif choose == "3":
            choose_option_obat()
        elif choose == "4":
            print("\n\033[1mTerima kasih! Kembali ke menu utama.\033[0m\n")
            time.sleep(2)  # Tunggu 2 detik sebelum kembali ke menu utama
            break  # Keluar dari loop dan kembali ke menu utama
        else:
            print("\033[91mOpsi tidak valid. Silakan coba lagi.\033[0m")
    main()  # Tampilkan kembali menu utama setelah keluar dari menu admin

def choose_option_dokter():
    os.system('clear')
    while True:
        print('\033[1m(1) Menambahkan data dokter\n(2) Melihat data dokter\n(3) Update data dokter\n(4) Menghapus data dokter\n(5) Kembali ke Menu Admin\033[0m')
        choose = input("\033[1mPilih Opsi: \033[0m")
        
        if choose == "1":
            tambah_data_dokter()
        elif choose == "2":
            read_data_dokter()
        elif choose == "3":
            update_data_dokter()
        elif choose == "4":
            hapus_data_dokter()
        elif choose == "5":
            choose_option_admin()  # Kembali ke menu admin
        else:
            print("\033[91mOpsi tidak valid. Silakan coba lagi.\033[0m")

def choose_option_pasien():
    os.system('clear')
    while True:
        print('\033[1m(1) Tambah Data Pasien\n(2) Lihat Data Pasien\n(3) Update Data Pasien\n(4) Hapus Data Pasien\n(5) Kembali ke menu utama\033[0m')
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
            print("\033[1mOpsi tidak valid. Silakan coba lagi.\033[0m")
          
def choose_option_obat():
    os.system('clear')
    while True:
        print('\033[1m(1) Menambahkan data obat\n(2) Melihat data obat\n(3) Update data obat\n(4) Menghapus data obat\n(5) Kembali ke menu utama\033[0m')
        choose = input("\033[1mPilih Opsi:\033[0m ")
        
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
            print("\033[1mOpsi tidak valid. Silakan coba lagi.\033[0m")

def choose_option_pasien():
    os.system('clear')
    while True:
        print('\033[1m(1) Tambahkan data pasien\n(2) Lihat data pasien\n(3) Update data pasien\n(4) Hapus data pasien\n(5) Kembali ke menu utama\033[0m')
        choose = input("\033[1mPilih Opsi:\033[0m ")
        
        if choose == "1":
            tambah_data_pasien()  # Panggil fungsi untuk menambahkan data pasien
        elif choose == "2":
            read_data_pasien()  # Panggil fungsi untuk melihat data pasien
        elif choose == "3":
            update_data_pasien()  # Panggil fungsi untuk mengupdate data pasien
        elif choose == "4":
            hapus_data_pasien()  # Panggil fungsi untuk menghapus data pasien
        elif choose == "5":
            break  # Keluar dari loop dan kembali ke menu utama
        else:
            print("\033[1mOpsi tidak valid. Silakan coba lagi.\033[0m")

def tambah_data_dokter():
    os.system('clear')
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

        total_input = int(input("\033[1mMau menambahkan berapa data?\033[0m "))
        for i in range(total_input):
            id_dokter = input("\033[1mMasukkan no id dokter:\033[0m ")
            nama_dokter = input("\033[1mMasukkan nama dokter:\033[0m ")
            alamat = input("\033[1mMasukkan alamat:\033[0m ")
            no_telepon = input("\033[1mMasukkan no telepon:\033[0m ")
            query = "INSERT INTO dokter(id_dokter, nama_dokter, alamat, no_telepon) VALUES (%s, %s, %s, %s)"
            cur.execute(query, (id_dokter, nama_dokter, alamat, no_telepon))
        
        conn.commit()
        print("\033[1mData dokter berhasil ditambahkan.\033[0m")
    except Exception as e:
        print(f"\033[1mError while inserting data:\033[0m {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def read_data_dokter():
    os.system('clear')
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
        print(f"\033[1mError while reading data:\033[0m {e}")
    finally:
        cur.close()
        conn.close()

def update_data_dokter():
    os.system('clear')
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

        id_dokter = input('\033[1mMasukkan ID dokter yang ingin di-update:\033[0m ')
        show_query = "SELECT * FROM dokter WHERE id_dokter = %s"
        cur.execute(show_query, (id_dokter,))
        data2 = cur.fetchone()

        if data2:
            table_single = PrettyTable()
            table_single.field_names = ["ID Dokter", "Nama Dokter", "Alamat", "No Telepon"]
            table_single.add_row(data2)
            print(table_single)

            nama_dokter = input(f"\033[1mMasukkan nama dokter (lama:\033[0m {data2[1]}): ")
            alamat = input(f"\033[1mMasukkan alamat (lama:\033[0m {data2[2]}): ")
            no_telepon = input(f"\033[1mMasukkan no telepon (lama:\033[0m {data2[3]}): ")

            update_query = "UPDATE dokter SET nama_dokter = %s, alamat = %s, no_telepon = %s WHERE id_dokter = %s"
            cur.execute(update_query, (nama_dokter, alamat, no_telepon, id_dokter))
            conn.commit()
            print("\033[1mData dokter berhasil diupdate.\033[0m")
        else:
            print("\033[1mData dokter tidak ditemukan.\033[0m")
    except Exception as e:
        print(f"\033[1mError while updating data:\033[0m {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def hapus_data_dokter():
    os.system('clear')
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
        
        id_dokter = input('\033[1mMasukkan id dokter yang ingin dihapus:\033[0m ')
        delete_query = "DELETE FROM dokter WHERE id_dokter = %s"
        cur.execute(delete_query, (id_dokter,))
        conn.commit()
        print(f"\033[1mData dokter dengan id {id_dokter} telah dihapus.\033[0m")
    except Exception as e:
        print(f"\033[1mError while deleting data:\033[0m {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def tambah_data_pasien():
    os.system('clear')
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
            table.add_row(row)
        
        print(table)
        
        total_input = int(input(f"\033[1mMau menambahkan berapa data?\033[0m "))
        for i in range(total_input):
            id_pasien = input(f"\033[1mMasukkan no id pasien:\033[0m ")
            nama_pasien = input(f"\033[1mMasukkan nama pasien:\033[0m ")
            tanggal_lahir = input(f"\033[1mMasukkan tanggal lahir (YYYY-MM-DD):\033[0m ")
            alamat = input(f"M\033[1masukkan alamat:\033[0m ")
            no_telepon = input(f"\033[1mMasukkan no telepon:\033[0m ")
            query = "INSERT INTO pasien(id_pasien, nama_pasien, tanggal_lahir, alamat, no_telepon) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(query, (id_pasien, nama_pasien, tanggal_lahir, alamat, no_telepon))
        
        conn.commit()
        print("\033[1mData pasien berhasil ditambahkan.\033[1m")
    except Exception as e:
        print(f"\033[1mError while inserting data:\033[1m {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def read_data_pasien():
    os.system('clear')
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
        print(f"\033[1mError while reading data:\033[1m {e}")
    finally:
        cur.close()
        conn.close()

def update_data_pasien():
    os.system('clear')
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
    
        id_pasien = input('\033[1mMasukkan id pasien yang ingin di-update:\033[0m ')
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

            nama_pasien = input(f"\033[1mMasukkan nama pasien (lama:\033[0m {data2[1]}): ")
            tanggal_lahir = input(f"\033[1mMasukkan tanggal lahir (lama:\033[0m {data2[2]}): ")
            alamat = input(f"\033[1mMasukkan alamat (lama:\033[0m {data2[3]}): ")
            no_telepon = input(f"\033[1mMasukkan no telepon (lama:\033[0m {data2[4]}): ")

            update_query = "UPDATE pasien SET nama_pasien = %s, tanggal_lahir = %s, alamat = %s, no_telepon = %s WHERE id_pasien = %s"
            cur.execute(update_query, (nama_pasien, tanggal_lahir, alamat, no_telepon, id_pasien))
            conn.commit()
            print("\033[1mData pasien berhasil diupdate.\033[0m")
        else:
            print("\033[1mData pasien tidak ditemukan.\033[0m")
    except Exception as e:
        print(f"\033[1mError while updating data:\033[1m {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def hapus_data_pasien():
    os.system('clear')
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
        
        id_pasien = input('\033[1mMasukkan id pasien yang ingin dihapus:\033[1m ')

        # Cek apakah pasien dengan ID tersebut ada
        check_query = "SELECT * FROM pasien WHERE id_pasien = %s"
        cur.execute(check_query, (id_pasien,))
        patient = cur.fetchone()

        if patient:
            delete_query = "DELETE FROM pasien WHERE id_pasien = %s"
            cur.execute(delete_query, (id_pasien,))
            conn.commit()
            print(f"\033[1mData pasien dengan id {id_pasien} telah dihapus.\033[1m")
        else:
            print(f"Pasien dengan id {id_pasien} tidak ditemukan.")
    except Exception as e:
        print(f"\033[1mError while deleting data:\033[1m {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def tambah_data_obat():
    os.system('clear')
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

        total_input = int(input("\033[1mMau menambahkan berapa data?\033[1m "))
        for i in range(total_input):
            id_obat = input("\033[1mMasukkan ID obat:\033[1m ")
            nama_obat = input("\033[1mMasukkan nama obat:\033[1m ")
            harga = float(input("\033[1mMasukkan harga:\033[1m "))
            jenis_obat_id_jenisobat = int(input("\033[1mMasukkan ID jenis obat:\033[1m "))

            query = "INSERT INTO obat (id_obat, nama_obat, harga, jenis_obat_id_jenisobat) VALUES (%s, %s, %s, %s)"
            cur.execute(query, (id_obat, nama_obat, harga, jenis_obat_id_jenisobat))
        
        conn.commit()
        print("\033[1mData obat berhasil ditambahkan.\033[1m")
    except Exception as e:
        print(f"Error while inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def read_data_obat():
    os.system('clear')
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
        print(f"\033[1mError while reading data:\033[1m {e}")
    finally:
        cur.close()
        conn.close()

def update_data_obat():
    os.system('clear')
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

        id_obat = input('\033[1mMasukkan ID obat yang ingin di-update:\033[1m ')
        show_query = "SELECT * FROM obat WHERE id_obat = %s"
        cur.execute(show_query, (id_obat,))
        data2 = cur.fetchone()

        if data2:
            table_single = PrettyTable()
            table_single.field_names = ["ID Obat", "Nama Obat", "Harga", "Jenis Obat ID"]
            table_single.add_row(data2)
            print(table_single)

            nama_obat = input(f"\033[1mMasukkan nama obat (lama:\033[1m {data2[1]}): ")
            harga = float(input(f"\033[1mMasukkan harga (lama:\033[1m {data2[2]}): "))
            jenis_obat_id_jenisobat = int(input(f"\033[1mMasukkan ID jenis obat (lama:\033[1m {data2[3]}): "))

            update_query = "UPDATE obat SET nama_obat = %s, harga = %s, jenis_obat_id_jenisobat = %s WHERE id_obat = %s"
            cur.execute(update_query, (nama_obat, harga, jenis_obat_id_jenisobat, id_obat))
            conn.commit()
            print("\033[1mData obat berhasil diupdate.\033[1m")
        else:
            print("\033[1mData obat tidak ditemukan.\033[1m")
    except Exception as e:
        print(f"\033[1mError while updating data:\033[1m {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def hapus_data_obat():
    os.system('clear')
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
        
        id_obat = input('\033[1mMasukkan id obat yang ingin dihapus:\033[1m ')
        delete_query = "DELETE FROM obat WHERE id_obat = %s"
        cur.execute(delete_query, (id_obat,))
        conn.commit()
        print(f"\033[1mData obat dengan id {id_obat} telah dihapus.\033[1m")
    except Exception as e:
        print(f"\033[1mError while deleting data:\033[1m {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def main():
    os.system('clear')
    print("\033[1;36m+========================================================+")
    print("|                   SELAMAT DATANG DI                    |")
    print("|                 KLINIK MITRA KELUARGA                  |")
    print("+========================================================+\033[0m")
    print("\033[1m|   [1]   Login Admin                                    |")
    print("|   [2]   Registrasi Pasien                              |")
    print("|   [3]   Login Pasien                                   |")
    print("|   [4]   Exit                                           |\033[0m")
    print("\033[1;36m+========================================================+\033[0m")
    while True:
        choice = input("\033[1mPilih Opsi: \033[0m")
        
        if choice == "1":
            if admin_login():
                choose_option_admin()
        elif choice == "2":
            patient_register()
            main()  # Setelah registrasi pasien, langsung keluar dari program
        elif choice == "3":
            if patient_login():
                main()  # Setelah login pasien, langsung keluar dari program
        elif choice == "4":
            print("\033[1;33mTerima kasih! Sampai jumpa lagi.\033[0m")
            break  # Hentikan eksekusi program setelah mencetak pesan terima kasih
        else:
            print("\033[91mOpsi tidak valid. Silakan coba lagi.\033[0m")

if __name__ == "__main__":
    main()
