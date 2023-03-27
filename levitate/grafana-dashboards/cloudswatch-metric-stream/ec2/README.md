## How to use?

This directory contains a sample Grafana dashboard's JSON file based on metrics from AWS Cloudwatch metric stream.

You can import this into any Grafana, select a data source and start using it.

## Dashboard structure

The dashboard contains following metrics and variables.

### Metrics

1. The percentage of CPU Utilization `amazonaws_com_AWS_EC2_CPUUtilization`
2. CPU Credit Balance `amazonaws_com_AWS_EC2_CPUCreditBalance`
3. Network In `amazonaws_com_AWS_EC2_NetworkIn_sum`
4. Network Out `amazonaws_com_AWS_EC2_NetworkOut_sum`
5. Status Check Failed `amazonaws_com_AWS_EC2_StatusCheckFailed_sum`
6. EBS IO Balance `amazonaws_com_AWS_EC2_EBSIOBalance_`
7. EBS Byte Balance `amazonaws_com_AWS_EC2_EBSByteBalance_`
8. CPU Surplus credits charged `amazonaws_com_AWS_EC2_CPUSurplusCreditsCharged_sum`

### Variables

1. EC2 Instance Identifier

## Integrate with AWS Cloudwatch Metric Stream for sending data to Levitate

Follow our integration guide for [AWS Cloudwatch Metric Stream](https://docs.last9.io/docs/how-to-send-cloudwatch-metrics-to-levitate-via-aws-cloudstream).

> Note that this step is optional, you can use the dashboard as it is with any other source apart from Levitate if you are already set up with AWS Cloudwatch Metric Stream.
