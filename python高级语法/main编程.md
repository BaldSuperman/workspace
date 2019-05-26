# Main编程
- 管理程序
    - Euroda使邮件普及
    - Netscape，outlook，forxmain后来居上
##邮件工作流程
  - MUA:邮件用户代理
  - MTA:邮件传输代理
  - MDA邮件投递代理
  - laoshi@qq.com
  - xuesheng@sina.com
  - 流程
    MUA ->MTA邮件已经在服务器上了
    qq MTA ->..........->sina MTA 邮件到达新浪邮箱
    sina MTA ->sina MDA.此时邮件在邮箱里
    sina MDA ->MUA，邮件下载到本地
  - 程序编写
    - 发送 MUA->MTA with SMTP：simpleMailTransferProtocal
    - 接受 MDA->MUA with POP3 and IMAP:PostOFFiceProtocal V3
  
  - 准备工作
    - 注册邮箱（以QQ邮箱为例）
    - 第三方邮箱需要特殊设置，以QQ邮箱为例
        - 进入设置中心
        - 取得授权码
  python for mail
    - SMTP协议负责发送邮件
        - 使用email模块构建邮件
        - 使用smtplib模块发送邮件
    - pop3协议接受邮件
    