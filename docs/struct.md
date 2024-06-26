# Структурные модели
### Диаграмма классов

![Диаграмма классов](https://www.planttext.com/api/plantuml/png/lLRDZfim4Bxp53vcjQ4FWDhLjdlOMrLrUwigom43Li16zf1iLFNTEnviC2IxlJM7A9d_RxwPWKS7miBOTvaxAZq8AthMAItXCaXcBBGcoyfEECUUhQhOxupX9sUWe9C5Ss2LReBCrBMJK32bWIJt-4l1RcMwJwtk2dOogWh6bHLdtc2ItLekgehhiNUyam3IEWxcbfbJZLxB_yJAlum0HhzREyduMLNGBW2Yk9MgQI6Lzz8vqMo372ZFTPGWlmxpogdxgUXoBRAo15uRots72WRZqCb4LR3XqeXUVlYEVxOk8NM0dBgMfZCs5GMwNdd2q9wj0qGI0tvFXMlDEIfk43hvxoZRfwz6oxLDsGgDSKZDVO_CITeDimE61XvJBgXIeWFJdqSmBwqQt4psTYXp9av2TUA0l1uwKnuT5Y-ZpdbVJWuROO5RuQB4M2Kr2516fv4hvVk-4eQclZdqfPK2vCJvLC_kPdrtQwQY6rQsmzquI6nUFTiJSM-5cM7SiqO2r_8y6L1ZAM1f_61Ga3MY_HNmFJM7UuzAQImfz6bJhd8KcPz4X_lfK_g_i-d1c2vTzg2dwP9mRP_qRnmgtuWjM093JSAf96VtRfZ136Fd0yK3GbsQ3yWphXTDLCxQiHU8_LidBj9cqoBrmuY7gM1FuTTAdDI6U6fiA9z62oVHcb5N75C0dyrR1RE1jwucI4lo2Gu_6tkSJizQZadyubt9Oqn_AhZVCkmH3McUP_EsJfsw8u5Vx7dh172wAINIxnSqcvPNujpuWh7RlNBHaqBLrlIyCdYoAs8nKNcFYQSOA8B7d0QYj1SATtnXOUfvu44ZZEJy8Yvahg27L3QldPDTlLzCfx139qePa7g36Qs93ZJE1VlX9_WdJJb-_KegYKI7MlvdQd_TGjfEwcPvq6okKj8PR7TOou-qb0yBwKcfuR6poRndKj-g9sxrg8y94YiRp38DyRy14PGyVmZ45ZG6niaAZ_QYV9hNArNJouXNlz16MrdZcm43V5cXNSqhSzQeVIPcb9zPKO9ZPmNjsc9wDtZVPdwgl6yMORJ2hHKB1Azwn8xY-zPV)

#### Описание
- **Game**: основной класс игры, управляющий ходом игры и взаимодействием между игроками, кнопками и сеткой.
- **Grid**: представляет игровую сетку с атрибутами для настройки и методами для рисования и подписывания.
- **Button**: отвечает за отображение и взаимодействие с кнопками на экране.
- **Player и Computer**: представляют игрока и компьютер соответственно, с атрибутами для кораблей и методами для размещения кораблей и стрельбы.
- **Ship**: класс для представления кораблей с атрибутами координат начала и конца, а также количеством попаданий.
- **AutoShip**: отвечает за автоматическое размещение кораблей на сетке.

### Диаграмма объектов/компонентов

![Диаграмма классов](https://www.planttext.com/api/plantuml/png/rLPDRzim3BtxLmWv9PW3B6cxGu4D1NPeZmC6x58KWcBBjbPPCYIwGJVqlu_wi2CxReS1ss6v918VgKVgaSgD1MQWRsLc7uNgc64jaK9nUEuuqGOQdMNwy9qNG9g-PUhMY9Byp0X-jWG4I4u-ajMTCn5dMqMJhYhB0MrNVkCT4Kh0sZjS4mj6g3gFe6kqmUQQF6bHHd1fs97M66uztMTbILNVMYev03UMWbw2ML6hwVxBc4MXswv7t-L4FaVh_v4Bwq5_RKHdnqHcLBU4FJ4XsK5oUf2wUBHekb_lSxBVv6HzaPEBpKD4MXU81k_xzIudEmVPHUZEGSFtvTJ5mLUE1TcjSX9-xLS3H1l15J0GMY7mVTmjXK7-OM-N5lNLAXQ6C-3KgpMaifwdXdV1dHVqdUGpDoIrnc8VkA6w6l5uIdvMeI6C51PYb9e3LVmO0BJI9WGij3Ono9XGN2TfnntdGPr7AHHIik606LrXVMJwn2HUk3lIBKVeGMkPgYVQdNAGypa-gL_VbQuGysHzChv8A6BlRDyCq-ckboxGe4XVfQIxUcCmyLlMyb6JVcwuvleYsJCtGrSDZPYstToMyCKSAopoAD2hd5mvGNvmtuFQcD6zAgba5kWOen6Gode_ebsyCXG2ZK7oAUTG3thK1aTZZH0mFLy083NNv6ytGkhmHqrMOosfVi94AgsSd-gbJ6TBkBNDC2yQVQGjjvRLUDr0dIvfWNV2pOWf6euwTdN1ss-5FNdxW9NHBIqrJgNIwsfYT5v1EwTmGwNnR0sd_PO9XOkNwGiIL32gGpcfd8d3oGjtnoSddH7EOvYxmr6TP0K_huG6twHbxBBDmZlm2fsv8YEXzFNu-vnykbut0nt9LGqD7dovE4zNTxZ-WR9WSY2AzsDFudf8IVhX6O_D2LSd2gVfqwl7aQpXDNPtwA3Vrl6FQ7_Z1aHnJleVqasrjvMyWksdH5upDMoDg1k7cDntbawtRQcFQeWHt1RjqyYBaF4PpxBJYpw9xxOMR6djinki4FwF-mK0)

#### Описание
В данной диаграмме классов объектов показано, как класс Main создает экземпляры классов AutoShips, Grid и использует Button. Класс Main также работает с экземплярами Grid, которые представляют сетки для компьютера и человека.


