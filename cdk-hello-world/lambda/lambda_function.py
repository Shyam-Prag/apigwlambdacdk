import requests 

def lambda_handler(event, context):
    
    print(event)
    
    return "Hello Lambda from CDK"