# Git Contribution Simulator

Git Contribution Simulator là một ứng dụng Python tự động hóa việc tạo commit trong Git repository. Công cụ này được thiết kế để giúp bạn làm đẹp bảng thống kê **contributions** trên GitHub bằng cách tạo các commit ngẫu nhiên trong khoảng thời gian tùy chỉnh.

## 🚀 Chức năng chính
- **Tự động commit** vào Git repository trong khoảng thời gian được chỉ định.
- Hỗ trợ tùy chọn:
  - Không commit vào cuối tuần.
  - Giới hạn số lượng commit tối đa mỗi ngày.
  - Tỷ lệ ngày có commit (%).
- **Tự động đẩy** commit lên remote repository.
- Tùy chỉnh tên và email người dùng cho Git.

## 🖥️ Yêu cầu hệ thống
- Python 3.6 trở lên
- Git được cài đặt trên hệ thống

## ⚙️ Cách sử dụng

### 1️⃣ Clone hoặc tải về dự án
```bash
git clone https://github.com/your-username/git-contribution-simulator.git
cd git-contribution-simulator
```
### 2️⃣ Cài đặt các thư viện cần thiết
Ứng dụng không yêu cầu thư viện ngoài, chỉ sử dụng các thư viện chuẩn của Python.

### 3️⃣ Tham số dòng lệnh
| Tham số              | Ý nghĩa                                                    | Giá trị mặc định      |
|----------------------|------------------------------------------------------------|------------------------|
| `-nw`, `--no_weekends`| Không tạo commit vào cuối tuần.                            | `False`                |
| `-mc`, `--max_commits`| Số lượng commit tối đa mỗi ngày. Giá trị từ 1 đến 20.     | `10`                   |
| `-fr`, `--frequency`  | Tỷ lệ ngày có commit (theo %).                             | `80`                   |
| `-r`, `--repository`  | URL repository từ xa (SSH hoặc HTTPS).                     | `None` (local repo)    |
| `-un`, `--user_name`  | Tên người dùng Git (override cấu hình toàn cục).           | `None`                 |
| `-ue`, `--user_email` | Email người dùng Git (override cấu hình toàn cục).         | `None`                 |
| `-db`, `--days_before`| Số ngày trước ngày hiện tại để bắt đầu commit.            | `365`                  |
| `-da`, `--days_after` | Số ngày sau ngày hiện tại để tiếp tục commit.             | `0`                    |

### 4️⃣ Ví dụ sử dụng
```bash
python3 simulate_contributions.py -r https://github.com/your-username/your-repository.git -un "Your Name" -ue "your-email@example.com" -mc 10 -fr 80 -db 365 -da 30
```
### 5️⃣ Lưu ý
- Nếu không chỉ định `-r`, công cụ sẽ tạo commit trên repository cục bộ.
- Nếu không chỉ định `-un` và `-ue`, công cụ sẽ sử dụng cấu hình Git toàn cục của bạn.

## 🎉 Chúc bạn thành công!

