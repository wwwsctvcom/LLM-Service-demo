# Introduction
项目提供了可以通过requests方式去获取LLM输出的方式，另外提供了通过网页页面进行问答，web端支持多轮对话问答；

# Web Show
启动web的demo通过如下方式：
```
streamlit run streamlit_web.py
```

# API Service
启动API获取服务，启动service：
```
python api_service.py
```
提供一个client获取LLM输出的demo：
```
python api_service_usage.py
```
