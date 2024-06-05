# Поведенческие модели
## Диаграмма состояний для автоматического расставления кораблей
```mermaid
graph TD
    A[Объявить множество доступных блоков для размещения кораблей] --> B{В множестве есть доступные корабли?}
    B -- Да --> C[Выбирает случайную координату]
    C --> D[Определяет начальный блок для корабля]
    D --> E[Устанавливает случайную ориентацию и направление]
    E --> F[Создает корабль с указанным числом блоков]
    
    F --> G{Проверка пересечений}
    G -- Пересекается с другими кораблями? --> H[Повторно пытается создать корабль]
    H --> C

    G -- Не пересекается --> I{Проверка выхода за границы}
    I -- Выходит за границы сетки? --> J[Меняет направление корабля]
    J --> I

    I -- Не выходит за границы --> K[Добавляет корабль в множество размещенных кораблей]
    K -- Удаляет корабль из множества доступных блоков] --> B
    
    B -- Нет --> M[Сетка заполняется кораблями]
    M --> O(Игра началась. Ваш ход!)
```
**Описание:**
В начале определяется множество доступных блоков для размещения кораблей. Проверяется имеются ли доступные корабли:
   - Если да, программа выбирает случайную координату и определяет начальный блок для корабля, устанавливая случайную ориентацию и направление. После этого создает корабль с указанным числом блоков. После размещения корабля происходит проверка: 
      - Если корабль пересекается с другими кораблями, программа повторно пытается создать корабль.
      - Если корабль выходит за границы сетки, программа меняет направление корабля.
      - Если всё верно: корабль добавляется в множество координат уже размещенных кораблей и корабль удаляется из множества кораблей доступных блоков.
   - Если нет, программа заполняется сетку кораблями и выдаёт сообщение "Игра началась. Ваш ход!"
## Диаграмма бомбы
```mermaid
flowchart TD
    start[Игра началась. Ваш ход!]
    initVars[Создаётся массив для отслеживания попаданий в координаты кораблей противника]
    hit[Попадание в корабль]
    updateCounter[Увеличивается счетчик попаданий]
    saveCoordinates[Сохраняются координаты попадания]
    check{Попаданий >= 5?}
    activate["Дополнительный ход, Бомба активирована"]
    determineCenter[Определяется центральная точка]
    applyBomb[Наносится удар 3x3]
    resetVars[Сбрасывается счетчик и координаты]

    start --> initVars
    initVars --> hit
    hit --> updateCounter
    updateCounter --> saveCoordinates
    saveCoordinates --> check
    check --> |Нет| hit
    check --> |Да| activate
    activate --> determineCenter
    determineCenter --> applyBomb
    applyBomb --> resetVars
    resetVars --> hit
```
**Описание:**
В начале игры создаётся массив для отслеживания попаданий в координаты кораблей противника. Бомба есть только у игрока и активируется она после 5 попаданий в координаты кораблей противника. После активации бомбы пользователь видит сообщение "Дополнительный ход, Бомба активировна". Игрок нажимает на координату выстрела бомбы  и бомба, размером 3x3 поражает поле противника.
## Диаграммы хода компьютера
### Диаграмма первого выстрела

![Диаграмма первого выстрела](https://www.planttext.com/api/plantuml/png/pLJ1Ji904BttApQS8E4Bw45-1ME9H4G3zGvjY1Y8N3nvq1ZZlIsjBQsKNvZz8z_C0W9oDH7ItMdtxRptPgTj3jnMtxsxxbeIM0rweRKUKa8nhaBFAT6UqYE4lhwdW9QqGlIeAAUIIY1ZocX5WVQqhoZIKpr2o0aA2cpaUyLDIHaUZp43ZNo7EDlgj5MLti6o1jq435DQ7e7EQigzT7h0nHJKB8KVQmt1NLAqhxJaJHZdMCeeKHWMeY72jQ1IWQNa3NKJvN2LWZ62YRaIjbJx0CoG9lYbbbqnksX-nbukH69IHGBvbDe9-Kur5W9vL1ZjHlyJzeHO-D5_egnJUIW9GiP1Zv9IPMoMybFKgA0UstjCRn2EC-MZqmz8VLnUHI4ynqP3R7nYRQPO6svHkph7Qz6nlOk07-gnn6mkLH3gYI1k6UcY5SObMoWuEUQCuSOJ7zFGj1DxM2DrOHlPJdVWe6m-FFzDqLB68KGxenGJB6mAvlGkEctJO1KXatPXVy3pEp7RDAXfw8fjRNLbO5i8vnV-WTeS-kv03ZHnMSpMyxxJkhBOS9NHsliFxTsW3tQdv9N4olxRksNCjM_00_VcrZ9rQsB2v-GR)

### Диаграмма неудачного предыдущего хода

![Диаграмма неудачного хода](https://github.com/KatrinKuzyutkina/First/blob/main/docs/diagrams/4.png)

### Диаграмма затонувших кораблей

![Диаграмма затонувших кораблей](https://www.planttext.com/api/plantuml/png/pLJBJi9G4Dtp5HDNal05TY6_WegHY8y0nYr2Y1e8nCIL2nDZt9VIGg6q_OMvV-IPkHGi47ScbWI6kVUUEMVct9QRhKgZTNTLBsXGkB-erQjqo2-cpn5nn25nQjeSi8-CRxhccKEU4tkcRnvCHvSYGlw1KmxC4yVOjpmkKgq969_TOe7mPBXldE28osEEp82mdY1qsKEbW6F04YyvHdOACE1Z9I6UiOim0NONXPyuDBsT2l8SyNl6LcYP4K0wf7WUA0u9B2C4ZoWv5pIaU85L8UL3M2o5JDTP8zREKUCp9svRF9YqBghNsrmoFcDRViq6M8agIv28KJCWV4s09RiIdeZW504Eb6oq0DqPAdjWDoAjEaCdq470kA8mHuXT9yT2DRm1GvG65jBJhLFjav9Ogz3nI2hAQx5wNZS3oxgxsx--9jTp7ibOjOMXYEV5FWhehEavUof-g3N4USFztkCnUk5RBhxLZpMOoveAFIr9d2gVx9-7_MtJqrZ4pWY4EqfCFA8EYl4z5ocHWECtBAb1HPkChstz8rfIG4TEddwrteJZmMtynytSSpksc5oVrSxpnZpGucepqO_pSby6AuER7XRyWmsArI8TCPt_QF4Z_XB6fDSKEwm0qKNIeQpuukVLbgVPkhdTYCorwQHoUdbVQPojvlHxgomg0BBtt8zEoVaGyYOwmoK-BgqkMM1jdvkmcCufx48frJBoU5b_0m00)

### Диаграмма раненных кораблей

![Диаграмма раненных кораблей](https://www.planttext.com/api/plantuml/png/pLJBIiD05DttAmPN2dv1iz1VgRPYiLQn5RS-A2WLYk1AH11nFyR4ngP9V-7C7tdkZKcR6XG4mHJAS6VctFEuoMQltpZg7-ztQhgedUosEospYXitH6mG8pAOkLE425W9t8MxGeHt0zyDtPaxrwtOi7w66K9tYOJdfXjhfjqZJ02xLZDySjmxfBnYyOBONHlkfrnQ-EmK8Y6imHG9gsy48pvtKeCnB9SfiI_O-1AH6tpf84yTjsHdyQezflpPoii6apaFDdxt5ABLRUOy4xO_pu3hUCnrkf6KXIKHGqpKZX1Jm_DMVIgaa4Va5SJQEyHyAdcqx245zNTRtML96OC74XLN_883iL8rA6L1keM6Vo9SJgLu5TzcNF32UhQQaDsOdNqQCZBQTKnF60HXhEfQ90JhbLYeXZjYq3lf9f2-7dqZvKnoMAXGBwGKbxNaCHMvvvuAgcGIy4uYTDom51CfY-zYOIJYCQcYG6VTmAle-AHcMGrA8eh4XgnpLNRX3sQqEZsE2Trx-ME95TExnAJRRE-KnsL5cslu8aPdbIb_ZfqRS2DOcQDaMXP7_dyDNXttaahkuc_YgkDPH1jz_tWYyq2iCM9opfylTFbUhtzmEFUfvFHMOtllf77K_8pwUxUzsjTlYs9liiwlxmS0)

**Описание:**
Процесс начинается с проверки успешности предыдущего выстрела.
   - Если выстрел был успешным и корабль добавлен в множество затонувших, то определяется новая случайная координата для следующего выстрела. Затем проверяется успешность следующего выстрела:
      - Если он попал в корабль, то обновляется состояние игрового поля и принимаются соответствующие действия (добавление координат корабля в список поврежденных или затонувших).
      - Если выстрел не попал, то ход переходит к игроку.
   - Если выстрел был успешным, но корабль не добавлен в множество затонувших, то происходит проверка определено ли направление атаки, компьютер стреляет в текущем направлении. Процесс повторяется до тех пор, пока не будет определено направление атаки.
      - В случае успешного выстрела компьютер продолжает атаковать в том же направлении.
      - Иначе меняет направление или переходит к ходу игрока.
        
Диаграмма также показывает возможность дополнительного хода после успешного выстрела.
## Диаграмма последовательности

![Диаграмма последовательности](https://www.planttext.com/api/plantuml/png/xLPDRzD04BtxLomvWGIdtdf0_IjHoQ5IQA8sI1pp8IXIgWOg9102GW_StRHMZTlOVs7s7_5crcjx_H4d26v4YXrxTzzxE_DcDWUde-x9wDNBljSz70rE52qffdjzJdUuhyZNKmhusHjYsj7XqR1xF5BqcMxqc7ptvHUA-ILTL-TVOMW2g5WlQ4qX80L1poi8z429FjSNpAl7xl076Ru6hzSaKprxdgdRL_G9SX8zqnEAy2lGKmLo9fvvNhSFo4iz1o1qAru1ZQpIXqP6ZIXKk6Ix0iKlJ-6p9VkF6aHVqOhvzHcjSRqmUEaQMTyOAo1-Xmo35Eef-Ef4Os-z_cbFqNimJILaB304Os02eHVrk_Lt4zE47xheLgiJoT3h7Rz06ejSbUoNGjW0v88qP0PGt_1qncyO0Zb7Bht-O32q6-RvUAdqM-mpeljTCdq5rB6CB8pB4ef5foYz1U3QhAr6sAaQG2rJATY_tI_0yFM1uvia28huTrax92GES6ioAsCAoDPix7pyseJT6FSEVHID66PWEm3tppdORp1msycH6pMM8juEcc5AeFBUeGgVBQtJJlQqmA0Gc8WhGXnhiidPAL5lSbQ6jLziKLL38InuWEkCex44BTLXoLMrbhCKMMJLiF5YAJ6kG7xSUxtt9y4hzopJWTDo2rGQsDout1ZaBatiAwO_5AtNrZ5-SZeObGieCDbXPXCzPpOwPP6mMfj_PrCxd5LIzlgTxUx6nvujELVz_nPKmgvnm_RDfy5jRL5lTfirH5HmsRzoM9uCYmt0t4qSELyznd4zuPNEyIb0Semd9iPeANgcP1zCVyCk2kcki27MyAI-83US0fVSgrQ8ky7ncVnHXs5PHJgU24DXHcT7dWq1oBB0tmDSyAVtDm00)

**Описание:**
Игра начинается с размещения кораблей, после чего игрок и компьютер поочередно делают ходы, стреляя по координатам на поле противника. Если попадание подтверждается, состояние игры обновляется, и игрок получает дополнительный ход. Помимо этого, если у игрока активирована бомба, он может использовать ее для атаки области 3x3. Игра продолжается до тех пор, пока не будут потоплены все корабли одного из игроков.

