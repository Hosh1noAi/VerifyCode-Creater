from random import choice
from string import ascii_uppercase, ascii_lowercase

local_digits = '0123456789'

def generate_check_code(length: int = 6) -> str:
    '''生成包含数字的验证码，长度为4到8位，默认为6。'''
    
    # 检查输入是否有效
    if not isinstance(length, int):
        raise TypeError("Length必须是整数")
    
    # 定义默认字符集合：大写字母、小写字母、数字
    chars = list(ascii_uppercase + ascii_lowercase + local_digits)
    
    # 初始化结果字符串和包含数字的标志
    code = []
    has_digit = False
    
    # 生成指定长度的字符
    for _ in range(length):
        char = choice(chars)
        code.append(char)
        if char in local_digits:
            has_digit = True
    
    # 确保当长度超过4位时，至少包含一个数字（如果没有已经包含的话）
    if length > 4 and not has_digit:
        # 需要重新生成直到满足条件为止
        current_length = len(code)
        while current_length < length:
            char = choice(chars)
            code.append(char)
            if char in local_digits:
                has_digit = True
                break
            # 防止无限循环，设置一个最长重试次数（例如5次）
            current_length += 1
            if current_length > length + 5:
                raise ValueError("无法生成满足条件的验证码")
    
    return ''.join(code)

if __name__ == "__main__":
    # 用户输入长度
    print("请输入检查码的长度（4到8位，留空则默认为6）：")
    input_len = input().strip()
    
    # 确定长度
    if not input_len:
        length = 6
    else:
        try:
            length = int(input_len)
            if length < 4 or length > 8:
                print("长度必须在4到8之间，请重新输入：")
                exit()
        except ValueError:
            print("请使用数字输入")
            exit()
    
    # 生成并打印验证码
    code = generate_check_code(length)
    print(f"生成的验证码为：{code}")