from datetime import datetime

VERSION = "2.0.0"
GIT_URL = "https://github.com/yang0/plugin4"
NAME = "示例任务4"
DESCRIPTION = "这是一个示例任务4，用于演示插件结构"

# 添加参数描述常量
PARAM_DESCRIPTIONS = {
    "test_param": {       
        "label": "测试参数",
        "description": "这是一个测试参数"
    },
}

def do_task(config={}):
    print(f"执行plugin4: {datetime.now()}")
    print(f"config['test_param']: {config['test_param']}")
