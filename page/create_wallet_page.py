"""创建钱包页页面模型"""

from common.common import Common

class CreateWalletPage(Common):
    # locator
    # 返回按钮
    go_back_button = ("xpath","//button[@mode='icon']")
    # 钱包名称input
    wallet_name_input = ("xpath","//input[@placeholder='输入1~12个字符']")
    # 钱包密码input
    wallet_pwd_input = ("xpath","//input[@placeholder='密码至少8个字符']")
    # 确认密码input
    wallet_confirm_pwd_input = ("xpath","//input[@placeholder='确认密码']")
    # 密码提示input
    wallet_pwd_hint_input = ("xpath","//input[@placeholder='输入密码提示信息']")
    # 选择助记词语言button
    Choose_mnemonic_language_button = ("xpath","//button/div[contains((text()),'English')]")
    # 选择助记词数量button
    Choose_mnemonic_number_button = ("xpath","//button/div[contains((text()),'12 个字')]")

    # acton
    def click_go_back(self):
        """点击返回按钮"""
        self.click(self.go_back_button)

    def input_wallet_name(self,wallet_name:str):
        """输入钱包名称"""
        self.input(self.wallet_name_input,wallet_name)
