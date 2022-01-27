from email import header
from pyspark import SparkConf,SQLContext,SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
sc = SparkContext().getOrCreate()
sql = SQLContext(sc)

df = sql.read.format("com.databricks.spark.csv").options(header=True,inferSchema=True).load('hdfs://localhost:9000/user/saidalikhonalikhonov/mnist/train.csv')

#selecting features 1st elements is label, from 2nd till end are features
inputcols = df.columns[1:]
assembler = VectorAssembler(inputCols=inputcols,outputCol='feature')
df = assembler.transform(df)

#splitting into train and test
df_train,df_test = df.randomSplit([0.75,0.25])

#model
clf = RandomForestClassifier(featuresCol='feature',labelCol='label')

#training
clf = clf.fit(df_train)

#prediction
predictions = clf.transform(df_test)

predictions.select(['label','prediction']).show()

#evaluation
criterion = MulticlassClassificationEvaluator(labelCol='label')
acc  = criterion.evaluate(predictions)
print(f'accuracy: {acc}')