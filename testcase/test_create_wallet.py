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


@allure.story("创建钱包测试")
class TestCreateWallet(
    LoginPage,
    CreateWalletPage,
    BackupOrNotWalletPage,
    BackupMnemonicPage,
    ConfirmMnemonicPage,
):
    """创建钱包测试用例集"""

    @pytest.mark.create_wallet
    @pytest.mark.parametrize("data",LoadFile(os.path.join(config.TESTCASE_DATA_PATH,"create_wallet_data.yaml")))
    def test_create_wallet(self,data):
        self.driver.get("http://127.0.0.1:6939/")
        self.click_create_wallet_button()
        self.input_wallet_name(data["data"]["wallet_name"])
        self.input_wallet_pwd(data["data"]["wallet_pwd"])
        self.input_wallet_confirm_pwd(data["data"]["wallet_confirm_pwd"])
        self.input_wallet_pwd_hint(data["data"]["wallet_pwd_hint"])
        self.click_user_agreement_checkbox()
        self.click_create_wallet_submit_button()
        assert self.locator(self.create_wallet_button).is_enabled() is data["except"]["is_enabled"]
        