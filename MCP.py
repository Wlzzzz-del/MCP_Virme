from openai import OpenAI
from MCP import NLU_MCP_Full,NLU_MCP_Batches
from openai_config import API_KEY,BASE_URL
import time
import json

class Base_MCP:
    def __init__(self,path):
        self.messages = []
        # System messsage构造
        self.messages.append(self.construct_system_message(self.construct_template_prompt()))
        self.read_markdown_file(path)
        self.agent = OpenAI(API_KEY,BASE_URL)
        self.model_type = "gpt-3.5-turbo"  # 可以根据需要更改模型类型
        self.out_put_path = "./output.gml"

    def convert(self):
        pass

    def read_markdown_file(self, file_path):
        """
        读取本地Markdown文件并打印内容
        :param file_path: Markdown文件的路径
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()
                for line in content:
                    # User message构造
                    if("-" in str(line)):
                        self.messages.append(self.construct_user_message(self.construct_asking_prompt(line.strip())))

        except FileNotFoundError:
            print(f"文件未找到: {file_path}")

        except Exception as e:
            print(f"读取文件时发生错误: {e}")

    def construct_asking_prompt(self,content):
        prompt = "Help me change this data based template to generate graph(only include node with id, label, x, y; edge with source, target, color, bw) , remember don't add extra content(any explained text) into the text in .json type, don't output any words, you just give me the new data:\n"
        return prompt+content

    def construct_template_prompt(self,):
        prompt = "Remember this data template: graph [\n name \"Brain\" \n node [\n id 0 \n label \"0\"\n x \"9.421921\"\n y \"48.559341\"\n edge [\nsource 0\ntarget 6\ncolor \"red\"\nbw 100.]]"
        return prompt

    def construct_system_message(self,content):
        return {'role': 'system', 'content': content}

    def construct_user_message(self,content):
        return {'role': 'user', 'content': content}

    def show_messages(self, nums = 5):
        cnt = 0
        for message in self.messages:
            if cnt<nums:
                print(f"{message['role']}: {message['content']}")
                cnt += 1
            else:
                break
    
    def convert_to_gml(self, json_content, output_file):
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

class NLU_MCP_Batches(Base_MCP):
    # NLU_MCP_Batches类用于分批处理NLU数据
    def __init__(self, path):
        super().__init__(path)

    def read_markdown_file(self, file_path):
        """
        读取本地Markdown文件并打印内容
        :param file_path: Markdown文件的路径
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()
                for line in content:
                    # User message构造
                    if("-" in str(line)):
                        self.messages.append(self.construct_user_message(self.construct_asking_prompt(line.strip())))
        except FileNotFoundError:
            print(f"文件未找到: {file_path}")

        except Exception as e:
            print(f"读取文件时发生错误: {e}")

class NLU_MCP_Full(Base_MCP):
    # NLU_MCP_Batches类用于一次性处理NLU数据
    def __init__(self, path):
        super().__init__(path)

    def convert(self):
        json_type = ""
        for i in range(len(self.messages)):
            print(self.messages[i])
            completion = self.agent.chat.completions.create(
                model=self.model_type,
                messages=[self.messages[i]]
            )
            print(completion.choices[0].message.content)
            json_type = str(completion.choices[0].message.content)
            time.sleep(10)
        self.convert_to_gml(json_type, self.out_put_path)  # 将转换后的JSON数据保存为GML文件

    def read_markdown_file(self, file_path):
        """
        读取本地Markdown文件并打印内容
        :param file_path: Markdown文件的路径
        """
        text = ""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()
                for line in content:
                    # User message构造
                    if("-" in str(line)):
                        text += line.strip()
        except FileNotFoundError:
            print(f"文件未找到: {file_path}")

        except Exception as e:
            print(f"读取文件时发生错误: {e}")

        self.messages.append(self.construct_user_message(self.construct_asking_prompt(text)))

if __name__ == "__main__":
    # 替换为您的Markdown文件路径
    markdown_file_path = "./nlu_half.md"
    M = NLU_MCP_Full(markdown_file_path)
    M.show_messages()
