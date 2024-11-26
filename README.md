Git Contribution Simulator
Git Contribution Simulator là một ứng dụng Python tự động hóa việc tạo commit trong Git repository. Công cụ này được thiết kế để giúp bạn làm đẹp bảng thống kê contributions trên GitHub bằng cách tạo các commit ngẫu nhiên trong khoảng thời gian tùy chỉnh.

Chức năng chính
Tự động commit vào Git repository trong khoảng thời gian được chỉ định.
Hỗ trợ tùy chọn:
Không commit vào cuối tuần.
Giới hạn số lượng commit tối đa mỗi ngày.
Tỷ lệ ngày có commit (%).
Tự động đẩy commit lên remote repository.
Tùy chỉnh tên và email người dùng cho Git.
Yêu cầu hệ thống
Python 3.6 trở lên
Git được cài đặt trên hệ thống
Cách sử dụng
1. Clone hoặc tải về dự án
bash
Sao chép mã
git clone https://github.com/your-username/git-contribution-simulator.git
cd git-contribution-simulator
2. Cài đặt các thư viện cần thiết
Ứng dụng này không yêu cầu thư viện ngoài, chỉ sử dụng các thư viện chuẩn của Python.

3. Chạy ứng dụng
Sử dụng các tùy chọn bên dưới để chạy ứng dụng:

bash
Sao chép mã
python contribute.py [options]
Tham số dòng lệnh
Tham số	Ý nghĩa	Giá trị mặc định
-nw, --no_weekends	Không tạo commit vào cuối tuần.	False
-mc, --max_commits	Số lượng commit tối đa mỗi ngày. Giá trị từ 1 đến 20.	10
-fr, --frequency	Tỷ lệ ngày có commit (theo %).	80
-r, --repository	URL repository từ xa (SSH hoặc HTTPS).	None (local repo)
-un, --user_name	Tên người dùng Git (override cấu hình toàn cục).	None
-ue, --user_email	Email người dùng Git (override cấu hình toàn cục).	None
-db, --days_before	Số ngày trước ngày hiện tại để bắt đầu commit.	365
-da, --days_after	Số ngày sau ngày hiện tại để tiếp tục commit.	0
Ví dụ
1. Tạo commit vào ngày hôm qua và hôm nay, không đẩy lên repository từ xa
bash
Sao chép mã
python contribute.py -db 1 -da 1 -mc 5
2. Tạo commit trong 30 ngày trước, chỉ commit vào ngày thường (không cuối tuần)
bash
Sao chép mã
python contribute.py -db 30 -nw -mc 10
3. Tạo commit và đẩy lên repository từ xa
bash
Sao chép mã
python contribute.py -r https://github.com/your-username/your-repository.git -un "Your Name" -ue "your-email@example.com"
Hướng dẫn phát triển
Chạy các bài test:
bash
Sao chép mã
python -m unittest discover
Chỉnh sửa và đóng góp:
Fork repository này.
Tạo một branch mới cho các tính năng hoặc sửa lỗi.
Gửi pull request về repository chính.
Ghi chú
Ứng dụng này chỉ nhằm mục đích thử nghiệm hoặc làm đẹp bảng contributions. Không sử dụng nó để thao túng dữ liệu GitHub một cách không hợp lệ.

