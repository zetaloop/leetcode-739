# import array
# import zlib

# def bytes_to_chinese_base(bytes_data):
#     # 定义基础Unicode点
#     base_unicode = 0x4E00
#     # 将bytes转为二进制字符串
#     binary_str = ''.join(format(byte, '08b') for byte in bytes_data)
#     # 计算需要填充的位数
#     padding = (14 - (len(binary_str) % 14)) % 14
#     binary_str += '0' * padding
#     # 每14位分割
#     chunks = [binary_str[i:i+14] for i in range(0, len(binary_str), 14)]
#     # 编码到中文字符
#     chinese_str = ''.join(chr(base_unicode + int(chunk, 2)) for chunk in chunks)
#     # 添加等号作为填充标志
#     padding_signs = '=' * (padding // 2)  # 每个等号代表两个字节
#     return chinese_str + padding_signs

# def chinese_base_to_bytes(chinese_str):
#     base_unicode = 0x4E00
#     # 移除填充标志
#     padding_count = chinese_str.count('=')
#     chinese_str = chinese_str.rstrip('=')
#     binary_str = ''.join(format(ord(ch) - base_unicode, '014b') for ch in chinese_str)
#     # 根据等号数量移除填充的0
#     if padding_count > 0:
#         binary_str = binary_str[:-padding_count*2*7]
#     # 每8位分割还原为bytes
#     bytes_data = bytes(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))
#     return bytes_data

# 示例压缩和编码
# int_array = [1, 2, 3, 10000, 123456789] * 10  # 增加数据量以展示填充效果
# bytes_array = array.array('I', int_array).tobytes()
# compressed_data = zlib.compress(bytes_array)
# encoded_data = bytes_to_chinese_base(compressed_data)
# print(encoded_data)


# def fulldecode(chinese): # 这是完整从头实现从中文一路解码到数组的函数
#     base_unicode = 0x4E00
#     padding_count = chinese.count('=')
#     chinese = chinese.rstrip('=')
#     binary_str = ''.join(format(ord(ch) - base_unicode, '014b') for ch in chinese)
#     if padding_count > 0:
#         binary_str = binary_str[:-padding_count*2*7]
#     bytes_data = bytes(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))
#     decompressed_data = zlib.decompress(bytes_data)
#     restored_array = array.array('I')
#     restored_array.frombytes(decompressed_data)
#     return restored_array.tolist()

import array
import bz2

def bytes_to_chinese_base(bytes_data):
    # 定义基础Unicode点
    base_unicode = 0x4E00
    # 将bytes转为二进制字符串
    binary_str = ''.join(format(byte, '08b') for byte in bytes_data)
    # 计算需要填充的位数
    padding = (14 - (len(binary_str) % 14)) % 14
    binary_str += '0' * padding
    # 每14位分割
    chunks = [binary_str[i:i+14] for i in range(0, len(binary_str), 14)]
    # 编码到中文字符
    chinese_str = ''.join(chr(base_unicode + int(chunk, 2)) for chunk in chunks)
    # 添加等号作为填充标志
    padding_signs = '=' * (padding // 2)  # 每个等号代表两个字节
    return chinese_str + padding_signs

def enco(list_data):
    bytes_array = array.array('I', list_data).tobytes()
    compressed_data = bz2.compress(bytes_array)
    return bytes_to_chinese_base(compressed_data)


def onel(C): return (lambda x:[x.frombytes(bz2.decompress((lambda x:bytes(int(x[i:i+8],2)for i in range(0,len(x),8)))(''.join(format(ord(ch)-0x4E00,'014b')for ch in C)[:(-C.count('=')*2*7)if'='in C else None]))),x.tolist()][1])(array.array('I'))
