import json
import os
import shutil
import tempfile
import sys
from time import sleep
import zipfile

# 获取文件完整路径
ugoiraFile = sys.argv[1]
# 分离文件路径和完整文件名
(ugoiraFilePath, tempUgoiraFileName) = os.path.split(ugoiraFile)
# 分离文件名和扩展名
(ugoiraFileName, extension) = os.path.splitext(tempUgoiraFileName)

print(ugoiraFile)

# 判断模式
try:
    int(sys.argv[2])
except:
    print('Mode Nomal')
else:
    print('Mode 0')

# 解压 zip 到临时文件夹
print('Extract')

tempPath = tempfile.mkdtemp()
extractPath = '%s\\extract' % tempPath
outputPath = '%s\\output' % tempPath
os.mkdir(extractPath)
os.mkdir(outputPath)
zfile = zipfile.ZipFile(ugoiraFile)
zfile.extractall(extractPath)

# 读取 json 文件
with open('%s\\animation.json' % (extractPath), 'r') as animationFile:
    animationData = json.load(animationFile)

# 生成 webm 片段
for n in range(0, len(animationData)):
    # 在最后一帧判断是否特殊处理
    if(n == len(animationData)-1):
        try:
            int(sys.argv[2])
        except:
            os.system('ffmpeg -loglevel error -r %s -loop 1 -t %s -f image2 -i %s\\%s -y %s\\output%s.webm' %
                      (1000/animationData[n].get('delay'), animationData[n].get('delay')/1000, extractPath, animationData[n].get('file'), outputPath, n))
        else:
            os.system('ffmpeg -loglevel error -r %s -loop 1 -t %s -f image2 -i %s\\%s -y %s\\output%s.webm' %
                      (1000/animationData[n-1].get('delay'), animationData[n].get('delay')/1000, extractPath, animationData[n].get('file'), outputPath, n))
    else:
        os.system('ffmpeg -loglevel error -r %s -loop 1 -t %s -f image2 -i %s\\%s -y %s\\output%s.webm' %
                  (1000/animationData[n].get('delay'), animationData[n].get('delay')/1000, extractPath, animationData[n].get('file'), outputPath, n))
        # 保存 webm 片段列表到 outputList.txt
    with open('%s\\outputList.txt' % (outputPath), 'a') as output_list:
        output_list.write("file 'output%s.webm'" % (n))
        output_list.write('\n')

    print('Generate:', n+1, '/', len(animationData), end="\r")

# 连接 webm
print('\nConcat')

os.system('ffmpeg -loglevel error -f concat -i %s\\outputList.txt -c copy -y %s\\%s.webm' %
          (outputPath, ugoiraFilePath, ugoiraFileName))
# 移除临时文件夹
shutil.rmtree(tempPath)

print('Success')
