order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]


def normalize_order(order_code, status):
    order_code = order_code.strip().upper()
    status = status.strip().upper()
    return f"{order_code} - {status}"


def show_orders():
    if len(order_list) == 0:
        print("Danh sách đơn hàng hiện đang trống.")
    else:
        print("Danh sách đơn hàng hiện tại:")
        for i in range(len(order_list)):
            print(f"{i + 1}. {order_list[i]}")


def add_order():
    order_code = input("Nhập mã đơn hàng: ")
    status = input("Nhập trạng thái đơn hàng: ")

    order = normalize_order(order_code, status)

    order_list.append(order)

    print("Thêm đơn hàng thành công.")


def edit_order():
    position = input("Nhập vị trí cần sửa: ")

    if not position.isdigit():
        print("Vị trí không hợp lệ!")
        return

    position = int(position)

    if position < 1 or position > len(order_list):
        print("Không tồn tại đơn hàng ở vị trí này!")
        return

    order_code = input("Nhập mã đơn hàng mới: ")
    status = input("Nhập trạng thái mới: ")

    order = normalize_order(order_code, status)

    order_list[position - 1] = order

    print("Cập nhật đơn hàng thành công.")


def delete_order():
    position = input("Nhập vị trí cần xóa: ")

    if not position.isdigit():
        print("Vị trí không hợp lệ!")
        return

    position = int(position)

    if position < 1 or position > len(order_list):
        print("Không tồn tại đơn hàng ở vị trí này!")
        return

    removed_order = order_list.pop(position - 1)

    print("Đã xóa đơn hàng:")
    print(removed_order)


def show_statistics():
    pending = 0
    delivering = 0
    completed = 0
    cancelled = 0

    for order in order_list:
        parts = order.split(" - ")

        if len(parts) != 2:
            continue

        status = parts[1]

        if status == "PENDING":
            pending += 1
        elif status == "DELIVERING":
            delivering += 1
        elif status == "COMPLETED":
            completed += 1
        elif status == "CANCELLED":
            cancelled += 1

    print("===== THỐNG KÊ ĐƠN HÀNG =====")
    print(f"PENDING: {pending}")
    print(f"DELIVERING: {delivering}")
    print(f"COMPLETED: {completed}")
    print(f"CANCELLED: {cancelled}")
    print(f"Tổng số đơn hàng: {len(order_list)}")


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        show_orders()

    elif choice == "2":
        while True:
            print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
            print("1. Thêm đơn hàng mới")
            print("2. Sửa đơn hàng theo vị trí")
            print("3. Xóa đơn hàng theo vị trí")
            print("4. Quay lại menu chính")

            update_choice = input("Chọn chức năng: ")

            if update_choice == "1":
                add_order()

            elif update_choice == "2":
                edit_order()

            elif update_choice == "3":
                delete_order()

            elif update_choice == "4":
                break

            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

    elif choice == "3":
        show_statistics()

    elif choice == "4":
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")