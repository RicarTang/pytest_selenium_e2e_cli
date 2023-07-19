import os
import allure
import pytest
from page.login_page import LoginPage
from page.restore_wallet_page import RestoreWalletPage
from utils.load_file import LoadFile
import config


@allure.epic("登录钱包")
@allure.feature("恢复钱包集")
class TestRestoreWallet(LoginPage, RestoreWalletPage):
    """创建钱包测试用例集"""

    def setup_class(self):
        """类前置"""
        pass

    def deardown_class(self):
        """类后置"""
        self.driver.quit()

    def setup_method(self):
        """方法前置"""
        self.get("/")

    @pytest.mark.restore_wallet
    @pytest.mark.parametrize("data",LoadFile(os.path.join(config.TESTCASE_DATA_PATH, "restore_wallet_data.yaml")))
    def test_restore_wallet_case(self,data):
        """恢复钱包测试用例"""
        allure.dynamic.title(data["title"])
        self.click_restore_wallet_button()
        self.input_wallet_mnemonic(data["data"]["wallet_mnemonic"])
        self.input_wallet_name(data["data"]["wallet_name"])
        self.input_wallet_pwd(data["data"]["wallet_pwd"])
        self.input_wallet_confirm_pwd(data["data"]["wallet_confirm_pwd"])
        self.input_wallet_pwd_hint(data["data"]["wallet_pwd_hint"])
        self.click_user_agreement_checkbox()
        assert (
            self.locator(self.restore_wallet_submit).is_enabled()
            is data["expect"]["is_enabled"]
        )
        self.click_restore_wallet_submit_button()

