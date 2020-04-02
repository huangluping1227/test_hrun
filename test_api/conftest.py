#_*_coding:utf-8_*_
# 作者     ：Administrator
# 创建时间 ：2020/4/114:58
# 文件     ：conftest.py

import os
import pytest
# 添加命令行参数
def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost",
        action="store",
        default="http://49.235.92.12:9000",
        help="test case project host address"
    )


@pytest.fixture(scope="session", autouse=True)
def host(request):
    '''获取命令行参数'''
    # 获取命令行参数给到环境变量
    os.environ["host"] = request.config.getoption("--cmdhost")
    print("当前用例运行测试环境:%s"%os.environ["host"])
