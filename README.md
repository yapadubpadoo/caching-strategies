# caching-strategies
Practicing on AWS practice 

https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/Strategies.html?fbclid=IwAR0NOW1MQOsXn9jlnSlO3G5xS13JJwo5-WVFgV9mOJpxQ9yz2ijFV0SzxZs

## CLI for POC
```
python cmd/cli/main.py
```
## HTTP API
```bash
uvicorn --app-dir=cmd/http_api/ main:app --reload
```