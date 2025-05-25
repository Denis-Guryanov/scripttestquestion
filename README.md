# Employee Salary Report Generator

Скрипт для генерации отчетов по заработной плате сотрудников на основе CSV-файлов. Поддерживает различные форматы колонок и группировку по отделам.

---

## 📋 Требования
- Python 3.6+

---

## 🚀 Запуск
1. Склонируйте репозиторий:
   ```
   git clone https://github.com/yourusername/employee-salary-report.git
   cd employee-salary-report
Запустите скрипт:

```
python3 main.py data1.csv data2.csv data3.csv --report payout
```
📌 Параметры
files — Пути к CSV-файлам (через пробел).

--report — Тип отчета (доступен только payout).

📂 Формат CSV-файлов
Файлы должны содержать следующие колонки (названия могут отличаться):

id, email, name, department — обязательные.

Для расчета зарплаты:

hours_worked + одна из колонок: hourly_rate, rate, salary.

Пример:

csv
id,email,name,department,hours_worked,hourly_rate
1,alice@example.com,Alice Johnson,Marketing,160,50
🛠 Добавление новых отчетов
Чтобы добавить новый отчет:

Создайте функцию-генератор отчета по аналогии с generate_payout_report.

Добавьте условие для вызова в main():

python

```
if args.report == "new_report":
    generate_new_report(files)
```

🧪 Тестирование
Запуск тестов:

```
python pytest
```
Тесты проверяют:

Корректность чтения CSV.

Расчет зарплаты.

Формирование отчета.

🚨 Возможные ошибки

Файл не найден — убедитесь, что пути указаны верно.

Некорректные колонки — проверьте названия колонок в CSV.

Неподдерживаемый отчет — используйте только payout.
