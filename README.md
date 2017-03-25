## Flask Hive boilerplate

Flask web framework boilerplate to access [Apache Hive](https://hive.apache.org/) using Cloudera's [Impyla](https://github.com/cloudera/impyla), a python DB API 2.0 client for Impala and Hive (HiveServer2 protocol).

*Twitter bootstrap and echarts js included*

### Prerequisites
Install flask
> pip install flask

Install impyla
> pip install impyla

Install thrift_sasl
> pip install thrift_sasl

Install sasl
> pip install sasl

Install thrift version 0.9.3, will not run on version 0.10.0
> pip install thrift==0.9.3


### CONSIDERATIONS 
Please take note that I don't recommend using this to query large data sets, as it will be super slow(this is by design, 
Hive isn't intended for real time usage) depends on the size of the data.
 
My intended usage is only to access summary tables in hive
 which consist of results of data that are already been processed and ready to show on the dashboard.

  
 

   
   
     
   