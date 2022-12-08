#импортируем библотеку eel для связки консольного кода и веб-интерфейса
#импортируем библотеку pyowm для отображения погоды через api
import eel
import pyowm

owm = pyowm.OWM("e0c909f50be272b73ef0b3896f9f0cbc")

#создаем функцию для для возврата погоды указанного места
@eel.expose


def get_weather(place):
	
	country = place
	mgr = owm.weather_manager()

	observation = mgr.weather_at_place(country)
	
	w = observation.weather

	temp = w.temperature('celsius')['temp']

	return "В городе " + country + " сейчас " + str(temp) + " градусов!"




eel.init("web")

eel.start("main.html", size=(700, 700))




