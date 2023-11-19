# README.md

- [English](README.md)
- [简体中文](README.zh_CN.md)

## 功能

比较两个语言文件的差异，使用第一个为模板

如果第二个语言文件存在翻译则使用翻译

如果不存在翻译则使用原文，且打上一个标签#WTT(Wait To Translate)标记

最后会将这些新的条目组成一个新的文件放入文件夹中，随后就可以开始翻译
![before](img/before.png)
![result](img/result.png)

## 如何使用

1. 确保你的电脑安装了Python
2. 打开终端进入脚本所在目录并执行 `python TransTool.py`
![Terminal](img/typeInCode.png)
3. 输入语言文件所在的目录地址
![GetPath](img/getPath.png)
![CopyIntoTerminal](img/copyIntoTermianl.png)
4. 输入源语言文件与目标语言文件
![InPutLangName](img/InPutLangName.png)
5. 新的语言文件将会在你指定的地址生成，使用查找即可快速翻译未翻译的条目
![Done](img/done.png)
![NewFileWithWTTTag](img/newFileWithWTTTag.png)
