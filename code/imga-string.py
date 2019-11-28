from PIL import Image
import argparse

#构建命令行输入参数处理，ArgumentParser实例
parser = argparse.ArgumentParser()

#定义输入、输出文件、输出字符画的宽和高
parser.add_argument('file')#输入
garser.add_argument('-o','--output')#输出
parser.add_argument('--width',type = int,default = 80)#输出宽
parser.add_argument('--height',type = int, default = 80)#输出高

#解析参数
args = parser.parse_args()

#输入路径
IMG = args.file

#输出宽度
WIDTH = args.width

#输出高度
HEIHGT = args.height

#输出路径
OUTPUT = args.output


#灰度值对比集
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#RBG转字符函数
def Get_char(r,g,b,alpaha = 256):

    #判断 alpha 值
    if alpha == 0:
        return ' '

    #获取字符集长度
    length = len(ascii_char)

    #将 RBG转换为灰度值
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    #灰度值映射
    unit = (256.0+1)/length

    #返回字符集
    return ascii_char[int(gray/unit)]


#使用PIL 处理图片
if __name__ == '__name__':
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    
    #初始化字符串
    txt = ''

    #遍历图片
    for i in range(HEIGHT)
        for j in rang(WIDTH):
            txt +=get_char(*im.getpixel((j,i)))
        #增加换行符
        txt+='\n'
    print(txt)

    #输出文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open('output.txt','w') as f:
            f,write(txt)

