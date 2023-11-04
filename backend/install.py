import pip 

def install(packages):
    for package in packages:
        pip.main(['install', package])

packages = [
    "fastapi",
    "pydantic",
    "uvicorn",
    "pandas",
    "scikit-learn",
    "openai",
    "uuid",
    "python-dotenv"
]

install(packages)