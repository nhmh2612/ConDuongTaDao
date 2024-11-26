import unittest
import contribute
from subprocess import check_output  # Dùng để chạy lệnh Git đếm commit trong repository

class TestContribute(unittest.TestCase):
    # Kiểm tra hàm xử lý tham số dòng lệnh
    def test_arguments(self):
        # Gọi hàm arguments() với tham số giả lập `-nw` (không commit vào cuối tuần)
        args = contribute.arguments(['-nw'])
        
        # Kiểm tra cờ `no_weekends` được bật
        self.assertTrue(args.no_weekends)
        
        # Kiểm tra giá trị mặc định của `max_commits` là 10
        self.assertEqual(args.max_commits, 10)
        
        # Kiểm tra số commit mỗi ngày nằm trong khoảng từ 1 đến 20
        self.assertTrue(1 <= contribute.contributions_per_day(args) <= 20)

    # Kiểm tra hàm `contributions_per_day` đảm bảo số commit nằm trong khoảng hợp lệ
    def test_contributions_per_day(self):
        # Tạo tham số đầu vào với cờ `-nw`
        args = contribute.arguments(['-nw'])
        
        # Xác nhận rằng số commit trả về nằm trong khoảng 1 đến 20
        self.assertTrue(1 <= contribute.contributions_per_day(args) <= 20)

    # Kiểm tra chức năng chính của script `contribute`
    def test_commits(self):
        # Đặt giới hạn commit tối đa là 11 cho mục đích kiểm tra
        contribute.NUM = 11
        
        # Gọi hàm main() với các tham số giả lập
        contribute.main([
            '-nw',  # Không commit vào cuối tuần
            '--user_name=sampleusername',  # Cung cấp tên người dùng Git
            '--user_email=your-username@users.noreply.github.com',  # Email người dùng Git
            '-mc=12',  # Giới hạn commit mỗi ngày tối đa là 12
            '-fr=82',  # Tần suất commit là 82%
            '-db=10',  # Tạo commit từ 10 ngày trước
            '-da=15'   # Tạo commit đến 15 ngày sau
        ])
        
        # Chạy lệnh Git để đếm tổng số commit đã thực hiện
        total_commits = int(check_output(
            ['git', 'rev-list', '--count', 'HEAD']  # Lệnh Git: đếm số commit trong HEAD
        ).decode('utf-8'))  # Giải mã kết quả từ byte sang chuỗi
        
        # Kiểm tra số commit nằm trong khoảng hợp lệ (1 đến tối đa 20 * số ngày)
        self.assertTrue(1 <= total_commits <= 20 * (10 + 15))
