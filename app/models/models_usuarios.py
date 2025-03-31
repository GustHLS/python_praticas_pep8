from pydantic import BaseModel # type: ignore

# Modelo base para um usuário
class Usuario(BaseModel):
    id: int
    nome: str
    