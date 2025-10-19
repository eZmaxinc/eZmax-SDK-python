# EzsignbulksendCreateObjectV2Request

Request for POST /2/object/ezsignbulksend

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignbulksend** | [**List[EzsignbulksendRequestCompoundV2]**](EzsignbulksendRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_create_object_v2_request import EzsignbulksendCreateObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendCreateObjectV2Request from a JSON string
ezsignbulksend_create_object_v2_request_instance = EzsignbulksendCreateObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendCreateObjectV2Request.to_json())

# convert the object into a dict
ezsignbulksend_create_object_v2_request_dict = ezsignbulksend_create_object_v2_request_instance.to_dict()
# create an instance of EzsignbulksendCreateObjectV2Request from a dict
ezsignbulksend_create_object_v2_request_from_dict = EzsignbulksendCreateObjectV2Request.from_dict(ezsignbulksend_create_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


