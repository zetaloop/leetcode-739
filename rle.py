def rle(s) -> str:
    """适用于Python字符串语法的行程编码"""
    encoded = "'"
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        if count > 10:
            encoded+=f"'+'{s[i]}'*{count}+'"
        else:
            encoded+=s[i]*count
        i += 1
    if encoded[-1]=="+":
        encoded=encoded[:-1]
    encoded+="'"
    return encoded


def xrle(lst: str):
    """Advanced RLE"""
    def nrle(lst,limit=10):
        result = []
        i = 0
        while i < len(lst):
            max_cover = 0
            chosen_seq = None
            chosen_count = 0
            for length in range(1, 11):
                if i + length > len(lst):
                    break
                repeat_seq = lst[i:i+length]
                count = 1
                while i + (count + 1) * length <= len(lst) and lst[i:i+length] == lst[i+count*length:i+(count+1)*length]:
                    count += 1
                cover = length * count
                if count > chosen_count or (count == chosen_count and cover > max_cover):
                    max_cover = cover
                    chosen_seq = repeat_seq
                    chosen_count = count
            if chosen_seq and chosen_count > 1:
                if chosen_count < limit:
                    for _ in range(chosen_count):
                        if len(chosen_seq)==1:
                            result.append((chosen_seq[0], 1))
                        else:
                            result.append((chosen_seq, 1))
                else:
                    result.append((chosen_seq, chosen_count))
                # result.append((chosen_seq, chosen_count))
                i += max_cover
            else:
                result.append((lst[i], 1))
                i += 1
        return result
    result = nrle(nrle(lst,10),1)
    # print(f'\n{result}\n')
    string = "'"
    for i in result: # e.g. [([('A', 5), ('C', 1)], 2), (('B', 15), 1), (('CB', 4), 1), ([('X', 16), ('B', 1)], 2), (('X', 16), 1)]
        if i[1]==1:
            if type(i[0])==tuple:
                if i[0][1]==1:
                    string += i[0][0]
                else:
                    string += f"'+'{i[0][0]}'*{i[0][1]}+'"
            else:
                assert len(i[0])>1
                istring = "'"
                for j in i[0]:
                    if j[1]==1:
                        istring += j[0]
                    else:
                        istring += f"'+'{j[0]}'*{j[1]}+'"
                istring += "'"
                string += f"'+{istring}+'"
        else:
            if len(i[0])==1:
                string += f"'+'{i[0][0][0]}'*{i[0][0][1]*i[1]}+'"
            else:
                istring = "'"
                for j in i[0]:
                    if j[1]==1:
                        istring += j[0]
                    else:
                        istring += f"'+'{j[0]}'*{j[1]}+'"
                istring += "'"
                string += f"'+({istring})*{i[1]}+'"
    string += "'"
    string = string.replace("+''", "").replace("''+", "")
    return string
