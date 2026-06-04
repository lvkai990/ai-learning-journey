import requests

class WeatherFetcher:
    def __init__(self, city):
        self.city = city
        self.base_url = "https://wttr.in"

    def get_weather(self):
        """返回简洁天气字符串"""
        try:
            url = f"{self.base_url}/{self.city}?format=3"
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # 如果状态码不是 2xx，抛出异常
            return response.text.strip()
        except requests.exceptions.RequestException as e:
            return f"天气查询失败: {e}"

    def get_detailed_weather(self):
        """返回字典，包含温度、描述、湿度"""
        try:
            url = f"{self.base_url}/{self.city}?format=j1"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            current = data['current_condition'][0]
            return {
                'temperature': current['temp_C'] + '°C',
                'description': current['weatherDesc'][0]['value'],
                'humidity': current['humidity'] + '%'
            }
        except requests.exceptions.RequestException as e:
            return {"error": f"天气查询失败: {e}"}
        except (KeyError, IndexError) as e:
            return {"error": f"数据解析失败: {e}"}

# 测试
weatherFetcher = WeatherFetcher("Jinan")
print(weatherFetcher.get_weather())
print(weatherFetcher.get_detailed_weather())