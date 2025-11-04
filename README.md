# Python学习项目 (python_test)

## 项目概述

这是一个Python学习和实践项目，包含了多个不同领域的Python应用示例，主要涵盖以下几个方面：

1. **机器学习/数据分析** - 鸢尾花数据集分析
2. **计算机视觉** - 人脸识别与面部特征处理
3. **网络爬虫** - 电视节目信息爬取

## 项目结构

```
python_test/
├── web/                          # Web相关代码
│   └── src/
│       ├── face_recognition/     # 人脸识别模块
│       ├── main_face/           # 面部特征处理
│       ├── main/                # 网络爬虫相关代码
│       └── request/             # HTTP请求示例
├── *.ipynb                      # Jupyter Notebook文件
├── iris.data                    # 鸢尾花数据集
└── README.md                    # 项目说明文档
```

## 主要功能模块

### 1. 鸢尾花数据分析 (莺尾花分析.ipynb)

**功能描述：**
- 这是一个经典的机器学习入门项目，使用著名的Iris（鸢尾花）数据集
- 包含数据可视化、统计分析和机器学习基础操作

**主要内容：**
- 数据加载与预处理
- 数据探索性分析（EDA）
  - 花萼长度/宽度的分布直方图
  - 花瓣长度/宽度的分布直方图
  - 花瓣散点图分析
- 数据可视化
  - 使用matplotlib绘制各种图表
  - 使用seaborn进行配对图分析
- 特征工程
  - 创建新特征（如花瓣面积）
  - 分类标签映射
- 统计建模
  - 使用statsmodels进行线性回归分析（OLS）

**技术栈：**
- pandas - 数据处理
- matplotlib - 数据可视化
- seaborn - 高级可视化
- numpy - 数值计算
- statsmodels - 统计建模
- requests - 数据下载

---

### 2. 人脸识别系统 (web/src/face_recognition/)

**功能描述：**
这是一个基于深度学习的实时人脸识别系统，可以从摄像头中识别人脸并与数据库中的人脸进行比对。

**核心文件：**

#### `face_reco_from_camera.py` - 实时人脸识别
- **功能：** 从摄像头实时捕获画面，识别人脸并与预存的人脸特征进行匹配
- **技术：**
  - 使用dlib库进行人脸检测
  - 使用预训练的ResNet模型提取128维人脸特征向量
  - 通过欧氏距离计算人脸相似度
  - 实时视频流处理
- **关键功能：**
  - 多人脸检测支持
  - 实时人脸特征提取
  - 人脸匹配（阈值：0.4）
  - 视频标注和显示

#### `get_face_from_camera.py` - 人脸采集
- 从摄像头采集人脸样本
- 保存人脸图像用于后续训练

#### `get_features_into_csv.py` - 特征提取
- 提取人脸的128维特征向量
- 将特征保存到CSV文件中
- 用于构建人脸特征数据库

#### `rgb2gray.py` - 图像预处理
- RGB图像转灰度图
- 图像预处理工具

**模型文件：**
- `dlib_face_recognition_resnet_model_v1.dat` - 人脸识别模型（22MB）
- `shape_predictor_68_face_landmarks.dat` - 68点面部特征点检测模型（95MB）
- `shape_predictor_5_face_landmarks.dat` - 5点面部特征点检测模型（9MB）

---

### 3. 面部特征处理 (web/src/main_face/)

**功能描述：**
面部美化和特征分析工具集

#### `face_beauty.py` - 数字化妆
- **功能：** 给照片中的人脸添加数字化妆效果
- **特效包括：**
  - 眉毛渲染
  - 口红效果
  - 眼影效果
  - 眼线效果
- **技术：** 使用face_recognition库和PIL进行图像处理

#### `face_to_match.py` - 人脸匹配
- 人脸相似度比对
- 人脸验证功能

#### `features.py` - 特征提取
- 提取面部关键点
- 面部特征分析

#### `find_all_face_show.py` - 多人脸检测
- 在图像中检测所有人脸
- 标注和显示人脸位置

#### `draw.py` - 绘图工具
- 面部特征点可视化
- 辅助绘图功能

---

### 4. 网络爬虫模块 (web/src/main/)

**功能描述：**
爬取电视节目相关信息的网络爬虫

#### `tvmao.py` - 电视猫网站爬虫
- **目标网站：** https://www.tvmao.com
- **功能：**
  - 爬取各省电视台信息
  - 获取电视节目列表
  - 将数据保存到Excel文件
- **技术栈：**
  - requests - HTTP请求
  - BeautifulSoup4 - HTML解析
  - xlwt - Excel文件写入
  - Tkinter - GUI界面（示例）

#### `tvopen.py` - 电视直播网站爬虫
- **目标网站：** http://www.tvyan.com
- **功能：**
  - 爬取电视台列表
  - 获取电视台介绍信息
  - 下载电视台图标
  - 保存到Excel文件
- **特点：**
  - 递归爬取多页内容
  - 自动去重
  - 数据持久化

#### `open_province_url.py` - 省级电视台URL采集
- 采集各省电视台的播放链接
- 数据整理和存储

#### 其他测试文件
- `test1.py`, `test2_opt.py`, `test3.py`, `test4.py` - 各种测试脚本
- `loss.py`, `power.py` - 工具函数

---

### 5. HTTP请求示例 (web/src/request/)

#### `request1.py` - 数据请求和处理
- **功能：**
  - 从UCI机器学习库下载Iris数据集
  - 使用pandas进行数据分析
  - 数据可视化（直方图）
- **示例代码：**
  - GitHub API调用
  - 数据统计分析
  - DataFrame操作
  - 数据筛选和查询

---

## 技术栈总结

### 数据科学与机器学习
- **pandas** - 数据处理和分析
- **numpy** - 数值计算
- **matplotlib** - 基础可视化
- **seaborn** - 高级统计可视化
- **statsmodels** - 统计建模

### 计算机视觉
- **dlib** - 人脸检测和识别
- **OpenCV (cv2)** - 图像处理和视频流
- **face_recognition** - 高级人脸识别API
- **PIL/Pillow** - 图像处理

### 网络爬虫
- **requests** - HTTP请求库
- **BeautifulSoup4** - HTML/XML解析
- **urllib3** - URL处理
- **xlwt** - Excel文件操作

### GUI
- **Tkinter** - Python标准GUI库

---

## 数据集

### Iris（鸢尾花）数据集 (iris.data)
- **来源：** UCI机器学习库
- **规模：** 150个样本
- **特征：** 4个数值特征（花萼长度、花萼宽度、花瓣长度、花瓣宽度）
- **类别：** 3个鸢尾花品种（Setosa、Versicolor、Virginica）
- **用途：** 经典的机器学习分类问题

---

## 项目特点

1. **多领域覆盖：** 涵盖数据分析、计算机视觉、网络爬虫等多个方向
2. **实用性强：** 包含实际可运行的应用示例
3. **学习价值高：** 适合Python初学者学习参考
4. **代码结构清晰：** 模块化组织，易于理解和扩展

---

## 使用说明

### 环境要求
```bash
# 主要依赖包
pip install pandas numpy matplotlib seaborn
pip install requests beautifulsoup4 xlwt
pip install opencv-python dlib face_recognition
pip install statsmodels jupyter
```

### 人脸识别系统使用
1. 运行 `get_face_from_camera.py` 采集人脸样本
2. 运行 `get_features_into_csv.py` 提取特征并保存
3. 运行 `face_reco_from_camera.py` 启动实时识别

### 数据分析
- 使用Jupyter Notebook打开 `莺尾花分析.ipynb`
- 按顺序执行单元格即可

### 网络爬虫
- 运行 `tvmao.py` 或 `tvopen.py`
- 结果会保存为Excel文件

---

## 注意事项

1. **路径配置：** 代码中包含硬编码的本地路径（如 `/Users/shucan/...`），使用前需要根据实际情况修改
2. **模型文件：** 人脸识别需要预先下载dlib模型文件
3. **Python版本：** 部分代码可能需要Python 2.x（如Tkinter导入），建议使用Python 3.x并适当修改
4. **网络爬虫：** 使用爬虫时请遵守robots.txt协议和网站使用条款

---

## 学习路径建议

1. **初学者：** 从Iris数据分析开始，学习数据处理和可视化
2. **进阶：** 尝试人脸识别系统，了解计算机视觉应用
3. **实战：** 运行网络爬虫，学习数据采集和处理

---

## 作者信息

- **作者：** ShuCan
- **用途：** Python学习与实践

---

## 总结

这是一个综合性的Python学习项目，通过三个主要应用方向（数据分析、计算机视觉、网络爬虫）展示了Python在不同领域的应用。项目代码实用性强，适合作为学习参考和实践练习。
