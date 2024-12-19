from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

def process_with_spark(input_csv, output_csv):
    spark = SparkSession.builder.appName("DataProcessing").getOrCreate()
    df = spark.read.csv(input_csv, header=True, inferSchema=True)
    df = df.withColumn("quality_score", when(col("clicks") > 100, 1).otherwise(0))
    df.write.mode("overwrite").csv(output_csv)
    spark.stop()

if __name__ == "__main__":
    process_with_spark("data/raw/campaigns_data.csv", "data/processed/spark_campaigns_output")