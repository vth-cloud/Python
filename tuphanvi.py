import numpy as np
from scipy import stats

def calculate_quantiles(data):
    # Tính trung vị (Q2), Q1 và Q3
    Q2 = np.median(data)  # Trung vị (Q2)
    Q1 = np.percentile(data, 25)  # Tứ phân vị thứ nhất (Q1)
    Q3 = np.percentile(data, 75)  # Tứ phân vị thứ ba (Q3)
    return Q1, Q2, Q3

def main():
    print("Chọn loại bảng số liệu:")
    print("1. Bảng số liệu không có tần số")
    print("2. Bảng số liệu có tần số")
    
    choice = int(input("Nhập lựa chọn của bạn (1 hoặc 2): "))
    
    if choice == 1:
        # Bảng số liệu không có tần số
        data = list(map(float, input("Nhập danh sách số liệu (cách nhau bởi dấu phẩy): ").split(',')))
        data.sort()  # Sắp xếp số liệu để tính các tứ phân vị
        Q1, Q2, Q3 = calculate_quantiles(data)
        print(f"Q1 (Tứ phân vị thứ nhất): {Q1}")
        print(f"Q2 (Trung vị): {Q2}")
        print(f"Q3 (Tứ phân vị thứ ba): {Q3}")
    
    elif choice == 2:
        # Bảng số liệu có tần số
        values = list(map(float, input("Nhập danh sách các giá trị (cách nhau bởi dấu phẩy): ").split(',')))
        frequencies = list(map(int, input("Nhập tần số tương ứng cho các giá trị (cách nhau bởi dấu phẩy): ").split(',')))
        
        # Lặp qua từng giá trị và tần số để tạo danh sách dữ liệu đầy đủ
        data = []
        for value, frequency in zip(values, frequencies):
            data.extend([value] * frequency)
        
        data.sort()  # Sắp xếp số liệu để tính các tứ phân vị
        Q1, Q2, Q3 = calculate_quantiles(data)
        print(f"Q1 (Tứ phân vị thứ nhất): {Q1}")
        print(f"Q2 (Trung vị): {Q2}")
        print(f"Q3 (Tứ phân vị thứ ba): {Q3}")
    
    else:
        print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
