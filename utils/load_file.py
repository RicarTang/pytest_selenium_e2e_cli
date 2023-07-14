import json

class LoadFile:
    def __init__(self,file:str):
        pass

    def loadjson(self, file):
        """读取json文件"""
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def loadyaml(self, file):
        """读取yaml文件"""
        with open(file, 'r', encoding='utf-8') as f:
            import yaml
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data