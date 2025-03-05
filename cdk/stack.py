from aws_cdk import core as cdk
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_ecs_patterns as ecs_patterns

class HelloWorldEcsStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        
        vpc = ec2.Vpc(self, "HelloWorldVpc", max_azs=2)
        
        cluster = ecs.Cluster(self, "HelloWorldCluster", vpc=vpc)
        
        ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "HelloWorldService",
            cluster=cluster,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")
            ),
            desired_count=2
        )
