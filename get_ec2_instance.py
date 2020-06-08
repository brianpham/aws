import boto3

'''
AWS Credentials should be set via CLI otherwise
python script will fail.
'''

ec2 = boto3.client('ec2')

def get_ec2_instance(name):

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

    for a in response['Reservations']:
        for i in a['Instances']:
            instanceId = i['InstanceId']
    return instanceId

# get_ec2_instance('TestPocMarket')
def main():
    '''
    Verify ec2 instance exist and return instance status
    along with other relevant information
    '''
    instanceId = get_ec2_instance('TestPocMarket')
    print(instanceId)

if __name__ == "__main__":
    main()