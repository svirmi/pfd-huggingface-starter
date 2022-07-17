# pfd-huggingface-starter
Poetry, FastAPI, Docker, Huggingface transformers starter template

```bash
source $(poetry env info --path)/bin/activate
$HOME/.poetry/bin/poetry shell
(inside-shell) ~/pfd-huggingface-starter/$ uvicorn src.main:app --reload
```

```bash
 poetry add torch --platform linux --python "^3.8"
```

Swagger http://127.0.0.1:8000/docs