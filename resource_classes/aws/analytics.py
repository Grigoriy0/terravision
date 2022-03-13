

from . import _AWS


class _Analytics(_AWS):
    _type = "analytics"
    _icon_dir = "resource_images/aws/analytics"


class Analytics(_Analytics):
    _icon = "analytics.png"


class Athena(_Analytics):
    _icon = "athena.png"


class CloudsearchSearchDocuments(_Analytics):
    _icon = "cloudsearch-search-documents.png"


class Cloudsearch(_Analytics):
    _icon = "cloudsearch.png"


class DataPipeline(_Analytics):
    _icon = "data-pipeline.png"


class ElasticsearchService(_Analytics):
    _icon = "elasticsearch-service.png"


class EMRCluster(_Analytics):
    _icon = "emr-cluster.png"


class EMRHdfsCluster(_Analytics):
    _icon = "emr-hdfs-cluster.png"


class EMR(_Analytics):
    _icon = "emr.png"


class GlueCrawlers(_Analytics):
    _icon = "glue-crawlers.png"


class GlueDataCatalog(_Analytics):
    _icon = "glue-data-catalog.png"


class Glue(_Analytics):
    _icon = "glue.png"


class KinesisDataAnalytics(_Analytics):
    _icon = "kinesis-data-analytics.png"


class KinesisDataFirehose(_Analytics):
    _icon = "kinesis-data-firehose.png"


class KinesisDataStreams(_Analytics):
    _icon = "kinesis-data-streams.png"


class KinesisVideoStreams(_Analytics):
    _icon = "kinesis-video-streams.png"


class Kinesis(_Analytics):
    _icon = "kinesis.png"


class LakeFormation(_Analytics):
    _icon = "lake-formation.png"


class ManagedStreamingForKafka(_Analytics):
    _icon = "managed-streaming-for-kafka.png"


class Quicksight(_Analytics):
    _icon = "quicksight.png"


class RedshiftDenseComputeNode(_Analytics):
    _icon = "redshift-dense-compute-node.png"


class RedshiftDenseStorageNode(_Analytics):
    _icon = "redshift-dense-storage-node.png"


class Redshift(_Analytics):
    _icon = "redshift.png"


# Aliases

ES = ElasticsearchService
