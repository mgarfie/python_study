import json
data = [{"name": "毛玉琳", "age": "19"}, {"name":"高梦莹", "age": "20"}]
json_str = json.dumps(data)
print(f"他的类型为{type(json_str)},他的内容为:{json_str}")
# 此时看到运行结果中中文不会正常显示，这是因为编码的问题，所以要加一句ensure_ascii=False,意思是不用 Ascll 转换
json_str = json.dumps(data, ensure_ascii=False)
print(f"他的类型为{type(json_str)}, 他的内容为:{json_str}")
# 相反操作，将json转换为list
data = json. loads(json_str)
print(f"他的类型为{type(data)}, 他的内容为:{data}")


