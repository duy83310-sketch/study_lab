print("\n[Đang chạy chức năng SỬA...]")
            sql = input("Nhập querry (UPDATE customer SET name, .. = name2,... WHERE name, ... = name2,..): ")
            try: 
                cursor.execute(sql)
                conn.commit()
                print(cursor.rowcount , "Đã sửa")
            except:
                conn.rollback()
                print("Lỗi không thể sửa!!! ")
            