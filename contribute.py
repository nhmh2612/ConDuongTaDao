#!/usr/bin/env python
import argparse
import os
from datetime import datetime
from datetime import timedelta
from random import randint
from subprocess import Popen
import sys


def main(def_args=sys.argv[1:]):
    """
    Hàm chính xử lý luồng thực thi:
    - Nhận tham số từ dòng lệnh.
    - Tạo repository và thực hiện commit dựa trên các thông số đầu vào.
    """
    # Phân tích tham số dòng lệnh
    args = arguments(def_args)
    curr_date = datetime.now()  # Ngày giờ hiện tại
    directory = 'repository-' + curr_date.strftime('%Y-%m-%d-%H-%M-%S')  # Tên thư mục mới dựa trên timestamp
    
    # Nếu có repository từ xa, tạo thư mục dựa trên tên repository
    repository = args.repository
    user_name = args.user_name
    user_email = args.user_email
    if repository is not None:
        start = repository.rfind('/') + 1
        end = repository.rfind('.')
        directory = repository[start:end]
    
    no_weekends = args.no_weekends  # Tùy chọn không commit vào cuối tuần
    frequency = args.frequency      # Tần suất commit (% ngày)
    days_before = args.days_before  # Số ngày trước hiện tại để commit
    if days_before < 0:
        sys.exit('days_before must not be negative')  # Kiểm tra giá trị âm
    days_after = args.days_after  # Số ngày sau hiện tại để commit
    if days_after < 0:
        sys.exit('days_after must not be negative')  # Kiểm tra giá trị âm
    
    # Tạo thư mục repository và chuyển vào đó
    os.mkdir(directory)
    os.chdir(directory)
    run(['git', 'init', '-b', 'main'])  # Khởi tạo Git repository

    # Cấu hình tên và email nếu được cung cấp
    if user_name is not None:
        run(['git', 'config', 'user.name', user_name])
    if user_email is not None:
        run(['git', 'config', 'user.email', user_email])

    # Tính toán ngày bắt đầu
    start_date = curr_date.replace(hour=20, minute=0) - timedelta(days_before)
    for day in (start_date + timedelta(n) for n in range(days_before + days_after)):
        # Nếu không có tùy chọn --no_weekends hoặc không phải cuối tuần
        if (not no_weekends or day.weekday() < 5) and randint(0, 100) < frequency:
            for commit_time in (day + timedelta(minutes=m) for m in range(contributions_per_day(args))):
                contribute(commit_time)  # Tạo commit tại thời điểm cụ thể

    # Nếu có repository từ xa, đẩy thay đổi lên đó
    if repository is not None:
        run(['git', 'remote', 'add', 'origin', repository])
        run(['git', 'branch', '-M', 'main'])
        run(['git', 'push', '-u', 'origin', 'main'])

    print('\nRepository generation ' +
          '\x1b[6;30;42mcompleted successfully\x1b[0m!')  # Thông báo thành công


def contribute(date):
    """
    Tạo commit tại thời điểm cụ thể.
    - Ghi nội dung vào file `README.md`.
    - Thực hiện `git add` và `git commit`.
    """
    with open(os.path.join(os.getcwd(), 'README.md'), 'a') as file:
        file.write(message(date) + '\n\n')  # Ghi thông điệp commit vào file README.md
    run(['git', 'add', '.'])  # Thêm tất cả thay đổi
    run(['git', 'commit', '-m', '"%s"' % message(date), '--date', date.strftime('"%Y-%m-%d %H:%M:%S"')])  # Commit với thời gian tùy chỉnh


def run(commands):
    """
    Chạy các lệnh shell thông qua subprocess.
    """
    Popen(commands).wait()  # Chờ lệnh hoàn thành


def message(date):
    """
    Sinh thông điệp commit dựa trên ngày tháng.
    """
    return date.strftime('Contribution: %Y-%m-%d %H:%M')  # Trả về chuỗi như "Contribution: 2024-11-26 20:15"


def contributions_per_day(args):
    """
    Xác định số commit sẽ thực hiện trong một ngày (ngẫu nhiên từ 1 đến `max_commits`).
    """
    max_c = args.max_commits
    if max_c > 20:  # Giới hạn số commit tối đa là 20
        max_c = 20
    if max_c < 1:  # Số commit tối thiểu là 1
        max_c = 1
    return randint(1, max_c)  # Trả về số commit ngẫu nhiên


def arguments(argsval):
    """
    Xử lý tham số dòng lệnh.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-nw', '--no_weekends',
                        required=False, action='store_true', default=False,
                        help="""do not commit on weekends""")
    parser.add_argument('-mc', '--max_commits', type=int, default=10,
                        required=False, help="""Defines the maximum amount of
                        commits a day the script can make. Accepts a number
                        from 1 to 20. If N is specified the script commits
                        from 1 to N times a day. The exact number of commits
                        is defined randomly for each day. The default value
                        is 10.""")
    parser.add_argument('-fr', '--frequency', type=int, default=80,
                        required=False, help="""Percentage of days when the
                        script performs commits. If N is specified, the script
                        will commit N%% of days in a year. The default value
                        is 80.""")
    parser.add_argument('-r', '--repository', type=str, required=False,
                        help="""A link on an empty non-initialized remote git
                        repository. If specified, the script pushes the changes
                        to the repository. The link is accepted in SSH or HTTPS
                        format. For example: git@github.com:user/repo.git or
                        https://github.com/user/repo.git""")
    parser.add_argument('-un', '--user_name', type=str, required=False,
                        help="""Overrides user.name git config.
                        If not specified, the global config is used.""")
    parser.add_argument('-ue', '--user_email', type=str, required=False,
                        help="""Overrides user.email git config.
                        If not specified, the global config is used.""")
    parser.add_argument('-db', '--days_before', type=int, default=365,
                        required=False, help="""Specifies the number of days
                        before the current date when the script will start
                        adding commits. For example: if it is set to 30 the
                        first commit date will be the current date minus 30
                        days.""")
    parser.add_argument('-da', '--days_after', type=int, default=0,
                        required=False, help="""Specifies the number of days
                        after the current date until which the script will be
                        adding commits. For example: if it is set to 30 the
                        last commit will be on a future date which is the
                        current date plus 30 days.""")
    return parser.parse_args(argsval)  # Trả về các tham số đã phân tích


if __name__ == "__main__":
    main()  # Chạy script
