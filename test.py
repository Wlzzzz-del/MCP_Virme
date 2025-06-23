from openai import OpenAI
from MCP import NLU_MCP_Full,NLU_MCP_Batches
import time
import json
# 文心client
# 在 https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Wm9cvy6rl 切换RPM\TPM更大的模型进行测试

def convert_to_gml(json_content, output_file):
    """
    将JSON格式的图数据转换为GML格式并保存到文件
    :param json_content: JSON格式的图数据
    :param output_file: 输出的GML文件路径
    """
    try:
        graph_data = json.loads(json_content)
        with open(output_file, 'w', encoding='utf-8') as gml_file:
            gml_file.write("graph [\n")
            
            # 写入节点
            for node in graph_data["nodes"]:
                gml_file.write(f'  node [\n')
                gml_file.write(f'    id "{node["id"]}"\n')
                gml_file.write(f'    label "{node["label"]}"\n')
                gml_file.write(f'    x {node["x"]}\n')
                gml_file.write(f'    y {node["y"]}\n')
                gml_file.write(f'  ]\n')
            
            # 写入边
            for edge in graph_data["edges"]:
                gml_file.write(f'  edge [\n')
                gml_file.write(f'    source "{edge["source"]}"\n')
                gml_file.write(f'    target "{edge["target"]}"\n')
                gml_file.write(f'    color "{edge["color"]}"\n')
                gml_file.write(f'    bw "{edge["bw"]}"\n')
                gml_file.write(f'  ]\n')
            
            gml_file.write("]\n")
        print(f"GML文件已成功保存到: {output_file}")
    except Exception as e:
        print(f"转换为GML格式时发生错误: {e}")

# Need a helpful api
client = OpenAI(

    api_key = "sk-1xKrdVF2iepfjaoS9e168GKJldRS7nRrUp0R1FZQx5EtDhxJ",
    base_url="https://poloai.top/v1"
)

markdown_file_path = "./nlu_half.md"
M = NLU_MCP_Full(markdown_file_path)

json_type = ""
for i in range(len(M.messages)):
    print(M.messages[i])
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo", # qifan-70b效果最好
        messages=[M.messages[i]]
    )
    print(completion.choices[0].message.content)
    json_type = str(completion.choices[0].message.content)
    time.sleep(10)

convert_to_gml(json_type, "output.gml")