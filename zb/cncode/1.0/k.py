keyk = {
    "输出": "print",
    "循环": "while",
    "导入": "import",
    "输入": "input",
    "如果": "if",
    "且": "and",
    "否则": "else",
    "非": "not",
    "或": "or",
    "遍历": "for",
    "真": "True",
    "假": "False",
    "定义": "def",
    "返回": "return",
    "在": "in",
}

code = """
    
"""
def run():
    global code
    for key in keyk:
        code = code.replace(key,keyk[key])
    exec(code)