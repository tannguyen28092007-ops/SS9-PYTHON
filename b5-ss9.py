order_list = [
    "GE001 - PENDING",
    "GE002 - ASSIGNED",
    "GE003 - DELIVERING"
]

def normalize_order_code(order_code):
    return order_code.strip().upper()


def find_order_index(order_code):
    for i in range(len(order_list)):
        code, status = order_list[i].split(" - ")

        if code == order_code:
            return i

    return -1

def show_orders():
    if len(order_list) == 0:
        print("Danh sách đơn hàng hiện đang trống.")
        return

    print("Danh sách đơn hàng hiện tại:")

    for i in range(len(order_list)):
        print(f"{i + 1}. {order_list[i]}")

def assign_driver():
    order_code = input("Nhập mã đơn hàng cần gán tài xế: ")
    order_code = normalize_order_code(order_code)

    index = find_order_index(order_code)

    if index == -1:
        print("Không tìm thấy mã đơn hàng.")
        return

    code, status = order_list[index].split(" - ")

    if status == "PENDING":
        order_list[index] = f"{code} - ASSIGNED"
        print("Gán tài xế thành công.")
    else:
        print("Chỉ có thể gán tài xế cho đơn hàng đang chờ xử lý.")

def update_delivery_status():
    order_code = input("Nhập mã đơn hàng cần cập nhật: ")
    order_code = normalize_order_code(order_code)

    index = find_order_index(order_code)

    if index == -1:
        print("Không tìm thấy mã đơn hàng.")
        return

    code, status = order_list[index].split(" - ")

    if status == "PENDING":
        print("Đơn hàng chưa được gán tài xế, không thể chuyển sang trạng thái giao hàng.")

    elif status == "ASSIGNED":
        order_list[index] = f"{code} - DELIVERING"
        print("Đơn hàng đã chuyển sang trạng thái DELIVERING.")

    elif status == "DELIVERING":
        order_list[index] = f"{code} - COMPLETED"
        print("Đơn hàng đã chuyển sang trạng thái COMPLETED.")

    elif status == "COMPLETED":
        print("Đơn hàng đã hoàn tất, không thể cập nhật tiếp.")

    elif status == "CANCELLED":
        print("Đơn hàng đã bị hủy, không thể cập nhật.")


def cancel_order():
    order_code = input("Nhập mã đơn hàng cần hủy: ")
    order_code = normalize_order_code(order_code)

    index = find_order_index(order_code)

    if index == -1:
        print("Không tìm thấy mã đơn hàng.")
        return

    code, status = order_list[index].split(" - ")

    if status == "PENDING" or status == "ASSIGNED":
        order_list[index] = f"{code} - CANCELLED"
        print("Hủy đơn hàng thành công.")

    elif status == "DELIVERING":
        print("Đơn hàng đang được giao, không thể hủy.")

    elif status == "COMPLETED":
        print("Đơn hàng đã hoàn tất, không thể hủy.")

    elif status == "CANCELLED":
        print("Đơn hàng đã được hủy trước đó.")


while True:
    print("\n===== HỆ THỐNG ĐIỀU PHỐI GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Gán tài xế cho đơn hàng")
    print("3. Cập nhật trạng thái giao hàng")
    print("4. Hủy đơn hàng")
    print("5. Thoát chương trình")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        show_orders()

    elif choice == "2":
        assign_driver()

    elif choice == "3":
        update_delivery_status()

    elif choice == "4":
        cancel_order()

    elif choice == "5":
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ!")