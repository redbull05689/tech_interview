<details>
<summary><strong>OWASP</strong></summary>

### Базовые понятия безопасности

- **Уязвимость** — незапертое окно на первом этаже.
- **Угроза** — вор, который ходит по району и проверяет окна.
- **Риск** — вероятность того, что именно этот вор:
  - обнаружит именно ваше окно,
  - проникнет в дом,
  - украдёт ценности
  что приведёт к финансовым и эмоциональным потерям.

---

### Классификации уязвимостей

- **CWE (Common Weakness Enumeration)** — каталог *типовых слабостей* в программном обеспечении.
- **CVE (Common Vulnerabilities and Exposures)** — база *конкретных публично известных уязвимостей*.

---

### OWASP

**OWASP (Open Web Application Security Project)** — некоммерческая организация,
цель которой — повышение уровня безопасности веб-приложений.

OWASP предоставляет:
- методологии
- гайды и best practices
- OWASP Top 10
- инструменты и обучающие материалы

---

### Burp Suite

**Burp Suite** — инструмент для тестирования безопасности веб-приложений.

Основные модули:
- **Intruder** — модуль для проведения автоматизированных атак (bruteforce, fuzzing).
- **Repeater** — модуль для ручного и контролируемого повторения HTTP-запросов.

</details>

<details>
<summary><strong>Broken Access Control</strong></summary>

### Insecure Direct Object References (IDOR)

**IDOR** — уязвимость контроля доступа, при которой пользователь может получить доступ
к объектам, не принадлежащим ему, манипулируя идентификаторами.

---

### Защита от IDOR

- **Проверка владения**



## CORS (Cross-Origin Resource Sharing)

**CORS — это механизм браузера, а не сервера.**
Сервер лишь указывает политику, но решение о доступе принимает браузер.

### ❌ Опасная конфигурация

Использование:

```http
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

### поиск скрытого контента

https://github.com/danielmiessler/SecLists
https://github.com/aels/subdirectories-discover/tree/main
https://github.com/kkrypt0nn/wordlists

Это огромная коллекция wordlist'ов, полезных для различных задач пентеста, включая content discovery. В Kali Linux многие списки уже предустановлены и находятся по пути /usr/share/wordlists

### homework


```http
ffuf -u http://<ip>/FUZZ -w /usr/share/wordlists/dirb/common.txt -fc 404

gobuster dir -u http://TARGET -w /usr/share/wordlists/dirb/common.txt
gobuster dir -u http://TARGET -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50
gobuster dir -u http://TARGET -w /usr/share/wordlists/dirb/common.txt -x md


```
</details>