# Decision_theory
The problem of packing in containers

## Lab 3
The problem of packing in containers

### Next Fit Algorithm
#### Алгоритм «заповнення наступного»
*Найбільш простий алгоритм, що в більшості випадків дає найгірші
результати. Його перевагою є те, що він потребує найменшу кількість операцій
порівняння.*

1) Беремо новий елемент.
2) Беремо новий контейнер.
3) Кладемо елемент в контейнер.
4) Беремо наступний елемент.
5) Якщо елемент вміщується в контейнер, то йдемо на крок 3. Якщо елемент не
вміщується – йдемо на крок 2.

### First Fit Algorithm
#### Алгоритм «заповнення першого, що підходить»
*Більш вдалий алгоритм, що намагається мінімізувати кількість
контейнерів, зменшуючи при цьому кількість порівнянь для пошуку найбільш
вдалого розташування.*

1) Беремо новий елемент.
2) Беремо новий контейнер.
3) Кладемо елемент в контейнер.
4) Беремо наступний елемент.
5) Якщо елемент вміщується в контейнер, то йдемо на крок 3. Якщо елемент не
вміщується, перевіряємо всі контейнери по черзі, починаючи з першого. Якщо
знайдено контейнер з достатньою кількістю місця для розташування вантажу –
йдемо на крок 3. Якщо вантаж не вміщується в жоден наявний контейнер –
йдемо на крок 2. Наступним активним контейнером (з якого починається
перевірка) доцільно обирати останній за номером, оскільки, потенційно, він є
найменш заповненим.

### Worst Fit Algorithm
#### Алгоритм заповнення «найменш повного»
*Головна ідея алгоритму – рівномірне розподілення вантажів по
контейнерах.*

1) Беремо новий елемент.
2) Беремо новий контейнер.
3) Кладемо елемент в контейнер.
4) Беремо наступний елемент.
5) Якщо елемент вміщується в контейнер, то йдемо на крок 3. Якщо елемент не
вміщується контейнер – перевіряємо всі контейнери на максимум вільного
місця. Якщо в мінімально заповнений контейнер вантаж вміщується – йдемо на
крок 3, якщо ні – на крок 2. Наступним активним контейнером (з якого
починається перевірка) доцільно обирати останній за номером, оскільки,
потенційно, він є найменш заповненим.

### Best Fit Algorithm
#### Алгоритм заповнення «найкращого»
*Головна ідея алгоритму – створення більшої кількості повністю
заповнених контейнерів.*

1) Беремо новий елемент.
2) Беремо новий контейнер.
3) Кладемо елемент в контейнер.
4) Беремо наступний елемент.
5) Якщо елемент вміщується в контейнер, то йдемо на крок 3. Якщо елемент не
вміщується контейнер – перевіряємо всі контейнери на мінімум вільного місця,
але в який ще можна покласти вантаж. Якщо такий контейнер знайдено – йдемо
на крок 3, якщо ні – на крок 2. Наступним активним контейнером (з якого
починається перевірка) обирається останній за номером.
