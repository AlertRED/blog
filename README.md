# Run tests

```shell
cd ./backend
python3 manage.py test
```

# Run develop
### Backend
Install dependencies
```shell
pip install requirements.txt
```
Change directory
``` shell
cd ./backend
```
Migrate DB
```shell
python3 manage.py migrate
```
Run backend server
```shell
python3 manage.py runserver
```

### Frontend
Change directory
``` shell
cd ./frontend
```
Install dependencies
```shell
npm install
```
Run frontend server
```shell
npm run dev
```

### Linting
Connection pre-commit to git hooks
```shell
pre-commit install
```

Check project by pre-commit
```shell
pre-commit run --all-files
```
