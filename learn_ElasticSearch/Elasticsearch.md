# Elasticsearch

标签（空格分隔）： 未分类

---

> Elasticsearch  ⇒ 索引   ⇒ 类型  ⇒ 文档  ⇒ 字段(Fields)
>                  megacorp  employee

## INSERT

    PUT /megacorp/employee/1
    {
        "first_name" : "John",
        "last_name" :  "Smith",
        "age" :        25,
        "about" :      "I love to go rock climbing",
        "interests": [ "sports", "music" ]
    }

## SEARCH

    GET /megacorp/employee/<id>
    









