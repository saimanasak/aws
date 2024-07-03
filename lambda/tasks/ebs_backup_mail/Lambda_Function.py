import boto3

ec2_resource = boto3.resource('ec2')
sns_client = boto3.client('sns')

snapshot_filter = [
    {
        'Name': 'tag:My Server',
        'Values': ['Yes']
    }
]

snapshot_details = []

for instance in ec2_resource.instances.filter(Filters=snapshot_filter):
    for volume in instance.volumes.all():
        snapshot = volume.create_snapshot(Description='Created by Lambda')
        snapshot_details.append(snapshot.snapshot_id)

sns_client.publish(
    TopicArn='arn:aws:sns:us-west-1:068261094692:MyTopic',
    Subject='My EBS Snapshots',
    Message=str(snapshot_details)
)
