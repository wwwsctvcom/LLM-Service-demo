# Introduction
本项目提供了两种方式让用户使用LLM模型，第一种是通过requests方式去获取LLM的输出，另外一种是提供了一个网页页面，让用户可以进行交互和问答，同时web端也支持多轮的问答；

# Web Show
启动web的demo通过如下方式：
```
streamlit run streamlit_web.py
```

# API Service
启动API获取服务，启动service服务：
```
python api_service.py
```
打开service之后显示的内容：
```
INFO:     Started server process [21844]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     0.0.0.0:54881 - "POST /v1/completions HTTP/1.1" 200 OK
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [21844]
```
打开service服务之后，可以通过如下的使用demo去获取service方提供的服务：
```
python api_service_usage.py
```

# Demo
```xml
问：写一个斐波那契额的算法demo？
答："斐波那契数列（Fibonacci sequence）是一个非常著名的数学序列，其特点是除了第一个和第二个数以外，任何一个数都是前两个数的和。斐波那契数列通常以 F(0) = 0, F(1) = 1 开始，其后的每一项都是前两项的和。即：\n\nF(n) = F(n-1) + F(n-2)\n\n下面是几种编程语言中实现斐波那契数列的简单示例：\n\n### Python 示例\n```python\ndef fibonacci(n):\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)\n\n# 打印前10个斐波那契数\nfor i in range(10):\n    print(fibonacci(i))\n```\n\n### Java 示例\n```java\npublic class Fibonacci {\n    public static int fibonacci(int n) {\n        if (n <= 0) {\n            return 0;\n        } else if (n == 1) {\n            return 1;\n        } else {\n            return fibonacci(n - 1) + fibonacci(n - 2);\n        }\n    }\n\n    public static void main(String[] args) {\n        // 打印前10个斐波那契数\n        for (int i = 0; i < 10; i++) {\n            System.out.println(fibonacci(i));\n        }\n    }\n}\n```\n\n### JavaScript 示例\n```javascript\nfunction fibonacci(n) {\n    if (n <= 0) {\n        return 0;\n    } else if (n === 1) {\n        return 1;\n    } else {\n        return fibonacci(n - 1) + fibonacci(n - 2);\n    }\n}\n\n// 打印前10个斐波那契数\nfor (let i = 0; i < 10; i++) {\n    console.log(fibonacci(i));\n}\n```\n\n请注意，上述递归方法虽然简单直观，但效率并不高，特别是对于较大的`n`值，因为它会重复计算很多子问题。为了提高效率，可以使用动态规划或者缓存已计算的斐波那契数来避免重复计算。"

```
