import allure


class UploadFile:
    """上传文件至allure报告"""
    def upload_png(self,img):
        """上传png图片"""
        with open(img,'rb') as i:
            file = i.read()
        allure.attach(file,'测试截图',allure.attachment_type.PNG)
