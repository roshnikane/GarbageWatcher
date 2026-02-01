### Environment setup
```bash
cd codebase
```
```python
python -m venv venv
```

```python
source venv/bin/activate
```

```python
pip install -r requirements.txt
```

### Client
```bash
cd client
```
```python
streamlit run Home.py
```

### Server
```bash
cd server
```
```python
uvicorn main:app --host 0.0.0.0 --port 8000
```
