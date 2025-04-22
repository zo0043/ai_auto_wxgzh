# CrewAI微信公众号全自动生成排版发布工具

![Python](https://img.shields.io/badge/Python-3.10+-blue)  ![PySimpleGUI](https://img.shields.io/badge/PySimpleGUI-4.60.5+-green) ![CrewAI](https://img.shields.io/badge/CrewAI-0.102.0+-red) ![Stars](https://img.shields.io/github/stars/iniwap/ai_auto_wxgzh?label=收藏)

基于 CrewAI 的微信公众号自动化工具，自动抓取知乎、微博等平台热点，生成高质量、排版酷炫的文章并发布到微信公众号。

![界面预览 / Interface Preview](image/preview.png)

## 🎯项目背景
为了学习CrewAI，特开发了这个小项目。最后才发现公众号（未认证）限制巨多，有认证微信公众号的可以更好的发挥这个项目的作用。👉[高大上文章排版预览](#模板发布效果预览)

**喜欢项目？点个 Star 支持一下吧！🌟**

## 💎基本功能介绍
- 自动获取各大平台热门话题
- 自动根据话题生成文章、排版（CrewAI多个角色共同完成）
- 自动发图文消息到公众号

### 🎁个性化功能

为了更好的满足各种需求情况，通过配置文件（`config.yaml`）来完成

- platforms：可以设定每个平台的随机选取的权重
- wechat: 支持配置多个微信公众号
- api：支持配置多个大模型平台，使用哪个修改`api_type`即可，只需改成你的api_key，其他不用变
    - model是列表，可以选用一个平台的多个模型中的一个，修改`model_index`即可
    - openrouter的api_key也设计了多个，可以用来切换多个号（每天有免费额度，用完切换账号即可，修改`key_index`）
- img_api：生成图片模型，主要是用来做公众号封面图的
    - picsum: 由于生成图片消耗太大，这里提供一种随机图片方式，修改成这个`api_type`即可
- use_template: 目前只有Claude 3.7有比较好的模板生成效果，由于无法直接使用（有API付费的可以，但消耗很高），这里特别设计是否使用内置模板（每天可以免费到Poe生成模板放到`knowledge/templates`文件夹下）
- need_auditor: 为了降低token消耗，提高发布成功率，可关闭“质量审核”agent/task（默认关闭）

## 🚀 快速开始
1. 克隆仓库：`git clone https://github.com/iniwap/ai_auto_wxgzh.git`
2. 安装依赖：
   - `pip install -r requirements.txt`
   - `pip install PySimpleGUI-4.60.5-py3-none-any.whl`
4. 配置 `config.yaml`（设置 微信公众号及大模型API KEY）
5. 运行：
    - 无UI界面：`python -m src.ai_auto_wxgzh.crew_main`
    - 有UI界面：`python .\main.py -d` (**还未完成**)

## 🔍问题定位
如果遇到没有发布成功或者没有生成final_article的情况，又找不到问题，请临时更换下CrewAI版本：
```shell
pip  uninstall crewai
pip  install crewai==0.102.0
```
**此版本会输出过程日志，仍看不出问题的，可将日志提交Issue（只需要最后进入`文章发布专家`任务的日志部分，如果没到这部分，说明已经中断出错了）**

恢复到最新版本：
```shell
pip  uninstall crewai
pip  install crewai
```
⚠️**免费的openrouter有可能服务不正常，无法正确运行（这种情况只能等用的人少的时候再试）；此外将config里的use_template改成false，可提高成功率。**
这应该跟其最近修改了付费策略有关系，免费的终究是没那么好用。

## 🔮模板发布效果预览
经过反复的微调，已经完成发布到微信公众号的模板效果如下：
- **template1**: https://mp.weixin.qq.com/s/9MoMFXgY7ieEMW0kqBqfvQ
- **template2**: https://mp.weixin.qq.com/s/0vCNvgbHfilSS77wKzM6Dg
- **template3**: https://mp.weixin.qq.com/s/ygroULs7dx5Q54FkR8P0uA
- **template4**: https://mp.weixin.qq.com/s/-SexfJ1yUcgNDtWay3eLnA
- **template5**: https://mp.weixin.qq.com/s/pDPkktE_5KnkQkJ1x2-y9Q
- **template6**: https://mp.weixin.qq.com/s/7F_Qdho-hzxeVV6NrsPmhQ
- **template7**: https://mp.weixin.qq.com/s/ug7NseZDziDMWBVwe3s1pw
- **template8**: https://mp.weixin.qq.com/s/uDjKVrWop4XNrM-csQ-IKw
- **template9**: https://mp.weixin.qq.com/s/EVhL67x8w35IuNnoxI1IEA
- **template10**: https://mp.weixin.qq.com/s/pDN5rgCgz0CbA8Q92CugYw

*有兴趣的可以继续微调（如边距等），上面的模板可以比较好的显示在微信公众号上了。执行代码时，自动随机选择模板，生成的文章会自动选取填充上面的模板发布文章。*

:smile: **调整这些模板花费了大量时间，麻烦关注下公众号** 👆

 ## 📢后续计划
- 优化模板，减少token消耗
- 优化处理，减少不必要的token消耗
- 增加功能，使输出效果更好
- 增加容错，提升成功率
- 增加界面，可视化操作
- 制作成Windows软件，不再依赖开发环境

## 📌其他说明
~~由于不熟悉微信公众号开发，哪位知道如何正确的使用“position: absolute;”，麻烦提一个issue 或者PR给我。
这个很必要，因为生成的模板都使用了，浏览器显示正常，但是发布到微信公众号，就变成了垂直排列，无法作为背景。整体效果差太多了。~~
### 经过分析，发现以下问题：
- **发布文章后，微信会自动移除position: absolute（position: relative好像不会移除） ，必须通过其他方式实现**
- 微信公众号支持animateMotion，不支持animate（经测试只支持透明度变化动画，也不全是模板1的动画没问题，这个需要继续测试）
- 调整好的模板，效果虽然不能完全和原来的相比，但是总体还不错（有背景装饰、有动画）
- 不支持button，会被自动移除
- 会自动移除 background: url
- `<linearGradient id="catGradient">`，此类动画，id会被自动移除，动画会失效
