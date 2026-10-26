## How to use?

This directory contains a sample Grafana dashboard's JSON file based on metrics from AWS Cloudwatch metric stream.

You can import this into any Grafana, select a data source and start using it.

## Dashboard structure

The dashboard contains following metrics and variables.

### Metrics

1. The percentage of CPU Utilization `amazonaws_com_AWS_RDS_CPUUtilization`
2. Number of DB Connections `amazonaws_com_AWS_RDS_DatabaseConnections`
3. EBS Byte Balance `amazonaws_com_AWS_RDS_EBSByteBalance_`
4. EBS I/O Balance `amazonaws_com_AWS_RDS_EBSIOBalance_`

### Variables

1. DB Instance Identifier
2. Cloud Region

## Integrate with AWS Cloudwatch Metric Stream for sending data to Last9

Follow our integration guide for [AWS Cloudwatch Metric Stream](https://last9.io/docs/integrations/observability/aws-cloudwatch-metrics/).

> Note that this step is optional, you can use the dashboard as it is with any other source apart from Last9 if you are already set up with AWS Cloudwatch Metric Stream.
