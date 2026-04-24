import pyodbc

server = 'PCB1201'
database = 'bank_system'

connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

conn = pyodbc.connect(connection_string)

cursor = conn.cursor()
def chuc_nang_xem():
    sql = "SELECT * FROM customer";
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            email = row[2]
            balance = row[3]
            print(id , name , email , balance)        
    except:
            print ("Lỗi không thể xem!!!" )        
def chuc_nang_them():
    sql = "INSERT into customer(name , email , balance) values (? , ? , ?)"
    print("\nThêm các trường thông tin sau: ")
    print("\n")
    name_add = input("Tên: ")
    email_add = input("Email: ")
    balance_add = input("Số dư: ")
    values = (name_add , email_add , balance_add)
    try: 
        cursor.execute(sql , values)
        conn.commit()
        print(cursor.rowcount , "Đã thêm")
    except:
        conn.rollback()
        print("Lỗi không thể thêm!!!")
def chuc_nang_sua():
    sql = input("Nhập querry (UPDATE customer SET name, .. = name2,... WHERE name, ... = name2,..): ")
    try: 
        cursor.execute(sql)
        conn.commit()
        print(cursor.rowcount , "Đã sửa")
    except:
        conn.rollback()
        print("Lỗi không thể sửa!!! ")
def chuc_nang_xoa():
    id_delete = int(input("Xóa nhân viên số: "))
    sql = "DELETE FROM customer WHERE customer_id = '%d'" % (id_delete)
    try: 
        cursor.execute(sql)
        conn.commit()
        print(cursor.rowcount , "Đã xóa")
    except:
        conn.rollback()
        print("Lỗi không thể xóa!!! ")

def hien_thi_menu():
    while True:
        print("\n--- HỆ THỐNG QUẢN LÝ ---")
        print("1. Xem danh sách")
        print("2. Thêm mới")
        print("3. Sửa thông tin")
        print("4. Xóa dữ liệu")
        print("5. Thoát")
        
        lua_chon = input("Vui lòng nhập lựa chọn (1-5): ")
        
        if lua_chon == '1':
            print("\n[Đang chạy chức năng XEM...]")
            chuc_nang_xem()
        
        elif lua_chon == '2':
            print("\n[Đang chạy chức năng THÊM...]")
            chuc_nang_them()
        
        elif lua_chon == '3':
            print("\n[Đang chạy chức năng SỬA...]")
            chuc_nang_sua()
            
        elif lua_chon == '4':
            print("\n[Đang chạy chức năng XÓA...]")
            chuc_nang_xoa()
            
        elif lua_chon == '5':
            print("\n[Đã thoát chương trình]")
            cursor.close()
            conn.close()
            break
            
        else:
            print("\n[Lựa chọn không hợp lệ, vui lòng nhập lại!]")

if __name__ == "__main__":
    hien_thi_menu()


