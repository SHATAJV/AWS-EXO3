import json

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    EMPLOYEES = [
        {
            "name": "bob",
            "employee_id": 121
        }
    ]

    try:

        print(event)

        result = ""

        if event["httpMethod"] == "GET" and event["resource"] == "/employee":
            result = json.dumps(EMPLOYEES)
        elif event["httpMethod"] == "POST" and event["resource"] == "/employee":
            EMPLOYEES.append(json.loads(event["body"]))
            result = json.dumps(EMPLOYEES)

        response = {
            "statusCode": 200,
            "body": json.dumps({"message": result})
        }
    except Exception as err:
        print(err)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(err)})
        }

    return response
