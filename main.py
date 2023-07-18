import os
import pytest
import config






if __name__ == '__main__':
    pytest.main(["--alluredir",config.REPORT_DATA,"--clean-alluredir"])
    os.system(f"allure generate {config.REPORT_DATA} -o {config.ALLURE_REPORT}")
    # 开启web服务，打开报告
    os.system(f"allure open {config.ALLURE_REPORT} -h 127.0.0.1 -p 8000")