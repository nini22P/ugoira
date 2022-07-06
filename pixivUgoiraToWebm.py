import json
import os
import shutil
import tempfile
import sys
from time import sleep
import zipfile

ugoiraFile = sys.argv[1]
(ugoiraFilePath, tempUgoiraFileName) = os.path.split(ugoiraFile)
(ugoiraFileName, extension) = os.path.splitext(tempUgoiraFileName)

try:
    int(sys.argv[2])
except:
    print('Mode Nomal')
else:
    print('Mode 0')

print(ugoiraFile)

# 解压 zip 到临时文件夹
tempPath = tempfile.mkdtemp()
extractPath = '%s\\extract' % tempPath
outputPath = '%s\\output' % tempPath
os.mkdir(extractPath)
os.mkdir(outputPath)
zfile = zipfile.ZipFile(ugoiraFile)
zfile.extractall(extractPath)

print('Extract')

# 读取 json 文件
with open('%s\\animation.json' % (extractPath), 'r') as animationFile:
    animationData = json.load(animationFile)

# 生成 webm 片段
for n in range(0, len(animationData)):

    try:
        int(sys.argv[2])
    except:
        # 正常模式
        os.system('ffmpeg -loglevel error -r %s -loop 1 -t %s -f image2 -i %s\\%s -y %s\\output%s.webm' %
                  (1000/animationData[n].get('delay'), animationData[n].get('delay')/1000, extractPath, animationData[n].get('file'), outputPath, n))
    else:
        # 合并后播放最后一段会跳跃时调用
        os.system('ffmpeg -loglevel error -r %s -loop 1 -t %s -f image2 -i %s\\%s -y %s\\output%s.webm' %
                  (1000/animationData[n-1].get('delay'), animationData[n].get('delay')/1000, extractPath, animationData[n].get('file'), outputPath, n))

    # 保存 webm 片段列表
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
