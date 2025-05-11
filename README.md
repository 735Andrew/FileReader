<h2>FileReader</h2>


<b>FileReader</b> - проект, занимающийся составлением отчётов по входящим .csv файлам.<br>

<div>
Приложение ставит перед собой задачу парсинга необходимых .csv документов по их содержимому<br>
и вывод информации в консоль в JSON-формате.
</div><br>
<div>
<b>:large_orange_diamond:Внедрённые особенности:large_orange_diamond:</b>
<ul>
<li>

Название отчёта передаётся через специальный флаг `--report <report_name>`
</li>
<li>Если файл находится в другой директории - к нему можно указать путь</li>
<li>Код написан с использованием стандартной библиотеки Python</li>
</ul>
</div><br>
<hr>
<div>
<h3>Локальное развёртывание проекта на ОС Windows</h3>

```cmd
    git clone https://github.com/735Andrew/FileReader 
    cd FileReader 
    python -m venv venv 
    venv\Scripts\activate
    (venv) pip install -r requirements.txt
    
    (venv) python main.py data\data1.csv data\data2.csv data\data3.csv --report payout   

    # Для удобства ознакомления проект идёт с экземплярами .csv файлов  
```
</div><br>
<hr>
<div>
<h3>:paperclip:Пример работы скрипта</h3>
<img src="data\work_examples\example1.png" width="850">
</div>
<hr>

