# SHU每日一报/每日两报 快捷指令 自动填报

本快捷指令(Shortcuts)可在iOS, iPadOS, watchOS上实现自动登录并打卡，可配合新版本中“自动化”实现自动填报

更新时间：20210417

 - **每日一报：**
    
     - 新版本可能存在密码泄露给第三方网站风险，具体见下"**20210417更新**"说明

    **新在校版**：[https://www.icloud.com/shortcuts/0fe049349965464ba7a01a4b3b790c68](https://www.icloud.com/shortcuts/0fe049349965464ba7a01a4b3b790c68)

    **新离校版：**[https://www.icloud.com/shortcuts/7541ec626eda43a2a273e58e063ddc24](https://www.icloud.com/shortcuts/7541ec626eda43a2a273e58e063ddc24)

    **0414在校版：**[https://www.icloud.com/shortcuts/e9f32fee8e154da2b7e1d91016f30c77](https://www.icloud.com/shortcuts/e9f32fee8e154da2b7e1d91016f30c77)

    **0414离校版：**[https://www.icloud.com/shortcuts/949066444fc84b59bdd31a103bf151aa](https://www.icloud.com/shortcuts/949066444fc84b59bdd31a103bf151aa)

    
 - 新版本导入后可能需要重新设置自动化
 - 每日两报已从本页面移除，如确有需要请查看以往commit


## **20210417更新**

由于统一认证采用了新的表单提交参数（将密码加密），0414版脚本若未对密码进行加密会提示“登录失败”

由于iOS快捷指令较难实现RSA加密，目前只能采用
1. 在快捷指令中保存加密后密码的方法（推荐）
或
2. 将密码提交给第三方网站进行加密处理

在快捷指令中保存加密后密码具体操作如下

### **方法1**
1. 在电脑浏览器中打开[https://selfreport.shu.edu.cn/](https://selfreport.shu.edu.cn/)(或其它需要登录的页面)(若已登录请退出)
2. 在统一认证网页中输入用户名，密码
3. 按F12进入`开发者模式`
4. 切换到`Network`选项卡
5. 点击网页上的登录按钮
6. 在登陆成功后将下面的列表框的滚动条拉到最顶端，单击第一项
7. 在右侧的窗口中滚动到最下端，右键单击`password`项，选择`Copy Value`
8. 将复制得到的加密字符串发送到iOS设备上
9. 重新导入0414版快捷方式或修改快捷指令保存的未加密密码
10. 将原先的明文密码替换为刚才得到的加密字符串即可

### **方法2**
本方法向第三方网站提交密码，获取加密后的密码以便自动提交，但该网站不会取得您的任何个人或账户信息与密码关联

由于会向该网站提交您的明文密码，请谨慎使用，若介意请使用方法1

更新版的快捷指令将会直接调用该网站的API（自动化执行如下步骤）

1. 打开[https://www.bejson.com/enc/rsa/](https://www.bejson.com/enc/rsa/)
2. 点击`根据公钥加密文本`选项卡
3. 在公钥文本框输入以下文本
```
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDl/aCgRl9f/4ON9MewoVnV58OLOU2ALBi2FKc5yIsfSpivKxe7A6FitJjHva3WpM7gvVOinMehp6if2UNIkbaN+plWf5IwqEVxsNZpeixc4GsbY9dXEk3WtRjwGSyDLySzEESH/kpJVoxO7ijRYqU+2oSRwTBNePOk1H+LRQokgQIDAQAB
-----END PUBLIC KEY-----
```
4. 在要加密的字符串文本框中输入你的密码
5. 在`执行`左边的下拉框中选择`RSA1`
6. 点击`执行`
7. 复制加密字符串
8. 之后的步骤同方法1步骤8以后

## **用法**

1. 在`App Store`中下载[快捷指令](https://apps.apple.com/cn/app/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/id1462947752)(在较新的iOS/iPadOS中是自带的)

2. 在Safari中打开对应版本的链接并选择“获取捷径”

    如提示`此快捷指令无法打开，因为您的"快捷指令"安全性设置不允许不收信任的快捷指令`，请前往`设置>快捷指令`打开`允许不受信任的快捷指令`

    你可能还需要运行任意一个快捷指令（自带或任意新建）才能打开以上开关

3. 跳转到`快捷指令`应用后滑至弹出确认页的底部，单击`添加不受信任的快捷指令`

4. 按提示输入相关信息

    这些信息将会本地保存在您设备上，仅用于自动登录并填报

5. 点击运行即可自动填报

    你可能需要在第一次运行时点选同意该快捷指令访问互联网（向特定网站发送数据）、显示通知

### 与`自动化`整合

1. 在`快捷指令`应用中点击底部的`自动化`选项卡

2. 点击右上角`+`创建个人自动化

3. 选择`特定时间`

4. 选择一个时间，如`7:00`；选择重复：`每天`(也可按情况选择`每周`的工作日/周末)；点击`下一步`

5. 点击`添加操作`，在搜索框中搜索`运行快捷指令`并选择

6. 将参数选择为刚刚添加的`每日X报（在校/离校）`快捷指令；点击`下一步`

7. 取消`运行前询问`选项（推荐，实现完全自动填报）；点击`完成`

## 说明

 - 本快捷指令可自定义所在省市县与地址

 - 在填报时默认绿码、无不适、无隔离、未接触中高风险地区，如有特殊情况建议手动填报或自行更改参数

 - 本快捷指令仅可填报当前时间段的日报，无法补报之前的日期，如有需要请自行更改参数

 - 有关添加与使用快捷指令的更多帮助，请参阅[快捷指令使用手册](https://support.apple.com/zh-cn/guide/shortcuts/welcome/ios)

## TODO
与Scriptable整合以便本地实现加密/更多功能

## 支持一下
欢迎点Star，提功能意见或[扫码捐助](https://ishs.gq/jz.html)

## 免责申明

本项目仅做学术交流使用。

