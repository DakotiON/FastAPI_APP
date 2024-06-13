from pydantic import BaseModel, EmailStr
from typing import ClassVar

class User(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra: ClassVar = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    schema_extra: ClassVar = {#примечание 1(смотри ниже)
        "example": {
            "email": "fastapi@packt.com",
            "password": "strong!!!"
        }
    }



"""Примечание 1:Ошибка, с которой вы столкнулись, указывает на то, что в ваш
ем классе User атрибут schema_extra не аннотирован как ClassVar. 
В Pydantic, если вы хотите добавить примеры или другие дополнительные метаданные, 
которые не должны быть частью модели данных, вы должны использовать ClassVar из модуля typing, 
чтобы явно указать, что эти атрибуты не являются полями модели.

Кроме того, в вашем коде есть некоторые ошибки, 
связанные с использованием IgnoredType. 
Вы присвоили IgnoredType атрибуту schema_extra, что не является корректным. 
Вам нужно определить schema_extra как ClassVar и предоставить ему словарь с примером.

Вот исправленный код для класса User:"""

#Больше про аннотирование атрибутов(типа schema_extra) читай или спрашивай у гпт