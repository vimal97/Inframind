import boto3
 
# Region your instances are in, e.g. 'us-east-1'
region = 'XX-XXXXX-X'
 
# instances ID: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
instances = ['X-XXXXXXXX']
 
def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    print 'started your instances: ' + str(instances)
