# SHU 每日一报/进出校 快捷指令 自动填报申请

本快捷指令(Shortcuts)可在 iOS, iPadOS, watchOS, macOS 上实现自动登录并打卡，可配合新版本中“自动化”实现自动填报

更新时间：2023.02.01

**每日一报：**

本代码仓库中现已上传快捷指令文件版，可直接导入

也可以使用以下的链接

- **最新版**链接(最后更新：2022.10.08):

  <https://www.icloud.com/shortcuts/c0d5f3ff954d4b9ea2d34bdcb7f5533b>

- **每日进出**快捷指令链接(最后更新：2023.02.01，**NEW！**):
  
  <https://www.icloud.com/shortcuts/6e93436757594f90ac9979ea7dbcbd13>

- **获取进出申请id**快捷指令链接(可用于撤销申请，**NEW！**):
  
  <https://www.icloud.com/shortcuts/423b847ae4684f238090baa52219e887>

- **撤销申请**快捷指令链接(**NEW！**):
  
  <https://www.icloud.com/shortcuts/24f3d2e98dab4fba901361d9ca838272>

- **获取加密密码**快捷指令链接

  <https://www.icloud.com/shortcuts/94442f1b832a4a47a0fc79577da306e4>

- **上传并获取图片id**快捷指令链接（请勿直接使用，参照文档）

  <https://www.icloud.com/shortcuts/135509fb218a434492b3a30b058fc541>

- **检查脚本更新**快捷指令链接

  <https://www.icloud.com/shortcuts/5f3acac7140143998eaaa022d7616934>

- 在导入每日一报快捷指令时必须使用**加密后**的密码

- 新版本导入后可能需要重新设置自动化

- 目前最新版只支持**在校**和**离校（在上海）**，若要提交不在上海状态请自行修改相关参数

## 20230201更新

- 添加一键进校、出校脚本
- 添加获取进出校申请id脚本与撤销申请脚本
- 由于现在无需提交行程码，原提交图片自动化部分可以自行删除

## 20221008 更新

- 通过在快捷指令间传递图片id的方式实现上传图片并提交日报
- 修复行程码图片提交参数异常的问题
- **请参照最新的[使用说明文档](Tutorial.md)修改现有自动化**（20230201更新：现无需更改）
- 现可以使用`检查脚本更新`快捷指令检查快捷指令更新

## **20220831 热更新版说明**

由于健康之路系统更新的参数往往仅是添加一些诸如“是否认定为密接”等问题，无特殊情况下大家都会选择“否”

而目前各脚本每次参数更新都需要发布新版本，用户需要重新下载、配置，十分麻烦

本次新更新的“热更新版”支持直接从在线网站（本代码仓库托管在Github Pages上的网站）获取填报参数

除非需要用户主动填写（如暑假时更新的“所在街道”字段），其余参数仅需在线配置更新即可，用户无需再下载新版快捷指令

同时此版本聚合在校、离校版，仅需在导入时填写版本字段即可

## 版本字段

| 字段    | 说明                                                         |
| ------- | :----------------------------------------------------------- |
| zx      | **在校**版参数，进学校，住校                                 |
| lx      | **离校**版参数，不进学校，在上海，是家庭地址                 |
| cx      | 常态化期间自动**出**校申请，详见[这里](Tutorial_CX.md)（20230201更新：已上传修改后版本，无需手动更改） |
| jx      | 常态化期间自动**进**校申请                                   |
| up      | 上传图片相关参数，地址等信息为冗余，默认即可                 |
| chexiao | 用于撤销已通过的进校、出校申请                               |

如有个性化需求，可以提issue、PR申请其它字段

## 提交页面

出校申请与进校申请的提交页面是不同的，请参照提示修改，如下表：

| 类型     | URL                                                       |
| -------- | :-------------------------------------------------------- |
| 出校申请 | https://selfreport.shu.edu.cn/XiaoYJC202207/XueSLXSQ.aspx |
| 进校申请 | https://selfreport.shu.edu.cn/XiaoYJC202207/XueSJXSQ.aspx |

## 加密密码说明

由于统一认证采用了新的表单提交参数（将密码加密），若未对密码进行加密会提示“登录失败”

由于 iOS 快捷指令较难实现 RSA 加密，目前只能采用在快捷指令中保存加密后密码的方法

若要获取加密后的密码，可以有如下方式

### **方法 1**

1. 导入`获取SHU加密密码`快捷指令
2. 按提示输入明文密码
3. 程序自动请求相关 API 获得加密后的密码
4. 你可以进行复制等操作并将其导入每日一报快捷指令中

本方法向第三方网站提交密码，获取加密后的密码以便自动提交，但该网站不会取得您的任何个人或账户信息与密码关联

由于会向该网站提交您的明文密码，请谨慎使用，若介意请使用方法 2

### **方法 2**

1. 在电脑浏览器中打开<https://selfreport.shu.edu.cn/>(或其它需要登录的页面)(若已登录请退出)
2. 在统一认证网页中输入用户名，密码
3. 按 F12 进入`开发者模式`
4. 切换到`Network`选项卡
5. 点击网页上的登录按钮
6. 在登陆成功后将下面的列表框的滚动条拉到最顶端，单击第一项
7. 在右侧的窗口中滚动到最下端，右键单击`password`项，选择`Copy Value`
8. 将复制得到的加密字符串发送到 iOS 设备上
9. 重新导入 0414 版快捷方式或修改快捷指令保存的未加密密码
10. 将原先的明文密码替换为刚才得到的加密字符串即可

### **方法 3**

手动调用相关 API 获得密码

`获取SHU加密密码`快捷指令中将会直接调用该网站的 API（自动化执行如下步骤）

1. 打开<https://www.bejson.com/enc/rsa/>
2. 点击`根据公钥加密文本`选项卡
3. 在公钥文本框输入以下文本

```text
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDl/aCgRl9f/4ON9MewoVnV58OLOU2ALBi2FKc5yIsfSpivKxe7A6FitJjHva3WpM7gvVOinMehp6if2UNIkbaN+plWf5IwqEVxsNZpeixc4GsbY9dXEk3WtRjwGSyDLySzEESH/kpJVoxO7ijRYqU+2oSRwTBNePOk1H+LRQokgQIDAQAB
-----END PUBLIC KEY-----
```

4. 在要加密的字符串文本框中输入你的密码
5. 在`执行`左边的下拉框中选择`RSA1`
6. 点击`执行`
7. 复制加密字符串
8. 之后的步骤同方法 1 步骤 8 以后

## **用法**

参照[使用说明文档](Tutorial.md)

## 说明

- 本快捷指令可自定义所在省市县与地址

- 在填报时默认绿码、无不适、无隔离、无密接、未去过低中高风险地区、未赴外省市，如有特殊情况建议手动填报或自行更改参数，如实填写

- 本快捷指令仅可填报当前时间段的日报，无法补报之前的日期，如有需要请自行更改参数

- 有关添加与使用快捷指令的更多帮助，请参阅[快捷指令使用手册](https://support.apple.com/zh-cn/guide/shortcuts/welcome/ios)

## TODO

~~与 Scriptable 整合以便本地实现加密/更多功能~~

## 支持一下

欢迎点 Star，提功能意见或[扫码捐助](https://ishs.gq/jz.html)

## 免责申明

本项目仅做学术交流使用。请遵守相关进出校规定与防疫要求。
