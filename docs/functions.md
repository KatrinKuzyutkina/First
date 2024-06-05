# Функциональные модели
### Расстановка кораблей
- **Приложение**: Предлагает выбрать режим: Авто или Ручной.
- **Пользователь**: Выбирает Ручной и начинает рисовать расстановку кораблей.
- **Приложение**: Проверяет не пересекаются ли корабли, не выходят ли за границы поля, расположены ли все корабли.
- **Приложение**: Сообщает код ошибки или сообщает "Игра началась. Ваш ход!"
- **Пользователь**: Нажимает кнопку отмены.
- **Приложение** Удаляет последний корабль, который нарисовал пользователь.
-  **Приложение**: Отображает корабли на поле, как была завершена расстановка.

![Расстановка кораблей](https://www.planttext.com/api/plantuml/png/ZLHHRjD04FttAPP-4GauGFBHNYKKLua80JL6_IKkXQ14DLH2GdpGIbp0SUBMQHBt2ZCtuitiajYEKzZ8iTSxR-RDp1iV3OBsQV3-JS_G3SKyn2-acDQKKqBt51lyvVm1hwQqvCXJSwzxOfxIJxp48IqCpbEwfOnMXmqJTFm-Jc_ud3-hdqN3CrXDkiPcoHEwK-Sn0gMo5tY6kEUKSbYEDsafzApJxVdmUOq3WQQuWvlrAqlvV1VkS0Vy25ocCCcsVEP5Urc3isvmtDda4NDKHCQ7PUlZzW0CAkmCRfeIO9iyYwjv0Ez500zfYMH7MhXL1V_ae5KNix9efLMTKLvYWrgY4U6s9n_rRCNZMbg_qQ_Ke2gvxJYktFRBz9_J0zmiqP0fhNdC5pk1wecMh383BzAe53cdMk1Bj6V8qR_Az0Yq4jVllx9TtBprUy84QK1AvJXD-YKvqbJ3tEBQLPi1C9RWkQHPZgKIkn92rJpbSJCuKXxKx17TkOH_q4o06XA55wHucRmmT8MdaU4Bq9XNDI7hvQdVVbqknDwqRUh_DNcgpPJc6DnB_e8vMDGEOw7utHDlTuUdl_EQmFStumOMqcfuZkXN78MoT_I41uBd8aeOPYYoXbsBGAtWosLEv6Eqqq7AdXbrIG_RBmL7CjbhwTiULHchkLf7Yaja2AGRy1KwwplftSonpFWJZvrmE79OIzYfoQKcLWfFQfJKycmLzqYr3b9Lx21u-yuxWXjyqVy0)

- **Приложение**: Предлагает выбрать режим: Авто или Ручной.
- **Пользователь**: Выбирает Авто.
- **Приложение**: Рандомно расставляет корабли, проверяя не пересекаются ли корабли, не выходят ли за границы поля, расположены ли все корабли.
- **Приложение**: Отображает корабли на поле, как была завершена расстановка.

### Ход игрока
- **Приложение**: "Игра началась. Ваш ход!"
- **Пользователь**: Указывает координаты выстрела на поле противника.
- **Приложение**: Проверяет, попал ли пользователь в корабль.
- **Приложение**: Обновляет состояние игрового поля, показывая результат выстрела (попадание или промах).
- **Приложение**: При попадании в корабль противника сообщает "Дополнительный ход".
- **Приложение**: После каждого хода сообщает координаты последнего хода пользователя.

![Ход игрока](https://www.planttext.com/api/plantuml/png/pLBBIiDG5DpVhpXcPK7yW6HXVqMmOA4-i1MtROeef1WG5wvq8UvZcj1gJF8BS_x8EJSMYtl1mCqzdCUScU7snvF3YydboKZmYWQ5O8sbJXb-87E-wC80ZpwP2MfaUeCC5U-PBlO5zunkHQzjUYU8N8WNcyLA4-IyIus5YGOD4Gh26qIiYI3NX1WnqwNXUN11ozOA9GEZeJ4dSbRM1Xgvg-FXQ22xU6PNQpm8u-6D7jvGwUAW9yCnMmfaFIVyGZonKdCYPptrZ7J64IxdF_NevO_od6U9vfkAfdjTj2LAK_6iLpgtZOJ9JEKlGL6tFS239skok8dDfGsX9jRxbd4TrRyqRt1wjF6lDkX_OS_ctRLSp4hdXzb4uPtsJwfPw9qPfrETHtoMP-UkJpLyj-uB)

### Ход компьютера
- **Приложение**: Рандомно выбирает координаты для выстрела.
- **Приложение**: Проверяет, попал ли в координаты корабля пользователя. 
- **Приложение**: Обновляет состояние игрового поля, показывая результат выстрела (попадание или промах).
- **Приложение**: При попадании в корабль противника сообщает "Дополнительный ход".
- **Приложение**: При ранени корабля пользователя следующий ход он делает вправо, влево, вверх или вниз от последней клетки, в которую попал.
- **Приложение**: После каждого хода сообщает координаты последнего хода компьютера.

![Ход компьютера](https://github.com/KatrinKuzyutkina/First/blob/main/docs/diagrams/3.png)

### Бомба
- **Пользователь**: Попадает в координату корабля противника.
- **Приложение**: Цель была поражена 5 раз.
- **Приложение**: Дополнительный ход, Бомба активирована.

![Бомба](https://www.planttext.com/api/plantuml/png/bP7DJi9G48Ntzob6LfAOk6935_8g9f98WcW4urPB41AQ88aBjxp11LkzjloymfatyjpRyhErINFRSy_CV3FJwW-k7mTFTrqJFamJd_ZI5soH2tOyTh18-MOQ2rQ2dDgMXXGE6rYDTHX4IXPB53fZd4-WCHqhUXolRMIURplTjfnZ4L8KclXJGjYFq7HQjLGf5g9loBpxgYwTFiFN_DreeXDaqgWRuTEiuIEGCgslnyeXXBufVaL7l4ZF1E_8AoZBh8walSj6BIfpdFRj-osg6cncogWm07qDtHtvA2K7miYqUpTLb_yXkn3CUQuvFIlCkuTq0OUmViu7p8METSwwOp_N8yot7qlegSI14mOlMMZeTxAdZxZc-mVJ8Ybt_WS0)
   
### Проверка окончания игры
- **Приложение**: После каждого хода проверяет состояние всех кораблей обоих игроков.
- **Приложение**: Если все корабли одного из игроков потоплены, объявляет "Вы выиграли!" или "Вы проиграли!".
- **Приложение**: Игра заканчивается.

![Завершение игры](https://www.planttext.com/api/plantuml/png/PP51ReCm54JtFeMRLNE5i6YkKYb4GQAqAbJT9f6gBbWWTTLThk0IQ2WHv0hpRzIn0wgJ8jd6CE_FVFrvcjq_PoyFiSPErkXHekRPmcXUMgvEtc7GeP52ey5Urf8hHwcPpqZ1VIiRocI3dYzRxeKbKMkK_5ZBcxOr2HbyuOWQFu5wNKLng6_nOHMN_niRecA97dlqrlumP1Z2bHedwkd4qzRh9B-RwYXblSxccIhDPuPF1x6fasChhYE-QJDa3bIOBCOa5SoPYvQyxQuD_cNyIsHedgt2n2_Y0apONZwwd_N6mfF0QS8u3IyZ-rGfkS_SZ52oY9RN_HseQUt0EBQ6a_4wJBF79pKdnN7_0W00)



