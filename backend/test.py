import pyspark
from pyspark import SparkConf
from pyspark.sql import SparkSession
import pprint

spark = SparkSession.builder.getOrCreate()

df = spark.read.csv("data/DEMO.csv")

print(df(0).show())