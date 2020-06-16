import boto3

'''
AWS Credentials should be set via CLI otherwise
python script will fail.
'''

def get_ec2_instance(name, region):
    ec2 = boto3.client('ec2', region_name=region)

    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [
                    name,
                ]
            },
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ],
        DryRun = False,
        MaxResults = 10
    )

    ec2_info = {}
    for a in response['Reservations']:
        for i in a['Instances']:
            instanceId = i['InstanceId']
            ec2_info['instanceId'] = instanceId
            instanceStatus = i['State']['Name']
            ec2_info['instanceStatus'] = instanceStatus
            instancePublicIp = i['PublicIpAddress']
            ec2_info['instancePublicIp'] = instancePublicIp

    return ec2_info

def main():

    '''
    Verify ec2 instance exist by passing in POC NAME
    and aws_region. Return instance information.
    '''

    ec2_data = get_ec2_instance('TestPocMarket', 'us-east-1')
    print(ec2_data)

if __name__ == "__main__":
    main()