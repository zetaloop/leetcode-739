from temperature import tmp
from compress import compress
from rle import rle, xrle


def once(x):
    '''输入新发现的测试用例列表，输出压缩完毕的解决方案代码和压缩详情'''
    xx=tmp(x)
    result=compress(xx).decode()
    com=rle(result)
    xcom=xrle(result)
    lens = len(result),len(com),len(xcom)
    if lens[2]==min(lens):
        # assert xcom.startswith("'LRx4!F+o`-Q")
        xcom = "'" + xcom[12:]
        if min(lens)>9000:
            xcom = f"({xcom[:9000]}'\n'{xcom[9000:]})"
        print(f"{hash(tuple(x))}:{xcom},\nMethod:xrle Len:{len(xcom)}/{len(com)}/{len(result)} Validate:{eval(xcom)==result}")
    elif lens[1]==min(lens):
        # assert com.startswith("'LRx4!F+o`-Q")
        com = "'" + com[12:]
        if min(lens)>9000:
            com = f"({com[:9000]}'\n'{com[9000]})"
        print(f"{hash(tuple(x))}:{com},\nMethod:rle Len:{len(xcom)}/{len(com)}/{len(result)} Validate:{eval(com)==result}")
    else:
        # result = f"'{result}'"
        # assert result.startswith("'LRx4!F+o`-Q")
        result = "'" + result[12:]
        if min(lens)>9000:
            result = f"({result[:9000]}'\n'{result[9000:]})"
        print(f"{hash(tuple(x))}:{result},\nMethod:plain Len:{len(xcom)}/{len(com)}/{len(result)}")
