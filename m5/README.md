# Task 5


1. На Server_1 налаштувати статичні адреси на всіх інтерфейсах.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/1-1.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/1-2.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/1-3.png)


2. На Server_1 налаштувати DHCP сервіс, який буде конфігурувати адреси Int1 Client_1 та Client_2

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/2-0.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/2-1.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/2-2.png)


3. За допомогою команд ping та traceroute перевірити зв'язок між віртуальними машинами. Результат пояснити.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/3-1.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/3-2.png)


4. На віртуальному інтерфейсу lo Client_1 призначити дві ІР адреси за таким правилом: 172.17.D+10.1/24 та 172.17.D+20.1/24. Налаштувати маршрутизацію таким чином, щоб трафік з Client_2 до 172.17.D+10.1 проходив через Server_1, а до 172.17.D+20.1 через Net4. Для перевірки використати traceroute.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/4-1.png)


5. Розрахувати спільну адресу та маску (summarizing) адрес 172.17.D+10.1 та 172.17.D+20.1, при чому маска має бути максимально можливою. Видалити маршрути, встановлені на попередньому кроці та замінити їх об’єднаним маршрутом, якій має проходити через Server_1.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/5-1.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/5-2.png)


6. Налаштувати SSH сервіс таким чином, щоб Client_1 та Client_2 могли підключатись до Server_1 та один до одного.

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/6-1.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/6-2.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/6-1.png)


7. Налаштуйте на Server_1 firewall таким чином:
• Дозволено підключатись через SSH з Client_1 та заборонено з Client_2
• З Client_1 на 172.17.D+10.1 ping проходив, а на 172.17.D+20.1 не проходив

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/7-1.png)
![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/7-2.png)

8. Якщо в п.3 була налаштована маршрутизація для доступу Client_1 та Client_2 до мережі Інтернет – видалити відповідні записи. На Server_1 налаштувати NAT сервіс таким чином, щоб з Client_1 та Client_2 проходив ping в мережу Інтернет

![](https://github.com/ArturMaksymchuk/materialsEpam/blob/master/m5/8.png)

