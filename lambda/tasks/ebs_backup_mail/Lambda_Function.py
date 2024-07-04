import boto3

# Initialize AWS clients
ec2_resource = boto3.resource('ec2') # EC2 resource
sns_client = boto3.client('sns')      # SNS client

# Define filter to find instances tagged with 'My Server'
snapshot_filter = [
    {
        'Name': 'tag:My Server',
        'Values': ['Yes']
    }
]

# An empty list to store the ids of snapshots
snapshot_details = []

# Iterate through instances matching the filter
for instance in ec2_resource.instances.filter(Filters=snapshot_filter):
    # Iterate through volumes attached to the instance
    for volume in instance.volumes.all():
        # Create a snapshot of the volume with a description
        snapshot = volume.create_snapshot(Description='Created by Lambda')
        # Append the snapshot ID to snapshot_details list
        snapshot_details.append(snapshot.snapshot_id)

# Publish snapshot details to an SNS topic
sns_client.publish(
    TopicArn='arn:aws:sns:<AWS-Region>:<AWS-Account-ID>:<SNS-Topic-Name>',
    Subject='My EBS Snapshots',
    Message=str(snapshot_details)
)
