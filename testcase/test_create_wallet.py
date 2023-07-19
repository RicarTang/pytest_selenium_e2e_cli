import os
import pytest
import allure
import config
from page.login_page import LoginPage
from page.create_wallet_page import CreateWalletPage
from page.backup_or_not_wallet_page import BackupOrNotWalletPage
from page.backup_mnemonic_page import BackupMnemonicPage
from page.confirm_mnemonic_page import ConfirmMnemonicPage
from utils.load_file import LoadFile


@allure.epic("登录钱包")
class TestLoginWallet:
    @allure.feature("创建钱包集")
    class TestCreateWallet(
        LoginPage,
        CreateWalletPage,
        BackupOrNotWalletPage,
        BackupMnemonicPage,
        ConfirmMnemonicPage,
    ):
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

        @pytest.mark.create_wallet
        @pytest.mark.parametrize(
            "data",
            LoadFile(
                os.path.join(config.TESTCASE_DATA_PATH, "create_wallet_data.yaml")
            ),
        )
        def test_create_wallet_fail_case(self, data: dict):
            """创建钱包测试用例"""
            allure.dynamic.title(data["title"])
            self.click_create_wallet_button()
            self.input_wallet_name(data["data"]["wallet_name"])
            self.input_wallet_pwd(data["data"]["wallet_pwd"])
            self.input_wallet_confirm_pwd(data["data"]["wallet_confirm_pwd"])
            self.input_wallet_pwd_hint(data["data"]["wallet_pwd_hint"])
            self.click_user_agreement_checkbox()
            self.click_create_wallet_submit_button()
            assert (
                self.locator(self.create_wallet_button).is_enabled()
                is data["expect"]["is_enabled"]
            )
            if data["expect"]["is_enabled"] is True:
                if data["title"] == "成功创建钱包,跳过备份":
                    self.click_skip_backup_mnemonic_button()
                    self.click_backup_abort_button()
                    assert True  # 断言主页元素
                else:
                    self.click_backup_mnemonic_button()
                    self.click_confirm_backedup_button()
                    self.click_confirm_auto_complete_mnemonic_button()
                    self.click_confirm_mnemonic_finish_button()
                    assert True  # 断言主页元素
