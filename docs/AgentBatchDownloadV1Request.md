# AgentBatchDownloadV1Request

Request for POST /1/object/agent/{pkiAgentID}/batchDownload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_attachment_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.agent_batch_download_v1_request import AgentBatchDownloadV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of AgentBatchDownloadV1Request from a JSON string
agent_batch_download_v1_request_instance = AgentBatchDownloadV1Request.from_json(json)
# print the JSON string representation of the object
print(AgentBatchDownloadV1Request.to_json())

# convert the object into a dict
agent_batch_download_v1_request_dict = agent_batch_download_v1_request_instance.to_dict()
# create an instance of AgentBatchDownloadV1Request from a dict
agent_batch_download_v1_request_from_dict = AgentBatchDownloadV1Request.from_dict(agent_batch_download_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


