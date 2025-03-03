# Tourist-Bot

Телегам бот, разработанный на Python для удобной записи на интересующие мероприятия.


## Авторы проекта

- [@Egor Rassokhin](https://github.com/Xlazzzy)
- [@Boris Suhomlin](https://github.com/BorisSuhomlin)
- [@Roman Uraykin](https://github.com/PapaSvinProgrammer)


## Описание

Разработанный бот позволяет осуществлять запись на мероприятия в выбранном городе, отслеживать интересные места, а также узнавать самые свежие новости. Для запуска бота достаточно в поиске телеграма написать название бота @TouristKudaGoBot и запустить его командой /start. Вы перейдете в меню, в котором вы можете выбрать интересующий вас вариант: события, новости и места. После выбора соответствующего раздела у вас появится выпадающий список с возможными вариантами, а также кнопки для перехода на сайт с записью на мероприятие. Если интересное мероприятие на странице найдено не было, то пользователь может обратиться к следующей странице. 


## Скриншоты

![App Screenshot](https://imgur.com/8MAr3FD)



## Функции

- Запуск в приложении и веб-версии телеграма
- Ежедневное обновление поборки мероприятий
- Круглосуточная работа
- Кроссплатформа


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Обратная связь

Если у вас есть какие-то интересные идеи, замечения, предложения -  можете написать на почту applejebxd@gmail.com




